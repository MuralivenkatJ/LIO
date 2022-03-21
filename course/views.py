import hashlib
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import date
from django.db.models import F

from course.forms import UploadForm
from course.models import Course, Course_skills
from faculty.models import Faculty
from faculty.views import getFacultyData
from institute.models import Institute
from student.models import Enrolls, Rates, Student, Wishlist

from python_files import playlist_duration

# Create your views here.
def unenrolled(request, c_id):

    course = Course.objects.get(c_id=c_id)

    Course.objects.filter(c_id=c_id).update(total_views=F('total_views') + 1)

    for f in Faculty.objects.raw('''
        SELECT f_id, f_name, qualification, F.image
        FROM faculty_faculty F, course_course C
        WHERE C.c_id = %s and C.f_id_id = F.f_id;''', [c_id]):
        faculty = f

    for i in Institute.objects.raw('''
        SELECT *
        FROM institute_institute I, faculty_faculty F
        WHERE F.f_id = %s and F.i_id_id = I.i_id;''', [faculty.f_id]):
        institute = i

    skills = []
    for s in Course_skills.objects.raw('''
        SELECT id, skills
        FROM course_course_skills
        WHERE c_id_id = %s;''',[c_id]):
        skills.append(s)
    
    rates = []
    for r in Rates.objects.raw('''
        SELECT R.id, R.rating, R.desc, S.s_name, S.image
        FROM student_rates R, student_student S
        WHERE R.c_id_id = %s and S.s_id = R.s_id_id''', [c_id]):
        rates.append(r)

    d = {'course': course, 'faculty': faculty, 'institute': institute, 'skills': skills, 'rates': rates}

    s_id = 0
    if 's_id' in request.COOKIES:
        s_id = request.COOKIES['s_id']
    else:
        d.update({'free': True})
    
    if s_id != 0:
        student = Student.objects.get(s_id=s_id)
        if student.i_id_id == institute.i_id:
            d.update({'free': True})

    return render(request, 'unenrolled.html', d)

def getCourseData(c_id):
    course = Course.objects.get(c_id=c_id)

    Course.objects.filter(c_id=c_id).update(total_views=F('total_views') + 1)

    for f in Faculty.objects.raw('''
        SELECT f_id, f_name, qualification, F.image
        FROM faculty_faculty F, course_course C
        WHERE C.c_id = %s and C.f_id_id = F.f_id;''', [c_id]):
        faculty = f

    for i in Institute.objects.raw('''
        SELECT *
        FROM institute_institute I, faculty_faculty F
        WHERE F.f_id = %s and F.i_id_id = I.i_id;''', [faculty.f_id]):
        institute = i

    skills = []
    for s in Course_skills.objects.raw('''
        SELECT id, skills
        FROM course_course_skills
        WHERE c_id_id = %s;''',[c_id]):
        skills.append(s)
    
    rates = []
    for r in Rates.objects.raw('''
        SELECT R.id, R.rating, R.desc, S.s_name, S.image
        FROM student_rates R, student_student S
        WHERE R.c_id_id = %s and S.s_id = R.s_id_id''', [c_id]):
        rates.append(r)
    
    return {'course': course, 'faculty': faculty, 'institute': institute, 'skills': skills, 'rates': rates}


def watched(request, c_id, index):
    s_id = int(request.COOKIES['s_id'])

    st = ''
    id = 0
    for c in Enrolls.objects.raw(
    ''' SELECT *
        FROM student_enrolls
        WHERE s_id_id = %s and c_id_id = %s''', [s_id, c_id]):
        st = c.watched
        id = c.id
    
    list = []
    if len(st) > 0:
        list = st.split(',')
    list.append(str(index))
    st = ','.join(list)

    Enrolls.objects.filter(id=id).update(watched=st)

    return HttpResponse(st)


def upload(request):
    if request.method == 'POST':
        req = request.POST.copy()

        playlistid = req['playlistid']
        req['duration'] = '00:00:00'
        req['no_videos'] = 0
        if playlistid != '':
            dict = playlist_duration.duration(playlistid)
            req['duration'] = dict['duration']
            req['no_videos'] = dict['no_videos']

        today = date.today()
        req['date'] = today

        f_id = request.COOKIES['f_id']
        req['f_id'] = f_id

        skills = req['skills']
        skill_list = skills.split(',')
        req.pop('skills')

        form = UploadForm(req, request.FILES)
        if form.is_valid():
            form.save()

            c_id = Course.objects.latest('c_id')

            for skill in skill_list:
                obj = Course_skills(skills=skill, c_id=c_id)
                obj.save()

            return redirect('faculty')
        else:
            f_id = request.COOKIES['f_id']
            d = getFacultyData(f_id)

            d.update({'form': form})

            return render(request, 'faculty.html', d)


def enroll(request, c_id):
    s_id = 0
    s_pass = ''

    if 's_id' in request.COOKIES:
        s_id = int(request.COOKIES['s_id'])
        s_pass = request.COOKIES['passw']
    else:
        return redirect('login1')

    passw = ''
    if s_id != 0:
        s = Student.objects.get(s_id=s_id)
        passw = s.password
    
    if s_pass != passw:
        return redirect('login1')
    else:
        record = Enrolls.objects.filter(c_id_id=c_id, s_id_id=s_id)

        if record.exists():
            pass
        else:
            s = Student.objects.get(s_id=s_id)
            s_i_id = s.i_id_id

            c = Course.objects.get(c_id=c_id)
            f_id = c.f_id_id
            f = Faculty.objects.get(f_id=f_id)
            f_i_id = f.i_id_id
        
            if s_i_id == f_i_id:
                enroll = Enrolls.objects.create(s_id=s, c_id=c)
                enroll.save()
            else:
                return redirect('paymentinfo', c_id=c_id)

    return redirect('mycourses')


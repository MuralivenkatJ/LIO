from django.shortcuts import render, redirect
import googleapiclient.discovery
from django.contrib import messages
from datetime import date
from django.db.models import F

from course.forms import UploadForm
from course.models import Course, Course_skills
from faculty.models import Faculty
from institute.models import Institute
from student.models import Enrolls, Rates, Student, Wishlist

from python_files import video_duration, playlist_duration

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
        SELECT i_id, i_name, I.image, I.email, website
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

    return render(request, 'unenrolled.html', {'course': course, 'faculty': faculty, 'institute': institute, 'skills': skills, 'rates': rates})


def enrolled(request, c_id):
    api_key = 'AIzaSyAThwinMHqAPzectaIrV7-RdL8wkrpfLa0'
    course = Course.objects.get(pk=c_id)
    playlistid = course.playlistid
    #playlistid = 'PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3'

    service = googleapiclient.discovery.build("youtube", "v3", developerKey = api_key)

    rqt = service.playlistItems().list(
        part = 'snippet, contentDetails',
        maxResults = 50,
        playlistId = playlistid,
    )

    res = rqt.execute()

    if 'nextPageToken' in res:
        token = res.get('nextPageToken')

    while ('nextPageToken' in res):
        rqt1 = service.playlistItems().list(
            part = 'snippet, contentDetails',
            maxResults = 50,
            playlistId = playlistid,
            pageToken = token,
        )
        res1 = rqt1.execute()

        res['items'] = res['items'] + res1['items']

        if 'nextPageToken' not in res1:
            res.pop('nextPageToken', None)
        else:
            token = res1['nextPageToken']

    vid_ids = []
    data = []
    dura = []

    index = 0

    for i in res["items"]:
        dictionary = {}

        if index % 50 == 0:
            temp = video_duration.duration(vid_ids)
            dura.extend(temp)
            vid_ids.clear()

        vid_ids.append(i["contentDetails"]["videoId"])

        dictionary["vidId"] = i["contentDetails"]["videoId"]
        dictionary["title"] = i["snippet"]["title"]
        dictionary["desc"]  = i["snippet"]["description"]
        dictionary["image"] = i["snippet"]["thumbnails"]["medium"]["url"]

        data.append(dictionary)

        index = index + 1
    
    temp = video_duration.duration(vid_ids)
    dura.extend(temp)
    vid_ids.clear()

    zipped_data = zip(data, dura)
    
    return render(request, 'course.html', {'z_data': zipped_data, 'data': data})


def upload(request):
    if request.method == 'POST':
        req = request.POST.copy()

        playlistid = req['playlistid']
        duration = playlist_duration.duration(playlistid)
        req['duration'] = duration

        skills = req['skills']
        skill_list = skills.split(',')
        req.pop('skills')

        f_id = request.COOKIES['f_id']
        req.update( {'f_id': f_id} )

        today = date.today()
        req['date'] = today

        course = UploadForm(req, request.FILES)
        if course.is_valid():
            course.save()

            c_id = Course.objects.latest('c_id')
            print(c_id)

            for skill in skill_list:
                obj = Course_skills(skills=skill, c_id=c_id)
                obj.save()

            return redirect('explore')
        else:
            messages.error(request, "Something is wrong")
        return render(request, 'upload.html')

    else:
        return render(request, 'upload.html')

    
def wish(request, c_id):
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
        s = Student.objects.get(s_id=s_id)
        c = Course.objects.get(c_id=c_id)
    
        wished = Wishlist.objects.create(s_id=s, c_id=c)
        wished.save()

    return redirect('wishlist')

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
        s = Student.objects.get(s_id=s_id)
        c = Course.objects.get(c_id=c_id)
    
        enroll = Enrolls.objects.create(s_id=s, c_id=c)
        enroll.save()

    return redirect('mycourses')


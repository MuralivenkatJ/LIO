from xml.etree.ElementTree import tostring
from django.shortcuts import render
from course.models import Course
from faculty.models import Faculty
from institute.models import Institute
from django.db.models import Q

from student.models import Student


def explore(request):
    s_id = 0
    s_pass = ''
    f_id = 0

    if 's_id' in request.COOKIES:
        s_id = request.COOKIES['s_id']
        s_pass = request.COOKIES['passw']
    if 'f_id' in request.COOKIES:
        f_id = request.COOKIES['f_id']

    color = ['red', 'purple', 'indigo', 'blue', 'deep-orange', 'blue-gray', 'dark-gray']
    i = 0
    j = 0
    color1 = []
    specialisation = []
    for s in Course.objects.raw('''
        SELECT c_id, specialization
        FROM course_course
        LIMIT 10;'''):
        if s.specialization not in specialisation:
            specialisation.append(s.specialization)
            temp = color[i]
            color1.append(temp)
            i = (i+1) % 7
            j = j+1
    
    zip_specialisation = zip(specialisation, color1)

    # FINDING THE NAME OF THE STUDENT
    s_name = ''
    passw = ''
    if s_id != 0:
        s = Student.objects.get(s_id=s_id)
        s_name = s.s_name
        passw = s.password

    # FINDING INSTITUTE NAME AND INSTITUTE ID and FREE COURSES
    iname = ''
    iid = 0
    free = []
    if s_pass == passw:
        for s in Institute.objects.raw('''
        SELECT i_name, I.i_id
        FROM student_student S, institute_institute I
        WHERE S.i_id_id = I.i_id;'''):
            iname = s.i_name
            iid = s.i_id
    
        
        for c in Course.objects.raw('''
            SELECT c_id
            FROM course_course C, faculty_faculty F
            WHERE C.f_id_id = F.f_id and F.i_id_id = %s''', [iid]):
            free.append(c)
    
    # MOST POPULAR
    most_popular = []
    for c in Course.objects.raw('''
        SELECT *
        FROM course_course
        ORDER BY total_views DESC
        LIMIT 10;'''):
        most_popular.append(c)

    # RECENTLY LAUNCHED
    recently_launched = []
    for c in Course.objects.raw('''
        SELECT *
        FROM course_course
        ORDER BY date DESC, c_id DESC
        LIMIT 10;'''):
        recently_launched.append(c)

    # GUIDED PROJECT
    guided_project = []
    for c in Course.objects.raw('''
        SELECT *
        FROM course_course
        WHERE guided_project = 1
        LIMIT 10;'''):
        guided_project.append(c)

    return render(request, 'explore.html', {'s_id': s_id, 's_name': s_name, 'f_id': f_id, 'i_name': iname, 'specialisation': zip_specialisation, 'freec': free, 'most_popular': most_popular, 'recently_launched': recently_launched, 'guided_project': guided_project})


def query(request):

    str = request.GET['search']
    print(str)

    course = Course.objects.filter(Q(c_name__icontains = str) | Q(description__icontains = str) | Q(specialization__icontains = str))


    faculty = Faculty.objects.filter(Q(f_name__icontains = str) | Q(qualification__icontains = str))

    f_courses = []
    for f in faculty:
        dict = {}
        dict['f_name'] = f.f_name

        c = Course.objects.filter(f_id = f.f_id)
        dict['course'] = c
        f_courses.append(dict)


    institute = Institute.objects.filter(i_name__icontains = str)

    i_courses = []
    for i in institute:
        dict = {}
        dict['i_name'] = i.i_name

        c = []
        for c1 in Course.objects.raw('''
            SELECT c_id, c_name, specialization, C.image, duration, price, total_views, f_id_id, level, guided_project, playlistid, description, date, rating
            FROM course_course C, faculty_faculty F, institute_institute I
            WHERE I.i_id = F.i_id_id and F.f_id = C.f_id_id'''):
            c.append(c1)
        dict['course'] = c
        i_courses.append(dict)


    return render(request, 'search.html', {'course': course, 'f_courses': f_courses, 'i_courses': i_courses})


def query1(request, str):

    course = Course.objects.filter(Q(c_name__icontains = str) | Q(description__icontains = str) | Q(specialization__icontains = str))

    return render(request, 'search.html', {'course': course})


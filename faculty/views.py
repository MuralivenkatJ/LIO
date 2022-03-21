import hashlib
from django.contrib import messages
from django.shortcuts import render, redirect
from course.models import Course
from explore.views import getExploreData

from faculty.forms import facultyForm
from faculty.models import Faculty
from institute.models import Institute
from student.models import Enrolls

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        id = 0
        passw = ''
        for row in Faculty.objects.raw(
            '''SELECT f_id 
               FROM faculty_faculty
               WHERE email=%s and password=%s''', [email, password]):
            id = row.f_id
            passw = row.password
        if(id > 0):
            response = redirect('explore')
            response.set_cookie('f_id', id)
            response.set_cookie('passw', passw)
            return response
        else:
            messages.error(request, 'incorrect email or password')
            d = getExploreData()
            d.update({'top': 'l2'})
            return render(request, 'explore.html', d)



def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            messages.error(request, "Password didn't match")
            d = getExploreData()
            d.update({'top': 's2'})
            return render(request, 'explore.html', d)
        else:
            if password != '':
                password = hashlib.md5(password.encode('utf-8')).hexdigest()
            req = request.POST.copy()
            req['password'] = password
            form = facultyForm(req, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('explore')
            else:
                # messages.error(request, form.errors)
                d = getExploreData()
                d.update({'form': form, 'top': 's2'})
                return render(request, 'explore.html', d)



def logout(request):
    response = redirect('explore')
    response.delete_cookie('f_id')
    response.delete_cookie('passw')
    return response



def faculty(request):

    f_id = 0
    f_pass = ''

    if 'f_id' in request.COOKIES:
        f_id = request.COOKIES['f_id']
        f_pass = request.COOKIES['passw']
    
    passw = ''
    f_name = ''
    profile = ''
    if f_id != 0:
        f = Faculty.objects.get(f_id=f_id)
        passw = f.password
        f_name = f.f_name
        profile = f.image

    if f_pass != passw:
        return redirect('login2')

    # UPLOADED COURSES
    course = []
    number = []

    for c in Course.objects.filter(f_id_id = f_id):
        in_progress = 0
        complete = 0
        enroll = Enrolls.objects.filter(c_id=c.c_id)

        for e in enroll:
            if e.status == "inprogress":
                in_progress = in_progress + 1
            elif e.status == "complete":
                complete = complete + 1
        
        dict = {}
        dict['inprogress'] = in_progress
        dict['complete'] = complete

        course.append(c)
        number.append(dict)

    zippedData = zip(course, number)

    return render(request, 'faculty.html', {'f_name': f_name, 'profile': profile, 'course': zippedData})


def getFacultyData(f_id):
    f = Faculty.objects.get(f_id=f_id)
    f_name = f.f_name
    profile = f.image

    course = []
    number = []

    for c in Course.objects.filter(f_id_id = f_id):
        in_progress = 0
        complete = 0
        enroll = Enrolls.objects.filter(c_id=c.c_id)

        for e in enroll:
            if e.status == "inprogress":
                in_progress = in_progress + 1
            elif e.status == "complete":
                complete = complete + 1
        
        dict = {}
        dict['inprogress'] = in_progress
        dict['complete'] = complete

        course.append(c)
        number.append(dict)

    zippedData = zip(course, number)

    return {'f_name': f_name, 'profile': profile, 'course': zippedData}

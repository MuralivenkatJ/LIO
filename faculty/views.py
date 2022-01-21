import hashlib
from django.contrib import messages
from django.shortcuts import render, redirect
from course.models import Course

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
               FROM faculty_faculty F 
               WHERE F.email=%s and F.password=%s''', [email, password]):
            id = row.f_id
            passw = row.password
        if(id > 0):
            response = redirect('explore')
            response.set_cookie('f_id', id)
            response.set_cookie('passw', passw)
            return response
        else:
            messages.error(request, 'incorrect email or password')
            return render(request, 'login1.html')

    else:
        return render(request, 'login2.html')



def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            messages.error(request, "Password didn't match")
        else:
            password = hashlib.md5(password.encode('utf-8')).hexdigest()
            req = request.POST.copy()
            req['password'] = password
            form = facultyForm(req, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('explore')
        return redirect('register2') 

    else:
        institutes = Institute.objects.all()

        return render(request, 'signup2.html', {'institute': institutes})



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
    if f_id != 0:
        f = Faculty.objects.get(f_id=f_id)
        passw = f.password
        f_name = f.f_name

    if f_pass != passw:
        return redirect('login2')

    # UPLOADED COURSES
    course = []
    number = []
    for c in Course.objects.raw('''
        SELECT c_id, image, c_name, description, duration
        FROM course_course
        WHERE f_id_id = %s''', [f_id]):

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

    return render(request, 'faculty.html', {'f_name': f_name, 'course': zippedData})
    
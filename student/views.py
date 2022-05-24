from datetime import date, datetime
import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import Course
from course.views import getCourseData
from explore.views import getExploreData
from faculty.models import Faculty
from institute.models import Institute
from student.forms import PaymentForm, studentForm

from student.models import Student

import random
from django.core.mail import send_mail

# Create your views here.
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        id = 0
        passw = ''
        n = ''
        for row in Student.objects.raw(
            '''SELECT s_id 
               FROM student_student S 
               WHERE S.email=%s and S.password=%s''', [email, password]):
            id=row.s_id
            passw = row.password
            n = row.s_name
        if(id > 0):
            response = redirect('explore')
            response.set_cookie('s_id', id)
            response.set_cookie('passw', passw)

            return response
        else:
            messages.error(request, 'incorrect email or password')
            d = getExploreData()
            d.update({'top': 'l1'})
            return render(request, 'explore.html', d)


def register(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        try:
            s = Student.objects.get(email=request.POST.get('email'))
            messages.error(request, "An account has already been created with this mail id")
            d = getExploreData()
            d.update({'top': 's1'})
            return render(request, 'explore.html', d)
        except Student.DoesNotExist:
            pass

        if password != cpassword:
            messages.error(request, "Password didn't match")
            d = getExploreData()
            d.update({'top': 's1'})
            return render(request, 'explore.html', d)
        else:
            if password != '':
                password = hashlib.md5(password.encode('utf-8')).hexdigest()
            req = request.POST.copy()
            req['password'] = password
            form = studentForm(req, request.FILES)
            if form.is_valid():
                
                # otp = random.randrange(100000, 999999)

                institute = Institute.objects.get(i_id=request.POST.get('i_id'))

                output = send_mail('Welcome to LIO', f'Hello {request.POST.get("s_name")}, \n\n\tLIO is an online educational platform to bring students and teachers all over the world together.\n\nYour registration was successful with the following details: \nName: {request.POST.get("s_name")} \nPhone: {request.POST.get("phone")} \nEmail Id: {request.POST.get("email")} \nInstitute: {institute.i_name} \n\nOur Best Wishes,\nTeam LIO', 'liolearnitonline@gmail.com', [request.POST.get('email')], fail_silently=False,)

                form.save()
                return redirect('explore')
            else:
                # messages.error(request, form.errors)
                d = getExploreData()
                d.update({'form': form, 'top': 's1'})
                return render(request, 'explore.html', d)


def logout(request):
    response = redirect('explore')
    response.delete_cookie('s_id')
    response.delete_cookie('passw')
    return response


def payment(request, c_id):
    
    c = Course.objects.get(c_id=c_id)
    f = Faculty.objects.get(f_id=c.f_id_id)
    i = Institute.objects.get(i_id=f.i_id_id)

    if 's_id' not in request.COOKIES:
        return redirect('login1')

    if request.method == 'POST':
        s_id = request.COOKIES['s_id']
        s = Student.objects.get(s_id=s_id)

        req = request.POST.copy()
        req['s_id'] = s_id
        req['c_id'] = c_id
        req['date'] = date.today()
        req['time'] = datetime.time(datetime.now())

        form = PaymentForm(req, request.FILES)
        if form.is_valid():

            output = send_mail('Payment Screenshot uploaded', f'Hello {s.s_name}, \n\n\tYour payment screenshot is uploaded. You will get access to the course {c.c_name} once the institute {i.i_name} verifies your payment details. \n\nBest Wishes, \nTeam LIO', 'liolearnitonline@gmail.com', [s.email], fail_silently=False,)

            form.save()
            return redirect('mycourses')
        else:
            d = getCourseData(c_id)
            d.update({'form': form})

            return render(request, 'unenrolled.html', d)
    
    return redirect('mycourses')


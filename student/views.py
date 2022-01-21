import hashlib
from urllib import response
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from institute.models import Institute
from student.forms import studentForm

from student.models import Student

# Create your views here.
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        id = 0
        passw = ''
        for row in Student.objects.raw(
            '''SELECT s_id 
               FROM student_student S 
               WHERE S.email=%s and S.password=%s''', [email, password]):
            id=row.s_id
            passw = row.password
        if(id > 0):
            response = redirect('explore')
            response.set_cookie('s_id', id)
            response.set_cookie('passw', passw)
            return response
        else:
            messages.error(request, 'incorrect email or password')
            return render(request, 'login1.html')

    else:
        return render(request, 'login1.html')

def register(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            messages.error(request, "Password didn't match")
            return render(request, 'signup2.html')
        else:
            password = hashlib.md5(password.encode('utf-8')).hexdigest()
            req = request.POST.copy()
            req['password'] = password
            form = studentForm(req, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('explore')

    else:

        institutes = Institute.objects.all()
        return render(request, 'signup1.html', {'institute': institutes})

def logout(request):
    response = redirect('explore')
    response.delete_cookie('s_id')
    response.delete_cookie('passw')
    return response
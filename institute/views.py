import hashlib
import os
from stat import S_IFDIR
from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import Course
from faculty.models import Faculty

from institute.models import Institute
from student.models import Enrolls, Pays, Student

from .forms import instituteForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            messages.error(request, "Password didn't match")
        else:
            if password != '':
                password = hashlib.md5(password.encode('utf-8')).hexdigest()
            req = request.POST.copy()
            req['password'] = password
            form = instituteForm(req, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('explore')
            else:
                # messages.error(request, form.errors)
                return render(request, 'signup3.html', {'form': form})
        return redirect('register3')
    else:
        return render(request, 'signup3.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        id = 0
        passw = ''
        for row in Institute.objects.raw(
            '''SELECT i_id
               FROM institute_institute
               WHERE email=%s and password=%s''', [email, password]):
            id = row.i_id
            passw = row.password
        if(id > 0):
            response = redirect('explore')
            response.set_cookie('i_id', id)
            response.set_cookie('passw', passw)
            return response
        else:
            messages.error(request, 'incorrect email or password')
            return redirect('login3')

    else:
        return render(request, 'login3.html')


def logout(request):
    response = redirect('explore')
    response.delete_cookie('i_id')
    response.delete_cookie('passw')
    return response


def approvals(request):
    i_id = 0
    i_pass = ''

    if 'i_id' in request.COOKIES:
        i_id = request.COOKIES['i_id']
        i_pass = request.COOKIES['passw']
    
    passw = ''
    i_name = ''
    profile = ''
    if i_id != 0:
        insti = Institute.objects.get(i_id=i_id)
        passw = insti.password
        i_name = insti.i_name
        profile = insti.image

    if i_pass != passw:
        return redirect('login3')
    
    approvals = Pays.objects.all()
    list1 = []
    list2 = []
    for approval in approvals:
        c = Course.objects.get(c_id=approval.c_id_id)
        f = Faculty.objects.get(f_id=c.f_id_id)

        if int(i_id) == f.i_id_id:

            a = {}
            a['c_name'] = c.c_name
            a['f_name'] = f.f_name
            s = Student.objects.get(s_id=approval.s_id_id)
            a['s_name'] = s.s_name

            list2.append(a)
            list1.append(approval)

    list = zip(list1, list2)

    return render(request, 'institute.html', {'i_id': i_id, 'i_name': i_name, 'profile': profile, 'list': list})


def screenshot(request, id):
    i_id = 0
    i_pass = ''

    if 'i_id' in request.COOKIES:
        i_id = request.COOKIES['i_id']
        i_pass = request.COOKIES['passw']
    
    passw = ''
    if i_id != 0:
        insti = Institute.objects.get(i_id=i_id)
        passw = insti.password

    if i_pass != passw:
        return redirect('login3')

    approval = Pays.objects.get(id=id)

    c = Course.objects.get(c_id=approval.c_id_id)
    f = Faculty.objects.get(f_id=c.f_id_id)
    s = Student.objects.get(s_id=approval.s_id_id)

    b = {'c_name': c.c_name, 'f_name': f.f_name, 's_name': s.s_name, 'price': c.price}

    return render(request, 'screenshot.html', {'a': approval, 'b': b})


def approve(request, id):
    i_id = 0
    i_pass = ''

    if 'i_id' in request.COOKIES:
        i_id = request.COOKIES['i_id']
        i_pass = request.COOKIES['passw']
    
    passw = ''
    if i_id != 0:
        insti = Institute.objects.get(i_id=i_id)
        passw = insti.password

    if i_pass != passw:
        return redirect('login3')

    approval = Pays.objects.get(id=id)

    s = Student.objects.get(s_id=approval.s_id_id)
    c = Course.objects.get(c_id=approval.c_id_id)

    enroll = Enrolls.objects.create(s_id=s, c_id=c)
    enroll.save()

    if approval.image:
        if os.path.isfile(approval.image.path):
            os.remove(approval.image.path)
            print("successfully deleted image")

    approval.delete()

    return redirect('approvals')
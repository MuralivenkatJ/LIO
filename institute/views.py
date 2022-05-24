import hashlib
import os
from stat import S_IFDIR
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from course.models import Course
from explore.views import getExploreData
from faculty.models import Faculty

from institute.models import Institute
from student.models import Enrolls, Pays, Student

from .forms import instituteForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        try:
            i = Institute.objects.get(email=request.POST.get('email'))
            messages.error(request, "An account has already been created with this mail id")
            d = getExploreData()
            d.update({'top': 's3'})
            return render(request, 'explore.html', d)
        except Institute.DoesNotExist:
            pass

        if password != cpassword:
            messages.error(request, "Password didn't match")
            d = getExploreData()
            d.update({'top': 's3'})
            return render(request, 'explore.html', d)
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
                d = getExploreData()
                d.update({'form': form, 'top': 's3'})
                return render(request, 'explore.html', d)


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
            d = getExploreData()
            d.update({'top': 'l3'})
            return render(request, 'explore.html', d)


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

    list3 = []
    for f in Faculty.objects.raw(
        ''' select *
            from faculty_faculty
            where status = "Pending" and i_id_id = %s;''', [i_id]):
        list3.append(f)

    list4 = []
    for s in Student.objects.raw(
        '''select *
           from student_student
           where status = "Pending" and i_id_id = %s;''', [i_id]):
        list4.append(s)

    return render(request, 'institute.html', {'i_id': i_id, 'i_name': i_name, 'profile': profile, 'list': list, 'list3': list3, 'list4': list4})


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

    output = send_mail(f'Enrolled for the course {c.c_name}', f'Hello {s.s_name}, \n\n\tCongratulations, you are enrolled for {c.c_name}. Happy learning. \n\nOur Best Wishes, \nTeam LIO', 'liolearnitonline@gmail.com', [s.email], fail_silently=False,)

    enroll = Enrolls.objects.create(s_id=s, c_id=c)
    enroll.save()

    if approval.image:
        if os.path.isfile(approval.image.path):
            os.remove(approval.image.path)
            print("successfully deleted image")

    approval.delete()

    return redirect('approvals')


def approve2(request, id):

    Faculty.objects.filter(f_id=id).update(status="Verified")

    return redirect('approvals')

def approve3(request, id):

    Student.objects.filter(s_id=id).update(status="Verified")

    s = Student.objects.get(s_id=id)
    i = Institute.objects.get(i_id=s.i_id_id)
    output = send_mail('Institute Verification', f'Hello {s.s_name}, \n\n\tYou are verified by the your institution {i.i_name}. Now you can enroll all the courses of {i.i_name} for free. \n\nBest Wishes, \nTeam LIO', 'liolearnitonline@gmail.com', [s.email], fail_silently=False,)

    return redirect('approvals')


from django.shortcuts import render, redirect
from course.models import Course

from student.models import Wishlist, Student

# Create your views here.
def wishlist(request):
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
        
        course = []
        for c in Course.objects.raw('''
            SELECT c_id, C.image, c_name, C.date, f_name, price
            FROM course_course C, faculty_faculty F
            WHERE C.f_id_id = F.f_id and C.c_id in 
                                (SELECT c_id_id
                                FROM student_wishlist
                                WHERE s_id_id = %s)''', [s.s_id]):
                                course.append(c)

        return render(request, 'wishlist.html', {'course': course})
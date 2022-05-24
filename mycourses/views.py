from django.shortcuts import render, redirect
from django.core.mail import send_mail

from python_files import video_duration, playlist_duration
import googleapiclient.discovery

from course.models import Course
from student.models import Enrolls, Rates, Student

# Create your views here.
def mycourses(request):
    s_id = 0
    s_pass = ''

    if 's_id' in request.COOKIES:
        s_id = int(request.COOKIES['s_id'])
        s_pass = request.COOKIES['passw']
    else:
        return redirect('login1')

    passw = ''
    profile = 'student/default.jpg'
    if s_id != 0:
        s = Student.objects.get(s_id=s_id)
        passw = s.password
        profile = s.image
    
    if s_pass != passw:
        return redirect('login1')
    else:
        s = Student.objects.get(s_id=s_id)
        
        course = []
        for c in Course.objects.raw('''
            SELECT c_id, C.image, c_name, C.date, f_name, price, playlistid, no_videos
            FROM course_course C, faculty_faculty F
            WHERE C.f_id_id = F.f_id and C.c_id in 
                                (SELECT c_id_id
                                FROM student_enrolls
                                WHERE s_id_id = %s)''', [s.s_id]):
                                course.append(c)
        
        watched = []
        for c in course:
            for e in Enrolls.objects.raw('''
                SELECT *
                FROM student_enrolls
                WHERE s_id_id = %s and c_id_id = %s''', [s_id, c.c_id]):
                st = e.watched
                list = []
                if len(st) > 0:
                    list = st.split(',')
                length = len(list)
                total = c.no_videos
                per = int(length / total * 100)
                watched.append(per)

                if(per == 100):
                    output = send_mail(f'Completion of the course {c.c_name}', f'Congratulations, you have completed the course {c.c_name}. Keep going and happy learning. \n\nOur Best Wishes, \nTeam LIO', 'liolearnitonline@gmail.com', [s.email], fail_silently=False,)

                    Enrolls.objects.filter(id=e.id).update(status="completed")
        
        data = zip(course, watched)

        return render(request, 'mycourses.html', {'data': data, 'profile': profile})


def reviews(request, c_id):

    if request.method == 'POST':
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

            ec = Enrolls.objects.filter(s_id=s, c_id=c)
            if ec:
                rating = request.POST['rating']
                desc = request.POST['desc']
                rate = Rates.objects.create(s_id=s, c_id=c, rating=rating, desc=desc)
                rate.save()
    
        return redirect('mycourses')

    else:
        return render(request, 'rating.html', {'c_id': c_id})


def enrolled(request, c_id):

    # Check if the student has enrolled for the course
    s_id = 0
    s_id = int(request.COOKIES['s_id'])
    passw = request.COOKIES['passw']

    s = Student.objects.get(s_id=s_id)
    password = s.password

    if s_id == 0 or passw != password:
        return render(request, 'login1.html')
    
    e = Enrolls.objects.filter(s_id_id=s_id, c_id_id=c_id)
    if not e:
        return redirect('mycourses')

    # Using api to get the tumbnail, title, description
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
        dictionary['index'] = index

        data.append(dictionary)

        index = index + 1
    
    temp = video_duration.duration(vid_ids)
    dura.extend(temp)
    vid_ids.clear()

    # getting the list of watched videos

    st = ''
    for c in Enrolls.objects.raw(
    ''' SELECT *
        FROM student_enrolls
        WHERE s_id_id = %s and c_id_id = %s''', [s_id, c_id]):
        st = c.watched
    
    list = []
    if len(st) > 0:
        list = st.split(',')
    for i in range(len(list)):
        list[i] = int(list[i])

    zipped_data = zip(data, dura)
    
    return render(request, 'course.html', {'z_data': zipped_data, 'data': data, 'course': course, 'watched': list})
from django.shortcuts import render
import googleapiclient.discovery

from python_files import video_duration

# Create your views here.
def unenrolled(request):
    return render(request, 'unenrolled.html')


def enrolled(request, playlistid):
    api_key = 'AIzaSyAThwinMHqAPzectaIrV7-RdL8wkrpfLa0'
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
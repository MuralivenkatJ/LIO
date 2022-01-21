import googleapiclient.discovery
import re
from datetime import timedelta

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

def duration(playlistid):

    api_key = 'AIzaSyAThwinMHqAPzectaIrV7-RdL8wkrpfLa0'
    # playlistid = 'PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3'

    service = googleapiclient.discovery.build('youtube', 'v3', developerKey = api_key)

    total_seconds = 0

    token = None
    while True:
        pl_request = service.playlistItems().list(
            part = 'contentDetails',
            playlistId = playlistid,
            maxResults = 50,
            pageToken = token,
        )

        pl_response = pl_request.execute()

        vid_ids = []
        for i in pl_response['items']:
            vid_ids.append(i['contentDetails']['videoId'])

        v_request = service.videos().list(
            part = 'contentDetails',
            id = ','.join(vid_ids),
        )

        v_response = v_request.execute()

        for i in v_response['items']:
            time = i['contentDetails']['duration']

            hours = hours_pattern.search(time)
            minutes = minutes_pattern.search(time)
            seconds = seconds_pattern.search(time)

            hours = int(hours.group(1) if hours else 0)
            minutes = int(minutes.group(1) if minutes else 0)
            seconds = int(seconds.group(1) if seconds else 0)

            vid_sec = timedelta(
                hours = hours,
                minutes = minutes,
                seconds = seconds,
            ).total_seconds()

            total_seconds += vid_sec

        token = pl_response.get('nextPageToken')
        if not token:
            break
    
    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    dura = str(hours) + ':' + str(minutes) + ':' + str(seconds)

    return dura

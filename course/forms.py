from django import forms
from course.models import Course

class UploadForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('c_name', 'image', 'specialization', 'level', 'playlistid', 'guided_project', 'description', 'price', 'duration', 'f_id', 'date', 'no_videos')
        labels = {'c_name': 'Title', 'image': 'image', 'specialization': 'specialization', 'level': 'Forwho', 'playlistid': 'Playlist_id', 'guided_project': 'guided_project', 'description': 'descrption', 'price': 'Price', 'duration': 'duration', 'f_id': 'f_id', 'date': 'date', 'no_videos': 'no_videos'}
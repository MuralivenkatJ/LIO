from django import forms
from course.models import Course
from python_files.playlist_duration import duration

class UploadForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('c_name', 'image', 'specialization', 'level', 'playlistid', 'guided_project', 'description', 'price', 'duration', 'f_id', 'date')
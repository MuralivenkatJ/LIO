from django import forms
from course.models import Course

class UploadForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('c_name', 'image', 'specialization', 'level', 'playlistid', 'guided_project', 'description', 'price', 'duration', 'f_id', 'date', 'no_videos')
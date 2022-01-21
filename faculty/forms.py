from django import forms

from faculty.models import Faculty

class facultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('f_name', 'email', 'qualification', 'i_id', 'image', 'phone', 'password')
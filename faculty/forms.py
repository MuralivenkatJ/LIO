from django import forms

from faculty.models import Faculty

class facultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('f_name', 'email', 'qualification', 'i_id', 'image', 'phone', 'password')
        labels = {'f_name': 'Name', 'email': 'Email', 'qualification': 'Qualificaion', 'i_id': 'Institute Name', 'image': 'Image', 'phone': 'Phone no', 'password': 'Password'}
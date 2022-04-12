from dataclasses import fields
from django import forms

from student.models import Student, Pays

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('s_name', 'phone', 'email', 'i_id', 'password')
        labels = {'s_name': 'Name', 'phone': 'Phone No', 'email': 'Email_Id', 'i_id': 'Institute', 'password': 'Password'}

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields = ('s_id', 'c_id', 'utr_no', 'image', 'date', 'time')
        labels = {'image': 'Screenshot', 'utr_no': 'UTR ID'}
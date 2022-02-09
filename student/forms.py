from dataclasses import fields
from django import forms

from student.models import Student, Pays

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('s_name', 'phone', 'email', 'i_id', 'password')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields = ('s_id', 'c_id', 'utr_no', 'image', 'date', 'time')
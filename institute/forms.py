from django import forms

from institute.models import Institute

class instituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('i_name', 'address', 'image', 'email', 'website', 'ac_no', 'ac_name', 'ifsc', 'b_name', 'password')
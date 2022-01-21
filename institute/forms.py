from socket import fromshare
from django import forms

from institute.models import Institute

class instituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('i_name', 'address', 'image', 'email', 'website')
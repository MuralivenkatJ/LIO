from django import forms

from institute.models import Institute

class instituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('i_name', 'address', 'image', 'email', 'website', 'b_name', 'ac_name', 'ac_no', 'ifsc', 'password')
        labels = {'i_name': 'Institute', 'address': 'Address', 'image': 'Image', 'email': 'Email', 'website': 'Website', 'b_name': 'Bank Name', 'ac_name': 'Account Holder', 'ac_no': 'Account Number', 'ifsc': 'IFSC Code', 'password': 'Password'}
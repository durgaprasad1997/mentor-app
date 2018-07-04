from django import forms
from onlineapp.models import *

class AddCollege(forms.ModelForm):
    class Meta:
        model = Colleges
        exclude = ['id']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),

            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}),

            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Acronym'}),

            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Details'}),

        }


class UpdateCollegeForm(forms.ModelForm):
    class Meta:
        model = Colleges
        exclude = ['id']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),

            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}),

            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Acronym'}),

            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Details'}),

        }


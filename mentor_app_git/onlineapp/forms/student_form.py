from django import forms
from onlineapp.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','Colleges']
        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),

            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter db_folder'}),

            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter dropped_out'}),
        }


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','Colleges']
        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),

            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter db_folder'}),

            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter dropped_out'}),
        }
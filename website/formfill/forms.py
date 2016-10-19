#https://docs.djangoproject.com/en/1.10/ref/forms/
from django import forms
from .models import Course
from django.forms.models import ModelForm

class UserForm(forms.Form):
    
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'user_name', 'contact', 'address', 'email']

    

    
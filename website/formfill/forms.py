#https://docs.djangoproject.com/en/1.10/ref/forms/
from django import forms

class UserForm(forms.Form):
    
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)



    

    
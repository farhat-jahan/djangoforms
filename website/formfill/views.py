from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
#from website.formfill.forms import UserForm
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form   = UserForm(request.POST) # look down for the output
        if form.is_valid():
            print "form['username']===",form['username']
            #form['username']=== <input id="id_username" maxlength="100" name="username" type="text" value="farhat" />
#             user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1'],
#             email=form.cleaned_data['email']
#             )
            return HttpResponseRedirect('success/')## this is a url address 
    else:
        form = UserForm()
        print form
    return render(request, 'registration.html', {'form':form})
            
def success_register(request):
    return render(request, 'registration_success.html')



'''
form   = UserForm(request.POST)=========> <tr><th><label for="id_username">Username:</label></th><td><input id="id_username" maxlength="100" name="username" type="text" value="farhat" /></td></tr>
<tr><th><label for="id_email">Email:</label></th><td><input id="id_email" name="email" type="email" value="1@gmail.com" /></td></tr>
<tr><th><label for="id_password1">Password1:</label></th><td><input id="id_password1" maxlength="30" name="password1" type="text" value="123" /></td></tr>
<tr><th><label for="id_password2">Password2:</label></th><td><input id="id_password2" maxlength="30" name="password2" type="text" value="123" /></td></tr>


form.cleaned_data==> {'username': u'farhat', 'password1': u'123', 'password2': u'123', 'email': u'1@gmail.com'}
'''

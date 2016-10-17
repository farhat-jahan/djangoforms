from django.conf.urls import include, url
from django.contrib import admin
from formfill.views import *
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registration/$', register, name='register'),
    url(r'^registration/success/$', success_register, name='success'),
]

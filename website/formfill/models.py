from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration =  models.CharField(max_length=100)
    user_name =  models.CharField(max_length=100, blank=True, null=True)
    contact =  models.CharField(max_length=100, blank=True, null=True)
    address =  models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'course'
 
    def __unicode__(self):
        return self.p_name

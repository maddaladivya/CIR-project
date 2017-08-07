from __future__ import unicode_literals

from django.db import models

class Student_login(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password =  models.TextField(max_length=50)
    confirm_password = models.TextField(max_length=50)


    def __str__(self):
        return self.first_name

# Create your models here.

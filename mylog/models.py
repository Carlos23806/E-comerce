from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    password = models.CharField(max_length=500)
    role = models.BooleanField(default= False)

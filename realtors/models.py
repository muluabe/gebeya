from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo =  models.ImageField(upload_to='realtor/%Y/%m/%d/', blank=True) #Optional extra photos
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=90)
    def __str__(self): #Show name as the identifying field
        return self.name
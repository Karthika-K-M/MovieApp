from django.db import models

from travelproject.settings import MEDIA_URL


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img  =models.ImageField(upload_to='pics')
    desc=models.TextField()
class Mobile(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img  = models.ImageField(upload_to = MEDIA_URL)
    def __str__(self):
        return   self.name
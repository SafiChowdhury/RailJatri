from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class journey(models.Model):
    passenger_name= models.CharField(max_length=15,default='name')
    from12= models.CharField(max_length=15)
    to= models.CharField(max_length=15)
    journey_date= models.DateField()
    adult= models.IntegerField()
    child= models.IntegerField()
    chair= models.CharField(max_length=15,default='class')


class station_name(models.Model):
    name= models.CharField(max_length=15)


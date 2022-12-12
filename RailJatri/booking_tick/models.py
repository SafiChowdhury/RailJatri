from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class journey(models.Model):
    passenger_nm = models.CharField(max_length=15, default='null')
    from12 = models.CharField(max_length=15)
    to = models.CharField(max_length=15)
    journey_date = models.DateField()
    adult = models.IntegerField()
    child = models.IntegerField()
    chair = models.CharField(max_length=15, default='class')
    total = models.IntegerField(default=0)



class station_name(models.Model):
    name= models.CharField(max_length=15)


class train_info(models.Model):
    name_train = models.CharField(max_length=20)
    train_number = models.IntegerField()
    time_train = models.TimeField(default="00:00:00")
    Dest = models.CharField(max_length=15,default='_TO_')
    arraival_time = models.TimeField(default='00:00:00')
    place = models.CharField(max_length=15,default='from')
    chair_class = models.CharField(max_length=15)
    fare = models.IntegerField(default=000)

class ticket_info(models.Model):
    cost = models.IntegerField()
    passenger_name = models.CharField(max_length=20)
    passenger_mail = models.CharField(max_length=30)
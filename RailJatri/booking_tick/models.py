from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class journey(models.Model):
    from12= models.CharField(max_length=15)
    to= models.CharField(max_length=15)
    journey_date= models.DateField()
    adult= models.IntegerField()
    child= models.IntegerField()
    chair= models.CharField(max_length=15,default='class')


class station_name(models.Model):
    name= models.CharField(max_length=15)

class passenger_details(models.Model):
    first_name=models.ForeignKey(User,on_delete=models.CASCADE)
    # last_name = models.ForeignKey(User, on_delete=models.CASCADE)
    # email= models.ForeignKey(User,on_delete=models.CASCADE)
    def f_name(self):
        return self.first_name.first_name
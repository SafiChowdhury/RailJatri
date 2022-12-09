from django.db import models

# Create your models here.

class journey(models.Model):
    from12= models.CharField(max_length=15)
    to= models.CharField(max_length=15)
    journey_date= models.DateField()
    adult= models.IntegerField()
    child= models.IntegerField()


class station_name(models.Model):
    name= models.CharField(max_length=15)
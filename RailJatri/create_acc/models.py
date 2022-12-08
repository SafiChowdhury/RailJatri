from django.db import models

# Create your models here.

class passenger(models.Model):
    
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    gender = models.CharField(max_length=15)
    email = models.CharField(max_length=50, primary_key=True)
    Nid_No=models.IntegerField()
    house_no= models.CharField(max_length=15,default='house_no')
    roadNo= models.CharField(max_length=15,default='road_no')
    zipCode=models.IntegerField(default=00)
    town= models.CharField(max_length=15, default='town')
    mobile_No= models.CharField(max_length=15)
    password= models.CharField(max_length=50)
    confirm_pass= models.CharField(max_length=50)




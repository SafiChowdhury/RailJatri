from django.db import models
from create_acc.models import passenger

# Create your models here.
class forget_password1(models.Model):
    
    email = models.ForeignKey(passenger, on_delete=models.CASCADE, related_name='sample1')
    mobile_No= models.ForeignKey(passenger, on_delete=models.CASCADE, related_name='sample2')
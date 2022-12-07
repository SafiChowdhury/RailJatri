from django.db import models
from create_acc.models import passenger

# Create your models here.

class login_details(models.Model):
    email = models.ForeignKey(passenger, on_delete=models.CASCADE, related_name='sample3')
    password = models.ForeignKey(passenger, on_delete=models.CASCADE, related_name='sample4')

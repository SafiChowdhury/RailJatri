from django.db import models
from create_acc.models import passenger
# Create your models here.
class forget_password3(models.Model):
    verification_code = models.IntegerField()

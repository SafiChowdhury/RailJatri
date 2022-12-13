from django.db import models
# Create your models here.
class forget_password3(models.Model):
    verification_code = models.IntegerField()

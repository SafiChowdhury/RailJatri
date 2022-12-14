from django.db import models

# Create your models here.
class profile_update(models.Model):
    f_name= models.CharField(max_length=15)
    l_name= models.CharField(max_length=15)
    dob= models.DateField()
    gender = models.CharField(max_length=10)
    nid_no= models.IntegerField()
    h_nm = models.CharField(max_length=15)
    r_nm = models.CharField(max_length=15)
    zp_cd = models.CharField(max_length=4)
    city = models.CharField(max_length=15)
    us_nm = models.CharField(max_length=15)
    ph_nmbr = models.CharField(max_length=13,default=0)
    full_name = models.CharField(max_length=50)
    f_add = models.CharField(max_length=50,default='NULL')
# Generated by Django 4.1.2 on 2022-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_profile', '0003_profile_update_f_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_update',
            name='ph_nmbr',
            field=models.CharField(default=0, max_length=14),
        ),
        migrations.AlterField(
            model_name='profile_update',
            name='zp_cd',
            field=models.CharField(max_length=4),
        ),
    ]
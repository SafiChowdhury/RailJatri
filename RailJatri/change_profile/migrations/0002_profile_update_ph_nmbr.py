# Generated by Django 4.1.2 on 2022-12-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_update',
            name='ph_nmbr',
            field=models.CharField(default=0, max_length=11),
        ),
    ]

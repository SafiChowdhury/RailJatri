# Generated by Django 4.1.2 on 2022-12-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_acc', '0003_passenger_tourist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='address',
        ),
        migrations.AddField(
            model_name='passenger',
            name='house_no',
            field=models.CharField(default='house_no', max_length=15),
        ),
        migrations.AddField(
            model_name='passenger',
            name='roadNo',
            field=models.CharField(default='road_no', max_length=15),
        ),
        migrations.AddField(
            model_name='passenger',
            name='town',
            field=models.CharField(default='town', max_length=15),
        ),
        migrations.AddField(
            model_name='passenger',
            name='zipCode',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0018_train_name_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_name',
            name='arraival_time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='train_name',
            name='time_train',
            field=models.TimeField(default='00:00:00'),
        ),
    ]

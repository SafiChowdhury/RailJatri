# Generated by Django 4.1.1 on 2022-12-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0029_chair_class_remove_station_name_chair_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train_name',
            name='fare',
        ),
        migrations.AddField(
            model_name='chair_class',
            name='fare',
            field=models.IntegerField(default=0),
        ),
    ]

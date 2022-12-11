# Generated by Django 4.1.1 on 2022-12-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0030_remove_train_name_fare_chair_class_fare'),
    ]

    operations = [
        migrations.CreateModel(
            name='train_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_train', models.CharField(max_length=20)),
                ('train_number', models.IntegerField()),
                ('time_train', models.TimeField(default='00:00:00')),
                ('place', models.CharField(default='_TO_', max_length=15)),
                ('arraival_time', models.TimeField(default='00:00:00')),
                ('from_dist', models.CharField(default='from', max_length=15)),
                ('chair_class', models.CharField(max_length=15)),
                ('fare', models.IntegerField(default=0)),
                ('to_dist', models.CharField(default='from', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='chair_class',
        ),
        migrations.DeleteModel(
            name='train_name',
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0017_train_name_time_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_name',
            name='place',
            field=models.CharField(default='_TO_', max_length=15),
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0019_train_name_arraival_time_alter_train_name_time_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_name',
            name='fare',
            field=models.IntegerField(default=0),
        ),
    ]

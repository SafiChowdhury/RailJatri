# Generated by Django 4.1.2 on 2022-12-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0032_remove_train_info_from_dist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_info',
            name='Dest',
            field=models.CharField(default='_TO_', max_length=15),
        ),
    ]
# Generated by Django 4.1.1 on 2022-12-11 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0008_rename_journeys_journey'),
    ]

    operations = [
        migrations.DeleteModel(
            name='journey',
        ),
    ]
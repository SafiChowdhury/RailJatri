# Generated by Django 4.1.1 on 2022-12-10 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_tick', '0004_journey_passenger_name_delete_passenger_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='passenger_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0034_journey_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('passenger_name', models.CharField(max_length=20)),
                ('passenger_mail', models.CharField(max_length=30)),
            ],
        ),
    ]

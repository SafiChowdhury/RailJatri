# Generated by Django 4.1.2 on 2022-12-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_acc', '0002_remove_passenger_id_alter_passenger_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='tourist',
            field=models.IntegerField(default=0),
        ),
    ]

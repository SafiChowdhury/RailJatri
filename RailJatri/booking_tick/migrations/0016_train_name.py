# Generated by Django 4.1.1 on 2022-12-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tick', '0015_journey'),
    ]

    operations = [
        migrations.CreateModel(
            name='train_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_train', models.CharField(max_length=20)),
                ('train_number', models.IntegerField()),
            ],
        ),
    ]

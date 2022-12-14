# Generated by Django 4.1.2 on 2022-12-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('nid_no', models.IntegerField()),
                ('h_nm', models.CharField(max_length=15)),
                ('r_nm', models.CharField(max_length=15)),
                ('zp_cd', models.IntegerField()),
                ('city', models.CharField(max_length=15)),
                ('us_nm', models.CharField(max_length=15)),
                ('full_name', models.CharField(max_length=50)),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2023-04-11 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_profile_date_of_birth_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]

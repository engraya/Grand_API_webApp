# Generated by Django 4.1.3 on 2023-04-06 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
    ]

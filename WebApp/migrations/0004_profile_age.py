# Generated by Django 4.1.7 on 2023-04-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_profile_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

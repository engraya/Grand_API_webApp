# Generated by Django 4.1.7 on 2023-04-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

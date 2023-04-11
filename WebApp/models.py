from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from PIL import Image
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='default.png', null=True, blank=True)
    country = CountryField(blank_label='Select Country', null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

   
    def save(self):
        super().save

        uploadedProfileImage = Image.open(self.profile_pic.path)

        if uploadedProfileImage.height > 300 or uploadedProfileImage.width > 300:
            output_dimension = (300, 300)
            uploadedProfileImage.thumbnail(output_dimension)
            uploadedProfileImage.save(self.profile_pic.path)



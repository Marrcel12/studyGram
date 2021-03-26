from django.db import models
from djrichtextfield.models import RichTextField


class profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, blank=False)
    thumbnail = models.ImageField(
        upload_to='thumbnails_users', blank=True, default=None)
    description = RichTextField(
        max_length=2500, default="", blank=True, verbose_name="Opis usera")
    # TODO: debug if it is social link
    facebook_social = models.CharField(max_length=180, blank=True)
    instagram_social = models.CharField(max_length=180, blank=True)


class photo_users(models.Model):
    id_photo = models.AutoField(primary_key=True)
    photo_file = models.ImageField(upload_to='photo_users')


class profile_photo(models.Model):
    id_product_photo = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(profile, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(photo_users, on_delete=models.CASCADE)

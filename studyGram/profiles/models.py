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
    is_creator = models.BooleanField(default=False)
    facebook_social = models.CharField(max_length=180, blank=True)
    instagram_social = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return self.username


class photo_users(models.Model):
    id_photo = models.AutoField(primary_key=True)
    photo_file = models.ImageField(upload_to='photo_users')
    name = models.CharField(max_length=100, blank=True, default=None)

    def __str__(self):
        return self.name


class profile_photo(models.Model):
    id_profile_photo = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(profile, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(photo_users, on_delete=models.CASCADE)


class raiting_users(models.Model):
    id_raiting = models.AutoField(primary_key=True)
    value = models.CharField(max_length=30, null=True)


class raitings_to_users(models.Model):
    raiting_product = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(profile, on_delete=models.CASCADE)
    id_raiting = models.ForeignKey(raiting_users, on_delete=models.CASCADE)

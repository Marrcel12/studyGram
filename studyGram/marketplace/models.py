from django.db import models
from profiles.models import profile


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails_products')
    description = RichTextField(
        max_length=2500, default="", blank=True, verbose_name="Opis produktu", blank=True)
    rate = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    author_id = models.ForeignKey(profile)
    monthly_rating = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True)
    tags = models.CharField(max_length=500, blank=False)


class photo(models.Model):
    id_photo = models.AutoField(primary_key=True)
    photo_file = models.ImageField(upload_to='photo_products')


class product_photo(models.Model):
    id_product_photo = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product)
    id_photo = models.ForeignKey(photo)


class category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = = models.CharField(max_length=30, blank=False)


class category_product(models.Model):
    id_category_product = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product)
    id_category = models.ForeignKey(category)

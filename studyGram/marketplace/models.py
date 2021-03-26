from django.db import models
from djrichtextfield.models import RichTextField
from profiles.models import profile


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    thumbnail = models.ImageField(upload_to='thumbnails_products')
    description = RichTextField(
        max_length=2500, default=None, blank=True, verbose_name="Opis produktu")
    rate = models.CharField(max_length=30)
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    author_id = models.ForeignKey(
        profile, on_delete=models.CASCADE)
    monthly_rating = models.DecimalField(
        max_digits=4, decimal_places=0)
    tags = models.CharField(max_length=500)


class photo(models.Model):
    id_photo = models.AutoField(primary_key=True)
    photo_file = models.ImageField(upload_to='photo_products')


class product_photo(models.Model):
    id_product_photo = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(photo, on_delete=models.CASCADE)


class category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)


class category_product(models.Model):
    id_category_product = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)

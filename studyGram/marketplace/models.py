from django.db import models


class product(models.Model):
    title = models.CharField(max_length=80)
    thumbnail = models.ImageField(upload_to='thumbnails_products')
    description = models.CharField(max_length=500)
    rate = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=80)
    product_id = models.AutoField(primary_key=True)

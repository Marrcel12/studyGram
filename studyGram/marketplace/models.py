from django.db import models
from djrichtextfield.models import RichTextField
from profiles.models import profile
from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):
    ...
    operations = [
        TrigramExtension(),
        ...
    ]
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    thumbnail = models.ImageField(
        upload_to='thumbnails_products', blank=True, default=None)
    description = RichTextField(
        max_length=25000000, default=None, blank=True, verbose_name="Opis produktu")
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    profile_id = models.ForeignKey(
        profile, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500, blank=True, default=None)

    def __str__(self):
        return self.title


class photo_products(models.Model):
    id_photo = models.AutoField(primary_key=True)
    photo_file = models.ImageField(upload_to='photo_products')
    name = models.CharField(max_length=100, blank=True, default=None)

    def __str__(self):
        return self.name


class product_photo(models.Model):
    id_product_photo = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(photo_products, on_delete=models.CASCADE)


class level(models.Model):
    id_level = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name


class subject(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name


class topic(models.Model):
    id_topic = models.AutoField(primary_key=True)
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class subject_topic(models.Model):
    id_subject_topic = models.AutoField(primary_key=True)
    id_topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(subject, on_delete=models.CASCADE)


class level_subject_topic_product(models.Model):
    id_level_subject_product = models.AutoField(primary_key=True)
    id_level = models.ForeignKey(level, on_delete=models.CASCADE)
    id_subject_topic = models.ForeignKey(
        subject_topic, on_delete=models.CASCADE)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)


class raiting_products(models.Model):
    id_raiting = models.AutoField(primary_key=True)
    value_text = models.CharField(max_length=30, null=True)
    value_number = models.IntegerField(choices=list(
        zip(range(1, 10), range(1, 10))), unique=True)
    id_user = models.ForeignKey(
        profile, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.value_text


class raitings_to_product(models.Model):
    raiting_product = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    id_raiting = models.ForeignKey(raiting_products, on_delete=models.CASCADE)

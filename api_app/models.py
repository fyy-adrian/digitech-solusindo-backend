from django.db import models

class Home(models.Model):
    image = models.ImageField(upload_to='hero/', max_length=255, default="default.jpg")

class Portofolio(models.Model):
    image = models.CharField(max_length=255, default="default.jpg")

class Price(models.Model):
    level = models.CharField(max_length=255)
    price = models.IntegerField()
    features = models.JSONField(models.CharField(max_length=255))
    special = models.BooleanField(default=False)

class Service(models.Model):
    header = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="default.jpg")

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)

class Partnership(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="default.jpg")
    
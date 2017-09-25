from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)


class Article(models.Model):
    name = models.CharField(max_length=128)

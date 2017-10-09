from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    # role = models.ForeignKey("Role")  # 一对多,

    role = models.ManyToManyField("Role")

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    desc = models.TextField()

    user = models.ManyToManyField("User")


class Article(models.Model):
    name = models.CharField(max_length=128)

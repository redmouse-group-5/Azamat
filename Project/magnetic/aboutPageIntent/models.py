from django.db import models

# Create your models here.


class HistoryOfNCKT(models.Model):
    name = models.CharField(max_length=50)
    paragraphe = models.TextField()
    publick = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OurOrder(models.Model):
    avatar = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    descryption = models.TextField()
    publick = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vip(models.Model):
    range = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=70)
    employment = models.CharField(max_length=70)
    email = models.EmailField()
    descryption = models.TextField()
    avatar = models.ImageField(upload_to="vip_avatar", blank=True, null=True, default=None)
    publick = models.BooleanField(default=True)

    def __str__(self):
        return self.name

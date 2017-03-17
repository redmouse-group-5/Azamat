# coding=utf-8

from django.db import models

# Create your models here.


class HeaderDate(models.Model):
    telephone = models.CharField(max_length=13)
    email = models.EmailField()
    def __str__(self):
        return 'телефон и почта'

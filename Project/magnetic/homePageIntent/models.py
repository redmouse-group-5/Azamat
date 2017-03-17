# coding=utf-8

from django.db import models

# Create your models here.


class HelloGrid(models.Model):
    hello = models.CharField(max_length=30)
    slogan = models.CharField(max_length=30)
    firstAdd = models.CharField(max_length=50)
    secondAdd = models.CharField(max_length=150)

    def __str__(self):
        return 'данные первого блока'


class SpectrFach(models.Model):
    avatar = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    mark = models.CharField(max_length=100)
    publick = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MoreInformation(models.Model):
    name = models.CharField(max_length=30)
    publick = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RawTitle(models.Model):
    title = models.CharField(max_length=50)
    rawsideLeft = models.BooleanField()
    name = models.ForeignKey(MoreInformation)

    def __str__(self):
        return self.title


class RawInformation(models.Model):
    title = models.ForeignKey(RawTitle)
    information = models.CharField(max_length=100)

    def __str__(self):
        return self.information
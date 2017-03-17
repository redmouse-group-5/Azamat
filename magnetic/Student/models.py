from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    # placeOfUni = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    def __str__(self):
        return self.name
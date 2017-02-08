from django.db import models

# Create your models here.

class GroupOfPicture(models.Model):
    name = models.CharField(max_length=30)
    descryption = models.TextField()

    def __str__(self):
        return self.name

class Picture(models.Model):
    group = models.ForeignKey(GroupOfPicture)
    picture = models.ImageField(upload_to="pictures", blank=True, null=True, default=None)
    descryption = models.CharField(max_length=30)
    publich_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descryption
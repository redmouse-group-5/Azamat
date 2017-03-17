from django.contrib import admin
from picture.models import GroupOfPicture, Picture

# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture
    extra = 3


class GroupAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

admin.site.register(GroupOfPicture, GroupAdmin)
admin.site.register(Picture)
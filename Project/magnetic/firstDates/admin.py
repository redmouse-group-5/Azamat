from django.contrib import admin

# Register your models here.
from firstDates.models import HeaderDate


class DateAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email')
    list_display_links = ('telephone', 'email')
    def has_add_permission(self, request):
        return False

admin.site.register(HeaderDate, DateAdmin)
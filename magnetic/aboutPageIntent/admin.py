from django.contrib import admin

# Register your models here.
from aboutPageIntent.models import HistoryOfNCKT, OurOrder, Vip

class CastomAdmin(admin.ModelAdmin):
    list_display = ('name','publick')
    list_editable = ('publick',)

admin.site.register(HistoryOfNCKT, CastomAdmin)
admin.site.register(OurOrder, CastomAdmin)
admin.site.register(Vip, CastomAdmin)
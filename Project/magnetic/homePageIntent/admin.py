from django.contrib import admin

# Register your models here.
from homePageIntent.models import HelloGrid, SpectrFach, MoreInformation, RawTitle, RawInformation


class RawTitleInline(admin.TabularInline):
    model = RawTitle
    extra = 0

class MoreInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'publick')
    list_editable = ('publick',)
    inlines = [RawTitleInline]

class RawInformationInline(admin.TabularInline):
    model = RawInformation
    extra = 1


class RawTitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'rawsideLeft')
    list_editable = ('rawsideLeft',)
    inlines = [RawInformationInline]

class HelloGridAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

class SpectrFachAdmin(admin.ModelAdmin):
    list_display = ('name', 'mark', 'publick')
    list_editable = ('publick',)

admin.site.register(HelloGrid, HelloGridAdmin)
admin.site.register(SpectrFach,SpectrFachAdmin)
admin.site.register(MoreInformation, MoreInformationAdmin)
admin.site.register(RawTitle, RawTitleAdmin)
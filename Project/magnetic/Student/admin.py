from django.contrib import admin

# Register your models here.
from  Student.models import StudentInfo

class StudentInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'name', 'surname', 'lat', 'lng')
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(StudentInfo, StudentInfoAdmin)
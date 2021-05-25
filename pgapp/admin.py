from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ("name","salary")
    def get_ordering(self, request):
        return ['id']

@admin.register(RoomTypeModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ("description","fees")
    def get_ordering(self, request):
        return ['id']

admin.site.register(
    [
        StudentModel,
        VisitorModel
    ]
)


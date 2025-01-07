from django.contrib import admin
from .models  import Student
# Register your models here.
# @admin.register(student)
# class AdminStudent(admin.ModelAdmin):
    # list_display = ['name','qualification','age','gender']
    # pass
    # list_display_links = ['qualification']
admin.site.register(Student)

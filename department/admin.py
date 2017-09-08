from django.contrib import admin

from .models import Department, Program, ClassLevel

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(ClassLevel) 
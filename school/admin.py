from django.contrib import admin

from  .models import School
from department.models import Department, Room

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Room)

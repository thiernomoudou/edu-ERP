from django.contrib import admin

from  .models import School
from department.models import Department, Room
from employee.models import Professor, Employee

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Professor)
admin.site.register(Employee)

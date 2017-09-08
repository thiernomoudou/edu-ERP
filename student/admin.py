from django.contrib import admin

from .models import Baccalaureat, Student, Country, StudentDetail

admin.site.register(Baccalaureat)
admin.site.register(Student)
admin.site.register(Country)
admin.site.register(StudentDetail) 

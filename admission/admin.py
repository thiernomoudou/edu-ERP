from django.contrib import admin

from .models import AcademicYear, Admission, AdmissionProcess

admin.site.register(AcademicYear)
admin.site.register(Admission)
admin.site.register(AdmissionProcess) 


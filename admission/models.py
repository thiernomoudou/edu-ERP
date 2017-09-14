from django.db import models

from department.models import ClassLevel
from student.models import Student

import datetime


class AcademicYear(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    label = models.CharField(max_length=45)

    def __str__(self):
        return (self.label)


class Admission(models.Model):
    academic_year=models.OneToOneField(AcademicYear)
    class_level = models.OneToOneField(ClassLevel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)




class AdmissionProcess(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE)

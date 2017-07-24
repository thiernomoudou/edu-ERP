from django.contrib import admin

from  .models import School, Batch
from department.models import Department, Room, Subject
from admission.models import Registration, Admission
from employee.models import Teacher, Employee
from student.models import Student, Exam, Grade

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Employee)
admin.site.register(Registration)
admin.site.register(Admission)
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Grade)
admin.site.register(Batch)


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
#admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Grade)
admin.site.register(Batch)

class GradeInline(admin.TabularInline):
    """
    Defines format of inline Grade insertion (used in StudentAdmin)
    """
    model = Grade


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Administration object for Student models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    # list_display = ('student.first_name', 'student.last_name', 'department', 'student.date_of_birth', 'department')
    # fields = ['student.first_name', 'student.last_name', 'department', ('student.date_of_birth', 'student.nationality')]
    # inlines = [GradeInline]

    # list_display = ('department', 'student_card_number')
    # fiels = ['department', 'student-card_number']
    inlines = [GradeInline]
from django.db import models

from admission.models import Registration
from department.models import Subject, Room, Department

class Student(models.Model):
    student_card_number = models.CharField(max_length=64)
    student = models.OneToOneField(Registration, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return (self.student.first_name)



class Exam(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return (self.name)


class Grade(models.Model):
    name = models.CharField(max_length=100)
    Grade_1 = models.IntegerField()
    Grade_2 = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Payment(models.Model):
    payment_number = models.CharField(max_length=64)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=2)
    total_paid = models.DecimalField(max_digits=32, decimal_places=2)
    balance = models.DecimalField(max_digits=32, decimal_places=2)

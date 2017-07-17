from django.db import models
from django_countries.fields import CountryField
from department.models import Course

class Professor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.ImageField()

    SELECT_BLOOD_GROUP = (
        ('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
        ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')
        )
    SELECT_GENDER = (
        ('male', 'Male'), ('female', 'Female')
        )
    blood_group = models.CharField(max_length=8, choices=SELECT_BLOOD_GROUP, null=True, 
    blank=True)
    gender = models.CharField(max_length=8, choices=SELECT_GENDER)
    nationality = CountryField(blank_label='(select country)')
    id_card_number = models.CharField(max_length=64)
    course = models.ManyToManyField(Course)





class Employee(models.Model):
    pass

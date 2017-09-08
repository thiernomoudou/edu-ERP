from django.db import models
from sysadmin.models import User


class Baccalaureat(models.Model):
    name = models.CharField(max_length=16)
    school_origin = models.CharField(max_length=100)
    bac_year = models.CharField(max_length=4)
    table_number = models.CharField(max_length=16)

    def __str__(self):
        return(self.name)


class Country(models.Model):
    country_name = models.CharField(max_length=45)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return (self.country_name)

class Student(models.Model):
    id_number =  models.CharField(max_length=16)
    baccalaureat = models.ForeignKey(Baccalaureat, on_delete=models.CASCADE)


    # def __str__(self):
    #     return (self)


class StudentDetail(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    detail_high_school = models.CharField(max_length=45)
    details_last_modified = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(first_name, last_name)


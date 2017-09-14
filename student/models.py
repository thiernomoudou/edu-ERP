from django.db import models

SELECT_GENDER = (
        ('male', 'Male'), ('female', 'Female'),(None, 'Select Gender')
        )


class Baccalaureat(models.Model):
    name = models.CharField(max_length=16)
    school_origin = models.CharField(max_length=100)
    bac_type = models.CharField(max_length=100)
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
    email_univ = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=80)
    gender = models.CharField(max_length=32, choices=SELECT_GENDER)
    id_card_number = models.CharField(max_length=100)
    baccalaureat_id = models.ForeignKey(Baccalaureat, on_delete=models.CASCADE)
    

    def __str__(self):
        return (self.id)


class StudentDetail(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    marital_status = models.CharField(max_length=45)
    occupation = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress_parents = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=45)
    email_parent = models.CharField(max_length=45, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)
    detail_high_school = models.CharField(max_length=45)
    last_modified = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(first_name, last_name)


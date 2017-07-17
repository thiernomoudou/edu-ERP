from django.db import models

# Create your models here.

class Saisie(models.Model):
    """
    Model representing a course(e.g. University).
    """
    nomber = models.IntegerField()
    first_name = models.CharField(max_length=100)
    #logo = models.ImageField(null=True, blank=True)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=100)
    sexe = models.CharField(max_length=5)
    filiation_one = models.CharField(max_length=200)
    filiation_two = models.CharField(max_length=200)
    guardian = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=100)
    adresse_one = models.CharField(max_length=100)
    adresse_two = models.CharField(max_length=100, null=True, blank=True)
    school_origin = models.CharField(max_length=100)


    def ___str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.first_name)

class Inscription(models.Model):
    """
    Model representing a course(e.g. University).
    """
    Nomber = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200, null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    sexe = models.CharField(max_length=50)

    def ___str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.first_name)

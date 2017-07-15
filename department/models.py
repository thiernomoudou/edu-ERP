from django.db import models

class Department(models.Model):
    """
    Model representing a course(e.g. economic sciences).
    """
    name = models.CharField(max_length=200)
    abreviation = models.CharField(max_length=10)
    administator_name = models.CharField(max_length=200)

    def __str__(self):
        return(self.name)

class Room(models.Model):
    code = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    places = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return (self.room_name)



class Course (models.Model):
    """
    Model representing a course(e.g. Programming, Accounting).
    """
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=8)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=200)
#     birth_date = models.DateField(null=True, blank=True)
#     id_card_number = models.CharField(max_length=64)
#     photo = models.ImageField(null=True, blank=True)
#     genre = models.CharField(max_length=2, choices = GENRE_CHOICE)

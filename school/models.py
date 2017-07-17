from django.db import models

class School(models.Model):
    """
    Model representing a course(e.g. University).
    """
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    adress_1 = models.CharField(max_length=200)
    adress_2 = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    authorization_number = models.CharField(max_length=100, null=True, blank=True)

   
    class Meta:
        ordering = ('id',)
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

     def __str__(self):
        return(self.name)
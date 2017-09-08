from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s " %(self.first_name, self.last_name)


class Role(models.Model):
    role_description = models.CharField(max_length=45)

    def __str__(self):
        return (self.role_description)

class UserHasRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


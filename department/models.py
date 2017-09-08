from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=45)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ClassLevel(models.Model):
    label = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

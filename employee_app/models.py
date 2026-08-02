from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    joining_date = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name
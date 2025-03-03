from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Department(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    designation = models.CharField(max_length=200)
    salary = models.IntegerField()
    experience = models.SmallIntegerField()
    department = models.ForeignKey("department", on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, default="", editable=False)


class Contact_details(models.Model):
    number = models.BigIntegerField()
    address = models.CharField(max_length=200)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


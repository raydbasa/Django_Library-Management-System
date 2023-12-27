from django.contrib.auth.models import AbstractUser
from django.db import models


class Gender(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Role(models.Model):
    role_name = models.CharField(max_length=50)


class Semester(models.Model):
    semester_name = models.CharField(max_length=50)


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)


class City(models.Model):
    city_name = models.CharField(max_length=50)


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.SET(1))

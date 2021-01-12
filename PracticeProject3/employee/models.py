from django.db import models

# Create your models here.

class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
    ]

    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122, blank=True)
    email = models.EmailField(max_length=122)
    gender = models.CharField(choices=GENDER_CHOICES ,max_length=1)
    phone_num = models.CharField(max_length=16)
    address = models.TextField()
    job = models.ManyToManyField('AvailableJobs', blank=True)
    date_of_birth = models.DateField()


class AvailableJobs(models.Model):
    name = models.CharField(max_length=60, blank=True)

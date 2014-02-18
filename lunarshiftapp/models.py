from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=100)
	email  = models.CharField(max_length=50)
	password = models.CharField(max_length=200)

class Managers(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person)

class Staff(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person)
	availableHours = 

class Schedule(models.Model):

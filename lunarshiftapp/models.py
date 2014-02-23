from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)
	availableTimes = Schedule

class Managers(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person)

class Staff(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person)

class Schedule(models.Model):
	#matrix = [[0 for x in xrange(24)] for x in xrange(7)] 

class Schedules(models.Model):
	

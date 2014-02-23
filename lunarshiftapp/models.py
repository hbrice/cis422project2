from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)
	#availableTimes = Schedule

class Manager(models.Model):
	employee = models.ForeignKey(Employee)
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)


#class Schedule(models.Model):
	#matrix = [[0 for x in xrange(24)] for x in xrange(7)] 

#class Schedules(models.Model):
	

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)
<<<<<<< HEAD
	#availableTimes = Schedule
=======
>>>>>>> c86b9a23753d58efc19e6665c1d1503ec6e78c80

class Manager(models.Model):
	employee = models.ForeignKey(Employee)
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)


<<<<<<< HEAD
#class Schedule(models.Model):
	#matrix = [[0 for x in xrange(24)] for x in xrange(7)] 

#class Schedules(models.Model):
	
=======
class Schedules(models.Model):
	userID = models.ForeignKey(User, unique=True)
	start = models.CharField(max_length=6) #format HR:DAY
	end = models.CharField(max_length=6) #format HR:DAY
	scheduleID = models.IntegerField(default=0)

class Availability(models.Model):
	userID = models.ForeignKey(User, unique=True)
	start = models.CharField(max_length=6) #format HR:DAY
	end = models.CharField(max_length=6) #format HR:DAY
	isAvailable = models.BooleanField(initial=True)
>>>>>>> c86b9a23753d58efc19e6665c1d1503ec6e78c80

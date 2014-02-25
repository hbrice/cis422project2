from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)

class Manager(models.Model):
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)


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

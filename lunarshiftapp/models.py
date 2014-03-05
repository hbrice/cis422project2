from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MONDAY = 'M'
TUESDAY = 'T'
WEDNESDAY = 'W'
THURSDAY = 'TH'
FRIDAY = 'F'
SATURDAY = 'S'
SUNDAY = 'SU'
AVAIL_DAY_CHOICES = ((MONDAY, 'M'),
	(TUESDAY, 'T'), (WEDNESDAY, 'W'),
	(THURSDAY, 'TH'), (FRIDAY, 'F'),
	(SATURDAY, 'S'), (SUNDAY, 'SU'))

class Employee(models.Model):
	user = models.ForeignKey(User, unique=True)
	company = models.CharField(max_length=100)
	isManager = models.BooleanField(default=False)
	setAvailibity = models.BooleanField(default=False)

class Availibity(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	
class Schedule(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	monthForSched = DateField(auto_now_add=True)

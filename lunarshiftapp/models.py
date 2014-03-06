from django.db import models
from django.contrib.auth.models import User

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

	def  __unicode__(self):
		name = self.user.first_name + ' ' + self.user.last_name
		work = name + ' works for ' + self.company + ' and is a Manager ' + str(self.isManager)
		avail =  ' and has set there availibity ' + str(self.setAvailibity)
		output = work + '\n' + avail
		return output

class Availibity(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')

	def __unicode__(self):
		name = self.user.first_name + ' ' + self.user.last_name
		avail = ' is availible ' + self.AvailibleDay + ' at ' + self.start_time + ' to ' + self.end_time
		return name + avail

class Schedule(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	monthForSched = models.DateField('month created', auto_now_add=True)

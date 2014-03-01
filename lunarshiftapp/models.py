from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):	
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)

class Employee(models.Model):
	manager = models.ForeignKey(Manager)
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)

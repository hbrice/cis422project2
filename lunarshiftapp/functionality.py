import models
from models import Employee, Availibity, Schedule
from datetime import time
from Queue import PriorityQueue
from django.contrib.auth.models import User

class ComputeSchedule:
	def __init__(self, employeeSet, manager):
		self.sched = {'M':[],'T':[],'W':[],'TH':[],'F':[],'S':[],'SU':[]}
		#struct = ScheduleStruct()
		struct = Alternative
		self.k = struct.determineHours(employeeSet, manager)
		self.queue = struct.getQueue()
		
		self.list = []
		
	def produceSchedules(self, list, template, k):
		if queue.empty():
			return
		
		node = queue.get_nowait()
		for x in range(node[0]):
			template[node[2]][node[3]] = node[1][x].user.username
			if k <= 0:
				list.append()
			produceSchedules(self, list, template, k)
		k -= 1
		
		
	
class ScheduleStruct:
	def __init__(self):
		"""
			schedule is a dictionary with a key being the 0 indexed day of the week
			and a 0 indexed hour of the day in military time.
		"""
		
		self.sched = {'M':[],'T':[],'W':[],'TH':[],'F':[],'S':[],'SU':[]}
		self.numberOfHours = 0
	
	def determineHours(self, employeesSet, manager):
		#daysNeedingCoverage return a list of Schedule records, each representing a day that needs coverage
		daysNeedingCoverage = Availibity.objects.filter(user__username=manager) # manager availability is coverage	
		
			
		#store the number of days that are in the schedule
		numberOfdays = len([Availibity.objects.filter(user__username=manager)])
		#variable to store the number of hour chunks needing to be covered
		
		#variable for returning messages (testing)
		returnMsg = ""
		numberOfHours = 0

		#loop through each day that has coverage
		for day in daysNeedingCoverage:
			#loop through each hour of coverage in the day
			for hour in range(day.start_time.hour, day.end_time.hour):
				#get the number of total hours in the schedule that need coverage
				numberOfHours += 1
				poolOfEmployees = []
				#get the set of employees who can cover this hour
				for e in Availibity.objects.filter(AvailibleDay=day):
					if e.start_time.hour>= hour and e.end_time.hour < hour:
						poolOfEmployees.append(e)
				tmpSet = employeesSet
				for x in poolOfEmployees:
					if x.name not in tmpSet:
						tmpSet.remove(x)
				if len(tmpSet) == 0:
					return None
				
				self.sched[day].insert(hour.hour,tmpSet) #(num, emp[])
				
		return numberOfHours
		

	def getQueue(self):
		queue = PriorityQueue(len([Employees.objects.all()]))
		for day in self.sched.keys():
			for hour in self.sched.values():
				queue.put_nowait((len(self.sched[day][hour]),self.sched[day][hour], day, hour)) #(num emps, emps[], day, hour)
				
		return queue
		
class Alternative:
	def __init__(self):
		"""
			schedule is a dictionary with a key being the 0 indexed day of the week
			and a 0 indexed hour of the day in military time.
		"""
		
		self.sched = {'M':[],'T':[],'W':[],'TH':[],'F':[],'S':[],'SU':[]}
		
	
	def determineHours(self, employeesSet, manager):
		#daysNeedingCoverage return a list of Schedule records, each representing a day that needs coverage
		daysNeedingCoverage = Availibity.objects.filter(user__username=manager) # manager availability is coverage	
		
			
		#store the number of days that are in the schedule
		numberOfdays = len([Availibity.objects.filter(user__username=manager)])
		#variable to store the number of hour chunks needing to be covered
		numberOfHours = 0
		#variable for returning messages (testing)
		returnMsg = ""


		#loop through each day that has coverage
		for day in daysNeedingCoverage:
			#loop through each hour of coverage in the day
			for hour in range(day.start_time.hour, day.end_time.hour):
				#get the number of total hours in the schedule that need coverage
				numberOfHours += 1
				#get the set of employees who can cover this hour
				for e in Availibity.objects.filter(AvailibleDay=day):
					if e.start_time.hour>= hour and e.end_time.hour < hour:
						poolOfEmployees.append(e)
				tmpSet = employeeSet
				for x in tmpSet:
					if x.name not in tmpSet:
						tmpSet.remove(x)
				if len(tmpSet) == 0:
					return None
				
				self.sched[day].insert(hour.hour,tmpSet[0]) #(num, emp)
				
		return self.sched
		

import models
from models import Employee, Availibity, Schedule
from datetime import time
from Queue import PriorityQueue
from django.contrib.auth.models import User

class ComputeSchedule:
	def __init__(self, employeeSet, manager):
		self.sched = {'M':[],'T':[],'W':[],'TH':[],'F':[],'S':[],'SU':[]}
		struct = ScheduleStruct()
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
		
	
	def determineHours(self, employeesSet, manager):
		#daysNeedingCoverage return a list of Schedule records, each representing a day that needs coverage
		daysNeedingCoverage = Availibity.objects.get(user__username=manager) # manager availability is coverage	
		
			
		#store the number of days that are in the schedule
		numberOfdays = daysNeedingCoverage.length
		#variable to store the number of hour chunks needing to be covered
		numberofHours = 0
		#variable for returning messages (testing)
		returnMsg = ""


		#loop through each day that has coverage
		for day in daysNeedingCoverage
			#loop through each hour of coverage in the day
			for hour in range(day.start_time, day.end_time)
				#get the number of total hours in the schedule that need coverage
				numberOfHours += 1
				#get the set of employees who can cover this hour
				poolOfEmployees=Availibity.objects.get(AvailibleDay=day, start_time<=hour<=end_time))
				for x in poolOfEmployees:
					if x.name not in employeesSet:
						employeeSet.remove(x)
				if poolOfEmployees.len == 0:
					return None
				
				self.sched[day].insert(hour.hour,poolOfEmployees) #(num, emp[])
				
		return numberOfHours
		

	def getQueue(self):
		queue = PriorityQueue(Employees.objects.all().len)
		for day in self.sched.keys():
			for hour in self.sched.values()
				queue.put_nowait((self.sched[day][hour].len,self.sched[day][hour], day, hour)) #(num emps, emps[], day, hour)
				
		return queue
		

"""
class DateTimeRange:
	def __init__(self, day, start, end):
		"""
			#day is a string as defined above for the day.
			#start and end can be either integers(representing hours) or time objects.
			#creates tuple self.time (day, start, end)
		"""
		startTime = datetime.time(start)
		endTime = datetime.time(end)
		self.time = (day,startTime,endTime)
	
	def isDisjoint(self, otherRng):
		"""
			#DateTimeRange otherRng: other DateTimeRange
			#returns bool whether self and other are disjoint
		"""
		return self.time[0] != otherRng.time[0] or ((self.time[1] < otherRng.time[1]) and (self.time[2] < otherRng.time[1])) or ((otherRng.time[1] < self.time[1]) and (otherRng.time[2] < self.time[1]))
		
	def hours(self):
		"""
			#returns a list of consecutive hours between start and end
		"""
		return List(range(self.time[1].hour,self.time[2].hour + 1))
		
"""

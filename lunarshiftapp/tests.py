from django.test import TestCase


from lunarshiftapp.models import Employee
from lunarshiftapp.models import Availibity
from lunarshiftapp.models import Schedule

# Create your tests here.

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(user="alice", company="macrosloft", isManager=False, setAvailibility = True)
        Employee.objects.create(user="bob", company="macrosloft", isManager=True, setAvailibility = True)
        Employee.objects.create(user="phil", company="macrosloft", isManager=False, setAvailibility = False)

class AvailibityTestCase(TestCase):
    def setUp(self):
        Availibity.objects.create(user="alice", AvailibleDay = 'M', start_time = "1:00" end_time = "5:00")
        
class ScheduleTestCase(TestCase):
    def setUp(self):
        print "placeholder"

"""
Example:

from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
"""


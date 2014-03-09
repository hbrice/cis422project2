from django.test import TestCase

import lunarshiftapp.models  #uhh not sure about these
import lunarshiftapp.data_models
# Create your tests here.
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

"""
class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(user="alice", company="macrosloft", isManager=False, setAvailibility = True)
        Employee.objects.create(user="bob", company="macrosloft", isManager=True, setAvailibility = True)
        Employee.objects.create(user="phil", company="macrosloft", isManager=False, setAvailibility = False)

    def test_isDisjoint(self):
"""        

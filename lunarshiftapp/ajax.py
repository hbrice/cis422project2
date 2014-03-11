from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

# Example from dajax website
@dajaxice_register
def multipy(request, a , b):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result', 'value', str(result))
	return dajax.json()
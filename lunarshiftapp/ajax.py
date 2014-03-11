from dajax.core import Dajax

# Example from dajax website
def multipy(request, a , b):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result', 'value', str(result))
	return dajax.json()
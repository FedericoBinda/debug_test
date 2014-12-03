import numpy as np

def factorial(a):
	"""return factorial of a"""
	if a == 0:
		return 1
	else:
		return np.prod(np.arange(int(a))+1)
	
def test_factorial():
	assert(factorial(0) == 1)
	assert(factorial(1) == 1)
	assert(factorial(4) == 24)
	
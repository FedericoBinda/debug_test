import numpy as np

def factorial(a):
	"""return factorial of a"""
	if a == 0:
		return 1
	else:
		return np.prod(np.arange(int(a))+1)
		
def another_func(a):
	"""just return a"""
	return 0
	
def test_factorial():
	assert(factorial(0) == 1)
	assert(factorial(1) == 1)
	assert(factorial(4) == 24)
	
def test_another_func():
	assert(another_func(0) == 0)
	assert(another_func(2) == 2)
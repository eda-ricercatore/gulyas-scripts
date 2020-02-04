#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s
# Use the math.ceil() and math.floor() functions
import math


"""
	A Python object to test performing an addition operation
		between a Python object that is not a basic data type
		and a number.
"""
class my_object:
	property = 0


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	# Add an integer to a string.
	a = 24
	b = "kobe bryant"
	try:
		c = a + b
		print("c is:", c, ".")
	except TypeError:
		# TypeError: unsupported operand type(s) for +: 'int' and 'str'
		print("=	Error: An addition operation cannot be performed between an integer and a string.")
	# Add a floating point number to a string.
	a = -54.26
	b = "kobe bryant"
	try:
		c = a + b
		print("c is:", c, ".")
	except TypeError:
		# TypeError: unsupported operand type(s) for +: 'float' and 'str'
		print("=	Error: An addition operation cannot be performed between a floating-point number and a string.")
	# Add an integer to a Python object.
	a = 24
	b = my_object()
	try:
		c = a + b
		print("c is:", c, ".")
	except TypeError:
		# TypeError: unsupported operand type(s) for +: 'int' and 'my_object'
		print("=	Error: An addition operation cannot be performed between an integer and a Python object.")
	# Add a floating point number to a Python object.
	a = 457687.45678096589
	b = my_object()
	try:
		c = a + b
		print("c is:", c, ".")
	except TypeError:
		# TypeError: unsupported operand type(s) for +: 'float' and 'my_object'
		print("=	Error: An addition operation cannot be performed between a floating-point number and a Python object.")
	# Add a Python object to a string.
	a = my_object()
	b = "Steph Curry"
	try:
		c = a + b
		print("c is:", c, ".")
	except TypeError:
		# TypeError: unsupported operand type(s) for +: 'my_object' and 'str'
		print("=	Error: An addition operation cannot be performed between a Python object and a string.")
	a = my_object()
	if 3489 == a:
		print("=Err	a = 3489!!!")
	else:
		print("=	Object a is not 3489.")
	a = "LeBron James"
	if 3489 == a:
		print("=Err	a = 3489!!!")
	else:
		print("=	String a is not 3489.")
	a = [12, 3, 5, "Hola todos", 348, 134523332]
	print("a is:",a,"=")
	absolute_list_of_numbers = []
	try:
		for elem in a:
			absolute_list_of_numbers.append(abs(elem))
		print("absolute_list_of_numbers is:",absolute_list_of_numbers,"=")
	except TypeError:
		# TypeError: bad operand type for abs(): 'str'
		print("= List contains a string, or an object, that cannot be processed as a number.")
	try:
		arith_avg = s.mean(a)
	except TypeError:
		# TypeError: can't convert type 'str' to numerator/denominator
		print("= A list can contain elements belonging to multiple classes.")

#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to test concepts with different
		or unusual operations with numbers.
"""

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


print("= Test if an object is a number object.")
print("isinstance(10, (int, float, complex):",isinstance(10, (int, float, complex)),".")
print("isinstance(float('NaN'), (int, float, complex)):",isinstance(float('NaN'), (int, float, complex)),".")
print("isinstance(float('nan'), (int, float, complex)):",isinstance(float('nan'), (int, float, complex)),".")
print("isinstance(float('inf'), (int, float, complex)):",isinstance(float('inf'), (int, float, complex)),".")
print("isinstance(float('-inf'), (int, float, complex)):",isinstance(float('-inf'), (int, float, complex)),".")
print("isinstance(True, (int, float, complex)) and not isinstance(True, bool):",isinstance(True, (int, float, complex)) and not isinstance(True, bool),".")
print("NaN, nan, inf, and -inf cannot be cast into integer objects.")


print("")
print("isinstance(457679, int) is:",isinstance(457679, int),"=")
print("isinstance(12.342, int) is:",isinstance(12.342, int),"=")
print("isinstance(12.342, float) is:",isinstance(12.342, float),"=")
print("isinstance(00, int) is:",isinstance(00, int),"=")
print("isinstance(0000000, int) is:",isinstance(0000000, int),"=")
print("")


try:
	print("isinstance(float('NaN'), (int, float, complex)):",isinstance(int('NaN'), (int, float, complex)),".")
except ValueError:
	print("= ValueError caught. Cannot cast NaN into an integer.")

try:
	print("isinstance(float('nan'), (int, float, complex)):",isinstance(int('nan'), (int, float, complex)),".")
except ValueError:
	print("= ValueError caught. Cannot cast nan into an integer.")

try:
	print("isinstance(float('inf'), (int, float, complex)):",isinstance(int('inf'), (int, float, complex)),".")
except ValueError:
	print("= ValueError caught. Cannot cast inf into an integer.")

try:
	print("isinstance(float('-inf'), (int, float, complex)):",isinstance(int('-inf'), (int, float, complex)),".")
except ValueError:
	print("= ValueError caught. Cannot cast '-inf' into an integer.")








print("isinstance(complex('5-9j'), (int, float, complex)):",isinstance(complex('5-9j'), (int, float, complex)),".")
print("isinstance(complex('5-9j'), (int, float)):",isinstance(complex('5-9j'), (int, float)),".")


try:
	if None.isnumeric():
		print("= Error!	The 'None' object should not be a number.")
	else:
		print("= The 'None' object is not a number.")
except AttributeError:
	print("= AttributeError caught. The 'None' object is not a number.")

temp_str = "6273879432er435"
if temp_str.isnumeric():
	print("= Error!	temp_str should not be a number")
else:
	print("= temp_str is not a number")

temp_str = "45768798"
if temp_str.isnumeric():
	print("= temp_str is a number")
else:
	print("= Error! temp_str should be a number")


temp_str = "12.435346"
if temp_str.isnumeric():
	print("= temp_str is a floating-point number.")
else:
	print("= Error! temp_str should be a floating-point number")
	print("The period in floating-point numbers causes it to be False.")
	# From \cite[Built-in Types]{DrakeJr2016b}
	print("isnumeric() returns 'True if all characters in the string are numeric characters, and there is at least one character, False otherwise'")
	


temp_str = "I love saag paneer."
if temp_str.isnumeric():
	print("= Error!	temp_str should not be a number. It is a string.")
else:
	print("= temp_str is a string.")

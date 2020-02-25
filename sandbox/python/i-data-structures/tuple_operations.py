#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		a Python dictionary.
	
	References:
	+ Refsnes Data staff, "Python Dictionaries", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/python_dictionaries.asp;
			February 3, 2020 was the last accessed date.
	+ Refsnes Data staff, "Python Dictionary values() Method", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/ref_dictionary_values.asp;
			February 3, 2020 was the last accessed date.
	+ Refsnes Data staff, "Python Dictionary keys() Method", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/ref_dictionary_keys.asp;
			February 3, 2020 was the last accessed date.
	+ \cite[Section/Chapter 5, Data Structures]{Brandl2017a}
	+ See references cited in the source code.
	+ [Wikipedia contributors2019]
		- Wikipedia contributors, "CAR and CDR," in Wikipedia, The Free
			Encyclopedia: Lisp (programming language), Wikimedia Foundation,
			San Francisco, CA, August 28, 2019.
			Available online from Wikipedia, The Free Encyclopedia:
				Lisp (programming language) at: https://en.wikipedia.org/wiki/CAR_and_CDR;
				February 19, 2020 was the last accessed date.
"""


# ============================================================
# Import packages and modules from Python libraries.
import pandas as pd



"""
	A Python object to test performing an addition operation
		between a Python object that is not a basic data type
		and a number.
"""
class my_object:
	property = 678


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	a = my_object()
	# Create a tuple of objects belonging to different classes.
	tuple_of_obj_of_diff_classes = (63.4, 299792458, "standard acceleration due to gravity", 9.80665, a, 101325)
	print("= Enumerate a tuple")
	for item in tuple_of_obj_of_diff_classes:
		print("	item is:", item, ".")
	print("= End enumeration of a tuple")
	print("tuple_of_obj_of_diff_classes is:",tuple_of_obj_of_diff_classes,"=")
	print("tuple_of_obj_of_diff_classes[1] is:",tuple_of_obj_of_diff_classes[1],"=")
	print("tuple_of_obj_of_diff_classes[3] is:",tuple_of_obj_of_diff_classes[3],"=")
	print("--------------------------------------------------")
	thistuple = ("apple", "banana", "cherry")
	try:
		thistuple[3] = "orange" # This will raise an error
	except TypeError:
		# TypeError: 'tuple' object does not support item assignment
		print("= tuples are immutable; they cannot be modified.")
		print("  items cannot be added to tuples.")
	try:
		thistuple[2] = None # This will raise an error
	except TypeError:
		# TypeError: 'tuple' object does not support item assignment
		print("= tuples are immutable; they cannot be modified.")
		print("  items cannot be removed from tuples.")
	print("--------------------------------------------------")
	print(thistuple)
	del thistuple
	try:
		print(thistuple)
	except NameError:
		# NameError: name 'thistuple' is not defined
		print("= thistuple has been deleted, no longer exists, & can't be accessed.")
	print("--------------------------------------------------")
	tuple1 = ("a", "b" , "c")
	tuple2 = (1, 2, 3)
	tuple3 = tuple1 + tuple2
	print("tuple1 is:",tuple1,".")
	print("tuple2 is:",tuple2,".")
	print("tuple3 is:",tuple3,".")
	print("--------------------------------------------------")
	tuple4 = ("mouse", [8, 4, 6], (1, 2, 3, 9, 8, 7))
	print("tuple4 is:",tuple4,".")
	# nested index
	print("tuple4[0][3] is:",tuple4[0][3])		# 's'
	print("tuple4[1][1] is:",tuple4[1][1])		# 4
	print("tuple4[2][4] is:",tuple4[2][4])		# 8
	print("--------------------------------------------------")
	"""
		From \cite[Learn Programming: Learn Python Programming, The Definitive Guide: Python Tuple]{ParewaLabsStaff20XY};
			available at: https://www.programiz.com/python-programming/tuple;
				last accessed on February 4, 2020.
	"""
	my_tuple = ('a','p','p','l','e',)
	print("my_tuple is:",my_tuple,".")
	# In operation: Is a character/element/object in the tuple?
	# Output: True
	print("'a' in my_tuple",'a' in my_tuple,"=")
	# Output: False
	print("'b' in my_tuple",'b' in my_tuple,"=")
	# Not in operation: Is a character/element/object not in the tuple?
	# Output: True
	print("'g' not in my_tuple",'g' not in my_tuple,"=")
	print("--------------------------------------------------")
	low_and_high_values = (-1, 0.5)
	print("Number of elements in low_and_high_values, only 1 tuple:",len(low_and_high_values),"=")
	if 0.5 in low_and_high_values:
		print("	0.5 is in 'low_and_high_values'.")
	else:
		print("	0.5 is NOT in 'low_and_high_values'.")
	if 2.5 not in low_and_high_values:
		print("	2.5 is not in 'low_and_high_values'.")
	else:
		print("	2.5 IS IN 'low_and_high_values'.")
	low_and_high_values = (-1, -4.5)
	if -4.5 in low_and_high_values:
		print("	-4.5 is in 'low_and_high_values'.")
	else:
		print("	-4.5 is NOT in 'low_and_high_values'.")
	print("--------------------------------------------------")
	low_and_high_values = ((-1,0.5), (-1,1), (-0.5,0.5), (23,8), (-0.5,1), (0,1))
	print("Number of elements in low_and_high_values, tuple of tuples:",len(low_and_high_values),"=")
	test_value = -0.5
	#if (-0.5) in low_and_high_values:
	if test_value in low_and_high_values:
		print("	-0.5 is in 'low_and_high_values'.")
	else:
		print("	-0.5 is NOT in 'low_and_high_values'.")
	print("Only the cdr of cons of tuples in a tuple can be tested with the 'in' operator.")
	if 23 in low_and_high_values:
		print("	23 is in 'low_and_high_values'.")
	else:
		print("	23 is NOT in 'low_and_high_values'.")
	if 8 in low_and_high_values:
		print("	8 is in 'low_and_high_values'.")
	else:
		print("	8 is NOT in 'low_and_high_values'.")
	if 3.5 not in low_and_high_values:
		print("	3.5 is not in 'low_and_high_values'.")
	else:
		print("	3.5 IS IN 'low_and_high_values'.")
	if (-0.5,1) in low_and_high_values:
		print("	(-0.5,1) is in 'low_and_high_values'.")
	else:
		print("	(-0.5,1) is NOT in 'low_and_high_values'.")
	if isinstance(low_and_high_values, tuple):
		print("low_and_high_values is a tuple.")
	else:
		print("low_and_high_values is NOT a tuple.")
	print("--------------------------------------------------")
	for car, cdr in low_and_high_values:
		if isinstance(low_and_high_values, tuple):
			print("	(car",car,"and cdr",cdr,") is a tuple.")
		else:
			print("	(car",car,"and cdr",cdr,") is NOT a tuple.")
	print("--------------------------------------------------")
	"""
	for car, cdr, index in low_and_high_values:
		if isinstance(low_and_high_values, tuple):
			print("	(car",car," and cdr ",cdr,") at index",index," is a tuple.")
		else:
			print("	(car",car," and cdr ",cdr,") at index",index," is NOT a tuple.")
	"""
	for elem in low_and_high_values:
		if isinstance(low_and_high_values, tuple):
			print("	elem is:",elem,"=")
		else:
			print("	elem is:",elem,"=. It is NOT a tuple!!!")
	print("--------------------------------------------------")
	for index, (car, cdr) in enumerate(low_and_high_values):
		if isinstance(low_and_high_values, tuple):
			print("	tuple index", index,"(car",car,"and cdr",cdr,") is a tuple.")
		else:
			print("	tuple index", index,"(car",car,"and cdr",cdr,") is NOT a tuple.")
	print("--------------------------------------------------")
	for index, cur_tuple in enumerate(low_and_high_values):
		if isinstance(low_and_high_values, tuple):
			print("	tuple index is", index,"cur_tuple is",cur_tuple,"=")
		else:
			print("	tuple index is", index,"cur_tuple is",cur_tuple,"=")
	print("--------------------------------------------------")
	empty_tuple = ()
	if not empty_tuple:
		print("	empty_tuple is:",empty_tuple,"=")
	else:
		print("	empty_tuple is NOT empty!!!")
	print("--------------------------------------------------")
	low_and_high_values = ((-1,0.5,1,"Gracias",-0.5,0,"Ciao mondo!"))
	if isinstance(low_and_high_values, tuple):
		print("	low_and_high_values is a tuple:",low_and_high_values,"=")
	else:
		print("	low_and_high_values is NOT a tuple:",low_and_high_values,"=")
	if 1==len(low_and_high_values):
		print("	low_and_high_values has a tuple:",low_and_high_values,"=")
	else:
		print("	low_and_high_values has multiple elements:",low_and_high_values,"=")
	for index, elem in enumerate(low_and_high_values):
		print("index:",index,"elem is:",elem,"=")
	print("--------------------------------------------------")
	embedded_tuple = (-1,0.5,1,"Gracias",-0.5,0,"Ciao mondo!")
	outer_tuple = (embedded_tuple)
	if 1==len(outer_tuple):
		print("	outer_tuple has a tuple:",outer_tuple,"=")
	else:
		print("	outer_tuple has multiple elements:",outer_tuple,"=")
	print("A tuple cannot be embedded within () to form a tuple of a single tuple.")
	print("A tuple of tuples with one element/tuple is not allowed.")
	print("--------------------------------------------------")
	"""
		Krishna, "Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key", from Guru99: Web: Python: Python Tutorial for Beginners -- Learn Python Programming in 7 Days -- Python Data Structure, Guru99 Tech Pvt Ltd, Ahmedabad, Gujarat, India, 2020.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://www.guru99.com/python-tuples-tutorial-comparing-deleting-slicing-keys-unpacking.html;
				February 25, 2020 was the last accessed date.
	"""
	deeply_embedded_tuple = (((((('geek',),),),),),)
	if 1==len(deeply_embedded_tuple):
		print("	deeply_embedded_tuple has a tuple:",deeply_embedded_tuple,"=")
	else:
		print("	deeply_embedded_tuple has multiple elements:",deeply_embedded_tuple,"=")
	print("--------------------------------------------------")
	deeply_embedded_tuple = (('geek',),)
	if 1==len(deeply_embedded_tuple):
		print("	less loops: deeply_embedded_tuple has a tuple:",deeply_embedded_tuple,"=")
	else:
		print("	less loops: deeply_embedded_tuple has multiple elements:",deeply_embedded_tuple,"=")
	print("--------------------------------------------------")
	if 1==len(deeply_embedded_tuple[0]):
		print("	less loops: deeply_embedded_tuple[0] has a tuple:",deeply_embedded_tuple[0],"=")
	else:
		print("	less loops: deeply_embedded_tuple[0] has multiple elements:",deeply_embedded_tuple[0],"=")
	print("deeply_embedded_tuple[0][0] is:",deeply_embedded_tuple[0][0],"=")
	for index, cur_tuple in enumerate(deeply_embedded_tuple):
		print("	tuple index is:", index,"cur_tuple is:",cur_tuple,"=")
		for idx, em_tuple in enumerate(deeply_embedded_tuple[index]):
			print("	em_tuple index is:", index,"em_tuple is",em_tuple,"=")
	print("--------------------------------------------------")
	deeply_embedded_tuple = (('geek'),)
	for index, cur_tuple in enumerate(deeply_embedded_tuple):
		print("	tuple index is:", index,"cur_tuple is:",cur_tuple,"=")
		for idx, em_tuple in enumerate(deeply_embedded_tuple[index]):
			print("	em_tuple index is:", index,"em_tuple is",em_tuple,"=")
	print("Printed value of the sole string tuple, and the letters of that string.")
	print("--------------------------------------------------")
	deeply_embedded_tuple = (('geek',))
	for index, cur_tuple in enumerate(deeply_embedded_tuple):
		print("	tuple index is:", index,"cur_tuple is:",cur_tuple,"=")
		for idx, em_tuple in enumerate(deeply_embedded_tuple[index]):
			print("	em_tuple index is:", index,"em_tuple is",em_tuple,"=")
	print("Again, printed value of the sole string tuple, and the letters of that string.")
	print("Printing a single tuple, with its own set of brackets, within a set of brackets will not define this as a tuple of a tuple.")
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
	print("tuple_of_obj_of_diff_classes is:",tuple_of_obj_of_diff_classes,".")
	print("--------------------------------------------------")
	thistuple = ("apple", "banana", "cherry")
	try:
		thistuple[3] = "orange" # This will raise an error
	except TypeError:
		# TypeError: 'tuple' object does not support item assignment
		print("= tuples are immutable; they cannot be modified.")
		print("  items cannot be added to or removed from tuples.")
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
	

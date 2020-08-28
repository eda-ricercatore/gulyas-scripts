#!/Users/zhiyang/anaconda3/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3
###	#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to demonstrate how to determine
		the type of Python objects.
	
	References:
	+ [Ong2020]
		- using type() cannot adequately process object/class type,
			due to its lack of support class inheritance;
			in the context of object/class type, class inheritance
				affects object/class type
	+ [Brandl2017a]
		- https://docs.python.org/3/tutorial/inputoutput.html
		- Section 7.2.1 Methods of File Objects
	+ Padraic Cunningham and edobez (Edoardo Bezzeccheri),
		"What can I do with a closed file object?", Stack Exchange Inc.,
		New York, NY, May 19, 2018.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/30379517/1531728 and https://stackoverflow.com/questions/30379488/what-can-i-do-with-a-closed-file-object/30379517#30379517; March 7, 2020 was the last accessed date.
	+ [PythonSoftwareFoundationcontributors2020]
		- https://docs.python.org/3/glossary.html#term-file-object   
	+ [Samaranyake2016]
		- Januka Samaranyake, Answer to "What is meaning of the file object?", Stack Exchange Inc., New York, NY, November 25, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/40798379/1531728 and https://stackoverflow.com/questions/40798143/what-is-meaning-of-the-file-object/40798379#40798379; March 7, 2020 was the last accessed date.
			+ f.mode - The mode attribute of a file object tells you in which mode the file was opened.
			+ f.name - The name attribute of a file object tells you the name of the file that the file object has open.
			+ f.closed - The closed attribute of a file object indicates whether the object has a file open or not. In this case, the file is still open (closed is False).
			+ f.close() - To close a file, call the close method of the file object.
			+ f.seek(0) - The seek method of a file object moves to another position in the open file
			+ f.tell() - The tell method of a file object tells you your current position in the open file
			+ f.read() - T0 read the content of file
"""


# ============================================================
# Import packages and modules from Python libraries.

import pandas as pd
from typing import TextIO




"""
	A Python object to test performing an addition operation
		between a Python object that is not a basic data type
		and a number.
"""
class my_object:
	property = 678


# Method implemented with set comprehension
"""
def remove_suffix(my_str,set_of_substr):
	return 
"""

###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	# Create instances of file object, a and b.
	a = open("../others/object-management/dummy-files/random-1.md","a")
	b = open("../others/object-management/dummy-files/random-2.md","a")
	# Object/Class type: <class '_io.TextIOWrapper'>
	print("type() - class of file object, a, has the type:",type(a),"=")
	"""
		Run-time error when using isinstance() without a type, or
			tuple of types, as a second argument.

		TypeError: isinstance() arg 2 must be a type or tuple of types
	"""
	if isinstance(a, type(a)):
		print("isinstance(obj, cls) - class of file object, a, has the type:=_io.TextIOWrapper=")
	else:
		print("isinstance(obj, cls) - class of file object, a, does not have the type:=_io.TextIOWrapper=")
	if isinstance(b, type(a)):
		print("isinstance(obj, cls) - class of file object, b, has the type:=_io.TextIOWrapper=")
	else:
		print("isinstance(obj, cls) - class of file object, b, does not have the type:=_io.TextIOWrapper=")
	print("= Trying to obtain the type/class of file objects, without using the type() function on an instance of file object to get the type/class.")
	"""
		From: https://www.w3schools.com/python/python_ref_file.asp
		+ 

		Reference:
		+ https://stackoverflow.com/questions/38569401/type-hint-for-a-file-or-file-like-object
	"""
	#if isinstance(b, _io.TextIOWrapper):
	#if isinstance(b, io.TextIOWrapper):
	#if isinstance(b, TextIOWrapper):
	#if isinstance(b, typing.IO):
	if isinstance(b, PyObject):
		print("isinstance(obj, cls) - class of file object, b, has the type:=_io.TextIOWrapper=")
	else:
		print("isinstance(obj, cls) - class of file object, b, does not have the type:=_io.TextIOWrapper=")
	# Close those instances of file object, a and b.
	a.close()
	b.close()
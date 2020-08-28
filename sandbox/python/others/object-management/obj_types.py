#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to determine
		the type of Python objects.
	
	References:
	+ [Brandl2017a]
		- https://docs.python.org/3/tutorial/inputoutput.html
		- \S7.2.1 Methods of File Objects
	+ Padraic Cunningham and edobez (Edoardo Bezzeccheri),
		"What can I do with a closed file object?", Stack Exchange Inc.,
		New York, NY, May 19, 2018.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/30379488/what-can-i-do-with-a-closed-file-object; March 7, 2020 was the last accessed date.
	+ [PythonSoftwareFoundationcontributors2020]
		- https://docs.python.org/3/glossary.html#term-file-object   
https://stackoverflow.com/a/40798379/1531728
   https://stackoverflow.com/questions/40798143/what-is-meaning-of-the-file-object/40798379#40798379   
1 min
   https://docs.python.org/3/tutorial/inputoutput.html   
   f.mode - The mode attribute of a file object tells you in which mode the file was opened.
f.name - The name attribute of a file object tells you the name of the file that the file object has open.
f.closed - The closed attribute of a file object indicates whether the object has a file open or not. In this case, the file is still open (closed is False).
f.close() - To close a file, call the close method of the file object.
f.seek(0) - The seek method of a file object moves to another position in the open file
f.tell() - The tell method of a file object tells you your current position in the open file
f.read() - T0 read the content of file
Januka samaranyake
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
	# Create an instance of file object, a.
	a = open("dummy-files/random.md","a")
	print("file object, a has the type:",a,"=")
	# Close that instance of file object, a.
	a.close()
	# Create an instance of a file object, a.
	print("file object, a has the type:",a,"=")
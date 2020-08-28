#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to write documents in another folder.

	Synopsis: command name and [argument(s)]
	./b-file-writer.py

	Revision History:
	September 11, 2018			Version 0.1, initial build.

	References:
	+ [Przywoski2015]
		- https://python-reference.readthedocs.io/en/latest/docs/file/closed.html
		- Page title: closed
	+ [zmo2019]
		- zmo and Aran-Fey, Answer to "What can I do with a closed file object?", Stack Exchange Inc., New York, NY, March 21, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/22127987/1531728 and https://stackoverflow.com/questions/22127960/read-from-file-after-write-before-closing/22127987#22127987; March 7, 2020 was the last accessed date.
	[Brandl2017a]
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


#	The MIT License (MIT)

#	Copyright (c) <2014-2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'September 11, 2018'

###############################################################

"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
				To make system calls.
	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.
	filecmp		For file comparison.
	datetime	For date and time processing.
	json		For parsing JSON files and processing JSON-based data.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
from datetime import date
import datetime
import json


###############################################################
#	Import Custom Python Modules

# Package and module to perform file I/O operations.
#from utilities.file_io import file_io_operations

###############################################################

# Create an output file, for writing purposes only.
op_file_obj = open("test-output-file.md", 'w')
prompt = "	Test: f.open_fo_write(...)	:{}\n"
op_file_obj.write(prompt .format("FAIL!!!"))
prompt = "	Test: f.open_fo_write(...)		:{}\n"
op_file_obj.write(prompt .format("FAIL!!!"))
op_file_obj.close()

"""
	Cannot use multiple file I/O modes

	From the run-time error:
	"ValueError: must have exactly one of create/read/write/append mode"
"""
op_file_obj_1 = open("test-write-to-&-read-from-file.md", 'a+')
op_file_obj_1.write("THis is line #1.\n")
op_file_obj_1.write("THis is line #2.\n")
op_file_obj_1.write("THis is line #3.\n")
op_file_obj_1.write("THis is line #4.\n")
op_file_obj_1.write("THis is line #5.\n")

# Make copies of the closed file object.
copy_1 = op_file_obj_1
copy_2 = op_file_obj_1
"""
	To read this closed file [zmo2019], reset the file object's
		current position to the begining of the file.
"""
op_file_obj_1.seek(0)
# io.UnsupportedOperation: not readable
#print("The file contains the following information:",op_file_obj.read(),"=")
data = op_file_obj_1.read()
print("The 2nd file contains the following information.")
print(data)
op_file_obj_1.write("THis is line #6.\n")
op_file_obj_1.seek(0,0)
data = op_file_obj_1.read()
print("The 2nd file does contain the following information.")
print(data)
op_file_obj_1.write("THis is line #7.\n")
data = op_file_obj_1.read()
print("After read() operation is performed, file object's current location needs to be reset for a proper read() operation.")
print(data)
op_file_obj_1.seek(0,0)
data = op_file_obj_1.read()
print("Try reading the 2nd file again.")
print(data)

op_file_obj_1.close()
if op_file_obj_1.closed:
	print("op_file_obj_1 is closed")
else:
	print("op_file_obj_1 is still open.")

"""
	Quick/easy solution to open file object op_file_obj_1 again [zmo2019].

	Alternate solution from [zmo2019] is more complicated, and not tested.
"""
data = open(op_file_obj_1.name).read()
print("Try reading the 2nd file after it has been closed and reopened.")
print(data)
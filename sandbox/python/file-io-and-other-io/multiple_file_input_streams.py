#!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to experiment with reading
		file read and string operations.


	Synopsis:
	Automatically test file read and string operations.

	This script can be executed as follows:
	./file_read.py




	Revision History:
	September 6, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


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

	pathlib->Path
				For mapping a string to a path.
	datetime	To obtain information about the current date and time.
	time	To obtain information about the current time.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
import time


filename = "README"
with open(filename, "r") as f_obj:
	list_of_lines = f_obj.readlines()
	print("	Number of lines in README file:",len(list_of_lines),"=")
	prompt = "	... Test if first name is provided:		{}."
	if any("first name:" in s for s in list_of_lines):
		print(prompt .format("OK"))
	else:
		print(prompt .format("FAIL!!!"))
	i_certify_statement = "I certify that I have listed all the sources that I used to develop the solutions/code to the submitted work."
	if i_certify_statement in list_of_lines:
		print(prompt .format("OK"))
	else:
		print(prompt .format("FAIL!!!"))
	prompt = "	... Test if 'Aggie honor promise' is provided:	{}."
	aggie_honor_promise = "On my honor as an Aggie, I have neither given nor received any unauthorized help on this academic work."
	if aggie_honor_promise in list_of_lines:
		print(prompt .format("OK"))
	else:
		print(prompt .format("FAIL!!!"))
	print("= Iterate lines in the text file.")
	for line in list_of_lines:
		print("	current line is:",line,"=")
		if line == i_certify_statement:
			print("		found i_certify_statement")
		temp_line = line.strip()
		if temp_line == i_certify_statement:
			print("		found i_certify_statement, with stripped whitespace")
		temp_line = line.lstrip()
		if temp_line == i_certify_statement:
			print("		found i_certify_statement, with stripped whitespace from the front")
		temp_line = line.rstrip()
		if temp_line == i_certify_statement:
			print("		found i_certify_statement, with stripped whitespace from the back")
		if line.rstrip() == aggie_honor_promise:
			print("		found aggie_honor_promise")
	print("= Check if I can iterate through lines of a textfile and strip its trailing whitespace")
	# I can do likewise for leading whitespace. 
	for line in list_of_lines:
		print("	current line is:",line,"=")
		if line.rstrip() == i_certify_statement:
			print("		found i_certify_statement with stripped whitespace during iteration")
		if line.rstrip() == aggie_honor_promise:
			print("		found aggie_honor_promise with stripped whitespace during iteration")
	print("> Check if find substring approach works.")
	"""
		Use find substrings approach to check if the document has
			the i_certify_statement and aggie_honor_promise.
	"""
	if any(i_certify_statement in s for s in list_of_lines):
		print("= Found: i_certify_statement.")
	if any(aggie_honor_promise in s for s in list_of_lines):
		print("= Found: aggie_honor_promise.")

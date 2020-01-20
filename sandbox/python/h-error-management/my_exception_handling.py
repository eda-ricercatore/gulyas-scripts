#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to test how to write error messages
		to standard error (or log messages).

	Synopsis: command name
	./e-print-error-output.py


	References:
	\cite{Ajitsaria2018}



	Revision History:
	September 11, 2018			Version 0.1, initial build.
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
	calendar	For performing operations on dates.
	logging		For debug, info, warning, error, and critical messages.
				+ logging.debug("")
				+ logging.info("")
				+ logging.warning("")
				+ logging.error("")
				+ logging.critical("")
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
import calendar
import logging
from sys import stdin, stdout, stderr



##############################################################

try:
	print("Test raising and catching AssertionError.")
	raise AssertionError("AssertionError occurred.")
except AssertionError:
	print("	Dealing with AssertionError.")

try:
	print("Test raising and catching AssertionError e.")
	raise AssertionError("AssertionError e occurred.")
except AssertionError as e:
	print("	Dealing with AssertionError e.")

"""
	The following does not work with Python 3.6, or Python 3.7
		and beyond.
try:
	print("Test (raising and) catching multiple exceptions.")
	raise AssertionError("AssertionError e occurred.")
except ZeroDivisionError, AssertionError as e:
	print("	Dealing with ZeroDivisionError or AssertionError e.")
"""



"""
The following does not work with Python 3.6, or Python 3.7
	and beyond.
try:
	print("Test (raising and) catching multiple exceptions.")
	raise AssertionError("AssertionError e occurred.")
except ZeroDivisionError, AssertionError:
	print("	Dealing with ZeroDivisionError or AssertionError e.")
"""


try:
	print("Test catching a generic exception.")
	raise AssertionError("AssertionError e occurred.")
except:
	print("	Dealing with generic exception.")




try:
	print("Test catching a sequence of exceptions.")
	raise AssertionError("AssertionError e occurred.")
except AssertionError:
	print("	Dealing with AssertionError.")
except ZeroDivisionError:
	print("	Dealing with AssertionError.")
except:
	print("	Dealing with generic exception.")






try:
	print("Test catching a sequence of exceptions; another order.")
	raise AssertionError("AssertionError e occurred.")
except ZeroDivisionError:
	print("	Dealing with AssertionError.")
except AssertionError:
	print("	Dealing with AssertionError.")
except:
	print("	Dealing with generic exception.")

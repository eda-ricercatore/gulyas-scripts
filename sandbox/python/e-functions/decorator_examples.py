#!/Users/zhiyang/anaconda3/bin/python3

"""
This Python script is written by Zhiyang Ong to try out ideas
	with Python decorators.

Synopsis:
	Execute examples for Python decorators.

	This script can be executed as follows:
	./decorator_examples.py






	References:
	+ !!!Insert references!!!
	+ [Chitipothu2019]

	I am inserting in-text citations and references as needed.


	Note:
	+ I am writing this script from memory.

	Revision History:
	September 6, 2019			Version 0.1	Script.
"""



__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2019'


#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?



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
	time		To obtain information about the current time.
				time_ns version provides information about the
					current time with nanosecond accuracy.
	warnings	Provide warnings to users without terminating the
					program abruptly.
	process_time (& process_time_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	perf_counter (& perf_counter_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	monotonic (& pm_monotonic_ns)
				To monotonically obtain time stamps, for performance
					measurement, and its alternative providing
					nanosecond accuracy.
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


from time import perf_counter as pc_timestamp
from time import perf_counter_ns as pc_timestamp_ns
from time import process_time as pt_timestamp
from time import process_time_ns as pt_timestamp_ns
from time import time_ns as t_ns
from time import monotonic as pm_monotonic
from time import monotonic_ns as pm_monotonic_ns

"""
	References:
	+ [Chitipothu2013]
	+ [Chitipothu2019]
		Anand Chitipothu, "Notes from Advaced Python Workshop," Stack Exchange Inc., New York, NY, July 24, 2013. Available online from  Anand Chitipothu's Web page.: Blog at: https://anandology.com/blog/notes-from-advaced-python-workshop/ and https://anandology.com/blog/notes-from-advaced-python-workshop.html; November 11, 2020 was the last accessed date.
	+ [ProjectJupyterContributors2019]
		- Anand "anandology" Chitipothu, Jupyter Notebook Viewer, from Project Jupyter: nbviewer: Jupyter Notebook Viewer.
		- From: Advanced Python Training at LinkedIn, February 26 - March 1, 2014.
		- Functional Programming
		- Advanced Python Workshop
			* First session
		- Advanced Python Workshop - Functional Programming
		- Advanced Python Workshop - Classes
		- Advanced Python Workshop - Context Managers
		- Advanced Python Workshop - Meta Classes


	
	Has information about Python decorators.
"""
print("= Experimenting with Python decorators from \cite{Chitipothu2019}.")
pc_timestamp_ns()



#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to measure the
		execution time of functions and programs in Python.


	Synopsis:
	Measure the execution time of functions and programs in Python.

	This script can be executed as follows:
	./performance_measurement_1.py





	Notes:
		"Using time.time to measure execution gives you the overall execution time of your commands including running time spent by other processes on your computer. It is the time the user notices, but is not good if you want to compare different code snippets / algorithms / functions / ..."
		https://stackoverflow.com/a/7370883/1531728



	Alternatives:
		https://stackoverflow.com/a/45178581/1531728
			import profile
			profile.run('main()')
		https://stackoverflow.com/a/56591404/1531728
			use snakeviz for performance profiling.




	Reference:
		https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
		gilbert8 and Acumenus, "Measure time elapsed in Python," Stack Exchange Inc., New York, NY, September 14, 2019. Available online from {\it Stack Exchange Inc.: Stack Overflow: Questions} at: \url{https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python} and \url{https://stackoverflow.com/q/7370801/1531728}; September 17, 2019 was the last accessed date.




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
	warnings	Provide warnings to users without terminating the
					program abruptly.
	timeit		To measure current time, get timestamp, and
					determine the elapsed time.
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
import warnings
import timeit


###############################################################
#	Import Custom Python Packages and Modules
"""
	Module to calculate the factorial of a number.
"""
from get_factorial import calculate_factorial

###############################################################
"""
	Module with methods that measure the execution time of functions
		and programs in Python.
"""
class execution_time_measurement:
	# Invalid timestamp.
	invalid_timestamp = -1234567890
	# Initial timestamp.
	initial_timestamp = invalid_timestamp
	# ============================================================
	##	Method to set the initial timestamp.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def set_initial_timestamp():
		execution_time_measurement.initial_timestamp = timeit.timeit()
	# ============================================================
	##	Method to get the initial timestamp.
	#	@return the initial timestamp.
	#	O(1) method.
	@staticmethod
	def get_initial_timestamp():
		return execution_time_measurement.initial_timestamp
	# ============================================================
	##	Method to determine the elapsed time from the initial
	#		timestamp.
	#	@return the elapsed time from the initial timestamp.
	#	O(1) method. 
	@staticmethod
	def get_elapsed_time():
		current_timestamp = timeit.timeit()
		return (current_timestamp - execution_time_measurement.initial_timestamp)


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	# Set the initial timestamp.
	execution_time_measurement.set_initial_timestamp()
	print("Calculate the factorial using recursion.")
	print("= current timestamp:",execution_time_measurement.get_initial_timestamp(),"=")
	for x in range(0,20+1):
		print("	factorial of",x," is:",calculate_factorial.get_factorial_recursion(x),"=")
	print("= elapsed time:",execution_time_measurement.get_elapsed_time(),"=")
	#print("= timeit.timeit():",timeit.timeit(),"=")
	print("Calculate the factorial using iteration.")
	print("= current timestamp:",execution_time_measurement.get_initial_timestamp(),"=")
	for x in range(0,20+1):
		print("	factorial of",x," is:",calculate_factorial.get_factorial_iteration(x),"=")
	print("= elapsed time:",execution_time_measurement.get_elapsed_time(),"=")
	"""
		The timeit.timeit() method can result in negative elapsed time.
	"""	

#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to calculate
		the factorial of a number.


	Synopsis:
	Calculate the factorial of a number.

	This script can be executed as follows:
	./get_factorial.py [a number]

	Parameters:
	[a number]:		A number that the user wants to determine the
						factorial of.


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

###############################################################
"""
	Module with methods that determine the factorial of a number.
"""
class calculate_factorial:
	# Number to determine the factorial of.
	default_number = 10
	# Number to compute the factorial of.
	number_to_compute = 10
	"""
		Number to indicate that the factorial for the given input
			does not exist.
	"""
	does_not_exist = -1234567890
	# ============================================================
	##	Method to process the optional input argument.
	#	If the number is not provided, use the value of "default_number".
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def process_optional_input_argument():
		# If the path to the README file is not specified
		if (2 > len(sys.argv)):
			"""
				The optional input argument is not provided by the
					user.
				We assume that the default number to determine the
					factorial of is indicated by the value of
					"default_number".
			"""
			calculate_factorial.number_to_compute = calculate_factorial.default_number
		else:
			calculate_factorial.number_to_compute = sys.argv[1]
	# ============================================================
	##	Method to determine the factorial of "number_to_compute"
	#		by recursion.
	#	@param given_number - Number to determine the factorial of.
	#	@return the factorial of given_number (if it is a non-negative
	#		integer);
	#		else, return 'None'.
	#	O(n) method, where n is the number of test cases used.
	@staticmethod
	def get_factorial_recursion(given_number):
		if isinstance(given_number, int):
			if (0 == (given_number) or (1 == given_number)):
				return 1
			elif (0 > given_number):
				warnings.warn("The factorial of a negative number cannot be determined.")
				return None
			else:
				return given_number * calculate_factorial.get_factorial_recursion(given_number - 1)
		else:
			warnings.warn("The factorial of a non-integer cannot be determined.")
			return None
	# ============================================================
	##	Method to determine the factorial of "number_to_compute"
	#		by iteration.
	#	@param given_number - Number to determine the factorial of.
	#	@return the factorial of given_number (if it is a non-negative
	#		integer);
	#		else, return 'None'.
	#	O(n) method, where n is the number of test cases used.
	@staticmethod
	def get_factorial_iteration(given_number):
		if isinstance(given_number, int):
			if (0 == (given_number) or (1 == given_number)):
				return 1
			elif (0 > given_number):
				warnings.warn("The factorial of a negative number cannot be determined.")
				return None
			else:
				result = 1
				while (1 < given_number):
					result = result * given_number
					given_number = given_number - 1
				return result
		else:
			warnings.warn("The factorial of a non-integer cannot be determined.")
			return None

###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	print("Calculate the factorial of a given number.")
	# get_factorial_iteration() requires and only accepts 1 input value.
	#calculate_factorial.process_optional_input_argument()
	#calculate_factorial.process_optional_input_argument(324324 23r23 4e5678 56789)
	# Change process_optional_input_argument() to accept no input.
	calculate_factorial.process_optional_input_argument()
	#print("get_factorial_iteration() for default value of 10:",calculate_factorial.get_factorial_iteration(4),"=")
	print("get_factorial_iteration(4):",calculate_factorial.get_factorial_iteration(4),"=")
	# ValueError: invalid literal for int() with base 10: 'my string'
	print("get_factorial_iteration('my string'):",calculate_factorial.get_factorial_iteration("my string"),"=")
	print("get_factorial_iteration(125.23429):",calculate_factorial.get_factorial_iteration(125.23429),"=")
	print("get_factorial_iteration(None):",calculate_factorial.get_factorial_iteration(None),"=")
	

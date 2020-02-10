#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to test how to write unit
		tests using the "unittest" module from The Python
		Standard Library.

	Synopsis: command name
	./trying_out_unittest.py


	References:
	\cite{Shaw2020}



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
	unittest	For unit testing purposes.
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
import unittest


##############################################################


# Module with methods that determine the factorial of a number.
class calculate_factorial(unittest.TestCase):
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
		elif isinstance(given_number, float):
			warnings.warn("The factorial of a floating-point number cannot be determined.")
			return None
		else:
			warnings.warn("The factorial of a non-integer cannot be determined.")
			return None
	# ============================================================
	##	Method to test the recursive factorial calculation method.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, where n is the largest number tested (to
	#		determine the factorial of).
	#		While I may test this for multiple numbers, the
	#			constant/scalar multiple of this is still O(n!).
	#	IMPORTANT NOTES:
	#	+ The "unittest" module uses the method call "unittest.main()"
	#		to run the methods associated with the "self" instance
	#		object \cite[Chapter 9, pp. 183]{Hall2009b}
	#		\cite[Chapters 7, pp. 148]{Hetland2005} \cite{Ong2020}.
	#@staticmethod
	def test_get_factorial_recursion(self):
		self.assertEqual(calculate_factorial.get_factorial_recursion(4),24,"4! should be 24.")
		self.assertEqual(calculate_factorial.get_factorial_recursion(3),6,"3! should be 6.")
		self.assertEqual(calculate_factorial.get_factorial_recursion(5),120,"5! should be 120.")
	# ============================================================
	##	Method to test the recursive factorial calculation method,
	#		just to increase the number of test methods.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, where n is the largest number tested (to
	#		determine the factorial of).
	#		While I may test this for multiple numbers, the
	#			constant/scalar multiple of this is still O(n!).
	#	IMPORTANT NOTES:
	#	+ The "unittest" module uses the method call "unittest.main()"
	#		to run the methods associated with the "self" instance
	#		object \cite[Chapter 9, pp. 183]{Hall2009b}
	#		\cite[Chapters 7, pp. 148]{Hetland2005} \cite{Ong2020}.
	#	+ The actual number of test cases don't matter, since
	#		they are not accounted for.
	#		- The number of instance methods to test methods,
	#			classes/modules, and packages, do.
	#	+ Conclusion:
	#		- Stick to my automated regression testing framework.
	#		- My framework is more informative about what was done
	#			and what test case failed.
	#@staticmethod
	def test_get_factorial_recursion_2(self):
		self.assertEqual(calculate_factorial.get_factorial_recursion(1),1,"1! should be 1.")
		self.assertEqual(calculate_factorial.get_factorial_recursion(0),1,"0! should be 1.")



if __name__ == "__main__":
	unittest.main()

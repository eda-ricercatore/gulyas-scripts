#!/usr/local/bin/python3

"""
	This Python script is written by Zhiyang Ong to test the
		module to calculate the factorial of a number.

	The results for this script are compared to the table of
		factorials in \cite{Pierce2019a}, and validated/verified
		for factorials from 0.
	 

	Synopsis:
	Test module that calculates the factorial of a number.



	Notes/Assumptions:
	+ Only the factorials of non-negative integers can be computed.
	+ If the input to the iterative or recursive factorial function
		is a negative number, not an integer (e.g., floating-point
		number), not a number (e.g., a string), return the "None"
		object for the method caller to process.
		- This avoids having to raise exceptions when users try
			to determine the factorial of anything that is not a
			non-negative integer.
		- See references on exception safety \cite{Abrahams1998,Abrahams2001,WikipediaContributors2016f} \cite[Subsection 4.4 on ``Writing exception safe code'']{WikibooksContributors2016}.


	Revision History:
	September 6, 2019			Version 0.1	Script.

	References:
		[Pierce2019a]
			Rod Pierce, "Factorial Function," from Maths Is Fun, 2019. Available online from "Maths Is Fun: Numbers" at: https://www.mathsisfun.com/numbers/factorial.html; September 19, 2019 is the last access date.
				[No address]
				https://www.mathsisfun.com/citation.php
		[niekas2016]
			niekas and Acumenus, Answer to "In Python, how does one catch warnings as if they were exceptions?," Stack Exchange Inc., New York, NY, June 20, 2016.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/30368735; January 28, 2019 was the last accessed date.
			\cite{niekas2016} in my BibTeX database.
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
#	Import Custom Python Modules

# Utilities package.
# Package and module that compute the factorial of a number.
from utilities.timing_measurements.get_factorial import calculate_factorial


# Statistics package.
"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistic_pkg.test_statistics_tester import statistical_analysis_tester


###############################################################
"""
	Module that tests methods that determine the factorial of
		a number.
"""
class calculate_factorial_tester:
	# ============================================================
	##	Method to test the method to calculate the factorial of
	#		a number by iteration.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	@staticmethod
	def test_get_factorial_iteration():
		print("	Testing calculate_factorial.get_factorial_iteration() method.")
		prompt = "	... Test: get_factorial_iteration(0)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 1 == calculate_factorial.get_factorial_iteration(0):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(1)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 1 == calculate_factorial.get_factorial_iteration(1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(2)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 2 == calculate_factorial.get_factorial_iteration(2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(3)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 6 == calculate_factorial.get_factorial_iteration(3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(4)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 24 == calculate_factorial.get_factorial_iteration(4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(5)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 120 == calculate_factorial.get_factorial_iteration(5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(6)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 720 == calculate_factorial.get_factorial_iteration(6):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(7)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 5040 == calculate_factorial.get_factorial_iteration(7):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(8)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 40320 == calculate_factorial.get_factorial_iteration(8):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(9)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 362880 == calculate_factorial.get_factorial_iteration(9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_iteration(10)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 3628800 == calculate_factorial.get_factorial_iteration(10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			Catch warnings, so that they show up on the command line.
			\cite{niekas2016}
		"""
		with warnings.catch_warnings(record=True) as w:
			# ValueError: invalid literal for int() with base 10: 'my string'
			prompt = "	... Test: get_factorial_iteration('my string')		{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_iteration('my string'):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_iteration('125.23429')		{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_iteration('125.23429'):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_iteration(None)			{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_iteration(None):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_iteration(-345)			{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_iteration(-345):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
	# ============================================================
	##	Method to test the method to calculate the factorial of
	#		a number by recursion.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	@staticmethod
	def test_get_factorial_recursion():
		print("	Testing calculate_factorial.get_factorial_recursion() method.")
		prompt = "	... Test: get_factorial_recursion(0)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 1 == calculate_factorial.get_factorial_recursion(0):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(1)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 1 == calculate_factorial.get_factorial_recursion(1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(2)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 2 == calculate_factorial.get_factorial_recursion(2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(3)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 6 == calculate_factorial.get_factorial_recursion(3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(4)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 24 == calculate_factorial.get_factorial_recursion(4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(5)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 120 == calculate_factorial.get_factorial_recursion(5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(6)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 720 == calculate_factorial.get_factorial_recursion(6):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(7)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 5040 == calculate_factorial.get_factorial_recursion(7):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(8)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 40320 == calculate_factorial.get_factorial_recursion(8):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(9)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 362880 == calculate_factorial.get_factorial_recursion(9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_factorial_recursion(10)			{}."
		statistical_analysis.increment_number_test_cases_used()
		if 3628800 == calculate_factorial.get_factorial_recursion(10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			Catch warnings, so that they show up on the command line.
			\cite{niekas2016}
		"""
		with warnings.catch_warnings(record=True) as w:
			# ValueError: invalid literal for int() with base 10: 'my string'
			prompt = "	... Test: get_factorial_recursion('my string')		{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_recursion('my string'):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_recursion('125.23429')		{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_recursion('125.23429'):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_recursion(None)			{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_recursion(None):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
			prompt = "	... Test: get_factorial_recursion(-345)			{}."
			statistical_analysis.increment_number_test_cases_used()
			if None == calculate_factorial.get_factorial_recursion(-345):
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt .format("FAIL!!!"))
	# =========================================================
	#	Method to test methods that determine the factorial of a
	#		number.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	#
	#	To search for the (specific) test results for this Python
	#		module, search for:
	#	==	Testing class: calculate_factorial. 
	@staticmethod
	def test_get_factorial_methods():
		print("")
		print("")
		print("==	Testing class: calculate_factorial.")
		"""
			"Handle warnings as errors"
			Reference:
			+ niekas and Acumenus, Answer to "In Python, how does one catch warnings as if they were exceptions?," Stack Exchange Inc., New York, NY, June 20, 2016.
				Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/30368735; January 28, 2019 was the last accessed date.
				\cite{niekas2016} in my BibTeX database.
		"""
		calculate_factorial_tester.test_get_factorial_iteration()
		"""
			Add whitespace before testing the factorial computation
				method using recursion.
		"""
		print("")
		calculate_factorial_tester.test_get_factorial_recursion()
		print("")

#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	Check for no usage of the term "error".
	This Python script is written by Zhiyang Ong to test the
		custom exception graph_exception, from the utilities.custom_exceptions package.

	Synopsis:
	Test the custom exception graph_exception.

	Notes/Assumptions:
	None at the moment.


	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	Revision History:
	August 1, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'August 1, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

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
	filecmp		For file comparison.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
# Copy a file from [source] to [destination]
from shutil import copyfile

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
"""
	Package and module to throw/raise the custom exception
		graph_exception.
"""
#from utilities.custom_exceptions.graph_error import graph_err
#import utilities.custom_exceptions.graph_error
from utilities.custom_exceptions.graph_error import *

###############################################################
"""
	Module with method that test the custom exception graph_exception.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "graph_error"
		and "graph_error_tester" objects.
	Test throwing/raising the graph_error exception.
"""
#class my_graph_error_tester:
class graph_error_tester:
	## =========================================================
	#	Method to test throwing/raising the graph_error exception.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def helloworld():
		print(":::	graph_error accessor method works.")
	## =========================================================
	#	Method to test throwing/raising the graph_error exception.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_raising_graph_error():
		print("")
		print("==	Testing the graph_error class/module.")
		try:
			prompt = "	... Test: raise graph_error exception, 2 arguments	{}"
			statistical_analysis.increment_number_test_cases_used()
			#raise graph_error("Can graph_error be caught")
			#raise utilities.custom_exceptions.graph_error("Can graph_error be caught")
			raise graph_error("Can graph_error be caught?","gyou")
		#except utilities.custom_exceptions.graph_error:
		except graph_error:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		try:
			prompt = "	... Test: raise graph_error exception, 1 argument	{}"
			statistical_analysis.increment_number_test_cases_used()
			#raise graph_error("Can graph_error be caught")
			#raise utilities.custom_exceptions.graph_error("Can graph_error be caught")
			raise graph_error("Can graph_error be caught?")
		#except utilities.custom_exceptions.graph_error:
		except graph_error:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))

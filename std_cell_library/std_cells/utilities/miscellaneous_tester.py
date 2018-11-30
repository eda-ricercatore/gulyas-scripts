#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test miscellaneous
		methods in the miscellaneous class.

	Synopsis:
	Perform a subset of the methods in the miscellaneous class.





	Revision History:
	July 31, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 31, 2018'

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
	calendar	For checking if given year is a leap year.
"""

import sys
#import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re
import calendar

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis


"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
"""
	Package and module to perform methods in the miscellaneous
		class.
"""
from utilities.miscellaneous import misc
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester

###############################################################
##	Module with methods that perform miscellaneous tasks.
class misc_tester:
	## =========================================================
	#	Method to test the methods that perform file I/O operations
	#		with an invalid file.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_check_filename_format():
		print("	Testing the filename format checker.")
		prompt = "	... Test: incorrect file extension is '.txt'.		{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.check_filename_format("tyuw.iew"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename no file extension has 6 tokens.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.check_filename_format("HH-MM-SS-uS.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with -ve DD/day.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.check_filename_format("-5-MM-YY-HH-MM-SS-uS.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with DD/day >29, Feb.		{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("35-2-2016-00-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with DD/day=29, Feb, leap year.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.check_filename_format("29-2-2016-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with DD/day=28, Feb, not leap year.	{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("28-2-2017-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with DD/day = 34.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("34-6-2017-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with DD/day=31, 31 day mth.		{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("31-7-2017-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with DD/day=30, 30 day mth.		{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-9-2017-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with MM/month = 0.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-0-2017-00-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with MM/month = -4.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30--4-2017-00-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with MM/month = 15.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-15-2017-00-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with MM/month = 9.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-9-2017-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with YY/year = 1582.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-11-1582-00-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with YY/year = 2083.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("2-2-2083-00-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with HH/hour = -3.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("30-5-2015--3-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with HH/hour = 25.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("3-5-2017-25-00-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with HH/hour = 17.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("12-1-2013-17-00-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with MM/minute = -8.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("7-4-2012-2--8-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with MM/minute = 73.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-73-00-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with MM/minute = 59.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-59-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with MM/minute = 0.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-0-00-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with SS/second = -4.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8--4-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with SS/second = 81.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-81-00.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with SS/second = 36.			{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-36-00.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with uS/microsecond = -129.		{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-4--129.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with uS/microsecond = 16534785929.	{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-32-16534785929.txt"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: filename with uS/microsecond = 0.		{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-32-0.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: filename with uS/microsecond = 999999.	{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			All fields/tokens need to be numbers, else an exception
				would be thrown.
		"""
		if misc.check_filename_format("25-1-2020-5-8-51-999999.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the miscellaneous method that determines
	#		where to store the results of experimental, simulation,
	#		verification, and testing runs.
	#	This does not correct check if the results file is placed
	#		in the correct subdirectory of the results repository.
	#	#### TO BE COMPLETED
	#		Test if the subdirectory is correct. This is busywork.
	#	@param - Nothing
	#	@return a string representing the location to store the
	#		aforementioned results.
	#	O(1) method.
	@staticmethod
	def test_find_desired_location_for_results():
		incorrect_format_result = "'filename' needs to have the format: DD-MM-YY-HH-MM-SS-uS.txt."
		print("==	Test: test_find_desired_location_for_results().")
		test_filename = "25-3-2010-5-8-51-9994073289.dwq"
		results_location = misc.find_desired_location_for_results(test_filename)
		prompt = "	... Test: filename is 25-3-2010-5-8-51-9994073289.dwq.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.find_desired_location_for_results(test_filename) == incorrect_format_result:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		print("==	Test: test_find_desired_location_for_results().")
		test_filename = "25-3-2010-5-8-51-9407.txt"
		results_location = misc.find_desired_location_for_results(test_filename)
		prompt = "	... Test: filename 25-3-2010-5-8-51-9407.txt included.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.check_absolute_path_to_store_results(results_location,test_filename):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: 25-3-2010-5-8-51-9407.txt, correct path.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if misc.get_absolute_path_to_store_results() in results_location:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			"""
			print("results_location:",results_location,"=")
			print("misc.get_absolute_path_to_store_results():",misc.get_absolute_path_to_store_results(),"=")
			print(results_location.find(misc.get_absolute_path_to_store_results()))
			"""
	## =========================================================
	#	Method to test the miscellaneous methods.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_miscellaneous_methods():
		print("==	Testing class: misc_tester.")
		misc_tester.test_check_filename_format()
		misc_tester.test_find_desired_location_for_results()

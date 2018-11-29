#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to test the automatically generated
		filename to store experimental data/results from running
		experiments/simulations, and/or automated software regression
		testing and hardware regression verification.



	Synopsis:
	Test if the generated filename conforms to the filename format
		that I have specified.

	Check if the filename is based on the following format:
		DD-MM-YY-HH-MM-SS.txt
	If it is not, warn the user.
		This is because it may create difficulties in developing
			scripts to process, analyze, and visualize the data.



	Notes/Assumptions:
	Since I would be categorizing and storing the experimental results
		based on the year and month, the filename containg experimental
		results would be named in the DD-MM-YY-HH-MM-SS format so that
		I can quickly find the file of a given build (or experimental
		run) as I read the filename from left to right.



	References:
	\cite{SaltyCrane2014}
		Eliot "Salty Crane", "How to get the current date and time in Python," from Salty Crane Blog, June 26, 2008. Available online from Salty Crane Blog at: https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/; modified on October 22, 2014; self-published; August 31, 2018 was the last accessed date

	\cite[datetime module, \S8.1.4 datetime Objects, now() function]{DrakeJr2016b}



	Revision History:
	April 17, 2017			Version 0.1, initial build.
"""


#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'Apr 17, 2017'

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
	calendar	For checking if given year is a leap year.
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
import calendar

###############################################################

#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to generate filename with time stamp.
from utilities.generate_results_filename import generate_filename
# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args


###############################################################
class generate_filename_tester:
	##	Method to check if the current month has 31 days.
	#	@param mm - Input month to determine if it has 31 days.
	#	@return a boolean true, if the current month has 31 days.
	#	O(1) method.
	@staticmethod
	def is_31_day_month(mm):
		if mm in [1, 3, 5, 7, 8, 10, 12]:
			return True
		else:
			return False
	##	Method to check if the current month has 30 days.
	#	@param mm - Input month to determine if it has 30 days.
	#	@return a boolean true, if the current month has 30 days.
	#	O(1) method.
	@staticmethod
	def is_30_day_month(mm):
		if mm in [4, 6, 9, 11]:
			return True
		else:
			return False
	##	Method to test method for generating a filename with
	#		the current time stamp.
	#	@param - Nothing.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def check_filename_format():
		print("	Generate a filename with the current time stamp.")
		temp_op_filename = generate_filename.create_filename()
		print("	Testing filename:",temp_op_filename,"=")
		print("	Check against the format: DD-MM-YY-HH-MM-SS.txt")
		print("	Tokenize generated filename.")
		# Tokenize the generated filename with the delimiter "-".
		tokens = temp_op_filename.split("-")
		"""
			Check against the format: DD-MM-YY-HH-MM-SS.txt.
			tokens[0] = DD/Day
			tokens[1] = MM/Month
			tokens[2] = YY/Year
			tokens[3] = HH/Hour
			tokens[4] = MM/Minute
			tokens[5] = SS/Second
		"""
		print("	Testing if 1st token is appropriate date (DD/date value).")
		prompt = "	... Test: DD value is >= 0.				{}"
		statistical_analysis.increment_number_test_cases_used()
		if 1 <= int(tokens[0]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# If month is February during a leap year, DD <= 29.
		prompt = "	... Test: DD value is <= 29, leap year Feb.		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 2 == int(tokens[1]) and 29 < int(tokens[0]) and calendar.isleap(tokens[2]):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		# If year isn't a leap year & month is February, DD <= 28.
		prompt = "	... Test: DD value is <= 28, non-leap year Feb.		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 2 == int(tokens[1]) and 29 < int(tokens[0]) and not calendar.isleap(tokens[2]):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: DD value is <= 30, 30-day month.		{}"
		statistical_analysis.increment_number_test_cases_used()
		if generate_filename_tester.is_30_day_month(tokens[1]) and 30 < int(tokens[0]):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: DD value is <= 31, 31-day month.		{}"
		statistical_analysis.increment_number_test_cases_used()
		if generate_filename_tester.is_31_day_month(tokens[1]) and 31 < int(tokens[0]):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		print("	Testing if 2nd token is appropriate date (MM/month value).")
		prompt = "	... Test: MM/month value is >= 1.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 1 <= int(tokens[1]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: MM/month value is <= 12.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 12 >= int(tokens[1]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		print("	Testing if 3rd token is appropriate date (YY/year value).")
		prompt = "	... Test: YY/year value is >= 2000.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 2000 <= int(tokens[2]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		print("	Testing if 4th token is appropriate date (HH/hour value).")
		prompt = "	... Test: HH/hour value is >= 0.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 <= int(tokens[3]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: HH/hour value is <= 23.			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 23 >= int(tokens[3]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	##	Method to test methods associated with generating filename with
	#		the current time stamp.
	#	@param - Nothing.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_filename_generation_methods():
		print("==	Testing class: generate_filename.")
		generate_filename_tester.check_filename_format()











#	Python database management
#	Python: date, time, now, string
#	Add references.
#	\cite{Hetland2005,Lutz2010,Lutz2011,Sileika2010,Younker2008}.
#	\cite[Chp. 17,25]{Beazley2009}

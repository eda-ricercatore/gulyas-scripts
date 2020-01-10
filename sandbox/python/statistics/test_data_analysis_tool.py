#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to test
		miscellaneous tasks in analyzing data.


	Synopsis:
	Test the miscellaneous tasks in analyzing data.


	Revision History:
	December 15, 2017			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'December 15, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2018> <Zhiyang Ong>

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

	collections -> namedtuple
				To use named tuples.
	operator -> attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
	statistics	Module with functions for mathematical statistics
					functions.
"""

#import sys
#import os
#import os.path
#from subprocess import call
#import time
import warnings
#import re
#from collections import namedtuple
#from operator import attrgetter
import statistics as s

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistics.data_analysis_tool import data_analysis





###############################################################
"""
	Module that tests the methods for performing miscellaneous
		tasks in data analysis.

	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "statistical_analysis"
		objects.

	Test each static method of the "data_analysis" class.
"""
class data_analysis_tester:
	## =========================================================
	#	Method to test the method that accesses reference values
	#		for a corresponding particular attribute/property,
	#		using the Python dictionary containing pairs/2-tuples
	#		of attributes/properties and values.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_reference_value():
		print("	Testing get_reference_value() method.")
		speed_of_light = 299792458
		#prompt = "	... Test: get_reference_value(c) == 299792458		{}"
		prompt = "	... Test: get_reference_value(c) == "
		prompt = prompt + str(speed_of_light) + "		{}"
		statistical_analysis.increment_number_test_cases_used()
		if speed_of_light == data_analysis.get_reference_value("c"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: method with default option == "
		prompt = prompt + str(speed_of_light) + "	{}"
		statistical_analysis.increment_number_test_cases_used()
		if speed_of_light == data_analysis.get_reference_value():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		standard_acceleration_due_to_gravity = 9.80665
		prompt = "	... Test: get_reference_value(g) == "
		prompt = prompt + str(standard_acceleration_due_to_gravity) + "		{}"
		statistical_analysis.increment_number_test_cases_used()
		if standard_acceleration_due_to_gravity == data_analysis.get_reference_value("standard acceleration due to gravity"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		standard_atmosphere = 101325
		prompt = "	... Test: get_reference_value(std atm) == "
		prompt = prompt + str(standard_atmosphere) + "	{}"
		statistical_analysis.increment_number_test_cases_used()
		if standard_atmosphere == data_analysis.get_reference_value("standard atmosphere"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the actual
	#		change between quantity1 and quantity2.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_actual_change():
		print("	Testing get_actual_change() method.")
		prompt = "	... Test: default option, get_actual_change(0,0) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_actual_change():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_actual_change(19,13) == 6			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 6 == data_analysis.get_actual_change(19,13):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_actual_change(10,14) == -4		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -4 == data_analysis.get_actual_change(10, 14):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_actual_change(-20,27) == -47		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -47 == data_analysis.get_actual_change(-20,27):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_actual_change(-7,-3) == -4		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -4 == data_analysis.get_actual_change(-7,-3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_actual_change(-4,-9) == 5			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 5 == data_analysis.get_actual_change(-4,-9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the absolute
	#		difference between quantity1 and quantity2.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_absolute_difference():
		print("	Testing get_absolute_difference() method.")
		prompt = "	... Test: default, get_absolute_difference(0,0) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_absolute_difference():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_absolute_difference(19,13) == 6		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 6 == data_analysis.get_absolute_difference(19,13):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_absolute_difference(10,14) == 4		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 4 == data_analysis.get_absolute_difference(10, 14):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_absolute_difference(-20,27) == 47		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 47 == data_analysis.get_absolute_difference(-20,27):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_absolute_difference(-7,-3) == 4		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 4 == data_analysis.get_absolute_difference(-7,-3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_absolute_difference(-4,-9) == 5		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 5 == data_analysis.get_absolute_difference(-4,-9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the relative change
	#		between quantity1 and quantity2.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_relative_change():
		print("	Testing get_relative_change() method.")
		prompt = "	... Test: default, get_relative_change(1,1) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_change():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_change(15,12) == 0.25		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.25 == data_analysis.get_relative_change(15,12):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print("data_analysis.get_relative_change(15,12):",data_analysis.get_relative_change(15,12),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_change(18,20) == -0.10		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -0.10 == data_analysis.get_relative_change(18,20):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_relative_change(18,20):",data_analysis.get_relative_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_change(-97,-100) == -0.10		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -0.10 == data_analysis.get_relative_change(18,20):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_relative_change(18,20):",data_analysis.get_relative_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
	# =========================================================
	##	Method to test the methods that perform miscellaneous
	#		tasks in data analysis.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_data_analysis():
		print("")
		print("")
		print("-------------------------------------------------")
		print("==	Testing class: data_analysis.")
		data_analysis_tester.test_get_reference_value()
		print("")
		data_analysis_tester.test_get_actual_change()
		print("")
		data_analysis_tester.test_get_absolute_difference()
		print("")
		data_analysis_tester.test_get_relative_change()
		# TEST ALL METHODS!!!

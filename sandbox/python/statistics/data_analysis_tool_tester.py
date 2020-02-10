#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3
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
	math		Use the math.isclose(number_1,number_2) function
					to determine if the numbers "number_1" and
					"number_2" are approximately equal.
	numpy.testing
				To use numpy.testing.assert_almost_equal() function.
				+ To compare if two numbers are approximately the same.
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
import math
import numpy as np
"""
	To use the npt.assert_approx_equal() function.
		Or, np.testing.assert_almost_equal() function.
		Or, numpy.testing.assert_almost_equal() function.
"""
#import np.testing as npt
import numpy.testing as npt

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis
"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistic_pkg.data_analysis_tool import data_analysis





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
	#	Method to test the method determining if each object
	#		in a list is an integer or a floating-point number.
	#	@param - None.
	#	@return - Nothing.
	#	O(n) method, where "n" is the maximum size of the lists
	#		being tested.
	@staticmethod
	def test_is_list_of_numbers():
		print("	Testing is_list_of_numbers() method.")
		list_of_objs = None
		prompt = "	... Test: is_list_of_numbers(None) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		not_a_list_obj = data_analysis()
		prompt = "	... Test: is_list_of_numbers(not_a_list_obj) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(not_a_list_obj):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_list_of_numbers([]) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers([]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_1 = [-221, 247, 0, "Ciao tutti!", 576372.32604]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_1) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(list_not_pure_numbers_1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_2 = ["Buona serata!"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_2) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(list_not_pure_numbers_2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_3 = ["Laszlo Tabori is a world record holder!", 2673, 92.23, 7823, 10129, 478334]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_3) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(list_not_pure_numbers_3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_4 = [54.2, 0.232, 2439, 1392849, "Albert-László Barabási"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_4) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(list_not_pure_numbers_4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = data_analysis()
		b = data_analysis()
		c = data_analysis()
		list_not_pure_numbers_5 = [2247, 273805, 0.23423, 9234.2347832, "network science", a, 785398, 0.23423, b, 45678, c, "data science", 5623]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_5) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_analysis.is_list_of_numbers(list_not_pure_numbers_5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_1 = [4567809, 67890, 5678090, 1, 9, 436790]
		prompt = "	... Test: is_list...numb(lst_pure_pos_integers) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_2 = [-2569, -1, -62739, 0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_not_pos) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_3 = [-2569, -1, -62739, -0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_neg_0) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_4 = [0.437693, 1.3224, 346973.5679, -0.34367, -242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_5 = [-210.437693, -56971.3224, -9.5679, -0.45634367, -32242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_neg_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_6 = [0, 0, 0, 0, 0, 0 , 0]
		prompt = "	... Test: is_list...numb(lst_pure_0s) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_6):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_7 = [0]
		prompt = "	... Test: is_list...numb([0]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_7):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_8 = [-56970]
		prompt = "	... Test: is_list...numb([-56970]) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_8):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_9 = [723]
		prompt = "	... Test: is_list...numb([723]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_10 = [54869, 2.23, 0.2345, 8203, 102.23, 12, 7.23, 923]
		prompt = "	... Test: is_list...numb(lst_fp_int_only) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_analysis.is_list_of_numbers(list_pure_numbers_10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that accesses reference values
	#		for a corresponding particular attribute/property,
	#		using the Python dictionary containing pairs/2-tuples
	#		of attributes/properties and values.
	#	@param - None.
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
		standard_atmosphere = 101325
		prompt = "	... Test: get_ref..._val('random string') == "
		prompt = prompt + str(standard_atmosphere) + "	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_reference_value("random string"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the actual
	#		change between quantity1 and quantity2.
	#	@param - None.
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
		"""
		non_number_object = data_analysis()
		prompt = "	Test:get_act..._change(non-number_object,13.23) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_actual_change(non_number_object,13.23):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	Test:get_act..._change(-7692,non-number_object) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_actual_change(-7692,non_number_object):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
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
		prompt = "	... Test: get_actual_change(3,-4) == 7			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 7 == data_analysis.get_actual_change(3,-4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_act...(object,569) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_actual_change(a,569):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_act...(865.12,'Buona serata!') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_actual_change(865.12,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_act...(97623.23,None) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_actual_change(97623.23,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the absolute
	#		difference between quantity1 and quantity2.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_absolute_difference():
		print("	Testing get_absolute_difference() method.")
		prompt = "	...Test:default,get_absolute_difference(0,0) == 0	{}"
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
		prompt = "	... Test: get_absolute_difference(3,-4) == 7		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 7 == data_analysis.get_absolute_difference(3,-4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_abs..._diff(object,569) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_absolute_difference(a,569):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_abs..._diff(865.12,'Buona...') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_absolute_difference(865.12,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_abs..._diff(112.08723,None) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_absolute_difference(112.08723,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the relative change
	#		between quantity1 and quantity2.
	#	@param - None.
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
		prompt = "	... Test: get_relative_change(-97,-100) == -0.03	{}"
		statistical_analysis.increment_number_test_cases_used()
		if -0.03 == data_analysis.get_relative_change(-97,-100):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_relative_change(18,20):",data_analysis.get_relative_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_change(3,0) can't compute	{}"
		try:
			statistical_analysis.increment_number_test_cases_used()
			relative_change_error = data_analysis.get_relative_change(3,0)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	...Test: get_relative_change(-100,-110) ~ -0.0909090909 {}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(-0.0909090909, data_analysis.get_relative_change(-100,-110)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_relative_change(18,20):",data_analysis.get_relative_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
			print("data_analysis.get_relative_change(-100,-110) is:",data_analysis.get_relative_change(-100,-110),".")
		prompt = "	...Test: get_relative_change(-98,-105) ~ -0.06666666666	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(-0.06666666666, data_analysis.get_relative_change(-98,-105)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_relative_change(18,20):",data_analysis.get_relative_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._change(object,569) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_relative_change(a,569):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._change(865.12,'Buona...') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_change(865.12,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._change(232,None) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_change(232,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the percentage change
	#		between quantity1 and quantity2.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_percentage_change():
		print("	Testing get_percentage_change() method.")
		prompt = "	... Test: default, get_percentage_change(1,1) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_percentage_change():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percentage_change(15,12) == 0.25		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 25 == data_analysis.get_percentage_change(15,12):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print("data_analysis.get_percentage_change(15,12):",data_analysis.get_percentage_change(15,12),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percentage_change(18,20) == -0.10		{}"
		statistical_analysis.increment_number_test_cases_used()
		if -10 == data_analysis.get_percentage_change(18,20):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_percentage_change(18,20):",data_analysis.get_percentage_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percentage_change(-97,-100) == -0.03	{}"
		statistical_analysis.increment_number_test_cases_used()
		if -3 == data_analysis.get_percentage_change(-97,-100):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_percentage_change(18,20):",data_analysis.get_percentage_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percentage_change(3,0) can't compute	{}"
		try:
			statistical_analysis.increment_number_test_cases_used()
			relative_change_error = data_analysis.get_percentage_change(3,0)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	..Test:get_percentage_change(-100,-110) ~ -0.0909090909 {}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(-9.09090909, data_analysis.get_percentage_change(-100,-110)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_percentage_change(18,20):",data_analysis.get_percentage_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	..Test:get_percentage_change(-98,-105) ~ -0.06666666666 {}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(-6.666666666, data_analysis.get_percentage_change(-98,-105)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			#print("data_analysis.get_percentage_change(18,20):",data_analysis.get_percentage_change(18,20),"=")
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_pct_change(object,569) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_percentage_change(a,569):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_pct_change(865.12,'Buona...') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_percentage_change(865.12,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_pct_change(232,None) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_percentage_change(232,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the relative
	#		error between experimental_value and theoretical_value.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_relative_error():
		print("	Testing get_relative_error() method.")
		prompt = "	... Test: default, get_relative_error(1,1) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_error():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(15,12) == 0.25		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.25 == data_analysis.get_relative_error(15,12):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(16,20) == 0.2		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.2 == data_analysis.get_relative_error(16,20):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(-9,-10) == 0.1		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.1 == data_analysis.get_relative_error(-9,-10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(-13,-10) == 0.3		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.3 == data_analysis.get_relative_error(-13,-10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(-3,-2) == 0.5		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0.5 == data_analysis.get_relative_error(-3,-2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_relative_error(3,0) can't compute		{}"
		try:
			statistical_analysis.increment_number_test_cases_used()
			relative_change_error = data_analysis.get_relative_error(3,0)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: get_rel..._err(object,7643) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_relative_error(a,7643):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._err(67923.23,'Buona...') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_error(67923.23,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._err(8346,None) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_error(8346,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that determines the percent
	#		error between experimental_value and theoretical_value.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_percent_error():
		print("	Testing get_percent_error() method.")
		prompt = "	... Test: default, get_percent_error(1,1) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_percent_error():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percent_error(15,12) == 25		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 25 == data_analysis.get_percent_error(15,12):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		
		prompt = "	... Test: get_percent_error(16,20) == 0.2		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 20 == data_analysis.get_percent_error(16,20):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percent_error(-9,-10) == 0.1		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 10 == data_analysis.get_percent_error(-9,-10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percent_error(-13,-10) == 0.3		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 30 == data_analysis.get_percent_error(-13,-10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percent_error(-3,-2) == 0.5		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 50 == data_analysis.get_percent_error(-3,-2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_percent_error(3,0) can't compute		{}"
		try:
			statistical_analysis.increment_number_test_cases_used()
			relative_change_error = data_analysis.get_percent_error(3,0)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: get_pct_err(object,6325) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		a = data_analysis()
		if None == data_analysis.get_percent_error(a,6325):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_pct_err(8.212,'Buona...') == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_percent_error(8.212,"Buona serata!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_pct_err(362,None) == None			{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_percent_error(362,None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method that calculates the arithmetic
	#		mean for the absolute values of a given list of numbers.
	#	@param - None.
	#	@return - Nothing.
	#	O(n) method, where n is the number of elements in the lists
	#		used to test the specified method.
	@staticmethod
	def test_get_arithmetic_average_of_absolute_values():
		print("	Testing get_arithmetic_average_of_absolute_values() method.")
		prompt = "	... Test: list_of_numbers is None			{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values(None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: list_of_numbers is '', empty string		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values(""):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: list_of_numbers is 'Ciao mondo!', a string	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values("Ciao mondo!"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		not_a_list_obj = data_analysis()
		prompt = "	... Test: list_of_numbers is 'not_a_list_obj'		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values(not_a_list_obj):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: list_of_numbers is [], empty list		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values([]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = data_analysis()
		b = data_analysis()
		c = data_analysis()
		list_not_pure_numbers = [2247, 273805, 0.23423, 9234.2347832, "network science", a, 785398, 0.23423, b, 45678, c, "data science", 5623]
		prompt = "	... Test: list_of_numbers is 'list_not_pure_numbers'	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_arithmetic_average_of_absolute_values(list_not_pure_numbers):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers = [23, -46, 12, 13, 65, -75, 10, 0.23423, -56, 38]
		prompt = "	... Test: [23,-46,12,13,65,-75,10,0.23423,-56,38]	{}"
		statistical_analysis.increment_number_test_cases_used()
		arith_mean_abs = data_analysis.get_arithmetic_average_of_absolute_values(list_pure_numbers)
		if math.isclose(33.823423, arith_mean_abs):
		#if npt.assert_approx_equal(33.823423, arith_mean_abs):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	results is:",arith_mean_abs,".")
		list_pure_numbers = [2,5,7,9,1,4,8]
		prompt = "	... Test: [2,5,7,9,1,4,8]				{}"
		statistical_analysis.increment_number_test_cases_used()
		arith_mean_abs = data_analysis.get_arithmetic_average_of_absolute_values(list_pure_numbers)
		if math.isclose(5.14285714286, arith_mean_abs):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	results is:",arith_mean_abs,".")
		list_pure_numbers = [0,-5,-235,-345.346346,-34534.67239,-23408,-0.242]
		prompt = "	Test:[0,-5,-235,-345.346346,-34534.67239,-23408,-0.242]	{}"
		statistical_analysis.increment_number_test_cases_used()
		arith_mean_abs = data_analysis.get_arithmetic_average_of_absolute_values(list_pure_numbers)
		if math.isclose(8361.18010514, arith_mean_abs):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	results is:",arith_mean_abs,".")
		list_pure_numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		prompt = "	... Test: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]		{}"
		statistical_analysis.increment_number_test_cases_used()
		arith_mean_abs = data_analysis.get_arithmetic_average_of_absolute_values(list_pure_numbers)
		if math.isclose(0.0, arith_mean_abs):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	results is:",arith_mean_abs,".")
		list_pure_numbers = [-743024.367935]
		prompt = "	... Test: [-743024.367935]				{}"
		statistical_analysis.increment_number_test_cases_used()
		arith_mean_abs = data_analysis.get_arithmetic_average_of_absolute_values(list_pure_numbers)
		if math.isclose(743024.367935, arith_mean_abs):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	results is:",arith_mean_abs,".")
	## =========================================================
	#	Method to test the method that calculates the relative
	#		difference.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_relative_difference():
		print("	Testing get_relative_difference() method.")
		prompt = "	... Test: default get_relative_difference(1,1) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_difference():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		not_number_obj = data_analysis()
		prompt = "	...Test:get_rel..._diff(not_number_obj,56897) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference(not_number_obj,56897):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	...Test:get_rel..._diff(-32.15, not_number_obj)==None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference(-32.15, not_number_obj):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-32.15, []) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference(-32.15, []):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(972, [623, 2032]) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference(972, [623, 2032, 12.087623]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff('Hola', 96) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference("Hola", 96):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			Testing for cases |quantity1 - quantity2| = 0.
			
			Cases |quantity1 - quantity2| < 0 cannot be tested,
				since this is mathematically impossible.
			If such cases occur, it is because there are bugs
				with implementing the method to determine
				|quantity1 - quantity2|.
		"""
		prompt = "	... Test: get_rel..._diff(0, 0) == None			{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_difference(0, 0):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(5, 5) == 0			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_difference(5, 5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-1.23, -1.23) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_difference(-1.23, -1.23):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-48, -48) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_difference(-48, -48):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(9.23, 9.23) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_difference(9.23, 9.23):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			We cannot test for:
			+ 0 <= (|quantity1| + |quantity1|)
			+ 0 <= 0.5 * (|quantity1| + |quantity1|)
			
			This is because both quantity1 and quantity2 cannot
				be zero.
			+ Our implementation would return None if the following
				is true: quantity1 = quantity2 = 0.
			
			Hence, we cannot test for the folowing:
			+ 0 = (|quantity1| + |quantity1|)
			+ 0 = 0.5 * (|quantity1| + |quantity1|)
			
			As for the following cases,
			+ 0 < (|quantity1| + |quantity1|)
			+ 0 < 0.5 * (|quantity1| + |quantity1|)
			they are mathematically impossible to test.
			If these cases occur, it is because the functions
				to implement these have (software) bugs/errors.
		"""
		prompt = "	... Test: get_rel..._diff(15, 12) == 0.22222222222	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(15, 12),0.22222222222):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(45, 50) == 0.10526315789	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(45, 50),0.10526315789):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-30,-35) == 0.15384615384	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(-30, -35),0.15384615384):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-2.8,-2.41) == 0.14971209213	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(-2.8, -2.41),0.14971209213):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(8.1,8.73) == 0.07486631016	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(8.1,8.73),0.07486631016):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel..._diff(-2,1.5) == 2			{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(-2,1.5),2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			"""
			print("data_analysis.get_relative_difference(-2,1.5):",data_analysis.get_relative_difference(-2,1.5),"=")
			print("data_analysis.get_absolute_difference(-2,1.5):",data_analysis.get_absolute_difference(-2,1.5),"=")
			"""
		prompt = "	... Test: get_rel..._diff(1.5,-2) == 2			{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_difference(1.5,-2),2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			#print("data_analysis.get_relative_difference(1.5,-2):",data_analysis.get_relative_difference(1.5,-2),"=")
	## =========================================================
	#	Method to test the method that calculates the relative
	#		percentage difference.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_relative_percentage_difference():
		print("	Testing get_relative_percentage_difference() method.")
		prompt = "	... Test: default get_rel_pct_diff(1,1) == 0	{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_percentage_difference():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		not_number_obj = data_analysis()
		prompt = "	...Test:get_rel_pct_diff(not_number_obj,56897) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference(not_number_obj,56897):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	...Test:get_rel_pct_diff(-32.15, not_number_obj)==None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference(-32.15, not_number_obj):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-32.15, []) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference(-32.15, []):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(972, [623, 2032]) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference(972, [623, 2032, 12.087623]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff('Hola', 96) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference("Hola", 96):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			Testing for cases |quantity1 - quantity2| = 0.
			
			Cases |quantity1 - quantity2| < 0 cannot be tested,
				since this is mathematically impossible.
			If such cases occur, it is because there are bugs
				with implementing the method to determine
				|quantity1 - quantity2|.
		"""
		prompt = "	... Test: get_rel_pct_diff(0, 0) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_analysis.get_relative_percentage_difference(0, 0):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(5, 5) == 0			{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_percentage_difference(5, 5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-1.23, -1.23) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_percentage_difference(-1.23, -1.23):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-48, -48) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_percentage_difference(-48, -48):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(9.23, 9.23) == 0		{}"
		statistical_analysis.increment_number_test_cases_used()
		if 0 == data_analysis.get_relative_percentage_difference(9.23, 9.23):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		"""
			We cannot test for:
			+ 0 <= (|quantity1| + |quantity1|)
			+ 0 <= 0.5 * (|quantity1| + |quantity1|)
			
			This is because both quantity1 and quantity2 cannot
				be zero.
			+ Our implementation would return None if the following
				is true: quantity1 = quantity2 = 0.
			
			Hence, we cannot test for the folowing:
			+ 0 = (|quantity1| + |quantity1|)
			+ 0 = 0.5 * (|quantity1| + |quantity1|)
			
			As for the following cases,
			+ 0 < (|quantity1| + |quantity1|)
			+ 0 < 0.5 * (|quantity1| + |quantity1|)
			they are mathematically impossible to test.
			If these cases occur, it is because the functions
				to implement these have (software) bugs/errors.
		"""
		prompt = "	... Test: get_rel_pct_diff(15, 12) == 22.2222222222	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(15, 12),22.222222222):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("answer=",data_analysis.get_relative_percentage_difference(15, 12),".")
		prompt = "	... Test: get_rel_pct_diff(45, 50) == 10.526315789	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(45, 50),10.526315789):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-30,-35) == 15.384615384	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(-30, -35),15.384615384):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-2.8,-2.41) == 14.971209213	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(-2.8, -2.41),14.971209213):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(8.1,8.73) == 7.486631016	{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(8.1,8.73),7.486631016):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: get_rel_pct_diff(-2,1.5) == 200		{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(-2,1.5),200):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			"""
			print("data_analysis.get_relative_difference(-2,1.5):",data_analysis.get_relative_difference(-2,1.5),"=")
			print("data_analysis.get_absolute_difference(-2,1.5):",data_analysis.get_absolute_difference(-2,1.5),"=")
			"""
		prompt = "	... Test: get_rel_pct_diff(1.5,-2) == 200		{}"
		statistical_analysis.increment_number_test_cases_used()
		if math.isclose(data_analysis.get_relative_percentage_difference(1.5,-2),200):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	# =========================================================
	#	Method to test the method that calculates the relative
	#		percentage difference.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	#	Test cases for this module end before the following string:
	#	=	Testing the utilities package.
	@staticmethod
	def test_data_analysis():
		print("")
		print("")
		print("-------------------------------------------------")
		print("==	Testing class: data_analysis.")
		data_analysis_tester.test_is_list_of_numbers()
		print("")
		data_analysis_tester.test_get_reference_value()
		print("")
		data_analysis_tester.test_get_actual_change()
		print("")
		data_analysis_tester.test_get_absolute_difference()
		print("")
		data_analysis_tester.test_get_relative_change()
		print("")
		data_analysis_tester.test_get_percentage_change()
		print("")
		data_analysis_tester.test_get_relative_error()
		print("")
		data_analysis_tester.test_get_percent_error()
		print("")
		data_analysis_tester.test_get_arithmetic_average_of_absolute_values()
		print("")
		data_analysis_tester.test_get_relative_difference()
		print("")
		data_analysis_tester.test_get_relative_percentage_difference()
		# TEST ALL METHODS!!!

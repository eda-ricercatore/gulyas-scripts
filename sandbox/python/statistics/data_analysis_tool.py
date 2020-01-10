#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to perform
		miscellaneous tasks in analyzing data.


	Synopsis:
	Perform miscellaneous tasks in data analysis.

	To-Do List:
	+ Add information for statistics regarding:
		- accuracy
		- precision



	Revision History:
	December 15, 2017			Version 0.1, initial build.




	Additional resources:
	+ https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
		- use of functional programming features to calculate the
			average of a list/array/container/series of numbers.
			* reduce(lambda x, y: x + y, l) / len(l)
	+ import itertools,operator
		list(itertools.accumulate(l,operator.add)).pop(-1) / len(l)
		https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
		https://docs.python.org/3/library/itertools.html
		https://docs.python.org/3/library/functional.html
	+ https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html
	+ https://acadgild.com/blog/python-mean-median-mode
	+ https://learnandlearn.com/python-programming/python-reference/find-calculate-arithmetic-mean-python-using-mean-function
	+ https://www.quora.com/How-do-I-get-the-average-value-in-Python-of-a-list-containing-NAN-value
		- Processing NANs in the data sets 
	+ https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#Scalar%20mean(InputArray%20src,%20InputArray%20mask)
	+ https://rails.devcamp.com/38/274/get-average-list-python
	+ from numpy
		- https://pythontic.com/numpy/ndarray/mean_std_var
	+ https://pytorch.org/docs/stable/torch.html#torch.mean
	

	Reference:
	[WikipediaContributors2019g]
		Address = San Francisco, CA
		Author = Wikipedia contributors
		Howpublished = Available online from Wikipedia, The Free Encyclopedia: Measurement at: https://en.wikipedia.org/wiki/Relative_change_and_difference; October 1, 2019 was the last accessed date
		Month = September 25
		Publisher = Wikimedia Foundation
		Title = Relative change and difference
		Url = https://en.wikipedia.org/wiki/Relative_change_and_difference
		Year = 2019
	[DrakeJr2016b]
		statistics package from Python Standard Library for Python 3.7.5rc1
		https://docs.python.org/3/library/statistics.html
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

	collections -> namedtuple
				To use named tuples.
	operator	attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
	statistics	Module with functions for mathematical statistics
					functions.
					+ reduce(lambda aggr, elem: (aggr[0] + elem, aggr[1]+1), l, (0.0,0))
					+ print reduce(lambda x, y: x + y, l) / len(l)
	pandas		Machine learning library
					https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mean.html
					For the whole documentation:
					https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mean.html

					And the whole documentation:
						https://pandas.pydata.org/pandas-docs/stable/10min.html
						https://pandas.pydata.org/pandas-docs/stable/10min.html
	NumPy		Numerical computing and machine learning library
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
#import pandas as pd

###############################################################
#	Import Custom Python Modules






###############################################################
"""
	Module with methods that perform miscellaneous tasks in
		data analysis.
"""
class data_analysis:
	#	Static variable declaration.
	#
	"""
		Dictionary of reference values.
		
		Note that "standard atmosphere" refers to standard
			atmospheric pressure.
		
		References:
			https://en.wikipedia.org/wiki/List_of_physical_constants
			https://en.wikipedia.org/wiki/Physical_constant
			https://en.wikipedia.org/wiki/List_of_common_physics_notations
	"""
	dict_of_reference_values = {"c":299792458, "standard acceleration due to gravity":9.80665, "standard atmosphere":101325}
	# =========================================================
	#	Method to access the reference value for a particular
	#		attribute/property.
	#	\cite{WikipediaContributors2019g}
	#	@return - The reference value for a particular attribute/property.
	#	O(1) method.
	@staticmethod
	def get_reference_value(property="c"):
		return data_analysis.dict_of_reference_values[property]
	# =========================================================
	#	Method to determine the actual change between quantity1 and
	#		quantity2.
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the actual
	#		change of.
	#	@param quantity2 - Another quantity that I want to find the
	#		actual change of.
	#	@return - The actual change.
	#	Note that the actual change can be negative.
	#	O(1) method.
	@staticmethod
	def get_actual_change(quantity1=0,quantity2=0):
		return (quantity1 - quantity2)
	# =========================================================
	#	Method to determine the absolute difference between quantity1
	#		and quantity2.
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		absolute difference of.
	#	@param quantity2 - Another quantity that I want to find the
	#		absolute difference of.
	#	@return - The absolute difference.
	#	@postcondition - absolute difference, |quantity1 - quantity2| >= 0.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Absolute_difference
	@staticmethod
	def get_absolute_difference(quantity1=0,quantity2=0):
		"""
			Check postcondition:
				absolute difference, |quantity1 - quantity2| >= 0.
		"""
		absolute_difference = abs(quantity1 - quantity2)
		if (0 > absolute_difference):
			raise Exception("	get_absolute_difference(): Absolute difference must be non-negative.")
		return absolute_difference
	# =========================================================
	#	Method to determine the relative change between quantity
	#		quantity1 and ref_qty (the reference quantity).
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		relative change of.
	#	@param ref_qty - A reference quantity that I want to find
	#		the relative change of.
	#	@return - The relative change.
	#	Note that the relative change can be negative.
	#	@precondition - ref_qty != 0.
	#	O(1) method.
	@staticmethod
	def get_relative_change(quantity1=1,ref_qty=1):
		# Check precondition: ref_qty != 0.
		if 0 == ref_qty:
			raise Exception("	ref_qty cannot be zero.")
		return (data_analysis.get_actual_change(quantity1,ref_qty)/ref_qty)
	# =========================================================
	#	Method to determine the percentage change between quantity
	#		quantity1 and ref_qty (the reference quantity).
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		percentage change of.
	#	@param ref_qty - A reference quantity that I want to find
	#		the percentage change of.
	#	@return - The percentage change.
	#	@precondition - ref_qty != 0.
	#	@postcondition - 0 <= percentage change <= 1.
	#	O(1) method.
	@staticmethod
	def get_percentage_change(quantity1=1,ref_qty=1):
		# Check precondition: ref_qty != 0.
		if 0 == ref_qty:
			raise Exception("	ref_qty cannot be zero.")
		relative_change = data_analysis.get_relative_change(quantity1,ref_qty)
		return (relative_change*100)
	# =========================================================
	#	Method to determine the relative error between experimental
	#		(measured) and theoretical (accepted) values:
	#		experimental_value and theoretical_value.
	#	\cite{WikipediaContributors2019g}
	#	@param experimental_value - The experimental (measured) value.
	#	@param theoretical_value - The theoretical (accepted) value.
	#	@return - The relative error.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Relative_change_and_difference
	@staticmethod
	def get_relative_error(experimental_value=1,theoretical_value=1):
		return (data_analysis.get_absolute_difference(experimental_value,theoretical_value)/abs(theoretical_value))
	# =========================================================
	#	Method to determine the percent error between experimental
	#		(measured) and theoretical (accepted) values:
	#		experimental_value and theoretical_value.
	#	\cite{WikipediaContributors2019g,Wenning2014a}
	#	@param experimental_value - The experimental (measured) value.
	#	@param theoretical_value - The theoretical (accepted) value.
	#	@return - The relative change.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Relative_change_and_difference
	@staticmethod
	def get_percent_error(experimental_value=1,theoretical_value=1):
		return (data_analysis.get_relative_error(experimental_value,theoretical_value)*100)
	# =========================================================
	#	Method to determine the arithmetic mean, or average, of
	#		a list of absolute values of numbers, which can be
	#		negative or otherwise.
	#	The list of numbers, which can be negative or otherwise,
	#		are copied into another list as their absolute values.
	#	This method computes the arithmetic mean for this new
	#		list of absolute values.
	#	
	#	@param list_of_numbers - A list of numbers that I want
	#		to find the arithmetic mean, or average, of.
	#	@return - The arithmetic mean, or average, of the list of
	#		absolute values.
	#	@precondition - list_of_numbers is not a None object.
	#	@postcondition - mean of absolute values of numbers >= 0.
	#	O(n) method, where n is the number of elements in the list.
	#	References:
	#		https://en.wikipedia.org/wiki/Arithmetic_mean
	#		https://en.wikipedia.org/wiki/Absolute_value
	#		https://en.wikipedia.org/wiki/Average
	@staticmethod
	def get_arithmetic_average_of_absolute_values(list_of_numbers=[]):
		# Check precondition: list_of_numbers is not a None object.
		if list_of_numbers is None:
			raise Exception("	A 'None' object is passed to the get_arithmetic_average_of_absolute_values() method.")
		# Else, is list_of_numbers an empty list?
		#elif 0 == len(list_of_numbers):
		elif not list_of_numbers:	# More Pythonic solution.
			return 0
		else:
			"""
				Copy the absolute values of numbers in the list to
					another list, absolute_list_of_numbers.
			"""
			absolute_list_of_numbers = []
			for elem in list_of_numbers:
				absolute_list_of_numbers.append(abs(elem))
			#print("absolute_list_of_numbers:",absolute_list_of_numbers,"=")
			# Determine the arithmetic mean of these absolute values.
			mean_absolute_list_of_numbers = s.mean(absolute_list_of_numbers)
			# Check postcondition: mean of absolute values of numbers >= 0.
			if 0 > mean_absolute_list_of_numbers:
				raise Exception("	mean of the list of absolute values. < 0.")
			return mean_absolute_list_of_numbers
	# =========================================================
	#	Method to determine the relative difference between
	#		quantity quantity1 and quantity quantity2.
	#	relative difference = |quantity1 - quantity2|/(0.5 * (abs(quantity1) + abs(quantity1)))
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		relative difference of.
	#	@param quantity2 - Another quantity that I want to find
	#		the relative difference of.
	#	@return - The relative difference.
	#	@precondition - (quantity1 != 0) or (quantity2 != 0).
	#	@assertion - absolute difference, |quantity1 - quantity2| >= 0.
	#	@postcondition - average_of_absolute_values > 0.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Absolute_difference
	@staticmethod
	def get_relative_difference(quantity1=1,quantity2=1):
		# Check for precondition: (quantity1 != 0) or (quantity2 != 0).
		if (0 == quantity1) and (0 == quantity2):
			raise Exception("	relative difference does not exist for quantity1 == quantity2.")
		absolute_diff = data_analysis.get_absolute_difference(quantity1,quantity2)
		# Check assertion: absolute difference, |quantity1 - quantity2| >= 0.
		if 0 > absolute_diff:
			raise Exception("	get_relative_difference(): Absolute difference must be non-negative.")
		list_of_values = [quantity1, quantity2]
		average_of_absolute_values = get_arithmetic_average_of_absolute_values(list_of_numbers)
		# Check postcondition: average_of_absolute_values > 0.
		if 0 >= average_of_absolute_values:
			raise Exception("	0 >= arithmetic mean of absolute values.")
		return (absolute_diff/average_of_absolute_values)
	

#!/Users/zhiyang/anaconda3/bin/python3
###	#!/usr/local/bin/python3

"""
	This Python script is written by Zhiyang Ong to measure the
		execution time of functions and programs in Python, and
		other processes and programs called from Python scripts
		or programs.


	Synopsis:
	Measure the execution time of functions and programs in Python.

	This script can be executed as follows:
	./performance_measurement.py



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
	time		To obtain information about the current time.
				time_ns version provides information about the
					current time with nanosecond accuracy.
	warnings	Provide warnings to users without terminating the
					program abruptly.
	process_time (& process_time_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	perf_counter (& perf_counter_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	monotonic (& pm_monotonic_ns)
				To monotonically obtain time stamps, for performance
					measurement, and its alternative providing
					nanosecond accuracy.
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
# ImportError: cannot import name 'perf_counter_ns'
from time import perf_counter as pc_timestamp
#from time import perf_counter_ns as pc_timestamp_ns
from time import process_time as pt_timestamp
#from time import process_time_ns as pt_timestamp_ns
#from time import time_ns as t_ns
from time import monotonic as pm_monotonic
#from time import monotonic_ns as pm_monotonic_ns

###############################################################
#	Import Custom Python Packages and Modules
"""
	Module to calculate the factorial of a number.
"""
#from get_factorial import calculate_factorial
from utilities.timing_measurements.get_factorial import calculate_factorial

###############################################################
"""
	Module with methods that measure the execution time of functions
		and programs in Python.

	Support is not provided for storing multiple initial timestamps,
		so that we can measure elapsed times from different initial
		timestamps.
		User have to call the functions (such as monotonic_ns())
			specifically, so that this Python module can be kept
			simple and short.
"""
class execution_time_measurement_no_ns:
	# Invalid timestamp.
	invalid_timestamp = -123456789012345678901234567890
	# Initial timestamp.
	initial_timestamp = invalid_timestamp
	# Types of performance measurement technique available.
	#types_of_performance_measurement_technique = ("perf_counter","perf_counter_ns","process_time","process_time_ns","time","time_ns","monotonic","monotonic_ns")
	types_of_performance_measurement_technique = ("perf_counter","process_time","time","monotonic")
	"""
		Type of current time measurement.
		Default option is: monotonic.
	"""
	type_current_time_measurement = "monotonic"
	# ============================================================
	##	Method to set the initial timestamp.
	#
	#	Use techniques for measuring performance (i.e., user
	#		execution time) and timestamps.
	#
	#	@param type_timestamp - Indicates if either of the following
	#				methods of performance measurement is preferred.
	#				* perf_counter, perf_counter(): pc_timestamp()
	#				* process_time, process_time(): pt_timestamp()
	#				* time, time.time(): time()
	#				* monotonic, monotonic(): pm_monotonic()
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def set_initial_timestamp(type_timestamp="monotonic"):
		execution_time_measurement_no_ns.type_current_time_measurement = type_timestamp
		"""
			Is the option for one of the following methods to measure
				time?
				* perf_counter, perf_counter(): pc_timestamp()
				* process_time, process_time(): pt_timestamp()
				* time, time.time(): time.time()
				* monotonic, monotonic(): pm_monotonic()
		"""
		if ("perf_counter" == type_timestamp):
			# Yes. Use perf_counter() to measure performance/time.
			execution_time_measurement_no_ns.initial_timestamp = pc_timestamp()
		elif ("process_time" == type_timestamp):
			# Yes. Use process_time() to measure performance/time.
			execution_time_measurement_no_ns.initial_timestamp = pt_timestamp()
		elif ("time" == type_timestamp):
			# Yes. Use time() to measure performance/time.
			execution_time_measurement_no_ns.initial_timestamp = time.time()
		else:
			# The default option is: "monotonic()"
			execution_time_measurement_no_ns.initial_timestamp = pm_monotonic()
	# ============================================================
	##	Method to reset the initial timestamp to "invalid_timestamp".
	#
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def reset_initial_timestamp():
		execution_time_measurement_no_ns.initial_timestamp = execution_time_measurement_no_ns.invalid_timestamp
	# ============================================================
	##	Method to get the initial timestamp.
	#	@return the initial timestamp.
	#	O(1) method.
	@staticmethod
	def get_initial_timestamp():
		return execution_time_measurement_no_ns.initial_timestamp
	# ============================================================
	##	Method to get the type/method of current time measurement.
	#	@return the type/method of current time measurement.
	#	O(1) method.
	@staticmethod
	def get_type_current_time_measurement():
		return execution_time_measurement_no_ns.type_current_time_measurement
	# ============================================================
	##	Method to determine the elapsed time from the initial
	#		timestamp.
	#	@return the elapsed time from the initial timestamp.
	#	@postcondition - (elapsed time > 0.0) shall always be true.
	#		Since methods can have microsecond precision (or better),
	#			I would just compare this to 0.0.
	#	O(1) method.
	@staticmethod
	def get_elapsed_time():
		"""
			Is the option for one of the following methods to measure
				time?
				* perf_counter, perf_counter(): pc_timestamp()
				* process_time, process_time(): pt_timestamp()
				* time, time.time_ns(): time_ns()
				* monotonic, monotonic(): pm_monotonic()
		"""
		if ("perf_counter" == execution_time_measurement_no_ns.get_type_current_time_measurement()):
			# Yes. Use perf_counter() to measure performance/time.
			current_timestamp = pc_timestamp()
		elif ("process_time" == execution_time_measurement_no_ns.get_type_current_time_measurement()):
			# Yes. Use process_time() to measure performance/time.
			current_timestamp = pt_timestamp()
		elif ("time" == execution_time_measurement_no_ns.get_type_current_time_measurement()):
			# Yes. Use time.time() to measure performance/time.
			current_timestamp = time.time()
		else:
			"""
				The default option is: "monotonic".
				Use monotonic() to measure performance/time.
			"""
			current_timestamp = pm_monotonic()
		# Postcondition. Check if elapsed_time_no_ns > 0.
		elapsed_time_no_ns = current_timestamp - execution_time_measurement_no_ns.get_initial_timestamp()
		execution_time_measurement_no_ns.check_elapsed_time(elapsed_time_no_ns)
		return elapsed_time_no_ns
	# ============================================================
	##	Method to convert seconds to days, hours, minutes, and
	#		seconds.
	#	@param time_in_seconds - amount of time in seconds to be
	#								converted to days, hours,
	#								minutes, and seconds.
	#							It has a default value of 0
	#								seconds. 
	#	@return - time in days, hours, minutes, and seconds.
	@staticmethod
	def convert_time_in_seconds_to_DD_HH_MM_SS(time_in_seconds=0):
		return datetime.timedelta(seconds=time_in_seconds)
	# ============================================================
	##	Method to compare techniques for measuring elapsed periods.
	#	It calculates the factorial of each number in a list, and
	#		uses each of the following methods of performance
	#		measurement to measure the elapsed periods.
	#		* perf_counter, perf_counter(): pc_timestamp()
	#		* process_time, process_time(): pt_timestamp()
	#		* time, time.time(): time()
	#		* monotonic, monotonic(): pm_monotonic()
	#	Subsequently, it writes the elapsed time to an output file.
	#	@return - Nothing.
	#	O(n!) method, where n is the largest number in the
	#		aforementioned list, since we are measuring the
	#		performance of calculating factorials.
	@staticmethod
	def compare_different_methods_to_measure_elapsed_periods():
		"""
			Create a file to store experimental data of measuring
				the performance of recursive and iterative methods.
		"""
		with open("compare_different_methods_to_measure_elapsed_periods.csv","a+") as op_f_obj:
			for perf_measurement_technique in execution_time_measurement_no_ns.types_of_performance_measurement_technique:
				print("The technique used is:",perf_measurement_technique,"=")
				"""
					Set the initial timestamp for calculating the
						factorial of numbers via recursion.
				"""
				execution_time_measurement_no_ns.set_initial_timestamp(perf_measurement_technique)
				print("	Calculate the factorial using recursion.")
				print("	= current timestamp:",execution_time_measurement_no_ns.get_initial_timestamp(),"=")
				for x in range(0,20+1):
					print("		factorial of",x," is:",calculate_factorial.get_factorial_recursion(x),"=")
				"""
					Get the elapsed time for calculating the factorial of
						numbers via recursion.
				"""
				elapsed_time_recursion = execution_time_measurement_no_ns.get_elapsed_time()
				print("	= elapsed_time_recursion:",elapsed_time_recursion,"=")
				"""
					Set the initial timestamp for calculating the
						factorial of numbers via iteration.
				"""
				execution_time_measurement_no_ns.set_initial_timestamp(perf_measurement_technique)
				print("	Calculate the factorial using iteration.")
				print("	= current timestamp:",execution_time_measurement_no_ns.get_initial_timestamp(),"=")
				for x in range(0,20+1):
					print("		factorial of",x," is:",calculate_factorial.get_factorial_iteration(x),"=")
				"""
					Get the elapsed time for calculating the factorial of
						numbers via iteration.
				"""
				elapsed_time_iteration = execution_time_measurement_no_ns.get_elapsed_time()
				print("	= elapsed_time_iteration:",elapsed_time_iteration,"=")
				"""
					The timeit.timeit() method can result in negative elapsed time.
				"""
				text = perf_measurement_technique + "," + str(elapsed_time_recursion) + "," + str(elapsed_time_iteration) + "\n"
				op_f_obj.write(text)
				#op_f_obj.write("\n")
	# ============================================================
	##	Method to check if the elapsed time is a positive period.
	#	If the elapsed time is not positive, raise a warning to
	#		user.
	#	Use this method as an invariant, precondition, assertion,
	#		or postcondition, to ensure that elapsed time is not
	#		non-positive.
	#	@param elapsed_time - The elapsed time/period in seconds.
	#		Let the default value of the elapsed time/period be
	#			0 second (s).
	#	@return - Nothing.
	@staticmethod
	def check_elapsed_time(elapsed_time=0.0):
		if 0 >= elapsed_time:
			warnings.warn("Elapsed time is <= 0. It shouldn't be, by definition.")




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	print("Compare techniques for measuring elapsed periods.")
	print("")
	execution_time_measurement_no_ns.compare_different_methods_to_measure_elapsed_periods()

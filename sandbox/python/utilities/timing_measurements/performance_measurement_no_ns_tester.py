#!/Users/zhiyang/anaconda3/bin/python3
###	#!/usr/local/bin/python3

"""
	This Python script is written by Zhiyang Ong to test methods
		that measure the current time.


	Synopsis:
	Test methods that measure the current time.


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

# Statistics package.
"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistic_pkg.test_statistics_tester import statistical_analysis_tester


"""
	Package and module to calculate the factorial of a number.
"""
#from get_factorial import calculate_factorial
from utilities.timing_measurements.get_factorial import calculate_factorial
# Package and module with methods to measure the current time.
from utilities.timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns

###############################################################
"""
	Module to test methods that measure the current time.
"""
class execution_time_measurement_no_ns_tester:
	# Types of performance measurement technique available.
	types_of_performance_measurement_technique = ("perf_counter","process_time","time","monotonic")
	# ============================================================
	##	Method to test setting and resetting the initial timestamp.
	#
	#	Not iterating through a list of types of current time
	#		measurements, which will cause formatting problems
	#		in standard output stream or file output.
	#	This is because different types have different word
	#		length (i.e., number of characters).
	#
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_set_reset_and_get_initial_timestamp():
		print("	Testing set, reset, get initial timestamp methods.")
		prompt = "	... Test: get_initial_timestamp() is invalid		{}."
		statistical_analysis.increment_number_test_cases_used()
		if execution_time_measurement_no_ns.invalid_timestamp == execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: set_initial_timestamp() not invalid		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp()
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: reset_initial_timestamp() is invalid		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.reset_initial_timestamp()
		if execution_time_measurement_no_ns.invalid_timestamp == execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: set_initial_timestamp("") not invalid		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp("")
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			"""
				Reset initial time stamp to test for other input
					parameters.
			"""
			execution_time_measurement_no_ns.reset_initial_timestamp()
		else:
			print(prompt .format("FAIL!!!"))
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		prompt = "	... Test: set_initial_timestamp('perf_counter')		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp("perf_counter")
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			"""
				Reset initial time stamp to test for other input
					parameters.
			"""
			execution_time_measurement_no_ns.reset_initial_timestamp()
		else:
			print(prompt .format("FAIL!!!"))
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		prompt = "	... Test: set_initial_timestamp('process_time')		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp("process_time")
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			"""
				Reset initial time stamp to test for other input
					parameters.
			"""
			execution_time_measurement_no_ns.reset_initial_timestamp()
		else:
			print(prompt .format("FAIL!!!"))
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		prompt = "	... Test: set_initial_timestamp('time')			{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp("time")
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			"""
				Reset initial time stamp to test for other input
					parameters.
			"""
			execution_time_measurement_no_ns.reset_initial_timestamp()
		else:
			print(prompt .format("FAIL!!!"))
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		prompt = "	... Test: set_initial_timestamp('monotonic')		{}."
		statistical_analysis.increment_number_test_cases_used()
		execution_time_measurement_no_ns.set_initial_timestamp("monotonic")
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			"""
				Reset initial time stamp to test for other input
					parameters.
			"""
			execution_time_measurement_no_ns.reset_initial_timestamp()
		else:
			print(prompt .format("FAIL!!!"))
	# ============================================================
	##	Method that tests method to check if the elapsed time
	#		is positive.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_check_elapsed_time():
		print("	Testing check_elapsed_time() method.")
		prompt = "	... Test: check_elapsed_time() works			{}."
		statistical_analysis.increment_number_test_cases_used()
		with warnings.catch_warnings(record=True) as w:
			# Check if default elapsed time = 0, and triggers warning.
			execution_time_measurement_no_ns.check_elapsed_time()
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			prompt = "	... Test: check_elapsed_time(-235435) works		{}."
			statistical_analysis.increment_number_test_cases_used()
			with warnings.catch_warnings(record=True) as w:
				# Check if default elapsed time < 0, and triggers warning.
				execution_time_measurement_no_ns.check_elapsed_time(-235435)
				print(prompt .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
		prompt = "	... Test: check_elapsed_time(5678) works		{}."
		statistical_analysis.increment_number_test_cases_used()
		"""
			Check if default elapsed time > 0, and does not trigger
				any warning.
		"""
		execution_time_measurement_no_ns.check_elapsed_time(5678)
		print(prompt .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
	# ============================================================
	##	Method to test the elapsed time measurement and the
	#		get_type_current_time_measurement() method.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_elapsed_time():
		print("	Testing get_elapsed_time() method.")
		# Set initial time stamp.
		execution_time_measurement_no_ns.set_initial_timestamp("perf_counter")
		prompt = "	... Test: for perf_counter				{}."
		statistical_analysis.increment_number_test_cases_used()
		elapsed_t = execution_time_measurement_no_ns.get_elapsed_time()
		execution_time_measurement_no_ns.check_elapsed_time(elapsed_t)
		print(prompt .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
		# Reset and set initial time stamp.
		execution_time_measurement_no_ns.reset_initial_timestamp()
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		execution_time_measurement_no_ns.set_initial_timestamp("process_time")
		prompt = "	... Test: for process_time				{}."
		statistical_analysis.increment_number_test_cases_used()
		elapsed_t = execution_time_measurement_no_ns.get_elapsed_time()
		execution_time_measurement_no_ns.check_elapsed_time(elapsed_t)
		print(prompt .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
		# Reset and set initial time stamp.
		execution_time_measurement_no_ns.reset_initial_timestamp()
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		execution_time_measurement_no_ns.set_initial_timestamp("time")
		prompt = "	... Test: for time					{}."
		statistical_analysis.increment_number_test_cases_used()
		elapsed_t = execution_time_measurement_no_ns.get_elapsed_time()
		execution_time_measurement_no_ns.check_elapsed_time(elapsed_t)
		print(prompt .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
		# Reset and set initial time stamp.
		execution_time_measurement_no_ns.reset_initial_timestamp()
		if execution_time_measurement_no_ns.invalid_timestamp != execution_time_measurement_no_ns.get_initial_timestamp():
			warnings.warn("Initial time stamp not reset between test cases.")
		execution_time_measurement_no_ns.set_initial_timestamp("monotonic")
		prompt = "	... Test: for monotonic					{}."
		statistical_analysis.increment_number_test_cases_used()
		elapsed_t = execution_time_measurement_no_ns.get_elapsed_time()
		execution_time_measurement_no_ns.check_elapsed_time(elapsed_t)
		print(prompt .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
	# ============================================================
	##	Method to test conversion from seconds to days, hours,
	#		minutes, and seconds.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_convert_time_in_seconds_to_DD_HH_MM_SS():
		print("	Testing convert_time_in_seconds_to_DD_HH_MM_SS() method.")
		prompt = "	... Test: convert_time_in_seconds_...() = 0s		{}."
		statistical_analysis.increment_number_test_cases_used()
		if "0:00:00" == str(execution_time_measurement_no_ns.convert_time_in_seconds_to_DD_HH_MM_SS()):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_time_in_seconds_...(32:17) = 32:17	{}."
		statistical_analysis.increment_number_test_cases_used()
		if "0:32:17" == str(execution_time_measurement_no_ns.convert_time_in_seconds_to_DD_HH_MM_SS(32*60+17)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_time_in_seconds_...(15:51:09) is ok	{}."
		statistical_analysis.increment_number_test_cases_used()
		if "15:51:09" == str(execution_time_measurement_no_ns.convert_time_in_seconds_to_DD_HH_MM_SS(15*60*60+51*60+9)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_time_...(73 days, 22:04:58) is ok	{}."
		statistical_analysis.increment_number_test_cases_used()
		if "73 days, 22:04:58" == str(execution_time_measurement_no_ns.convert_time_in_seconds_to_DD_HH_MM_SS(73*24*60*60+22*60*60+4*60+58)):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	# =========================================================
	#	Method to test methods that measure the current time.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	#
	#	To search for the (specific) test results for this Python
	#		module, search for:
	#	==	Testing class: execution_time_measurement_no_ns. 
	@staticmethod
	def test_current_time_measurement_methods():
		print("")
		print("")
		print("==	Testing class: execution_time_measurement_no_ns.")
		"""
			"Handle warnings as errors"
			Reference:
			+ niekas and Acumenus, Answer to "In Python, how does one catch warnings as if they were exceptions?," Stack Exchange Inc., New York, NY, June 20, 2016.
				Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/30368735; January 28, 2019 was the last accessed date.
				\cite{niekas2016} in my BibTeX database.
		"""
		execution_time_measurement_no_ns_tester.test_set_reset_and_get_initial_timestamp()
		execution_time_measurement_no_ns_tester.test_convert_time_in_seconds_to_DD_HH_MM_SS()
		execution_time_measurement_no_ns_tester.test_check_elapsed_time()
		execution_time_measurement_no_ns_tester.test_get_elapsed_time()
		#execution_time_measurement_no_ns.compare_different_methods_to_measure_elapsed_periods()
		print("")

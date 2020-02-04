#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test support functions
        to process input arguments for a genetic technology mapping software.


	Synopsis:
	Test support functions to process input arguments for a genetic technology
        mapping software.


	Notes/Assumptions:
	Raise an exception when the 2nd parameter of the software matches the
		filename of an existing file.
		This prevents its contents from being overwritten.
	Raise an exception when the user manual cannot be accessed
		due to errors, or when errors occur in an input argument.

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
	collections -> namedtuple
				To use named tuples.
	operator -> attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
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

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args



###############################################################
"""
	Module that tests the methods for processing input arguments
		of a genetic technology mapping software.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "queue_ip_args"
		objects.
	Test each static method of the "queue_ip_args" class.
"""
class queue_ip_args_tester:
	## =========================================================
	#	Method to test the O(1) methods that print information
	#		to the standard output, or are accessor methods.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	#	O(n) in terms of the number of input arguments.
	@staticmethod
	def test_o1_methods():
		print("	Test: queue_ip_args.how_to_use_script()			OK")
		queue_ip_args.how_to_use_script()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		print("	Test: queue_ip_args.print_help_option()			OK")
		queue_ip_args.print_help_option()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		print("	Test: queue_ip_args.get_list_of_input_arguments()	OK")
		temp_set_ip_args = queue_ip_args.get_list_of_input_arguments()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		print("	Test: queue_ip_args.print_all_input_arguments()		OK")
		queue_ip_args.print_all_input_arguments()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		prompt = "	Test: queue_ip_args.get_1st_input_argument()		{}"
		statistical_analysis.increment_number_test_cases_used()
		if queue_ip_args.get_1st_input_argument() is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		prompt = "	Test: queue_ip_args.get_2nd_input_argument()		{}"
		statistical_analysis.increment_number_test_cases_used()
		if queue_ip_args.get_2nd_input_argument() is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		print("	Testing for an empty list...")
		prompt1 = "	... Test: queue_ip_args.get_list_of_input_arguments()	{}"
		statistical_analysis.increment_number_test_cases_used()
		prompt2 = "	... Test: queue_ip_args.get_number_of_input_arguments()	{}"
		statistical_analysis.increment_number_test_cases_used()
		prompt4 = "	... Test: queue_ip_args.set_input_arguments(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		prompt5 = "	... Test: queue_ip_args.get_1st_input_argument()	{}"
		prompt6 = "	... Test: queue_ip_args.get_2nd_input_argument()	{}"
		#	List of input arguments.
		old_list_ip_args = queue_ip_args.get_list_of_input_arguments()
		new_list_ip_args = []
		"""
			Assign input arguments to "set_input_arguments(...)" for
				processing.
			Statement should fail.
		"""
		try:
			queue_ip_args.set_input_arguments(new_list_ip_args)
		except:
			if old_list_ip_args == queue_ip_args.get_list_of_input_arguments():
				print(prompt1 .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt1 .format("FAIL!!!"))
				#print(queue_ip_args.get_list_of_input_arguments())
			if len(old_list_ip_args) == queue_ip_args.get_number_of_input_arguments():
				print(prompt2 .format("OK"))
				statistical_analysis.increment_number_test_cases_passed()
			else:
				print(prompt2 .format("FAIL!!!"))
				#print(queue_ip_args.get_number_of_input_arguments())
			print(prompt4 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		print("	Testing for list with 1 argument...")
		"""
			Set the list of input arguments to have 1 argument, in addition
				to the name of the script.
			Hence, the list would have 2 arguments, since the first
				"argument" is dumped during the method call to
				set_input_arguments(...);
				this first "argument" is the name of the currently executing
					script.
		"""
		name_of_script_dumped = "name-of-the-script"
		current_1st_ip_arg = "benchmarks/majority_netlist.json"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		statistical_analysis.increment_number_test_cases_used()
		if new_list_ip_args == queue_ip_args.get_list_of_input_arguments():
			print(prompt1 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt1 .format("FAIL!!!"))
			#print(queue_ip_args.get_list_of_input_arguments())
		statistical_analysis.increment_number_test_cases_used()
		if len(new_list_ip_args) == queue_ip_args.get_number_of_input_arguments():
			print(prompt2 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt2 .format("FAIL!!!"))
			#print(len(new_list_ip_args)-1)
			#print(queue_ip_args.get_number_of_input_arguments())
		statistical_analysis.increment_number_test_cases_used()
		print(prompt4 .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		statistical_analysis.increment_number_test_cases_used()
		if current_1st_ip_arg == queue_ip_args.get_1st_input_argument():
			print(prompt5 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt5 .format("FAIL!!!"))
		"""
			If an input argument for the software is "-h", show the
				brief user manual to the user.
			Else, there is no need to test for more than 2 input arguments
				for the software, since only the first two are processed.
			So, the list shall have 3 elements, since the first element
				is dumped during the method call to set_input_arguments(...).
		"""
		print("	Testing for list with 2 arguments...")
		#	Set the list of input arguments to have 2 arguments.
		#new_list_ip_args = ["benchmarks/majority_netlist.json" "nonsense.json"]
		current_1st_ip_arg = "garbage.json"
		current_2nd_ip_arg = "nonsense.json"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		statistical_analysis.increment_number_test_cases_used()
		if new_list_ip_args == queue_ip_args.get_list_of_input_arguments():
			print(prompt1 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt1 .format("FAIL!!!"))
			#print(queue_ip_args.get_list_of_input_arguments())
		statistical_analysis.increment_number_test_cases_used()
		if len(new_list_ip_args) == queue_ip_args.get_number_of_input_arguments():
			print(prompt2 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt2 .format("FAIL!!!"))
			#print(queue_ip_args.get_number_of_input_arguments())
		statistical_analysis.increment_number_test_cases_used()
		print(prompt4 .format("OK"))
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		statistical_analysis.increment_number_test_cases_used()
		if current_2nd_ip_arg == queue_ip_args.get_2nd_input_argument():
			print(prompt6 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt6 .format("FAIL!!!"))
		prompt7 = "	... Test: queue_ip_args.input_arguments_error()	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			queue_ip_args.input_arguments_error()
			print(prompt7 .format("FAIL!!!"))
		except:
			print(prompt7 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
    ## =========================================================
	#	Method to test if the user wants to read the brief user
	#		manual.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_if_help_needed():
		print("	Testing for no help needed...")
		#	Set the list of input arguments to have 2 arguments.
		name_of_script_dumped = "name-of-the-script"
		current_1st_ip_arg = "garbage.json"
		current_2nd_ip_arg = "nonsense.json"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		prompt8 = "	... Test: queue_ip_args.check_if_help_wanted()	{}"
		statistical_analysis.increment_number_test_cases_used()
		queue_ip_args.check_if_help_wanted()
		print(prompt8 .format("	OK"))
		statistical_analysis.increment_number_test_cases_passed()
		print("	Testing for help needed (1st arg)... ")
		#	Change the list of input arguments to have "-h" option.
		current_1st_ip_arg = "-h"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		statistical_analysis.increment_number_test_cases_used()
		try:
			queue_ip_args.check_if_help_wanted()
			print(prompt8 .format("FAIL!!!"))
		except:
			print(prompt8 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		print("	Testing for help needed (2nd arg)... ")
		current_1st_ip_arg = "garbage.json"
		current_2nd_ip_arg = "-h"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		statistical_analysis.increment_number_test_cases_used()
		try:
			queue_ip_args.check_if_help_wanted()
			print(prompt8 .format("FAIL!!!"))
		except:
			print(prompt8 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		print("	Testing for help needed (3rd arg)... ")
		current_1st_ip_arg = "garbage.json"
		current_2nd_ip_arg = "nonsense.json"
		current_3rd_ip_arg = "-h"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg, current_3rd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		statistical_analysis.increment_number_test_cases_used()
		try:
			queue_ip_args.check_if_help_wanted()
			print(prompt8 .format("FAIL!!!"))
		except:
			print(prompt8 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
	## =========================================================
	#	Method to test the processing of the 1st & 2nd input arguments.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_processing_input_arguments():
		print("	Test: queue_ip_args.process_1st_ip_arg()... ")
		name_of_script_dumped = "name-of-the-script"
		current_1st_ip_arg = "garbage.json"
		current_2nd_ip_arg = "notes/guidelines/guidelines.tex"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		#	Assign input arguments to "set_input_arguments(...)" for processing.
		queue_ip_args.set_input_arguments(new_list_ip_args)
		prompt9 = "	... Invalid path to file	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			ip_fname = queue_ip_args.process_1st_ip_arg()
			print(prompt9 .format("		FAIL!!!"))
		except:
			print(prompt9 .format("			OK"))
			statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-
		"""
			1st input argument: Valid path to file, no JSON file extension.
		"""
		#current_1st_ip_arg = "benchmarks/majority_netlist.json"
		current_1st_ip_arg = "notes/mit-license.text"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		queue_ip_args.set_input_arguments(new_list_ip_args)
		prompt10 = "	... Valid path to file, no JSON file extension.	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			ip_fname = queue_ip_args.process_1st_ip_arg()
			print(prompt10 .format("		FAIL!!!"))
		except:
			print(prompt10 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		"""
			1st input argument: Valid path to file, JSON file extension.
		"""
		current_1st_ip_arg = "benchmarks/majority_netlist.json"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		queue_ip_args.set_input_arguments(new_list_ip_args)
		prompt10 = "	... Valid path to file, JSON file extension.	{}"
		statistical_analysis.increment_number_test_cases_used()
		ip_fname = queue_ip_args.process_1st_ip_arg()
		print(prompt10 .format("	OK"))
		statistical_analysis.increment_number_test_cases_passed()
		print("	-	-	-	-	-	-	-	-")
		print("	Test: queue_ip_args.process_2nd_ip_arg()... ")
		prompt11 = "	... Valid path to file	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			op_fname = queue_ip_args.process_2nd_ip_arg()
			print(prompt11 .format("				FAIL!!!"))
		except:
			print(prompt11 .format("				OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt12 = "	... Invalid path to file, no JSON extension	{}"
		statistical_analysis.increment_number_test_cases_used()
		current_2nd_ip_arg = "nonsense"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		queue_ip_args.set_input_arguments(new_list_ip_args)
		try:
			op_fname = queue_ip_args.process_2nd_ip_arg()
			print(prompt12 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt12 .format("	FAIL!!!"))
		prompt13 = "	... Invalid path to file, JSON extension	{}"
		statistical_analysis.increment_number_test_cases_used()
		current_2nd_ip_arg = "nonsense.json"
		new_list_ip_args = [name_of_script_dumped, current_1st_ip_arg, current_2nd_ip_arg]
		queue_ip_args.set_input_arguments(new_list_ip_args)
		try:
			op_fname = queue_ip_args.process_2nd_ip_arg()
			print(prompt13 .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt13 .format("	FAIL!!!"))

	## =========================================================
	#	Method to test methods that process input arguments to
	#		the software.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_queue_ip_args():
		print("")
		print("")
		print("==	Testing class: queue_ip_args.")
		queue_ip_args_tester.test_o1_methods()
		queue_ip_args_tester.test_if_help_needed()
		queue_ip_args_tester.test_processing_input_arguments()

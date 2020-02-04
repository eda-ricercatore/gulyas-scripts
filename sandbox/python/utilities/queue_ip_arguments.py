#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to process input
		arguments for a genetic technology mapping software.


	Synopsis:
	Process input arguments for a genetic technology mapping software.


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
"""

import sys
#import os
import os.path
#from subprocess import call
#import time
import warnings
#import re

###############################################################
#	Import Custom Python Modules


###############################################################
##	Module with methods that clean BibTeX files.
class queue_ip_args:
	#	List of input arguments
	set_of_input_arguments = []
	#	First input argument
	first_input_argument = "First input argument."
	#	Second input argument
	second_input_argument = "Second input argument."
	#	File extension for JSON files.
	json_f_ext = ".json"
	# ============================================================
	#	Accessor methods.
	# ============================================================
	##	Method to get the list of input arguments.
	#	@return - List of input arguments to the program.
	#	O(1) method.
	@staticmethod
	def get_list_of_input_arguments():
		"""
		print "=	Set_of_input_arguments:"
		for cur_ip_arg in queue_ip_args.set_of_input_arguments:
			print "	"+cur_ip_arg
		"""
		return queue_ip_args.set_of_input_arguments
	# ============================================================
	##	Method to print all the input arguments.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def print_all_input_arguments():
		println = "~	Set_of_input_arguments:"
		println += "=".join(str(x) for x in queue_ip_args.set_of_input_arguments)
		print(println)
	# ============================================================
	##	Method to get the first input argument.
	#	@return - First input argument for the program.
	#	O(1) method.
	@staticmethod
	def get_1st_input_argument():
		if 0 < len(queue_ip_args.get_list_of_input_arguments()):
			return queue_ip_args.set_of_input_arguments[0]
		else:
			warnings.warn("	1st input argument is missing!!!")
			queue_ip_args.input_arguments_error()
	# ============================================================
	##	Method to get the second input argument.
	#	@return - Second input argument for the program.
	#	O(1) method.
	@staticmethod
	def get_2nd_input_argument():
		if 1 < len(queue_ip_args.get_list_of_input_arguments()):
			return queue_ip_args.set_of_input_arguments[1]
		else:
			warnings.warn("	2nd input argument is missing!!!")
			queue_ip_args.input_arguments_error()
	# ============================================================
	##	Method to get the number of input arguments.
	#	@return - Number of input arguments for the program.
	#	O(1) method.
	@staticmethod
	def get_number_of_input_arguments():
		return len(queue_ip_args.set_of_input_arguments)
	# ============================================================
	#	Mutator methods.
	# ============================================================
	##	Method to set the input arguments.
	#		And, remove the name of the script from the list of input
	#		arguments, for easier processing.
	#	@param list_of_ip_arguments - A list of input arguments to
	#		the program.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def set_input_arguments(list_of_ip_arguments):
		#	Is the number of input arguments to the script <1?
		if 1 > len(list_of_ip_arguments):
			warnings.warn("	There are no input arguments!!!")
			queue_ip_args.input_arguments_error()
		queue_ip_args.set_of_input_arguments = list_of_ip_arguments
		# Remove the name of the script from the list of input arguments.
		queue_ip_args.set_of_input_arguments.pop(0)
	# ============================================================
	#	Other methods.
	# ============================================================
	##	Method to determine if the user wants help, and conequently
	#		display the user manual.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def check_if_help_wanted():
		# If user wants to read the brief user manual,
		if "-h" in queue_ip_args.set_of_input_arguments:
			# Display the user manual and exit.
			queue_ip_args.how_to_use_script()
			sys.exit()
	# ============================================================
	##	Method to provide information on how to run this script.
	#	O(1) method.
	@staticmethod
	def how_to_use_script():
		print("-------------------------------------------------")
		print("==>	This script performs genetic technology mapping.")
		print("")
		print("This script can be executed as follows:")
		print("./problem1_solution.py [input JSON netlist] [output JSON technology mapping] [-h]")
		print("")
		print("==>	This other script performs incremental regression testing")
		print("	of my solution for genetic technology mapping.")
		print("")
		print("This other script can be executed as follows:")
		print("./incremental_test.py [input JSON netlist] [output JSON technology mapping] [-h]")
		queue_ip_args.print_help_option()
		print("-------------------------------------------------")
	# ============================================================
	##	Method to print the help option to access the user manual.
	#	O(1) method.
	@staticmethod
	def print_help_option():
		print("An optional '-h' flag can be used as any input argument")
		print("	to show the brief user manual and exit.")
		print("")
	# ============================================================
	##	Method to indicate error wth input arguments.
	#	O(1) method.
	@staticmethod
	def input_arguments_error():
		queue_ip_args.how_to_use_script()
		# Inform the user what went wrong.
		raise Exception("Error with input arguments.")
	# ============================================================
	##	Method to process the first input argument.
	#	@return - 1st input argument, input filename.
	#	O(1) method.
	@staticmethod
	def process_1st_ip_arg():
		#	Is the number of input arguments to the script <1?
		if 1 > len(queue_ip_args.get_list_of_input_arguments()):
			warnings.warn("	There are no input arguments!!!")
			queue_ip_args.input_arguments_error()
		queue_ip_args.first_input_argument = queue_ip_args.get_1st_input_argument()
		println = "==	Is the 1st input argument a valid path to a file?"
		if (os.path.exists(queue_ip_args.first_input_argument) and os.path.isfile(queue_ip_args.first_input_argument)):
			print(println .format("	Yes."))
		else:
			raise Exception("1st input argument isn't a valid path to a file!")
		#	Does 1st input argument have a BibTeX file extension?
		println = "==	Does 1st input argument have a JSON file extension?"
		#	Get the filename and file extension of the 1st input argument.
		ip_fname1, ip_f_ext1 = os.path.splitext(queue_ip_args.first_input_argument)
#	print "==	File name of 1st input argument:"+ip_fname
#	print "==	File extension of 1st input argument:"+ip_f_ext
		if(ip_f_ext1 == queue_ip_args.json_f_ext):
			print(println .format("	Yes."))
			#	Add BibTeX file extension back to input filename.
			ip_fname1 = queue_ip_args.first_input_argument
		else:
			#	Add BibTeX file extension to input filename.
			ip_fname1 += queue_ip_args.json_f_ext
			print("	New output filename is: {}" .format(ip_fname1))
			raise Exception("1st input argument doesn't have JSON file extension!")
		return ip_fname1
	# ============================================================
	##	Method to process the second input argument.
	#	@return the output filename, based on the second input argument
	#	O(1) method.
	@staticmethod
	def process_2nd_ip_arg():
		#	Is the number of input arguments to the script <2?
		if 2 > len(queue_ip_args.get_list_of_input_arguments()):
			warnings.warn("	2nd input argument isn't available!!!")
			queue_ip_args.input_arguments_error()
		queue_ip_args.second_input_argument = queue_ip_args.get_2nd_input_argument()
		"""
		The 2nd input argument shouldn't be a valid path to an existing file.
		If it is, warn the user about overwritting the file & exit.
		"""
		println = "==	Is the 2nd input argument a valid path to a file?"
		if (os.path.exists(queue_ip_args.second_input_argument) and os.path.isfile(queue_ip_args.second_input_argument)):
			print("	2nd input argument is a valid path to a file!")
			println = "	File would be overwritten:"
			println += queue_ip_args.second_input_argument
			raise Exception("End program to avoid overwritting file.")
		else:
			print(println.format("	Yes."))
		#	Get the filename and file extension of the 2nd input argument.
		ip_fname2, ip_f_ext2 = os.path.splitext(queue_ip_args.second_input_argument)
		#	Does 2nd input argument have a BibTeX file extension?
		println = "==	Does 2nd input argument have a JSON file extension?"
		if(ip_f_ext2 == queue_ip_args.json_f_ext):
			print(println.format("	Yes."))
			ip_fname2 = queue_ip_args.second_input_argument
		else:
			print(println.format("	No."))
			#	Add BibTeX file extension to output filename.
			ip_fname2 = queue_ip_args.second_input_argument
			ip_fname2 += queue_ip_args.json_f_ext
			print("	New output filename is: {}" .format(ip_fname2))
		return ip_fname2

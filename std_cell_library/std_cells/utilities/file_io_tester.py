#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		input/output (I/O) operations on files, such as BibTeX
		databases/files, LaTeX documents, and JSON files.

	Synopsis:
	Test input/output (I/O) operations on files.

	Notes/Assumptions:
	Assume that the user/developer would protect the code base
		with try-except blocks to handle file I/O errors.

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
# Package and module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations

###############################################################
"""
	Module with methods that perform file I/O operations.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "file_io_operations"
		objects.
	Test each static method of the "file_io_operations" class.
"""
class file_io_operations_tester:
	## =========================================================
	#	Method to test the methods that perform file I/O operations
	#		with an invalid file.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_with_invalid_file():
		print("	... Testing file operations with invalid file.")
		filename = "nonsense"
		prompt = "	Test: file_io_operations.is_path_valid(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		if not file_io_operations.is_path_valid(filename):
			print(prompt .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("	FAIL!!!"))
		prompt = "	Test: file_io_operations.open_file_object_read(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_read(filename)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	Test: file_io_operations.open_file_object_write(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_write(filename)
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt .format("FAIL!!!"))
		prompt = "	Test: file_io_ops[BLAH].open_file_object_write_new(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_write_new(filename)
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt .format("FAIL!!!"))
		try:
			#	Close the file object, and delete the file.
			statistical_analysis.increment_number_test_cases_used()
			file_io_operations.close_file_object(f_obj)
			os.remove(filename)
			print("	Test: file_io_operations.close_file_object(...)		OK")
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the methods that perform file I/O operations
	#		with a valid file.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_with_valid_file():
		print("	... Testing file operations with valid file.")
		filename = "dev-notes/run_regression_testing.py"
		prompt = "	Test: file_io_operations.is_path_valid(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.is_path_valid(filename):
			print(prompt .format("	OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("	FAIL!!!"))
		prompt = "	Test: file_io_operations.open_file_object_read(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_read(filename)
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt .format("FAIL!!!"))
		prompt = "	Test: file_io_operations.open_file_object_write(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_write(filename)
			print(prompt .format("FAIL!!!"))
		except:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		prompt = "	Test: file_io_ops[BLAH].open_file_object_write_new(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		try:
			f_obj = file_io_operations.open_file_object_write_new(filename)
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except:
			print(prompt .format("FAIL!!!"))
		"""
			Close the file object to preserve data in the test data file.
			filename = "dev-notes/run_regression_testing.py"
		"""
		file_io_operations.close_file_object(f_obj)
		# Copy a file from [source] to [destination]
		#copyfile("dev-notes/run_regression_testing-copy.py","dev-notes/run_regression_testing.py")
		copyfile("dev-notes/run_regression_testing.py","dev-notes/run_regression_testing-copy.py")
	## =========================================================
	#	Method to test file operations on files with the same content.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_on_files_with_same_content():
		print("	Testing file operations on files with the same content.")
		prompt = "	... Test: file_io_operations.file_comparison(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.file_comparison("dev-notes/run_regression_testing.py","dev-notes/run_regression_testing-copy.py"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		print("	Testing file operations on files with the different content.")
		prompt = "	... Test: file_io_operations.file_comparison(...)	{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.file_comparison("dev-notes/run_regression_testing.py","makefile"):
			print(prompt .format("FAIL!!!"))
		else:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
	## =========================================================
	#	Method to test file_io_operations.get_file_extension() method.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_get_file_extension():
		print("	Testing file_io_operations.get_file_extension() method.")
		prompt = "	... Test: one file extension				{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.get_file_extension("something.text") == ".text":
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: double/dual file extensions			{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.get_file_extension("something.tar.gz") == ".tar.gz":
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			#print(file_io_operations.get_file_extension("something.tar.gz"))
		prompt = "	... Test: multiple file extensions			{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.get_file_extension("something.pdf.tar.gz") == ".pdf.tar.gz":
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test file_io_operations.check_file_extension() method.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_check_file_extension():
		print("	Testing file_io_operations.check_file_extension() method.")
		prompt = "	... Test: same file extension				{}"
		statistical_analysis.increment_number_test_cases_used()
		if file_io_operations.check_file_extension("something.text",".text"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: different file extensions			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not file_io_operations.check_file_extension("something.tar.gz",".rtsdtfyg"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test file_io_operations.open_file_object_write_results()
	#		method.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations_open_file_object_write_results():
		prompt = "	Test: file_io_BLAH.open_file_object_write_results()	{}"
		statistical_analysis.increment_number_test_cases_used()
		results_f_obj = file_io_operations.open_file_object_write_results()
		if results_f_obj:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(results_f_obj)
	## =========================================================
	#	Method to test the methods that perform file I/O operations.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_file_io_operations():
		print("==	Testing class: file_io_operations.")
		file_io_operations_tester.test_file_io_operations_with_invalid_file()
		file_io_operations_tester.test_file_io_operations_with_valid_file()
		file_io_operations_tester.test_file_io_operations_on_files_with_same_content()
		file_io_operations_tester.test_file_io_operations_get_file_extension()
		file_io_operations_tester.test_file_io_operations_check_file_extension()
		file_io_operations_tester.test_file_io_operations_open_file_object_write_results()

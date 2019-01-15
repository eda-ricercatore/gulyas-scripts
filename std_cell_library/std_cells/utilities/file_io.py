#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to perform
		input/output (I/O) operations on files, such as BibTeX
		databases/files, LaTeX documents, and JSON files.

	Synopsis:
	Perform input/output (I/O) operations on files.

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
    	from my BibTeX database (set of BibTeX entries).

	[DrakeJr2016b]
		Section 11 File and Directory Access, Subsection 11.2 os.path - Common pathname manipulations


"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

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
	calendar	For performing operations on dates.
	logging		For debug, info, warning, error, and critical messages.
				+ logging.debug("")
				+ logging.info("")
				+ logging.warning("")
				+ logging.error("")
				+ logging.critical("")
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import calendar
import logging

###############################################################
#	Import Custom Python Modules

# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations
"""
	Module to generate the filename for storing the experimental
		results and simulation output.
"""
from utilities.generate_results_filename import generate_filename

###############################################################
#	Module with methods that perform file I/O operations.
class file_io_operations:
	"""
		Location to store simulation and/or experimental results.
		Requires an absolute path, since no processing will be done
			to check if this is an absolute path or relative path.
	"""
	#result_repository = "~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	result_repository = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	# Backup of the standard output.
	std_op_backup = None
	# Backup of the standard error.
	std_err_backup = None
	#
	# ============================================================
	##	Method to check if a path to file is valid.
	#	@param filename - Path to a file.
	#	@return a boolean TRUE, if the path to the file is valid.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_path_valid(filename):
		if (os.path.exists(filename) and os.path.isfile(filename)):
			return True
		else:
			return False
	# ============================================================
	##	Method to open a file object for read/input operations.
	#	@param filename - Path to a file.
	#	@return file object ip_file_obj
	#	@throws Exception for invalid path to the file.
	#	O(1) method.
	@staticmethod
	def open_file_object_read(filename):
		if file_io_operations.is_path_valid(filename):
			ip_file_obj = open(filename, 'r')
			return ip_file_obj
		else:
			raise Exception("File Read Operation: Path to file is invalid.")
	# ============================================================
	##	Method to open a file object for write/output operations.
	#	@param filename - Path to a file.
	#	@return file object op_file_obj that enables writing to the
	#		file named "filename".
	#	@throws Exception for invalid path to the file.
	#	O(1) method.
	@staticmethod
	def open_file_object_write(filename):
		if not file_io_operations.is_path_valid(filename):
			op_file_obj = open(filename, 'w')
			return op_file_obj
		else:
			raise Exception("File Write Operation: Path to file is valid.")
	# ============================================================
	##	Method to open a new file object for write/output operations.
	#	@param filename - Path to a file.
	#	@return file object op_file_obj that enables writing to the
	#		file named "filename".
	#	O(1) method.
	@staticmethod
	def open_file_object_write_new(filename):
		if file_io_operations.is_path_valid(filename):
			os.remove(filename)
		op_file_obj = open(filename, 'w')
		return op_file_obj
	# ============================================================
	##	Method to open a new file object for write/output operations
	#		to store simulation and/or experimental results.
	#	@param - None.
	#	@return file object "results_file_obj" that writes data
	#		containing simulation and/or experimental results.
	#	O(1) method.
	@staticmethod
	def open_file_object_write_results():
		# Determine path to store simulation/experimental results.
		results_filename = generate_filename.create_filename()
		# Tokenize this filename (DD-MM-YY-HR-MN-SS-US format).
		tokens = date_time_operations.get_date_time_tokens_of_filename(results_filename)
		# Determine which year should the results file be placed in.
		current_path = os.path.join(file_io_operations.result_repository,tokens[2])
		#if (os.path.exists(current_path) and os.path.isdir(current_path)):
		if os.path.isdir(current_path):
			# Determine which month should the results file be placed in.
			#print("tokens[1]=",tokens[1],"=")
			#print("date_time_operations.mth_number_name[tokens[1]]=",date_time_operations.mth_number_name[tokens[1]],"=")
			current_path = os.path.join(current_path,date_time_operations.mth_number_name[tokens[1]])
			if not os.path.isdir(current_path):
				print("	... Creating directory for month at:",current_path)
				try:
					os.makedirs(current_path, exist_ok = True)
				except OSError:
					print("Encountered error in making directory.", file=sys.stderr)
					logging.error("Determine why directory for month cannot be created.")
			else:
				print(current_path,"=works= ... From: file_io.py, line 146.")
		else:
			print("	... Creating directory for year at:",current_path)
			try:
				os.makedirs(current_path, exist_ok = True)
			except OSError:
				print("Encountered error in making directory.", file=sys.stderr)
				logging.error("Determine why directory for year cannot be created.")
			# Determine which month should the results file be placed in.
			current_path = os.path.join(current_path, date_time_operations.mth_number_name[tokens[1]])
			print("	...os.path.exists(current_path:",os.path.exists(current_path))
			print("	...os.path.isdir(current_path):",os.path.isdir(current_path))
			print("	... Creating directory for month at:",current_path)
			try:
				os.makedirs(current_path, exist_ok = True)
			except OSError:
				print("Encountered error in making directory.", file=sys.stderr)
				logging.error("Determine why directory for month cannot be created.")
		results_filename = os.path.join(current_path, results_filename)
		return file_io_operations.open_file_object_write(results_filename)
	# ============================================================
	##	Method to close a file object.
	#	@param file_obj - A file object.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def close_file_object(file_obj):
		file_obj.close()
	# ============================================================
	##	Method to determine if two files are equivalent.
	#	@param file1 - Path to a file.
	#	@param file2 - Path to another file.
	#	@return a boolean TRUE, if the files are equivalent. Else,
	#		return FALSE.
	#	O(n) method, with respect to the number of lines in the
	#		larger (if the files are different), or either, of the
	#		files.
	@staticmethod
	def file_comparison(file1, file2):
		return filecmp.cmp(file1,file2,shallow=False)
	# ============================================================
	##	Method to determine the file extension of a file.
	#	@param filename - Name of a file.
	#	@return the file extension of a file.
	#	O(n) method, with respect to the number of characters in the
	#		path_to_file argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	#	References:
	#	1) \cite{Dharmkar2017}\cite{nosklo2017}
	#	2) \cite[\S11 File and Directory Access, \S11.2 os.path - Common pathname manipulations]{DrakeJr2016b}
	@staticmethod
	def get_file_extension(filename):
		temp_filename_extension = ""
		while True:
			filename_prefix, filename_extension = os.path.splitext(filename)
			if not filename_extension:
				break
			else:
				filename  = filename_prefix
				temp_filename_extension = filename_extension + temp_filename_extension
		return temp_filename_extension
	# ============================================================
	##	Method to determine if the file extension of a file matches with
	#		a given file extension.
	#	@param filename - Name of a file.
	#	@param file_extension - Extension
	#	@return boolean True if the file extension of the given filename
	#		matches file_extension; else, return False.
	#	O(n) method, with respect to the number of characters in the
	#		path_to_file argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	@staticmethod
	def check_file_extension(filename, file_extension):
		if file_extension == file_io_operations.get_file_extension(filename):
			return True
		else:
			return False
	# ============================================================
	##	Method to end redirection of standard output.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def stop_redirecting_std_op():
		sys.stdout = file_io_operations.std_op_backup
	# ============================================================
	##	Method to redirect standard output to a file object with
	#		write access.
	#	@param file_obj - File object with write access.
	#	@return boolean True if standard output is redirected to
	#		a file object with write access; else, return False.
	#	O(1) method.
	@staticmethod
	def redirect_std_op_to_file_obj(file_obj):
		file_io_operations.std_op_backup = sys.stdout
		sys.stdout = file_obj
	# ============================================================
	##	Method to end redirection of standard error.
	#	@param - None.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def stop_redirecting_std_err():
		sys.stderr = file_io_operations.std_err_backup
	# ============================================================
	##	Method to redirect standard error to a file object with
	#		write access.
	#	@param file_obj - File object with write access.
	#	@return boolean True if standard error is redirected to
	#		a file object with write access; else, return False.
	#	O(1) method.
	@staticmethod
	def redirect_std_err_to_file_obj(file_obj):
		file_io_operations.std_err_backup = sys.stderr
		sys.stderr = file_obj

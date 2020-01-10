#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to implement
		miscellaneous tasks.
	1) Add, commit, and push additions and updates to a Git repository.
	2) ???

	Synopsis:
	Perform miscellaneous tasks.


	#### IMPORTANT NOTES:
	#### IMPORTANT ASSUMPTIONS:
	A complete test suite for this Python module is not provided.
	This is because it would require a Python interface to Git in order
		to test if differences between the last build (or build *n*) and
		the previous last build (or build *n*-1) have been committed and
		pushed to the cloud-based Git repository.
		It involves checking for file additions and deletions, and file
			updates.
	I cannot simply and quickly write a test suite for this, so I have
		only tested this manually.


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
	calendar	For checking if given year is a leap year.
"""

import sys
#import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re
import calendar
from calendar import month_name

###############################################################
#	Import Custom Python Modules

"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
# Package and module to generate filename with time stamp.
#from utilities.generate_results_filename import generate_filename
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester

###############################################################
##	Module with methods that perform miscellaneous tasks.
class misc:
	absolute_path_to_store_results = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	# ============================================================
	##	Method to get the absolute path to store results.
	#	It is an accessor method.
	#	@param - Nothing.
	#	@return the absolute path to store results.
	#	O(1) method.
	@staticmethod
	def get_absolute_path_to_store_results():
		return misc.absolute_path_to_store_results
	# ============================================================
	##	Method to validate the absolute path to store results.
	#	It is an query method
	#	@param path_to_file - A path to store the results file.
	#	@param filename - A filename.
	#	@return boolean True, if the path to the desired location can
	#		be contains the value in "misc.absolute_path_to_store_results"
	#		and the filename of the results file.
	#		Else, return boolean False.
	#	O(1) method.
	@staticmethod
	def check_absolute_path_to_store_results(path_to_file,filename):
		if path_to_file.find(filename):
			return True
		else:
			return False
	# ============================================================
	##	Method to determine if a filename has the DD-MM-YY-HH-MM-SS-uS.txt
	#		format.
	#	@param filename - A filename.
	#	@return boolean True if the path to the desired location can
	#		be found;
	#		Else, return boolean False.
	#	O(1) method.
	@staticmethod
	def check_filename_format(filename):
		filename_wo_extn, file_extn = os.path.splitext(filename)
		if ".txt" != file_extn:
			return False
		tokens = filename_wo_extn.split("-")
		"""
			Check against the format: DD-MM-YY-HH-MM-SS-uS[.txt].
			tokens[0] = DD/Day
			tokens[1] = MM/Month
			tokens[2] = YY/Year
			tokens[3] = HH/Hour
			tokens[4] = MM/Minute
			tokens[5] = [SS/Second]
			tokens[6] = [uS/Microsecond]
		"""
		if 7 != len(tokens):
			return False
		if 1 > int(tokens[0]):
			return False
		if 2 == int(tokens[1]) and 29 < int(tokens[0]) and calendar.isleap(int(tokens[2])):
			return False
		if 2 == int(tokens[1]) and 28 < int(tokens[0]) and not calendar.isleap(int(tokens[2])):
			return False
		if generate_filename_tester.is_30_day_month(tokens[1]) and 30 < int(tokens[0]):
			return False
		if generate_filename_tester.is_31_day_month(tokens[1]) and 31 < int(tokens[0]):
			return False
		if 1 > int(tokens[1]):
			return False
		if 12 < int(tokens[1]):
			return False
		if 2000 > int(tokens[2]):
			return False
		if 0 > int(tokens[3]):
			return False
		if 23 < int(tokens[3]):
			return False
		if 0 > int(tokens[4]):
			return False
		if 59 < int(tokens[4]):
			return False
		if 0 > int(tokens[5]):
			return False
		if 59 < int(tokens[5]):
			return False
		if 0 > int(tokens[6]):
			return False
		if 999999 < int(tokens[6]):
			return False
		return True
	# ============================================================
	##	Method to determine where to store the results of the
	#		experimental, simulation, verification, or testing runs
	#	@param filename - A filename that has the DD-MM-YY-HH-MM-SS-uS.txt.
	#	@return a string representing the absolute path of the location.
	#	O(1) method.
	@staticmethod
	def find_desired_location_for_results(filename):
		# Does filename have the DD-MM-YY-HH-MM-SS-uS.txt format?
		if not misc.check_filename_format(filename):
			return "'filename' needs to have the format: DD-MM-YY-HH-MM-SS-uS.txt."
		# Remove file extension, and tokenize the filename.
		filename_wo_extn, file_extn = os.path.splitext(filename)
		tokens = filename_wo_extn.split("-")
		"""
			In the repository to store results from experiments,
				simulations, and verification runs, and testing runs,
				classify the files by subdirectories according to year
				first before the month.
		"""
		# Does a directory for the specified year exists?
		path_to_results_file = misc.get_absolute_path_to_store_results() +  "/" + tokens[2]
		if not os.path.isdir(path_to_results_file):
			# Creat the directory for the specified year.
			os.mkdir(path_to_results_file)
		# Does a directory for the specified month exists?
		path_to_results_file = path_to_results_file + "/" + month_name[int(tokens[1])].lower()
		if not os.path.isdir(path_to_results_file):
			# Creat the directory for the specified month.
			os.mkdir(path_to_results_file)
		path_to_results_file = path_to_results_file + "/" + filename
		#print("path_to_results_file:",path_to_results_file,"=")
		return path_to_results_file
	# ============================================================
	##	Method to store the results file in the specified absolute path.
	#	@param path_to_file - A path to store the results file.
	#	@return a file object for the results file.
	#	O(1) method.
	@staticmethod
	def store_results(path_to_file):
		if path_to_file is not None:
			return open(path_to_file, 'w+')
		else:
			return None
	# ============================================================
	##	Method to add, commit, and push additions and updates
	#		to a Git repository.
	#	@param comment - A comment for this commit/build [to the
	#						repository].
	#	@return boolean True if updates can be added, committed,
	#		and push additions to a Git repository;
	#		Else, return boolean False.
	#	O(1) method.
	@staticmethod
	def add_commit_push_updates_to_git_repository(comment):
		try:
			print("-------------------------------------------------")
			cmd = ['git', 'add', "-A"]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			#p = subprocess.call(cmd, cwd=config_manager.result_repository)
			print("-	Added. Commit now.")
			comment = "Update build via Python."
			cmd = ["git", "commit", "-m", comment]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			p.wait()
			print("-	Committed. Push now.")
			cmd = ["git", "push"]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			p.wait()
			print("-------------------------------------------------")
			return True
		except:
			return False

#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to implement
		miscellaneous tasks.
	1) Add, commit, and push additions and updates to a Git repository.
	2) ???

	Synopsis:
	Perform miscellaneous tasks.


	#### IMPORTANT NOTES:
	#### IMPORTANT ASSUMPTIONS:
	A test suite for this Python module is not provided.
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
"""

import sys
#import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re

###############################################################
#	Import Custom Python Modules

"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager

###############################################################
##	Module with methods that perform miscellaneous tasks.
class misc:
	# ============================================================
	##	Method to determine where to store the results of the
	#		experimental, simulation, verification, or testing runs
	#	@param filename - A filename that has the DD-MM-YY-HH-MM-SS.txt.
	#	@return boolean True if the path to the desired location can
	#		be found;
	#		Else, return boolean False.
	#	O(1) method.
	@staticmethod
	def find_desired_location_for_results(filename):
		return True
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

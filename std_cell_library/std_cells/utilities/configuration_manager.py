#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to configure the
		software application's parameters, via a JSON-based
		"parameters.config" (or "configuration.json") file.

	Synopsis:
	Manage the configuration of the software application's parameters.

	Notes/Assumptions:
	The "configuration.json" is parsed by the "config_file_parser.py",
		and its fields are mapped from a JSON object into a Python object
		represented by "json_object.py".
	In this parsing process, it sets the field(s) in this Python module/class.

		JSON (JavaScript Object Notation) is a subset of YAML
			(YAML Ain't Markup Language) \cite{WikipediaContributors2018o}.
		Hence, JSON is simpler to parse than YAML.
		Also, since XML (Extensible Markup Language)
			\cite{WikipediaContributors2018n} is more complex
			to parse than JSON \cite{Desai2015}, I am going to
			use the JSON format to represent data that is used
			to configure the parameters of the software application.

	Assume that relative paths refer to paths that begin from the
		user's home directory ("~/").
	Regarding Python's "os.path" module, paths that begin with
		"../" or "statistics"

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


###############################################################
#	Import Custom Python Modules


###############################################################
#	Module with methods that perform file I/O operations.
class config_manager:
	#	Base location to store simulation and/or experimental results.
	#result_repository = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	result_repository = "Unknown location."
	#
	# ============================================================
	##	Method to set the location of simulation/experimental results.
	#	@param location - Location of a directory.
	#	@return a boolean TRUE, if the location is a valid directory.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def set_result_repository(location):
		if not os.path.isabs(location):
			#print("	location is a relative path.")
			# Change the relative path to an absolute path.
			location = os.path.expanduser(location)
		#else:
		#	print("	location is an absolute path.")
		if os.path.isdir(location):
			#print("	location is a valid directory.")
			config_manager.result_repository = location
			return True
		else:
			#print("	location is an invalid directory.")
			return False
	# ============================================================
	##	Method to get the location of simulation/experimental results.
	#	@param - None.
	#	@return the location of simulation/experimental results.
	#	O(1) method.
	@staticmethod
	def get_result_repository():
		return config_manager.result_repository

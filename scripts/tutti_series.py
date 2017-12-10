#!/usr/bin/python

"""
	This is written by Zhiyang Ong to display series from my BibTeX
		entries, in my BibTeX database.



	Synopsis: command name and [argument(s)]
	./tutti_series.py [input BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is described as follows:
	Initialize an empty list of keywords.
	Enumerate each line in the input BibTeX database.
		If the currently enumerated line contains the 'Series'
			BibTeX field,
			Add its contents to set of series. 
	Sort the set of series.

	Notes/Assumptions:
	Assume that the 'Keywords' standard BibTeX field is a single line
		field.


	Revision History:
	April 17, 2017			Version 0.1, initial build.
"""

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'Apr 17, 2017'

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

###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
from queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from file_io import file_io_operations


###############################################################
#	Module with methods that collects the set of keywords found
#		in all the 'Keywords' fields in this BibTeX database.
class keywords_show:
	list_of_keywords = []
	# ============================================================
	#	Method to collect keywords from each BibTeX entry's
	#		'Keywords' field, sort them, and display them in
	#		standard output.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def collect_and_list_keywords(ip_f_obj,ip_file):
		print "=	Reading input BibTeX file:"+ip_file
		# List/set of keywords found in the BibTeX database
		set_of_keywords = []
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			if(keywords_show.is_keywords_BibTeX_field(line)):
				keywds_line = line.replace("	Keywords = {","")
				keywds_line = keywds_line.replace("},\n","")
				keywds_line = keywds_line.split(", ")
				set_of_keywords = list(set(set_of_keywords+keywds_line))
				set_of_keywords = sorted(set_of_keywords)
		for kwd in set_of_keywords:
			print kwd
		print "===	Number of keyphrases:",len(set_of_keywords)

	# ============================================================
	#	Method to determine if a string 'a_str' starts with the
	#		'Keywords' standard BibTeX field.
	#	@param a_str - a string to be processed.
	#	@return True, if 'a_str' starts with the 'Keywords'
	#		standard BibTeX field.
	#		Else, return False.
	#	O(1) method.
	@staticmethod
	def is_keywords_BibTeX_field(a_str):
		if(a_str.startswith("	Keywords = {")):
			return True
		else:
			return False



















###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	# --------------------------------------------------------
	#	= Start of Preprocessing.
	queue_ip_args.preprocessing()
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print "==================================================="
	print "Displaying Sorted List of Keywords from a BibTeX Database."
	print ""
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.KEYWORDS_DISPLAY)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print "=	Process the first input argument." 
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print "=	Create a file object for reading."
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	"""
		Collect the set of all keywords found in the BibTeX database.
		Sort the set/list.
		Display the set.
	"""
	keywords_show.collect_and_list_keywords(ip_file_obj, ip_filename)
	# Close the file object for reading.
	print "=	Close the file object for reading."
	file_io_operations.close_file_object(ip_file_obj)

#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to determine if a
		non-standard BibTeX field ("Bdsk-Url-1" or "Bdsk-Url-2")
		exist, when "Doi" nor "Url" BibTeX field exist.
	When "Bdsk-Url-1" or "Bdsk-Url-2" exists, copy their values to
		the "Url" BibTeX field (and "Doi" field, if it is a DOI).
	
	Synopsis:
	For each BibTeX entry in the BibTeX database, check if it has the
		"Bdsk-Url-1" (and "Bdsk-Url-2") field(s), and if the "Url"
		(and Doi) field(s) is(/are) missing.

	This script can be executed as follows:
	./validate_url.py [input BibTeX file] [output BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have duplicate
								BibTeX entries, metadata, and
								non-standard BibTeX fields.
	[output BibTeX file]:	A clean BibTeX file without duplicate
								BibTeX entries, metadata, and
								non-standard BibTeX fields.
							[Optional parameter]

	The 2nd (and subsequent) input argument(s) is(/are) optional.

	The 2nd input argument mustn't be a valid path to an existing file.
	If it is, warn the user about overwritting the file & exit.

	If 2nd input argument has no file extension, add the BibTeX file
		extension to it.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).




	Revision History:
	April 8, 2017			Version 0.1, initial build.

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
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re


###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
from queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from file_io import file_io_operations


###############################################################
#	Module with methods that clean BibTeX files.
class validate_url_field:
	# ============================================================
	#	Method to determine if the user wants help, and conequently
	#		display the user manual.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def check_if_help_wanted():
		# If user wants to read the brief user manual,
		if "-h" in queue_ip_args.set_of_input_arguments:
			# Display the user manual and exit.
			validate_url_field.how_to_use_script()
			sys.exit()



























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
	print "Validating the URLs/DOIs of BibTeX entries."
	print ""
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print "=	Process the first input argument." 
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Check if 2nd input argument is missing/available.
	queue_ip_args.missing_2nd_ip_arg()
	# Process the second input argument.
	print "=	Process the second input argument." 
	op_filename = queue_ip_args.process_2nd_ip_arg()
	# Create a file object for reading.
	print "=	Create a file object for reading."
	ip_file_obj = Duplicate_BibTeX_entries_finder.read_input_BibTeX_file(ip_filename)
	# Create a file object for writing.
	print "=	Create a file object for writing."
	op_file_obj = file_io_operations.open_file_object_write(op_filename)
	# Close the file object for reading.
	print "=	Close the file object for reading."
	file_io_operations.close_file_object(ip_file_obj)
	# Close the file object for writing.
	print "=	Close the file object for writing."
	file_io_operations.close_file_object(op_file_obj)

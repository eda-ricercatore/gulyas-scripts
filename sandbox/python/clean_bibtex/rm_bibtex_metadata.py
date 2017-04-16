#!/usr/bin/python

"""
	This is written by Zhiyang Ong to delint/remove BibTeX metadata
		from my BibTeX database.

	That is, it will create a clean BibTeX database from my "dirty"
		BibTeX database.



	Synopsis: command name and [argument(s)]
	./rm_bibtex_metadata.py [input BibTeX file] [output BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have BibTeX
								metadata and non-standard BibTeX
								fields.
	[output BibTeX file]:	A clean BibTeX file without BibTeX
								metadata and non-standard BibTeX
								fields.
							[Optional parameter]

	The 2nd (and subsequent) input argument(s) is(/are) optional.

	The 2nd input argument mustn't be a valid path to an existing file.
	If it is, warn the user about overwritting the file & exit.

	If 2nd input argument has no file extension, add the BibTeX file
		extension to it.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is given as follows:
	Enumerate each line in the input BibTeX database.
		If the currently enumerated line contains a standard BibTeX
			field,
			Copy the line to the output BibTeX file. 


	Notes/Assumptions:
	Do not consider the 'Annote' field as a 'standard' BibTeX field.

	Assume that each 'standard' BibTeX field is a single line field.

	If the BibTeX field 'Annote' has multiple lines, only its last
		line will end with '}}' and that 'Annote' is the last field
		of the BibTeX entry.


	Revision History:
	April 8, 2017			Version 0.1, initial build.
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
__date__ = 'Apr 13, 2017'

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
#	Module with methods that delint/remove metadata in a copy
#		of an input BibTeX database.
class rm_metadata:
	#	Set to 'False' if line ending with '}}' is found before the next entry.
	print_final_close_curly_brace = True
	# BibTeX field 'Annote'
	BibTeX_field_annote = "	Annote = {"
	end_of_entry = "}}\n"
	# ============================================================
	#	Method to copy data from the input BibTeX file to the output
	#		BibTeX file, except for BibTeX metadata.
	#	That is, BibTeX metadata will not be copied to the output file.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param op_f_obj - The file object for the output stream,
	#						which writes the output to a BibTeX file.
	#	@param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def lint(ip_f_obj,op_f_obj,ip_file):
		print "=	Reading input BibTeX file:"+ip_file
		# FIFO queue to store fields of a BibTeX entry.
		fifo_queue = []
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				print "	First line of BibTeX entry."
				# If the last line of the previous entry ends with '},'
				if(rm_metadata.print_final_close_curly_brace):
					# Empty all but the last line of the FIFO queue
					while(1 < len(fifo_queue)):
						# Write each line to the output file.
						print "	Size of FIFO queue:"+str(len(fifo_queue))
						op_f_obj.write(fifo_queue.pop(0))
					# For the last line, change '},' to '}}' at the end.
					print "===	Size of FIFO queue:"+str(len(fifo_queue))
					if(1 == len(fifo_queue)):
						a_str  = fifo_queue.pop(0)
						# Remove the '\n' character.
						a_str = a_str[:-1]
						# Remove the ',' character.
						a_str = a_str[:-1] + "}"
						# Write last line of previous entry to output file.
						op_f_obj.write(a_str)
				else:
					# Empty the FIF queue of its contents.
					while(0 < len(fifo_queue)):
						# Write each line to the output file.
						print "	length of FIFO queue:"+str(len(fifo_queue))
						op_f_obj.write(fifo_queue.pop(0))
				# No, last line of the previous entry ends with '}}'.
				# Print a blank line to distinguish it from the
				#	previous BibTeX entry.
				op_f_obj.write("\n")
				op_f_obj.write("\n")
				# Enqueue this line to the FIFO queue.
				fifo_queue.append(line)
			# No. Does this line starts with a standatd BibTeX field?
			elif(rm_metadata.is_std_BibTeX_field(line)):
				# Enqueue this line to the FIFO queue.
				fifo_queue.append(line)
				print "	Line is enqueued."
				# Yes. Is this the last line of the BibTeX entry?
				if(rm_metadata.is_last_line(line)):
					# Yes. Set corresponding flag to True.
					rm_metadata.print_final_close_curly_brace = False
					print "	Found last line of BibTeX entry."
		if(rm_metadata.print_final_close_curly_brace):
			# Empty all but the last line of the FIFO queue
			while(1 < len(fifo_queue)):
				# Write each line to the output file.
				print "	cardinality of FIFO queue:"+str(len(fifo_queue))
				op_f_obj.write(fifo_queue.pop(0))
				# For the last line, change '},' to '}}' at the end.
				print "===	cardinality of FIFO queue:"+str(len(fifo_queue))
				if(1 == len(fifo_queue)):
					a_str  = fifo_queue.pop(0)
					# Remove the '\n' character.
					a_str = a_str[:-1]
					# Remove the ',' character.
					a_str = a_str[:-1] + "}"
					# Write last line of previous entry to output file.
					op_f_obj.write(a_str)
		else:
			# Empty the FIF queue of its contents.
			while(0 < len(fifo_queue)):
				# Write each line to the output file.
				print "	length of FIFO queue:"+str(len(fifo_queue))
				op_f_obj.write(fifo_queue.pop(0))
	# ============================================================
	#	Method to determine if a string 'a_str' starts with a
	#		standard BibTeX field.
	#	@param a_str - a string to be processed.
	#	@return True, if 'a_str' starts with a standard BibTeX field.
	#		Else, return False.
	#	O(n) method, with respect to the number of BibTeX fields.
	@staticmethod
	def is_std_BibTeX_field(a_str):
		for field_f in queue_ip_args.set_of_std_BibTeX_fields:
			if(a_str.startswith(field_f)):
				return True
		return False
	# ============================================================
	#	Method to determine if a string 'a_str' does not start
	#		with a standard BibTeX field.
	#	@param a_str - a string to be processed.
	#	@return True, if 'a_str' doesn't start with a standard
	#		BibTeX field.
	#		Else, return False.
	#	O(n) method, with respect to the number of BibTeX fields.
	@staticmethod
	def is_not_std_BibTeX_field(a_str):
		if(rm_metadata.is_std_BibTeX_field(a_str)):
			return False
		else:
			return True
	# ============================================================
	#	Method to determine if a line in the BibTeX database is the
	#		last line of a BibTeX entry.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line is the last line of a
	#		BibTeX entry.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_last_line(a_str):
		if(a_str.endswith(rm_metadata.end_of_entry)):
			return True
		else:
			return False
	# ============================================================
	#	Method to ensure that the output BibTeX file has no BibTeX
	#		metadata.
	#	That is, BibTeX metadata isn't copied to the output file.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param op_file - The filename of the output BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def ensure_no_metedata(ip_f_obj,op_file):
		print "=	Reading output BibTeX file:"+op_file
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			# Is this line the 1st line of a BibTeX entry?
			if(("@" != line[0]) and (rm_metadata.is_not_std_BibTeX_field(line))):
				if(0 == len(line)):
					raise Exception("Metadata exists in output BibTeX file.")




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
	print "Removing metadata from a BibTeX database."
	print ""
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.REMOVE_METADATA)
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
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	# Create a file object for writing.
	print "=	Create a file object for writing."
	op_file_obj = file_io_operations.open_file_object_write(op_filename)
	"""
		Copy data from input BibTeX file to output BibTeX file,
		without metadata.
	"""
	rm_metadata.lint(ip_file_obj, op_file_obj,ip_filename)
	# Close the file object for reading.
	print "=	Close the file object for reading."
	file_io_operations.close_file_object(ip_file_obj)
	# Close the file object for writing.
	print "=	Close the file object for writing."
	file_io_operations.close_file_object(op_file_obj)
	# Compare the input and output BibTeX files.
	if (file_io_operations.file_comparison(ip_filename,op_filename)):
		print "=	The input and output BibTeX files are EQUIVALENT!!!"
	else:
		print "=	The input and output BibTeX files are different."
	# Ensure that no BibTeX metadata exists in the output BibTeX file.
	ip_file_obj = file_io_operations.open_file_object_read(op_filename)
	rm_metadata.ensure_no_metedata(ip_file_obj,op_filename)
	file_io_operations.close_file_object(ip_file_obj)
	print "=	Output BibTeX file has no BibTeX metadata."
	# Delete the output BibTeX file.
#	os.remove(op_filename)

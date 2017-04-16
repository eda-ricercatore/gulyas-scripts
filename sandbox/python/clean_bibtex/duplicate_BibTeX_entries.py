#!/usr/bin/python
###	#!/usr/bin/python -mtimeit


"""
	This Python script is written by Zhiyang Ong to determine if
		duplicate BibTeX entries exist in my BibTeX database.
	If such entries exist, warn the user that duplicate BibTeX
		entries exist. 

	Synopsis:
	Find duplicate BibTeX entries in my BibTeX database, and indicate
		the location of their existence (if they exist).

	This script can be executed as follows:
	./duplicate-BibTeX-entries.py [input BibTeX file]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have duplicate
								BibTeX entries.




	Revision History:
	??????, 2014		Version 0.1
	March 14, 2017		Version 0.2	Testing the first argument.
	March 22, 2017		Version 0.3	Working on second argument.
	April 7, 2017		Version 0.4	Refactored script.
	April 14, 2017		Version 1.0 Working script release.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Apr 14, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

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

	pathlib->Path
				For mapping a string to a path. 
"""

import sys
import os
import os.path
#from pathlib import Path
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
class Duplicate_BibTeX_entries_finder:
	# List of BibTeX keys
	set_of_BibTeX_keys = []
	num_of_bibtex_entries = 0
	# ============================================================
	#	Other methods.
	# ============================================================
	#	Method to add BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n) method, where n is the number of BibTeX keys.
	@staticmethod
	def add_BibTeX_key(found_BibTeX_key):
		if (found_BibTeX_key in Duplicate_BibTeX_entries_finder.set_of_BibTeX_keys):
			temp_str = "Duplicate BibTeX key:"+found_BibTeX_key
			warnings.warn(temp_str)
			raise Exception("Multiple instances of a BibTeX key")
		Duplicate_BibTeX_entries_finder.set_of_BibTeX_keys.append(found_BibTeX_key)
	# ============================================================
	#	Method to sort BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n*log(n)) method, where n is the number of BibTeX keys.
	@staticmethod
	def sort_BibTeX_keys():
		Duplicate_BibTeX_entries_finder.set_of_BibTeX_keys = sorted(Duplicate_BibTeX_entries_finder.set_of_BibTeX_keys)
	# ============================================================
	#	Method to read each line of the input BibTeX file.
	#	O(n) method, where n is the number of lines of the BibTeX file.
	@staticmethod
	def read_input_BibTeX_file(ip_file_object,input_BibTeX_file):
		#print "--------------------------------------------------------"
		print "=	Reading input BibTeX file:"+input_BibTeX_file
		# Read each available line in the input BibTeX file.
		for line in ip_file_object:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
#				print "...	First line of a BibTeX entry."
				# Increment number of BibTeX entries.
				Duplicate_BibTeX_entries_finder.num_of_bibtex_entries = Duplicate_BibTeX_entries_finder.num_of_bibtex_entries + 1
				tokenized_BibTeX_entry = re.split('@|{|,',line)
				# Is the type of the BibTeX entry valid?
				if (tokenized_BibTeX_entry[1] in queue_ip_args.BibTeX_entry_types):
					# Yes. Try adding the BibTeX entry to "set_of_BibTeX_keys".
					Duplicate_BibTeX_entries_finder.add_BibTeX_key(tokenized_BibTeX_entry[2])
				else:
					# No. Warn user that the type of BibTeX entry is invalid!
					temp_str = "Invalid type of BibTeX entry:"+tokenized_BibTeX_entry[1]
					print temp_str
					warnings.warn(temp_str)
					raise Exception("BibTeX entry has an invalid type!")
		if (Duplicate_BibTeX_entries_finder.num_of_bibtex_entries != len(Duplicate_BibTeX_entries_finder.set_of_BibTeX_keys)):
			raise Exception("Mismatch in number of BibTeX entries processed.")
		else:
			print "=	Number of BibTeX entries processed:"+str(Duplicate_BibTeX_entries_finder.num_of_bibtex_entries)











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
	print "Finding duplicate BibTeX entries in my BibTeX database."
	print "	And, if they exist, warn the user about them."
	print ""
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.DUPLICATE_ENTRIES)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print "=	Process the first input argument." 
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print "=	Create a file object for reading."
	# Create a file object for input BibTeX file, in reading mode.
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	Duplicate_BibTeX_entries_finder.read_input_BibTeX_file(ip_file_obj,ip_filename)
	# Close the file object for reading.
	print "=	Close the file object for reading."
	file_io_operations.close_file_object(ip_file_obj)

#!/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to clean
		BibTeX databases/files of metadata and non-standard BibTeX
		fields.
	As for non-standard types of BibTeX entries, it shall change
		their BibTeX type to "misc".
	
	Synopsis:
	Remove non-standard BibTeX fields and correct non-standard
		BibTeX types.

	This script can be executed as follows:
	./clean-bibtex-db.py [BibTeX file]

	Parameters:
	[BibTeX file]: A BibTeX file to be processed.
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
#	Module with methods that clean BibTeX files.
class file_io_operations:
	# ============================================================
	#	Method to provide information on how to run this script.
	#	O(1) method.
	@staticmethod
	def how_to_use_script():
		print "-------------------------------------------------"
		print "==>	This script determines if duplicate BibTeX entries"
		print "	exist in my BibTeX database."
		print "	If they do, remove the duplicate BibTeX entries."
		print ""
		print "This script can be executed as follows:"
		print "./duplicate-BibTeX-entries.py [input BibTeX file] [output BibTeX file]"
		print ""
		print "2nd input argument mustn't be a valid path to an existing file."
		print "If it is, warn the user about overwritting the file & exit."
		print ""
		print "If 2nd input argument has no file extension, add the"
		print "	BibTeX file extension to it."
		print ""
		print "-------------------------------------------------"
		# Inform the user what went wrong.
		raise Exception("Error with input arguments.")






	

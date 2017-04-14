#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to perform
		input/output (I/O) operations on files, such as BibTeX
		databases/files and LaTeX documents.
"""

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Apr 14, 2017'

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
#	Module with methods that perform file I/O operations.
class file_io_operations:
	# ============================================================
	#	Method to open a file object for read/input operations.
	#	O(1) method.
	@staticmethod
	def open_file_object_read(filename):
		ip_file_obj = open(filename, 'r')
		return ip_file_obj
	# ============================================================
	#	Method to open a file object for write/output operations.
	#	O(1) method.
	@staticmethod
	def open_file_object_write(filename):
		op_file_obj = open(filename, 'w')
		return op_file_obj
	# ============================================================
	#	Method to close a file object.
	#	O(1) method.
	@staticmethod
	def close_file_object(file_obj):
		file_obj.close()




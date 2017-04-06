#!/usr/bin/python

"""
	This is written by Zhiyang Ong to comment out print statements in C++.
 
	Synopsis:
	Script to comment out print/trace statements in C++.
	
	Procedure:
	1)	Create file objects for read and write separately
			(for the same input file).
	2)	Read the file, or a set of files individually.
	3)	Modify currently enumerated line.
	4)	Write the modified line to the input file.
	
	
	Required files:
	cons_tuple.py		To store a list of cons 2-tuples



	IMPORTANT NOTE!!!
	=================
	The list of source files to be processed would not be recursively
		processed for a given directory.
	The absolute path for each file should be specified, and added
		to the set of all files (specified by their absolute paths).
	
			
	References:
	Adam Pierce and Matthew Eager (Editor), Answer to "How do
		I modify a text file in Python?", in Stack Overflow,
		Stack Exchange Inc., New York, NY, September 24, 2008
		(Modified October 9, 2012).

	Revision History:
	1)	November 13, 2014. Initial working version.
	2)	November 16, 2014. Specify each file individually, since I do
			not want to comment out original print/trace statements
			automatically with this script.
 
 
 
 	The MIT License (MIT)
 
 	Copyright (c) <2014> <Zhiyang Ong>
 
 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""


#	Import packages and functions from the Python Standard Library.
import os.path, string, sys
from os.path import isfile
from os import remove
from string import find
from shutil import move

#	Import my Python modules
from cons_tuple import cons_tuple


#	============================================================

#	Preliminaries: Set up the file objects/streams for processing.

#	Location of C++ source files.
#	/home/grads/z/zhiyang/personale/scripts/modfile/z-cpp-inputs

#	List of filesnames, specified by their absolute paths.
list_fnames = ["/home/grads/z/zhiyang/personale/scripts/modfile/z-cpp-inputs/ip1.cpp", "/home/grads/z/zhiyang/personale/scripts/modfile/z-cpp-inputs/ip2.cpp", "/home/grads/z/zhiyang/personale/scripts/modfile/z-cpp-inputs/ip3.cpp"];

"""
	For each file in the list of files to be processed, remove its
		trace statements.
"""
for src_file in list_fnames:
	#	Is the specified input test file a valid file?
	if not(isfile(src_file)):
		#	No. Raise an Error (i.e., Exception).
		print "==	Path to input file is:::" + src_file
		raise IOError("Input File does NOT exists.")
	#	Create separate input and output file objects
	ip_f_obj = open(src_file, "r");
	#	Filename for output test file.
	op_file = "output-file.txt"
	op_f_obj = open(op_file, "w");
	#	============================================================
	#	Create a list of cons to store (original, updated) value pairs.
#	list_cons = [cons_tuple("cout", "// cout"), cons_tuple("	cout", "	// cout"), cons_tuple("		cout", "		// cout"), cons_tuple("			cout", "// 			cout"), cons_tuple("				cout", "				// cout"), cons_tuple("printer::debug_std_op", "// printer::debug_std_")]
	list_cons = [cons_tuple("cout", "// cout"), cons_tuple("printer::debug_std_", "// printer::debug_std_")]
	#	============================================================
	#	Enumerate all lines of the input text file.
	for ln_num, cur_ln in enumerate(ip_f_obj):
		print "<<		Currently enumerated line:" + cur_ln	#.lstrip()
		temp_str = cur_ln	#.lstrip()
		#	Enumerate all cons_tuples.
		for c_instance in list_cons:
			if -1 < string.find(temp_str, c_instance.get_car()):
				print ">>	String with the term, "+c_instance.get_car()+", is found!"
				temp_str = string.replace(temp_str,c_instance.get_car(), c_instance.get_cdr())
				print "<<		Modified line:" + temp_str
		op_f_obj.write(temp_str)
	#	============================================================
	#	Close the input and output file objects.
	ip_f_obj.close()
	op_f_obj.close()
	#	move(ip_f_obj,op_f_obj)
	move(op_file,src_file)

#	============================================================
print ">>>	End of program.		<<<"


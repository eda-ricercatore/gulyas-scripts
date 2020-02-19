#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to test concepts in string processing.

	Synopsis:
	Script to process strings.


 Revision History:
 1) November 13, 2014. Initial working version.



 	The MIT License (MIT)

 	Copyright (c) <2014> <Zhiyang Ong>

 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""


#	Import packages and functions from the Python Standard Library.
import string
import os


#	============================================================


my_str = "UC Berkeley's logic synthesis tool, ABC, is the best logic synthesis and verification tool in the world."
print(my_str)

my_str = my_str.replace("UC Berkeley", "MIT")
print(my_str)

filename, file_extension = os.path.splitext('daniela-stefanescu')
if None == file_extension:
	print("file_extension is equal to None.")
else:
	print("file_extension is equal to something else.")

if not file_extension:
	print("file_extension is empty.")
else:
	print("file_extension is not empty???")


base_directory = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
a_path = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/2020"
if a_path.startswith(base_directory):
	print("=	a_path starts with base_directory.")
else:
	print("=	a_path DOES NOT start with base_directory.")
if "tyriuoipo".startswith(base_directory):
	print("=	tyriuoipo STARTS WITH base_directory.")
else:
	print("=	a_path does not start with base_directory.")
if "tyriuoipo".startswith("dwedew"):
	print("=	tyriuoipo STARTS WITH base_directory.")
else:
	print("=	a_path does not start with base_directory.")








print("\n\n")
"""
	The Python method "os.path.splitext()" to split the path
		for a file into the root of the path (without the
		file extension suffix) and the file extension.


	Unfortunately, by default, it defines the file extension
		as the string starting from the last period (if it
		exists) till the end of the string.
	Hence, file extensions such as ".tar.gz" would not be
		recognized and detected correctly.
	If I want to define file extension otherwise, I have
		to provide an implementation of a Python method
		complying with the new definition.

	References:
	+ BibTeX key: DrakeJr2016b
		- From the section "File and Directory Access",
			subsection "os.path - Common pathname manipulations".
		- By definition of the "os.path.splitext ()" (Python)
			method returns the root of the file's path and
			the file extension.
"""
print ("25-3-2010-5-8-51-9407.txt is being partitioned into the filename without the file extension suffix and the file extension.")
filename_wo_extn, file_extn = os.path.splitext ("25-3-2010-5-8-51-9407.txt")
print ("filename_wo_extn is:", filename_wo_extn, "=")
print("file_extn is:",file_extn,"=")
print("/path/to/filename.pdf.tar.gz is being partioned into the filename without the file extension suffix and the file extension.")
filename_wo_extn, file_extn = os.path.splitext("/path/to/filename.pdf.tar.gz")
print("filename_wo_extn is:",filename_wo_extn,"=")
print("file_extn is:",file_extn,"=")
tokens = filename_wo_extn.split("-")
print("isinstance(tokens, list) is:",isinstance(tokens, list),"=")
print("isinstance(None, list) is:",isinstance(None, list),"=")
print("isinstance('dewd323 vrevnoi.123', str) is:",isinstance("dewd323 vrevnoi.123", str),"=")
print("isinstance(None, str) is:",isinstance(None, str),"=")
print("isinstance(32.234, str) is:",isinstance(32.234, str),"=")
print("\n\n")




months_of_the_year = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
print("months_of_the_year[2] is:",months_of_the_year[2-1],"=")
#print("months_of_the_year[02] is:",months_of_the_year[int(02)],"=")
print("months_of_the_year[10] is:",months_of_the_year[10-1],"=")



a_bin_str = "0b0010100110"
b_bin_str = a_bin_str[2:]
print("b_bin_str is:",b_bin_str,"=")


c_string = "I love fried plantains."
for char in c_string:
	print("current character is:", char, "=")
	if ('a' == char) or ('n' == char):
		print("=	Found 'a' or 'n'.")
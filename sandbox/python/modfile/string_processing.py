#!/usr/bin/python

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
print my_str

my_str = my_str.replace("UC Berkeley", "MIT")
print my_str

filename, file_extension = os.path.splitext('daniela-stefanescu')
if None == file_extension:
	print("file_extension is equal to None.")
else:
	print("file_extension is equal to something else.")

if not file_extension:
	print("file_extension is empty.")
else:
	print("file_extension is not empty???")

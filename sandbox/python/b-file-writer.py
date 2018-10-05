#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to write documents in another folder.

	Synopsis: command name and [argument(s)]
	./b-file-writer.py

	Revision History:
	September 11, 2018			Version 0.1, initial build.
"""


#	The MIT License (MIT)

#	Copyright (c) <2014-2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'September 11, 2018'

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
	datetime	For date and time processing.
	json		For parsing JSON files and processing JSON-based data.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
from datetime import date
import datetime
import json


###############################################################
#	Import Custom Python Modules

# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations

###############################################################

"""
	A function with three return values.
"""
def function_with_3_return_values():
	month = 5
	year = 2018
	filename = "name_of_file.txt"
	#	Return values as a dictionary.
	#return {"month":month, "year":year, "filename":filename}
	#	Return values as a tuple.
	return month, year, filename








"""
	Create a dictionary (associative memories, or associative arrays) of
		(number, name) months.
"""
#mth_number_name = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
mth_number_name = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july", 8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}

print("	Current month is:",mth_number_name[10])
try:
	print("	Current month is:",mth_number_name[74])
except KeyError:
	print("	Numerical representation for the month is out of bounds.")


# Test function with three return values.
# ~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization
cur_month, cur_year, cur_filename = function_with_3_return_values()
print("cur_month is:",cur_month)
print("cur_year is:",cur_year)
print("cur_filename is:",cur_filename)
something = function_with_3_return_values()
print("something is:",something)
"""
	The following line does not work, since it returns three values
		and there are only two output variables/placeholders (i.e.,
		two variables to store/hold the three output values).
"""
left_holder, right_holder = function_with_3_return_values()
print("left_holder is:",left_holder)
print("right_holder is:",right_holder)

#	Location to store simulation and/or experimental results.
result_repository_relative_path = "~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
result_repository_absolute_path = os.path.expanduser(result_repository_relative_path)
print("result_repository_absolute_path is:",result_repository_absolute_path,"=")



# A dictionary.
a = {'one': 1, 'two': 2, 'three': 3}
print("a is:",a,"=")
a.clear()
print("a is:",a,"=")
b = dict()
print("b is:",b,"=")
if a==b:
	print("a is equal to b.")

Congleton2017_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/Congleton2017.json"
WikipediaContributors2018p_1_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-1.json"
WikipediaContributors2018p_2_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-2.json"
WikipediaContributors2018p_3_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-3.json"
WikipediaContributors2018p_4_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-4.json"

# Parsing JSON files \cite{Congleton2017}.
if file_io_operations.is_path_valid(Congleton2017_json):
	print("=	Start parsing Congleton2017_json.")
# Create a file object to read the file Congleton2017_json.
Congleton2017_json_fo = file_io_operations.open_file_object_read(Congleton2017_json)
# Load the JSON file (object) into a dictionary.
Congleton2017_json_dict = json.load(Congleton2017_json_fo)
print("=	Print the entire Congleton2017_json_dict.")
print(Congleton2017_json_dict)
print("=	For each dictionary in Congleton2017_json_dict, print its name field.")
for dict in Congleton2017_json_dict:
	print(dict['Name'])
print("=	Close the file objects.")
file_io_operations.close_file_object(Congleton2017_json_fo)

print("=	Learning about transforming relative paths.")
print(os.path.expanduser("~/Documents/ricerca"))
print(os.path.expanduser("~/this/is/nonsense"))
print(os.path.expanduser("../../"))
print(os.path.expanduser("statistics/__pycache__/"))
print("	Is this path '../../' a directory?:",os.path.isdir("../../"),"=")
print(os.getcwd())
print("	Is this path 'statistics/__pycache__/' a directory?:",os.path.isdir("statistics/__pycache__/"),"=")
"""
	This shows the following.
	Relative paths begin from the home directory, and is a string
		that starts with "~/".
	Paths based on the current working directory, such as paths
		that begin with "../" or a "[name of subdirectory]", are
		not considered relative paths.
"""

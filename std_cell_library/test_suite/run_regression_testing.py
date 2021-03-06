#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to execute another run of automated
		regression testing, and store the experimental data/results
        from running experiments, simulation results, and/or automated
        software regression testing and hardware regression
		verification.

	Synopsis: command name and [argument(s)]
	./run_regression_testing.py [-h]

	Parameters:
	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is described as follows:
	If the optional "-h" flag is specified,
		display the brief user manual and exit.
	Generate filename of the output file, for storing experimental or
		simulation results.
	Run the experiments and/or simulations.
		Write the experimental and/or simulation results to output file.



	Notes/Assumptions:
	Since I would be categorizing and storing the experimental results
		based on the year and month, the filename containg experimental
		results would be named in the DD-MM-YY-HR-MN-SS-US format so that
		I can quickly find the file of a given build (or experimental
		run) as I read the filename from left to right.

	To implement functions to write output files to a specific directory,
		I would not be using the methods "os.chdir()" and "os.path.join()".
	Instead, I would be specifying a base directory that is appended
		with information from the current date (i.e., year and month).
	This avoids having to implement and test methods that I would
		probably not use often.



	References:
	[DrakeJr2016b]
		datetime module, section 8.1.4 datetime Objects, now() function

	[DrakeJr2016b]
		Section 11 File and Directory Access, subsection 11.2 os.path - Common pathname manipulations;
		see https://docs.python.org/3/library/os.path.html;

	[Hong2016]
		see https://www.bogotobogo.com/python/python_files.php;

	[nosklo2017]

	Revision History:
	August 30, 2018			Version 0.1, initial build.
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
__date__ = 'August 30, 2018'

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
from datetime import date
import datetime
from calendar import month_name

###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
"""
	Module to generate the filename for storing the experimental
		results and simulation output.
"""
from utilities.generate_results_filename import generate_filename

###############################################################
class run_regression_tests:
	@staticmethod
	def check_filename():
		temp_op_filename = generate_filename.create_filename()
		"""
			Implement functions to write output files to a
				specific directory:
		"""


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	generate_filename.check_if_help_wanted()
	print("===================================================")
	print("Run automated regression testing to obtain a set of")
	print("	experimental/simulation results.")
	print("")
	filename = generate_filename.create_filename()
	print("")
	print("	Month #4 is:",month_name[4])
	print("	Month #0 is:",month_name[0],"=end.")
	try:
		print("	Month #100 is:",month_name[100])
	except IndexError:
		print("	Cannot have month indices > 12.")
	try:
		print("	Month #-78 is:",month_name[-78])
	except IndexError:
		print("	Cannot have negative month indices.")
	print("")
	print("	= end =")

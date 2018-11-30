#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to execute another run of automated
		regression testing, and store the experimental data/results
        from running experiments, simulation results, and/or automated
        software regression testing and hardware regression
		verification.
 the program).


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

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

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

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistics.test_statistics_tester import statistical_ons
# Package and module to test date and time operations.
from utilities.date_time_processing_tester import date_time_operations_tester
# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
"""
	Package and module to test the configuration of the software
		application's parameters.
"""
from utilities.configuration_manager_tester import config_manager_tester
"""
	Module to generate the filename for storing the experimental
		results and simulation output.
"""
from utilities.generate_results_filename import generate_filename
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester
"""
	Module to test miscellaneous methods.
"""
from utilities.miscellaneous import misc
from utilities.miscellaneous_tester import misc_tester



###############################################################
class run_regression_tests:
	# ============================================================
	##	Method to determine if the user wants help, and conequently
	#		display the user manual.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def check_if_help_wanted():
		# If user wants to read the brief user manual,
		if "-h" in sys.argv:
			# Display the user manual and exit.
			print("-------------------------------------------------")
			print("==>	This script performs regression testing on my")
			print("	Python scripts to model standard cells.")
			print("")
			print("This script can be executed as follows:")
			print("./run_regression_testing.py [-h]")
			print("")
			print("An optional '-h' flag can be used as any input argument")
			print("	to show the brief user manual and exit.")
			print("")
			print("-------------------------------------------------")



###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	run_regression_tests.check_if_help_wanted()
	print("===================================================")
	print("Run automated regression testinysis package
	statistical_analysis_tester.test_statistical_analysis()
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the utilities package.
	file_io_operations_tester.test_file_io_operations()
	#queue_ip_args_tester.test_queue_ip!	!	!")
	print(">>	Get statistics of the software testing process.")
	statistical_analysis.print_statistics_of_software_testing()

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
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	#os.rename("/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/.git/index.lock","/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/.git/index.lock-spare")
"""
	absolute_path = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	if config_manager.set_result_repository(absolute_path) and misc.add_commit_push_updates_to_git_repository("Update build: Added access to Git repository"):
		print("Update repository of simulation/experimental results.")
	else:
		print("DID NOT update repository of simulation/experimental results.")
	print("	= end =")
"""

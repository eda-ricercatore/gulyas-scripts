#!/usr/local/bin/python3

"""
	This Python script is written by Zhiyang Ong to determine
		if I can use a method to measure the current time, and
		another method to measure the current time at delta time
		later, and use these time measurements to find the
		elapsed time.

	If I cannot do this, I have to select a method, and stick
		with it to determine the elapsed time.


	Synopsis:
	Try to measure the execution time of functions and programs in Python
		using different methods.

	This script can be executed as follows:
	./a_combined_measurement_techniques.py



	Revision History:
	September 6, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

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
	datetime	To obtain information about the current date and time.
	time		To obtain information about the current time.
				time_ns version provides information about the
					current time with nanosecond accuracy.
	warnings	Provide warnings to users without terminating the
					program abruptly.
	process_time (& process_time_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	perf_counter (& perf_counter_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	monotonic (& pm_monotonic_ns)
				To monotonically obtain time stamps, for performance
					measurement, and its alternative providing
					nanosecond accuracy.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
# ImportError: cannot import name 'perf_counter_ns'
from time import perf_counter as pc_timestamp
from time import perf_counter_ns as pc_timestamp_ns
from time import process_time as pt_timestamp
from time import process_time_ns as pt_timestamp_ns
from time import time_ns as t_ns
from time import monotonic as pm_monotonic
from time import monotonic_ns as pm_monotonic_ns


# =======================================================

"""
	Perform timing measurements with different methods and
		determine their elapsed time (or differences).
"""

print("==================================================")

# Time units in seconds (s).
initial_timestamp = pc_timestamp()
# Time units in nanoseconds (ns).
current_timestamp = pc_timestamp_ns()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via perf_counter is:",initial_timestamp,".")
print("current_timestamp via perf_counter_ns is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements in seconds and nanosecond precision would store their values in different time units.")

# Time units in seconds (s).
initial_timestamp = pt_timestamp()
# Time units in nanoseconds (ns).
current_timestamp = pt_timestamp_ns()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via process_time is:",initial_timestamp,".")
print("current_timestamp via process_time_ns is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements in seconds and nanosecond precision would store their values in different time units.")

# Time units in seconds (s).
initial_timestamp = time.time()
# Time units in nanoseconds (ns).
current_timestamp = t_ns()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via time.time() is:",initial_timestamp,".")
print("current_timestamp via time.time_ns() is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements in seconds and nanosecond precision would store their values in different time units.")

# Time units in seconds (s).
initial_timestamp = pm_monotonic()
# Time units in nanoseconds (ns).
current_timestamp = pm_monotonic_ns()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via monotonic is:",initial_timestamp,".")
print("current_timestamp via monotonic_ns is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements in seconds and nanosecond precision would store their values in different time units.")

print("")
print("Conclusion: Cannot combine time measurements in seconds and in nanoseconds.")
print("")

initial_timestamp = pc_timestamp()
current_timestamp = pt_timestamp()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via perf_counter is:",initial_timestamp,".")
print("current_timestamp via process_time is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements using different methods would cause inaccuracies.")
print("	Each method of time measurement has its own baseline.")
print("	Initial non-zero/significant numbers (after adjusting to the same scale, in s or ns) don't match.")


initial_timestamp = pc_timestamp()
current_timestamp = pm_monotonic()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via perf_counter is:",initial_timestamp,".")
print("current_timestamp via monotonic is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Combining time measurements using perf_counter and monotonic may work.")


initial_timestamp = pc_timestamp_ns()
current_timestamp = pm_monotonic_ns()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via perf_counter_ns is:",initial_timestamp,".")
print("current_timestamp via monotonic_ns is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Combining time measurements using perf_counter_ns and monotonic_ns may work.")

initial_timestamp = pt_timestamp()
current_timestamp = pm_monotonic()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via process_time is:",initial_timestamp,".")
print("current_timestamp via monotonic is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements using different methods would cause inaccuracies.")
print("	Each method of time measurement has its own baseline.")
print("	Initial non-zero/significant numbers (after adjusting to the same scale, in s or ns) don't match.")
print("	Major error!!! Elapsed time is negative!")


initial_timestamp = time.time()
current_timestamp = pm_monotonic()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via time.time() is:",initial_timestamp,".")
print("current_timestamp via monotonic is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements using different methods would cause inaccuracies.")
print("	Each method of time measurement has its own baseline.")
print("	Initial non-zero/significant numbers (after adjusting to the same scale, in s or ns) don't match.")
print("	Major error!!! Elapsed time is negative!")


initial_timestamp = time.time()
current_timestamp = pc_timestamp()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via time.time() is:",initial_timestamp,".")
print("current_timestamp via perf_counter is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements using different methods would cause inaccuracies.")
print("	Each method of time measurement has its own baseline.")
print("	Initial non-zero/significant numbers (after adjusting to the same scale, in s or ns) don't match.")
print("	Major error!!! Elapsed time is negative!")


initial_timestamp = time.time()
current_timestamp = pt_timestamp()
elapsed_time = current_timestamp - initial_timestamp
print("initial_timestamp via time.time() is:",initial_timestamp,".")
print("current_timestamp via process_time is:",current_timestamp,".")
print("elapsed_time is:",elapsed_time,".")
print("	Error! Combining time measurements using different methods would cause inaccuracies.")
print("	Each method of time measurement has its own baseline.")
print("	Initial non-zero/significant numbers (after adjusting to the same scale, in s or ns) don't match.")
print("	Major error!!! Elapsed time is negative!")

print("")
print("--------------------------------------------------")
print("Final conclusion:")
print("'Acceptable' combination: perf_counter and monotonic.")
print("'Acceptable' combination: perf_counter_ns and monotonic_ns.")
print("Other combinations do not work.")

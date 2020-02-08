#	This Makefile is written by Zhiyang Ong for build automation
#		of Python scripts to test modules in the "timing_measurements"
#		package that:
#	+ calculate the factorial of a number.
#	+ measure the current time.


#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.









# Makefile for "timing_measurements" Python package for current
#	timing measurements.
# @author Zhiyang Ong

# =============================================================

# Definition of macro flags...
# IMPORTANT NOTE:








# Basic software architecture description at the module level.
# Paths for different modules/packages of the software.
#
# Note that the paths of the modules are relative.
# The modules are located in the "src" directory.
# This is because I am building and testing the software in a
#	separate directory, so that I can isolate the object files
#	and the executable from the source code.
# Such isolation would make it easier to clean up the directory where
#	the software resides, so that it is easier to maintain.
#
# Module that calculates the factorial of a given number.
FACTORIAL=		./utilities/timing_measurements/get_factorial.py
# Module for measuring the current time without nanosecond accuracy.
MEASUREMENT=	./utilities/timing_measurements/performance_measurement_no_ns.py
# Module for measuring the current time with nanosecond accuracy.
NANOSECOND=		./utilities/timing_measurements/performance_measurement.py



# UNIX commands/utilities that are used
TIME=			time #-p
DATE=			date






# =============================================================

# Definition of Target Rules
# Use a FOR loop to sweep through the list of benchmarks when
#	the parse is ready, and do regression testing when the router
#	is done.

########################################################################
# TEST FACTORIAL METHOD
########################################################################
# Test Python code to get factorial of non-negative integers.
fac:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	@echo === Test Python code to get factorial of non-negative integers.
	$(TIME) $(FACTORIAL)
	@echo
	@echo
	@echo
	@echo "The code is rather buggy; use is at own risk."
	@echo "-- Donald Chai"
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo







########################################################################
# TEST CURRENT TIME MEASUREMENT: No nanosecond accuracy
########################################################################
# Test Python code to measure the current time. No nanosecond accuracy.
measure:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	@echo === Test Python code to measure the current time, us.
	$(TIME) $(MEASUREMENT)
	@echo
	@echo
	@echo
	@echo "The code is rather buggy; use is at own risk."
	@echo "-- Donald Chai"
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo





########################################################################
# TEST CURRENT TIME MEASUREMENT: Nanosecond accuracy.
########################################################################
# Test Python code to measure the current time. Nanosecond accuracy.
nano:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	@echo === Test Python code to measure the current time, ns.
	$(TIME) $(NANOSECOND)
	@echo
	@echo
	@echo
	@echo "The code is rather buggy; use is at own risk."
	@echo "-- Donald Chai"
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo

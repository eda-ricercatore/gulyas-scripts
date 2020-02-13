#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test how
		to squelch standard output and standard error output.


	Synopsis:
	Test techniques to squelch standard output and standard
		error output.

	This script can be executed as follows:
	./squelching_std_op_and_std_err_op.py




	Revision History:
	September 6, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2018'

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
	time	To obtain information about the current time.
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
import time

from sys import stdin, stdout, stderr
from contextlib import contextmanager
import contextlib




temp_std_op = sys.stdout
temp_std_err = sys.stderr


print("= Test squelching approach 1.")
print("	Approach 1: Printing to standard output: OK.")
stderr.write("	Approach 1: Printing to standard error output: OK.\n")
# Squelch the standard output and standard error output.
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
print("	Approach 1: Try printing to standard output.")
stderr.write("	Approach 1: Try printing to standard error output: Fail!!!\n")
# Running commands from the command line still produces output.
os.system("ls -la")
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
"""
print("Printing to standard output: Fail!!!")
stderr.write("Printing to standard error output: Fail!!!\n")
sys.stdout = temp_std_op
sys.stderr = temp_std_err
"""
print("	Approach 1: Printing to standard output: OK again.")
stderr.write("	Approach 1: Printing to standard error output: OK again.\n")




print("")
print("")
print("= Test squelching approach 2.")
@contextmanager
def silence_stdout():
	sys.stdout = open(os.devnull, "w")
	try:
		yield sys.stdout
	finally:
		sys.stdout = temp_std_op

with silence_stdout():
	print("	Approach 2: Try printing to standard output.")
	os.system("ls -la")
	stderr.write("	Approach 2: Try printing to standard error output: Fail!!!\n")

print("	Approach 2: Printing to standard output: OK again.")
stderr.write("	Approach 2: Printing to standard error output: OK again.\n")






print("")
print("")
print("= Test squelching approach 3.")
with contextlib.redirect_stdout(None):
	print("	Approach 3: Try printing to standard output.")
	os.system("ls -la")
	stderr.write("	Approach 3: Try printing to standard error output: Fail!!!\n")
print("	Approach 3: Printing to standard output: OK again.")
stderr.write("	Approach 3: Printing to standard error output: OK again.\n")


"""
print("")
print("")
print("= Test squelching approach 4.")
print("	Approach 4: Printing to standard output: OK.")
stderr.write("	Approach 4: Printing to standard error output: OK.\n")
sys.stdout.close()
sys.stderr.close()
print("	Approach 4: Try printing to standard output.")
os.system("ls -la")
stderr.write("	Approach 4: Try printing to standard error output.\n")
sys.stdout = temp_std_op
sys.stderr = temp_std_err
print("	Approach 4: Printing to standard output: Still Failed!!!")
stderr.write("	Approach 4: Printing to standard error output: Still Failed!!!\n")
sys.stdout.open()
sys.stderr.open()
sys.stdout = temp_std_op
sys.stderr = temp_std_err
print("	Approach 4: Printing to standard output: OK again.")
stderr.write("	Approach 4: Printing to standard error output: OK again.\n")
# Standard output and standard error output streams cannot be restored.
"""






"""
print("")
print("")
print("= Test squelching approach 5.")
print("	Approach 5: Printing to standard output: OK.")
stderr.write("	Approach 5: Printing to standard error output: OK.\n")
os.close(0)		# close C's stdin stream
os.close(1)		# close C's stdout stream
os.close(2)		# close C's stderr stream
print("	Approach 4: Try printing to standard output.")
os.system("ls -la")
stderr.write("	Approach 4: Try printing to standard error output.\n")
os.open(0)		# close C's stdin stream
os.open(1)		# close C's stdout stream
os.open(2)		# close C's stderr stream
print("	Approach 4: Printing to standard output: OK again.")
stderr.write("	Approach 4: Printing to standard error output: OK again.\n")
# Standard output and standard error output streams cannot be restored.
"""

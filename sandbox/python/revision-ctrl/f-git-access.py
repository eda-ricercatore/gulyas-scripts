#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This is written by Zhiyang Ong to test how to add, commit,
		and push additions and updates.

	Synopsis: command name
	./f-git-access.py


	References:
	...



	Revision History:
	October 7, 2018			Version 0.1, initial build.
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
__date__ = 'October 7, 2018'

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
	calendar	For performing operations on dates.
	logging		For debug, info, warning, error, and critical messages.
				+ logging.debug("")
				+ logging.info("")
				+ logging.warning("")
				+ logging.error("")
				+ logging.critical("")
	git			For accessing Git repositories.
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
import calendar
import logging
from sys import stdin, stdout, stderr
#import git
import subprocess



##############################################################
#import sh

#git = repo.git

#repo = git.Repo("/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization")

print("=	Solution 1: Via Python's subprocess module.")
repo_dir = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"

cmd = ['git', 'add', "-A"]
p = subprocess.Popen(cmd, cwd=repo_dir)

comment = "Update build via Python."
cmd = ["git", "commit", "-m", comment]
p = subprocess.Popen(cmd, cwd=repo_dir)
p.wait()

cmd = ["git", "push"]
p = subprocess.Popen(cmd, cwd=repo_dir)
p.wait()

print("-------------------------------------------------------")
print("=	Solution 2: Via Python module Gittle.")

#git = sh.git.bake(_cwd=repo_dir)

print("=End=")

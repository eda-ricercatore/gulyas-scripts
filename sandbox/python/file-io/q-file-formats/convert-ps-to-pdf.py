#!/usr/bin/python

"""
	This is written by Zhiyang Ong to convert all PostScript files to PDF format.
 
	Synopsis:
	Script to convert all PostScript files in a given directory to PDF format.
	

 Revision History:
 1) November 11, 2014. Initial working version.
 2)	March 14, 2017. Updated comments for the script.
 
 
 
 	The MIT License (MIT)
 
 	Copyright (c) <2014> <Zhiyang Ong>
 
 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""


#	Import packages and functions from the Python Standard Library.
from os import listdir, system
from os.path import isfile, join, splitext
#from os.subprocess import call
import subprocess

#	============================================================

# Absolute/relative path of directory which files are to be processed.
mypath = "/Users/zhiyang/Downloads"

# Create a collection of filenames of each file in this directory.
"""
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	print onlyfiles
"""

#	============================================================

# For each file
for f in listdir(mypath):
	# Determine if currently enumerated file is a valid file.
	if isfile(join(mypath,f)):
		# Is this file a PostScript file?
		print "Filename is:::",f
		filename_wo_extn, file_extn = splitext(f)
		print "	filename_wo_extn:::", filename_wo_extn
		print "	file_extn:::", file_extn
		if file_extn == ".ps":
			print "		This is a Postcript file"
			#system('ls -al %fe' %(f))
			#system("ps2pdf f")
			#subprocess.call(['ls', '-al', f])
			# Convert the PostScript file to a PDF file.
			subprocess.call(['ps2pdf', f])

#	============================================================
print "==	End of program."


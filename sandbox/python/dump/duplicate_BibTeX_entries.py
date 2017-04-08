#!/usr/bin/python 
###	#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit


"""
	This Python script is written by Zhiyang Ong to determine if
		duplicate BibTeX entries exist in my BibTeX database.
	If such entries exist, produce a copy of the BibTeX database as
		an output file without the duplicate BibTeX entries. 

	Synopsis:
	Remove duplicate BibTeX entries in my BibTeX database.

	This script can be executed as follows:
	./duplicate-BibTeX-entries.py [input BibTeX file] [output BibTeX file]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have duplicate
								BibTeX entries.
	[output BibTeX file]:	A BibTeX file without duplicate BibTeX
								entries.

	The 2nd input argument mustn't be a valid path to an existing file.
	If it is, warn the user about overwritting the file & exit.
	
	Since this program can be executed on different operating systems
		(OSes) including UNIX-like operating systems and Microsoft
		Windows, the file extension of the output BibTeX file need
		not be checked.
	Since all files (regardless of the file extension) are regular
		files in any UNIX-like OS, this relaxed constraint is used.
	However, this would cause problems in Microsoft Windows, since it
		may not have a file extension and Microsoft Windows does not
		know which application can be used to open the file.
	Hence, if the second input argument (a string) has no file
		extension, a BibTeX file extension ".bib" would be added to
		the output filename to address such circumstances.






	Revision History:
	2014				Version 0.1
	March 14, 2017		Version 0.2 Testing the first argument.
	March 22, 2017		Version 0.3 Working on second argument.

"""

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

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
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re



#	Import modules from Zhiyang Ong's Python library.




###############################################################
#	Module with methods that clean BibTeX files.
class Duplicate_BibTeX_entries:
	# List of BibTeX keys
	set_of_BibTeX_keys = []
	# Set of BibTeX entry types
	BibTeX_entry_types = ["article", "book", "booklet", "inbook", "incollection", "inproceedings", "manual", "mastersthesis", "misc", "phdthesis", "proceedings", "techreport", "unpublished"]
	# ============================================================
	#	Method to provide information on how to run this script.
	#	O(1) method.
	@staticmethod
	def how_to_use_script():
		print "-------------------------------------------------"
		print "==>	This script determines if duplicate BibTeX entries"
		print "	exist in my BibTeX database."
		print "	If they do, remove the duplicate BibTeX entries."
		print ""
		print "This script can be executed as follows:"
		print "./duplicate-BibTeX-entries.py [input BibTeX file] [output BibTeX file]"
		print ""
		print "2nd input argument mustn't be a valid path to an existing file."
		print "If it is, warn the user about overwritting the file & exit."
		print ""
		print "If 2nd input argument has no file extension, add the"
		print "	BibTeX file extension to it."
		print ""
		print "-------------------------------------------------"
		# Inform the user what went wrong.
		raise Exception("Error with input arguments.")
	# ============================================================
	#	Method to add BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n) method, where n is the number of BibTeX keys.
	@staticmethod
	def add_BibTeX_key(found_BibTeX_key):
		if (found_BibTeX_key in Duplicate_BibTeX_entries.set_of_BibTeX_keys):
			temp_str = "Duplicate BibTeX key:"+found_BibTeX_key
			warnings.warn(temp_str)
		Duplicate_BibTeX_entries.set_of_BibTeX_keys.append(found_BibTeX_key)
	# ============================================================
	#	Method to sort BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n*log(n)) method, where n is the number of BibTeX keys.
	@staticmethod
	def sort_BibTeX_keys():
		Duplicate_BibTeX_entries.set_of_BibTeX_keys = sorted(Duplicate_BibTeX_entries.set_of_BibTeX_keys)
	# ============================================================
	#	Method to read each line of the input BibTeX file.
	#	O(n) method, where n is the number of lines of the BibTeX file.
	@staticmethod
	def read_input_BibTeX_file(input_BibTeX_file):
		print "--------------------------------------------------------"
		print "=	Reading input BibTeX file:"+input_BibTeX_file
		# Create a file object for input BibTeX file, in reading mode.
		ip_file_obj = open(input_BibTeX_file, 'r')
		# Read each available line in the input BibTeX file.
		for line in ip_file_obj:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
				print "...	First line of a BibTeX entry."
				tokenized_BibTeX_entry = re.split('@|{|,',line)
				# Is the type of the BibTeX entry valid?
				if (tokenized_BibTeX_entry[1] in Duplicate_BibTeX_entries.BibTeX_entry_types):
					# Yes. Try adding the BibTeX entry to "set_of_BibTeX_keys".
					Duplicate_BibTeX_entries.add_BibTeX_key(tokenized_BibTeX_entry[2])
				else:
					# No. Warn user that the BibTeX entry has an invalid type!
					temp_str = "Invalid type of BibTeX entry:"+tokenized_BibTeX_entry[1]
					warnings.warn(temp_str)
#	
		#	Destroy the file object for the input BibTeX file.
		ip_file_obj.close()
















###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	start_time = time.time()
	# --------------------------------------------------------
	#	= Start of Preprocessing.
	#	Set filtering mechanism to always provide warnings.
	warnings.filterwarnings('always')
	#	Check if set of BibTeX entry types is complete.
	#	The cardinality of standard BibTeX entry types is 13.
	if 13 != len(Duplicate_BibTeX_entries.BibTeX_entry_types):
		raise Exception("Set of BibTeX entry types has incorrect size.")
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print "==================================================="
	print "Finding duplicate BibTeX entries in my BibTeX database."
	print "	And, removing the duplicate BibTeX entries."
	
	
	#	Is the number of input arguments to the script <2? 
	if len(sys.argv) < 3:
		Duplicate_BibTeX_entries.how_to_use_script()
	
	first_input_argument = sys.argv[1]
	print "==	Is the 1st input argument a valid path to a file?"
	if (os.path.exists(first_input_argument) and os.path.isfile(first_input_argument)):
		print "	Yes."
	else:
		raise Exception("1st input argument isn't a valid path to a file!")
	#	Does 1st input argument have a BibTeX file extension?
	print "==	Does 1st input argument have a BibTeX file extension?"
	#	Get the filename and file extension of the 1st input argument.
	ip_fname1, ip_f_ext1 = os.path.splitext(first_input_argument)
#	print "==	File name of 1st input argument:"+ip_fname
#	print "==	File extension of 1st input argument:"+ip_f_ext
	#	BibTeX file extension
	bibtex_f_ext = ".bib"
	if(ip_f_ext1 == bibtex_f_ext):
		print "	Yes."
	else:
		raise Exception("1st input argument isn't a valid BibTeX file!")

	second_input_argument = sys.argv[2]
	"""
	The 2nd input argument needn't be a valid path to an existing file.
	If it is, warn the user about overwritting the file & exit.
	"""
	print "==	Is the 2nd input argument a valid path to a file?"
	if (os.path.exists(second_input_argument) and os.path.isfile(second_input_argument)):
		print "	2nd input argument is a valid path to a file!"
		print "	File would be overwritten:"+second_input_argument
		raise Exception("End program to avoid overwritting file.")
	else:
		print "	Yes."
	#	Get the filename and file extension of the 2nd input argument.
	ip_fname2, ip_f_ext2 = os.path.splitext(second_input_argument)
	#	Does 2nd input argument have a BibTeX file extension?
	print "==	Does 2nd input argument have a BibTeX file extension?"
	if(ip_f_ext2 == bibtex_f_ext):
		print "	Yes."
	else:
		print "	No."
		#	Add BibTeX file extension to output filename.
		ip_fname2 = ip_fname2 + bibtex_f_ext
		print "	New output filename is:"+ip_fname2
	#	=======================================================
	#	Add items to the list.
	"""
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("parma2016")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia1982")
	Duplicate_BibTeX_entries.add_BibTeX_key("pisa1721")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste1233")
	Duplicate_BibTeX_entries.add_BibTeX_key("bari2011")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia1823")
	Duplicate_BibTeX_entries.add_BibTeX_key("aprilia1816")
	Duplicate_BibTeX_entries.add_BibTeX_key("firenze1861")
	Duplicate_BibTeX_entries.add_BibTeX_key("laquila1171")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("milan2007")
	Duplicate_BibTeX_entries.add_BibTeX_key("modena1219")
	Duplicate_BibTeX_entries.add_BibTeX_key("bologna1999")
	Duplicate_BibTeX_entries.add_BibTeX_key("carpi1981")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("genoa1982")
	Duplicate_BibTeX_entries.add_BibTeX_key("catania1811")
	Duplicate_BibTeX_entries.add_BibTeX_key("como2003")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia1951")
	Duplicate_BibTeX_entries.add_BibTeX_key("ferrara1991")
	Duplicate_BibTeX_entries.add_BibTeX_key("firenze1991")
	Duplicate_BibTeX_entries.add_BibTeX_key("genoa2010")
	Duplicate_BibTeX_entries.add_BibTeX_key("lecce1993")
	Duplicate_BibTeX_entries.add_BibTeX_key("firenze1861")
	Duplicate_BibTeX_entries.add_BibTeX_key("verona1997")
	Duplicate_BibTeX_entries.add_BibTeX_key("napoli1347")
	Duplicate_BibTeX_entries.add_BibTeX_key("siena1887")
	Duplicate_BibTeX_entries.add_BibTeX_key("firenze1761")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia1726")
	Duplicate_BibTeX_entries.add_BibTeX_key("genoa1271")
	Duplicate_BibTeX_entries.add_BibTeX_key("torino191")
	Duplicate_BibTeX_entries.add_BibTeX_key("trento1542")
	Duplicate_BibTeX_entries.add_BibTeX_key("roma1865")
	Duplicate_BibTeX_entries.add_BibTeX_key("firenze1861")
	Duplicate_BibTeX_entries.add_BibTeX_key("salerno1521")
	Duplicate_BibTeX_entries.add_BibTeX_key("trieste2017")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia2012")
	Duplicate_BibTeX_entries.add_BibTeX_key("venezia1789")
	Duplicate_BibTeX_entries.add_BibTeX_key("padova1214")
	Duplicate_BibTeX_entries.add_BibTeX_key("pavia1951")
	Duplicate_BibTeX_entries.add_BibTeX_key("palermo1816")
	#	Print each item in the list.
	for bk in Duplicate_BibTeX_entries.set_of_BibTeX_keys:
		print(bk)
	print "-------------------------------------------------"
	#	Sort the items in the list.
	Duplicate_BibTeX_entries.sort_BibTeX_keys()
	#	Print each item in the list.
	for bk in Duplicate_BibTeX_entries.set_of_BibTeX_keys:
		print(bk)
	#	Tokenize the first line of each BibTeX entry.
	a_BibTeX_entry = "@article{como2003,"
	if "@" == a_BibTeX_entry[0]:
		print "...	First line of a BibTeX entry."
	tokenized_BibTeX_entry = re.split('@|{|,',a_BibTeX_entry)
	print tokenized_BibTeX_entry
	print tokenized_BibTeX_entry[1]
	print tokenized_BibTeX_entry[2]
	"""
	Duplicate_BibTeX_entries.read_input_BibTeX_file(first_input_argument)
	print "	: Sort the items in the list."
	Duplicate_BibTeX_entries.sort_BibTeX_keys()
	print "	: Print each item in the list."
	for bk in Duplicate_BibTeX_entries.set_of_BibTeX_keys:
		print(bk)
	#	BLAH.
	print "==================================================="
	print "==	End of program."
	end_time = time.time()
	elapsed_time = end_time - start_time
	print "==	Elapsed time:"+str(elapsed_time)+" seconds."
	
	

#	Duplicate_BibTeX_entries.how_to_use_script()
	

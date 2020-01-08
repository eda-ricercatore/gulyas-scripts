#!/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


"""
	This Python script is written by Zhiyang Ong to process input
		arguments for a script to clean BibTeX databases/files.
	
	
	Synopsis:
	Process input arguments for a script to clean BibTeX databases.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Apr 14, 2017'

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
"""

import sys
#import os
import os.path
#from subprocess import call
#import time
import warnings
#import re

###############################################################
#	Import Custom Python Modules


###############################################################
#	Module with methods that clean BibTeX files.
class queue_ip_args:
	#	List of input arguments
	set_of_input_arguments = []
	#	First input argument
	first_input_argument = "First input argument."
	#	Second input argument
	second_input_argument = "Second input argument."
	#	BibTeX file extension
	bibtex_f_ext = ".bib"
	# Set of BibTeX entry types.
	BibTeX_entry_types = ["article", "book", "booklet", "inbook", "incollection", "inproceedings", "manual", "mastersthesis", "misc", "phdthesis", "proceedings", "techreport", "unpublished"]
	# Set of BibTeX entry types, with metadata.
	BibTeX_entry_types = ["@article{", "@book{", "@booklet{", "@inbook{", "@incollection{", "@inproceedings{", "@manual{", "@mastersthesis{", "@misc{", "@phdthesis{", "@proceedings{", "@techreport{", "@unpublished{"]
	# Set of BibTeX fields.
	set_of_BibTeX_fields = ["	Address = {", "	Annote = {", "	Author = {", "	Booktitle = {", "	Chapter = {", "	Crossref = {", "	Doi = {", "	Edition = {", "	Editor = {", "	Howpublished = {", "	Institution = {", "	Journal = {", "	Month = {", "	Note = {", "	Number = {", "	Organization = {", "	Pages = {", "	Publisher = {", "	School = {", "	Series = {", "	Title = {", "	Type = {", "	Url = {", "	Volume = {", "	Year = {"]
	# Index for the script that is currently executed.
	CURRENT_SCRIPT = "No script is currently being executed." 
	# "Constant"s for navigating types of help in the "user manual".
	DUPLICATE_ENTRIES = "duplicate_BibTeX_entries.py"
	EXTRACT_BIBTEX_KEYS = "extract_citations.py"
	UNDEFINED_REFERENCES = "not_defined_references.py"
	REMOVE_METADATA = "rm_bibtex_metadata.py"
	STANDARDIZE_BIBTEX = "standardize_bibtex_entries.py"
	UNCOMMENT_LATEX = "uncomment_latex_src_files.py"
	VALIDATE_URL_DOI = "validate_url.py"
	# ============================================================
	#	Accessor methods.
	# ============================================================
	#	Method to get the input arguments.
	#	@return - List of input arguments to the program.
	#	O(1) method.
	@staticmethod
	def get_input_arguments():
		"""
		print "=	Set_of_input_arguments:"
		for cur_ip_arg in queue_ip_args.set_of_input_arguments:
			print "	"+cur_ip_arg
		"""
		return queue_ip_args.set_of_input_arguments
	# ============================================================
	#	Method to print all the input arguments.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def print_all_input_arguments():
		print "=	Set_of_input_arguments:"
		for cur_ip_arg in queue_ip_args.set_of_input_arguments:
			print "	"+cur_ip_arg
	# ============================================================
	#	Method to get the first input argument.
	#	@return - First input argument for the program.
	#	O(1) method.
	@staticmethod
	def get_1st_input_argument():
		if 0 < len(queue_ip_args.get_input_arguments()):
			return queue_ip_args.set_of_input_arguments[0]
		else:
			warnings.warn("	1st input argument is missing!!!")
			queue_ip_args.input_arguments_error()
	# ============================================================
	#	Method to get the second input argument.
	#	@return - Second input argument for the program.
	#	O(1) method.
	@staticmethod
	def get_2nd_input_argument():
		if 1 < len(queue_ip_args.get_input_arguments()):
			return queue_ip_args.set_of_input_arguments[1]
		else:
			warnings.warn("	2nd input argument is missing!!!")
			queue_ip_args.input_arguments_error()
	# ============================================================
	#	Mutator methods.
	# ============================================================
	#	Method to set the input arguments.
	#		And, remove the name of the script from the list of input
	#		arguments, for easier processing.
	#	@param list_of_ip_arguments - A list of input arguments to
	#		the program.
	#	@param which_script - Which script is currently being executed.
	#	O(1) method.
	@staticmethod
	def set_input_arguments(list_of_ip_arguments,which_script):
		queue_ip_args.set_of_input_arguments = list_of_ip_arguments
		# Remove the name of the script from the list of input arguments. 
		queue_ip_args.set_of_input_arguments.pop(0)
		queue_ip_args.CURRENT_SCRIPT = which_script
	# ============================================================
	#	Other methods.
	# ============================================================
	#	Method to determine if the user wants help, and conequently
	#		display the user manual.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def check_if_help_wanted():
		# If user wants to read the brief user manual,  
		if "-h" in queue_ip_args.set_of_input_arguments:
			# Display the user manual and exit.
			queue_ip_args.how_to_use_script()
			sys.exit()
	# ============================================================
	#	Method to provide information on how to run this script.
	#	O(1) method.
	@staticmethod
	def how_to_use_script():
		print "-------------------------------------------------"
		if(queue_ip_args.DUPLICATE_ENTRIES == queue_ip_args.CURRENT_SCRIPT):
			print "==>	This script determines if duplicate BibTeX entries"
			print "	exist in my BibTeX database."
			print "	If they do, let the user know about them."
			print ""
			print "This script can be executed as follows:"
			print "./duplicate_BibTeX_entries.py [input BibTeX file] [-h]"
			print ""
		elif(queue_ip_args.EXTRACT_BIBTEX_KEYS == queue_ip_args.CURRENT_SCRIPT):
			print "=	Get user manual of:"+queue_ip_args.EXTRACT_BIBTEX_KEYS
		elif(queue_ip_args.UNDEFINED_REFERENCES == queue_ip_args.CURRENT_SCRIPT):
			print "=	Get user manual of:"+queue_ip_args.UNDEFINED_REFERENCES
		elif(queue_ip_args.REMOVE_METADATA == queue_ip_args.CURRENT_SCRIPT):
#			print "=	Get user manual of:"+queue_ip_args.REMOVE_METADATA
			print "==>	'Remove' BibTeX metadata from the input BibTeX database,"
			print "	by copying data from the input BibTeX database to"
			print "	the output BibTeX database without copying the"
			print "	metedata."
			print ""
			print "This script can be executed as follows:"
			print "./rm_bibtex_metadata.py [input BibTeX file] [output BibTeX file] [-h]"
			print ""
			queue_ip_args.print_2nd_argument()
		elif(queue_ip_args.STANDARDIZE_BIBTEX == queue_ip_args.CURRENT_SCRIPT):
			print "=	Get user manual of:"+queue_ip_args.STANDARDIZE_BIBTEX
		elif(queue_ip_args.UNCOMMENT_LATEX == queue_ip_args.CURRENT_SCRIPT):
			print "=	Get user manual of:"+queue_ip_args.UNCOMMENT_LATEX
		elif(queue_ip_args.VALIDATE_URL_DOI == queue_ip_args.CURRENT_SCRIPT):
			print "==>	Determine if URL (and DOI) field(s) is(/are)"
			print "	missing from the BibTeX database."
			print "	If they are missing, copy their values from the"
			print "	backup URL field."
			print ""
			print "This script can be executed as follows:"
			print "./validate_url.py [input BibTeX file] [output BibTeX file] [-h]"
			print ""
			queue_ip_args.print_2nd_argument()
		else:
			raise Exception("Error in accessing user manual.")
		queue_ip_args.print_help_option()
		print "-------------------------------------------------"
	# ============================================================
	#	Method to provide information on the second input argument.
	#	O(1) method.
	@staticmethod
	def print_2nd_argument():
		print "The 2nd (and subsequent) input argument(s) is(/are) optional."
		print ""
		print "The 2nd input argument mustn't be a valid path to an existing file."
		print "If it is, warn the user about overwritting the file & exit."
		print ""
		print "If 2nd input argument has no file extension, add the"
		print "BibTeX file extension to it."
		print ""
	# ============================================================
	#	Method to print the help option to access the user manual.
	#	O(1) method.
	@staticmethod
	def print_help_option():
		print "An optional '-h' flag can be used as any input argument"
		print "	to show the brief user manual and exit."
		print ""
	# ============================================================
	#	Method to indicate error wth input arguments.
	#	O(1) method.
	@staticmethod
	def input_arguments_error():
		queue_ip_args.how_to_use_script()
		# Inform the user what went wrong.
		raise Exception("Error with input arguments.")
	# ============================================================
	#	Method to process the first input argument.
	#	O(1) method.
	@staticmethod
	def process_1st_ip_arg():
		#	Is the number of input arguments to the script <1? 
		if 1 > len(queue_ip_args.get_input_arguments()):
			warnings.warn("	There are no input arguments!!!")
			queue_ip_args.input_arguments_error()
		queue_ip_args.first_input_argument = queue_ip_args.get_1st_input_argument()
		print "==	Is the 1st input argument a valid path to a file?"
		if (os.path.exists(queue_ip_args.first_input_argument) and os.path.isfile(queue_ip_args.first_input_argument)):
			print "	Yes."
		else:
			raise Exception("1st input argument isn't a valid path to a file!")
		#	Does 1st input argument have a BibTeX file extension?
		print "==	Does 1st input argument have a BibTeX file extension?"
		#	Get the filename and file extension of the 1st input argument.
		ip_fname1, ip_f_ext1 = os.path.splitext(queue_ip_args.first_input_argument)
#	print "==	File name of 1st input argument:"+ip_fname
#	print "==	File extension of 1st input argument:"+ip_f_ext
		if(ip_f_ext1 == queue_ip_args.bibtex_f_ext):
			print "	Yes."
		else:
			raise Exception("1st input argument isn't a valid BibTeX file!")
		return queue_ip_args.first_input_argument
	# ============================================================
	#	Method to process the second input argument.
	#	@return the output filename, based on the second input argument
	#	O(1) method.
	@staticmethod
	def process_2nd_ip_arg():
		#	Is the number of input arguments to the script <2? 
		if 2 > len(queue_ip_args.get_input_arguments()):
			warnings.warn("	2nd input argument isn't available!!!")
			queue_ip_args.input_arguments_error()
		queue_ip_args.second_input_argument = queue_ip_args.get_2nd_input_argument()
		"""
		The 2nd input argument shouldn't be a valid path to an existing file.
		If it is, warn the user about overwritting the file & exit.
		"""
		print "==	Is the 2nd input argument a valid path to a file?"
		if (os.path.exists(queue_ip_args.second_input_argument) and os.path.isfile(queue_ip_args.second_input_argument)):
			print "	2nd input argument is a valid path to a file!"
			print "	File would be overwritten:"+queue_ip_args.second_input_argument
			raise Exception("End program to avoid overwritting file.")
		else:
			print "	Yes."
		#	Get the filename and file extension of the 2nd input argument.
		ip_fname2, ip_f_ext2 = os.path.splitext(queue_ip_args.second_input_argument)
		#	Does 2nd input argument have a BibTeX file extension?
		print "==	Does 2nd input argument have a BibTeX file extension?"
		if(ip_f_ext2 == queue_ip_args.bibtex_f_ext):
			print "	Yes."
			ip_fname2 = queue_ip_args.second_input_argument
		else:
			print "	No."
			#	Add BibTeX file extension to output filename.
			ip_fname2 = queue_ip_args.second_input_argument + queue_ip_args.bibtex_f_ext
			print "	New output filename is:"+ip_fname2
		return ip_fname2
	# ============================================================
	#	Method to handle missing second input argument.
	#	Append the input filename (1st input argument), without the
	#		file extension, with "_op.bib", and set the result as the
	#		second input argument.
	#	O(1) method.
	@staticmethod
	def missing_2nd_ip_arg():
		#	Is the number of input arguments to the script <2? 
		if 2 > len(queue_ip_args.get_input_arguments()):
			#	Get the filename and file extension of the 1st input argument.
			ip_fname1, ip_f_ext1 = os.path.splitext(queue_ip_args.first_input_argument)
			#	Set the result as the 2nd input argument.
			queue_ip_args.set_of_input_arguments.append(ip_fname1+"_op.bib")
	# ============================================================
	#	Method to validate the number of the types of BibTeX entries.
	#	O(1) method.
	@staticmethod
	def preprocessing():
		#	Set filtering mechanism to always provide warnings.
		warnings.filterwarnings('always')
		#	Check if set of BibTeX entry types is complete.
		#	The cardinality of standard BibTeX entry types is 13.
		if 13 != len(queue_ip_args.BibTeX_entry_types):
			raise Exception("Set of BibTeX entry types has incorrect size.")

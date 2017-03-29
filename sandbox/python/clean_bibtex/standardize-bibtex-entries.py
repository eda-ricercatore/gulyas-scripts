#!/usr/bin/python

"""
	This is written by Zhiyang Ong to extract the cited BibTeX
	entries from my BibTeX database.
	
	That is, it will create a "working" BibTeX reference list based
	on citations from my BibTeX database.
	
	
	
	
	Synopsis: command name and [argument(s)]
	./clean_bibtex.py
	This script will find all citations from my BibTeX database by
	searching for the string "\cite{[BibTeX key]}", and variants of
	it.
	For each unique citation, it will store them in a set, and use
	it to search for the corresponding BibTeX entry in my BibTeX
	database, copy that into a output file (another BibTeX file).
	The resultant output file is another BibTeX file that contains
	BibTeX entries for all cited references from my BibTeX database.
	This output file will also not contain any metadata that is
	application-specific, with regards to reference management
	software (such as Mendeley).
	
	e.g., ./clean_bibtex.py
	This finds all BibTeX entries in my BibTeX database that are
	cited in working documents and in the source code of my
	project(s).
	
	
	
	
	
	
	Its procedure is given as follows:
	Recursively search through the working directory and (sub)^n
	-directories for citations.
	
	Store all citations in a collection/set (e.g., list, array,
	stack, or otherwise).
	
	For each element in the set, copy its BibTeX entry into my
	working BibTeX reference list.
"""

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.1'
__date__ = 'Nov 19, 2013'

"""
	Import the necessary modules from the Python library
	getopt - C-style parser for command line options
	random - Generate pseudo-random numbers
	re - Regular expression operations
	math - Mathematical functions
	os - Miscellaneous operating system interfaces
	sys - System-specific parameters and functions
"""
import getopt, math, os, random, re, sys

#	==========================================================

# Global variables that I would use throughout the program.
CURRENT_WORKING_DIR = "."
# Prefix indicator for hidden files in UNIX-like systems.
HIDDEN_FILE = "."
RANDOM = "RANDOM"

#	==========================================================

#	if os.access("myfile", os.R_OK):
#		with open("myfile") as fp:
#			return fp.read()
#	return "some default data"

#	is better written as:

#	try:
#		fp = open("myfile")#	except IOError as e:
#		if e.errno == errno.EACCES:
#			return "some default data"
#		# Not a permission error.
#		raise
#	else:
#		with fp:
#			return fp.read()


"""
	Function to recursively search through the working directory
	and (sub)^n -directories for citations.
	
	For each citation, store it in a collection/set (e.g., list,
	array, stack, or otherwise).
	
	Input: list_citations is the set of references cited in the
		project. They are indicated by the\cite{key} LaTeX command.

	Output: Return list_citations, the set of collected citations.
"""
def collect_citations(list_citations):
	if list_citations is None:
		list_citations = []
		list_citations.append(RANDOM)
		print ">>	Initial list is empty."
	# List all the entries in the current working directory.
	#print os.listdir(CURRENT_WORKING_DIR)

	# Enumerate all the entries in the current working directory.
	for file_i in os.listdir(CURRENT_WORKING_DIR):
		# Process files that are not hidden
		if not file_i.startswith(HIDDEN_FILE):
			# If file is a directory, recursively explore it.
			if os.path.isdir(file_i):
				# Enter that directory.
				os.chdir(file_i)
				list_citations = collect_citations(list_citations)
				# Return to parent directory.
				os.chdir(os.pardir)
			# Else, check if this is a non-binary file.
			elif os.path.isfile(file_i):
			# Yes. Collect the citations.
				list_citations = get_citations_in_txt_file(file_i, list_citations)
				print "==	file:" + file_i + "###"
			else:
				continue
		else:
			continue
#	print "=exit for Loop"
	return list_citations



"""
	Function to collect all the citations in a text file.
	
	For each citation, store it in an array of strings.
	
	Input: fname is the filename of the file to be read/processed.
	
	Input: list_citations is the set of references cited in the
	project. They are indicated by the\cite{key} LaTeX command.
	
	Output: Return list_citations, the set of collected citations.
"""
def get_citations_in_txt_file(fname, list_citations):
	if "clean_bibtex.py" == fname:
		return list_citations
	else:
		if list_citations is None:
			list_citations = []
			list_citations.append(RANDOM)
			print ">>	Initial list is empty."
		
		# FILE OPERATIONS (Read the file!!!):
		# read - r, write - w, read/write - r+
		fo = open(fname,'r')

		# For each line in the file...
		for cur_ln in fo:
			# While there are more citations in this line...
			while 0 <= cur_ln.find("\cite"):
				t = cur_ln.find("\cite")
				
				print "Current Line"
				print cur_ln
				# Get the next available BibTeX key.
				if 0 <= cur_ln.find("{",t):
					#tt = str.find("{",t)
					temp_str = cur_ln.split('{',1)
					if 0 < len(temp_str):
						for ts in temp_str:
							key_arr = ts.split('}',1)
							if 1 < len(key_arr):
								key = key_arr[0]
								#print ">>	key:::"+key+"=="
								list_citations = list_citations.append(key)
								if list_citations is None:
									list_citations = []
									list_citations.append(key)
									
									print ">>	Initial list is EMPTY."
									print list_citations
								else:
									print "<< List NOT empty"
									print list_citations
									print "<< List still NOT empty"
									list_citations.append(key)
									print list_citations
								print type(list_citations)
								print "=	Type of Object:::"
								print list_citations
								cur_ln = key_arr[1]
				else:
					break
	print "++ Printing list of citations:::"
	print list_citations
	return list_citations




"""
	For each element in the set, copy its BibTeX entry into my
	working BibTeX reference list.
"""








# Get the list of citations
list_citations = []
list_citations.append(RANDOM)
list_citations = collect_citations(list_citations)
print "=Ciao Mondo"
print list_citations
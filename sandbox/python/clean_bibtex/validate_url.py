#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to determine if a
		non-standard BibTeX field ("Bdsk-Url-1" or "Bdsk-Url-2")
		exist, when "Doi" nor "Url" BibTeX field exist.
	When "Bdsk-Url-1" or "Bdsk-Url-2" exists, copy their values to
		the "Url" BibTeX field (and "Doi" field, if it is a DOI).
	
	Synopsis:
	For each BibTeX entry in the BibTeX database, check if it has the
		"Bdsk-Url-1" (and "Bdsk-Url-2") field(s), and if the "Url"
		(and Doi) field(s) is(/are) missing.

	This script can be executed as follows:
	./validate_url.py [input BibTeX file] [output BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have duplicate
								BibTeX entries, metadata, and
								non-standard BibTeX fields.
	[output BibTeX file]:	A clean BibTeX file without duplicate
								BibTeX entries, metadata, and
								non-standard BibTeX fields.
							[Optional parameter]

	The 2nd (and subsequent) input argument(s) is(/are) optional.

	The 2nd input argument mustn't be a valid path to an existing file.
	If it is, warn the user about overwritting the file & exit.

	If 2nd input argument has no file extension, add the BibTeX file
		extension to it.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).




	Assumptions:
	Assume that a DOI field should not be the last line in a BibTeX
		entry.
	If a DOI field is the last line in a BibTeX entry, throw an
		exception.
	Assume that an URL field should not be the last line in a BibTeX
		entry.
	If an URL field is the last line in a BibTeX entry, throw an
		exception.
	Assume that the backup URL field "Bdsk-Url-2" should end with "}}".
	Assume that all URL fields are valid.
		This is because a server hosting a URL web page can be down,
		and the script could report errors that would otherwise
		not be found (when the server is up and running again).


	Revision History:
	April 8, 2017			Version 0.1, initial build.

"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

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


###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
from queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from file_io import file_io_operations


###############################################################
#	Module with methods that validate DOI/URL fields in BibTeX
#		databases.
class validate_url_field:
	"""
		List of strings representing common lines in my BibTeX database
			that I have to process.
	"""
	bdsk_url_1 = "	Bdsk-Url-1 = {"
	bdsk_url_2 = "	Bdsk-Url-2 = {"
	end_of_line = "},\n"
	end_of_entry = "}}\n"
	url_field = "	Url = {"
	doi_field = "	Doi = {"
	doi_value = "http://dx.doi.org/"
	# Boolean flags to distinguish between different BibTeX entries.
	doi_is_missing = False
	url_is_missing = False
	has_bdsk_url_1 = True
	has_bdsk_url_2 = True
	# ============================================================
	#	Method to copy data from the input BibTeX file to the output
	#		BibTeX file.
	#	In the process, any existence of a backup URL field in a
	#		BibTeX entry, which has no URL (and DOI) field(s),
	#		implies that a URL field (and a DOI field, if appropriate),
	#		will be added to that BibTeX entry in the output BibTeX
	#		file.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param op_f_obj - The file object for the output stream,
	#						which writes the output to a BibTeX file.
	#	@param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def data_copying_n_insertion(ip_f_obj,op_f_obj,ip_file):
		print "=	Reading input BibTeX file:"+ip_file
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
				validate_url_field.doi_is_missing = True
				validate_url_field.url_is_missing = True
				validate_url_field.has_bdsk_url_1 = False
				validate_url_field.has_bdsk_url_2 = False
			else:
				# No. Line is not the 1st line of a BibTeX entry.
				# Does this line contain the URL field? 
				if(validate_url_field.is_url(line)):
					# Yes.
					validate_url_field.url_is_missing = False
				# No. Does this line contain the DOI field? 
				elif(validate_url_field.is_doi(line)):
					# Yes.
					validate_url_field.doi_is_missing = False
				# No. Does this line contain backup URL field 1?
				elif(line.startswith(validate_url_field.bdsk_url_1)):
					# Yes.
					validate_url_field.has_bdsk_url_1 = True
					# Get the URL value of this backup URL field.
#					print "	>>	line is:::"+line
					temp_url = validate_url_field.get_url(line)
#					print "	>>	temp_url is:::"+temp_url
					# If URL value is a DOI, and DOI is missing for this entry,
					if(validate_url_field.has_doi_value(temp_url) and validate_url_field.doi_is_missing):
						# Print DOI field.
						new_url_field = validate_url_field.doi_field+temp_url+validate_url_field.end_of_line
						op_f_obj.write(new_url_field)
						validate_url_field.doi_is_missing = False
					# If URL is missing for this entry,
					if(validate_url_field.url_is_missing):
						# Print URL field.
						new_url_field = validate_url_field.url_field+temp_url+validate_url_field.end_of_line
						op_f_obj.write(new_url_field)
						validate_url_field.url_is_missing = False
				# No. Does this line contain backup URL field 2?
				elif(line.startswith(validate_url_field.bdsk_url_2)):
					# Yes.
					validate_url_field.has_bdsk_url_2 = True
					if(validate_url_field.has_bdsk_url_1 == False):
						raise Exception("Backup URL field 2 exists without Backup URL field 1!!!")
					# Get the URL value of this backup URL field.
					temp_url = validate_url_field.get_url(line)
					# If URL value is a DOI, and DOI is missing for this entry,
					if(validate_url_field.has_doi_value(temp_url) and validate_url_field.doi_is_missing):
						# Print DOI field.
						new_url_field = validate_url_field.doi_field+temp_url+validate_url_field.end_of_line
						op_f_obj.write(new_url_field)
						validate_url_field.doi_is_missing = False
					# If URL is missing for this entry,
					if(validate_url_field.url_is_missing):
						# Print URL field.
						new_url_field = validate_url_field.url_field+temp_url+validate_url_field.end_of_line
						op_f_obj.write(new_url_field)
						validate_url_field.url_is_missing = False
			# Copy this line to the output file.
			op_f_obj.write(line)
	# ============================================================
	#	Method to determine if two files are equivalent.
	#	@return a boolean TRUE, if the files are equivalent. Else,
	#		return FALSE.
	#	O(n) method, with respect to the number of lines in the
	#		larger (if the files are different), or either, of the
	#		files.
	@staticmethod
	def file_comparison(file1, file2):
		return filecmp.cmp(file1,file2,shallow=False)
	# ============================================================
	#	Method to determine if a line in the BibTeX database contains
	#		the URL field.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line contains the the URL field.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_url(a_str):
		if(a_str.startswith(validate_url_field.url_field)):
			validate_url_field.url_is_missing = False
			return True
		else:
			return False
	# ============================================================
	#	Method to determine if a line in the BibTeX database contains
	#		the DOI field.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line contains the the DOI field.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_doi(a_str):
		if(a_str.startswith(validate_url_field.doi_field)):
			validate_url_field.doi_is_missing = False
			return True
		else:
			return False
	# ============================================================
	#	Method to determine if a URL contains a DOI value.
	#	@param a_str - An URL to be validated.
	#	@return a boolean TRUE, if the URL contains a DOI value.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def has_doi_value(a_str):
		if(a_str.startswith(validate_url_field.doi_value)):
			return True
		else:
			return False
	# ============================================================
	#	Method to determine if a line in the BibTeX database is the
	#		last line of a BibTeX entry.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line is the last line of a
	#		BibTeX entry.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_last_line(a_str):
		if(a_str.endswith(validate_url_field.end_of_entry)):
			return True
		else:
			return False
	# ============================================================
	#	Method to determine if a line in the BibTeX database ends
	#		with "},", if it is not the last line of a BibTeX entry.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line is not the last line of a
	#		BibTeX entry, and ends with "},".
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def ends_with_comma(a_str):
		if(a_str.endswith(validate_url_field.end_of_line)):
			return True
		else:
			return False
	# ============================================================
	#	Method to extract the URL from a backup URL field in the
	#		BibTeX database.
	#	@param a_str - A string containing/representing a line in
	#		a BibTeX database.
	#	@return a string representing the URL in the backup URL
	#		field. Else, return None.
	#	O(1) method.
	@staticmethod
	def get_url(a_str):
		return_str = a_str
		# If the string starts with "Bdsk-Url-1",
		if(return_str.startswith(validate_url_field.bdsk_url_1)):
			# Delete the initial substring "Bdsk-Url-1".
			return_str = return_str.replace(validate_url_field.bdsk_url_1,'')
#			print "	>>	return_str:::"+return_str 
		# Else if the string starts with "Bdsk-Url-1",
		elif(return_str.startswith(validate_url_field.bdsk_url_2)):
			# Delete the initial substring "Bdsk-Url-2".
			return_str = return_str.replace(validate_url_field.bdsk_url_2,'')
		else:
			# Else, this string is not a URL.
			return None
		# If the string ends with "},",
		if(validate_url_field.ends_with_comma(return_str)):
			# Delete the substring "},".
			return_str = return_str.replace(validate_url_field.end_of_line,'')
#			print "	<<	return_str:::"+return_str
			return return_str
		# Else if the string ends with "}}",
		elif(validate_url_field.is_last_line(return_str)):
			# Delete the substring "}}".
			return_str = return_str.replace(validate_url_field.end_of_entry,'')
#			print "	>>	return_str:::"+return_str
			return return_str
		else:
			# Else, this string does not contain a single-line
			#	backup URL field.
#			print "	??	return_str:::"+return_str
#			print "	&&	validate_url_field.end_of_line:::"+validate_url_field.end_of_line
#			if(return_str.endswith(validate_url_field.end_of_line)):
#				print "	||	End of line is not processed correctly."
#			print "	&&	validate_url_field.end_of_entry:::"+validate_url_field.end_of_entry
#			if(return_str.endswith(validate_url_field.end_of_entry)):
#				print "	||	Last line is not processed correctly."
			return None
	# ============================================================
	#	Method to determine if a line in the BibTeX database is a
	#		backup URL field.
	#	@param a_str - A string containing/representing a line in a
	#		BibTeX database.
	#	@return a boolean TRUE, if the line contains a backup URL field.
	#		Else, return FALSE.
	#	O(1) method.
	def is_bdsk_url(a_str):
		# If the string starts with "Bdsk-Url-1",
		if(a_str.startswith(validate_url_field.bdsk_url_1)):
			return True
		elif(a_str.startswith(validate_url_field.bdsk_url_2)):
			return True
		else:
			return False
	# ============================================================
	#	Method to ensure that URL and DOI fields exist for each
	#		BibTeX entry, if the BibTeX entry has one/two backup
	#		URL fields.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param ip_file - The filename of the output BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def ensure_doi_url(ip_f_obj,ip_file):
		print "=	Reading output BibTeX file:"+ip_file
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
				validate_url_field.doi_is_missing = True
				validate_url_field.url_is_missing = True
				validate_url_field.has_bdsk_url_1 = False
				validate_url_field.has_bdsk_url_2 = False
			else:
				# No. Line is not the 1st line of a BibTeX entry.
				# Does this line contain the URL field? 
				if(validate_url_field.is_url(line)):
					# Yes.
					validate_url_field.url_is_missing = False
				# No. Does this line contain the DOI field? 
				elif(validate_url_field.is_doi(line)):
					# Yes.
					validate_url_field.doi_is_missing = False
				# No. Does this line contain backup URL field 1?
				elif(line.startswith(validate_url_field.bdsk_url_1)):
					# Yes.
					validate_url_field.has_bdsk_url_1 = True
					# Get the URL value of this backup URL field.
#					print "	>>	line is:::"+line
					temp_url = validate_url_field.get_url(line)
#					print "	>>	temp_url is:::"+temp_url
					# If URL value is a DOI, and DOI is missing for this entry,
					if(validate_url_field.has_doi_value(temp_url) and validate_url_field.doi_is_missing):
						raise Exception("DOI field is missing!!!")
					# If URL is missing for this entry,
					if(validate_url_field.url_is_missing):
						raise Exception("URL field is missing!!!")
				# No. Does this line contain backup URL field 2?
				elif(line.startswith(validate_url_field.bdsk_url_2)):
					# Yes.
					validate_url_field.has_bdsk_url_2 = True
					if(validate_url_field.has_bdsk_url_1 == False):
						raise Exception("Backup URL field 2 exists without Backup URL field 1!!!")
					# Get the URL value of this backup URL field.
					temp_url = validate_url_field.get_url(line)
					# If URL value is a DOI, and DOI is missing for this entry,
					if(validate_url_field.has_doi_value(temp_url) and validate_url_field.doi_is_missing):
						raise Exception("DOI field 2 is missing!!!")
					# If URL is missing for this entry,
					if(validate_url_field.url_is_missing):
						raise Exception("URL field 2 is missing!!!")





###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	# --------------------------------------------------------
	#	= Start of Preprocessing.
	queue_ip_args.preprocessing()
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print "==================================================="
	print "Validating the URLs/DOIs of BibTeX entries."
	print ""
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.VALIDATE_URL_DOI)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print "=	Process the first input argument." 
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Check if 2nd input argument is missing/available.
	queue_ip_args.missing_2nd_ip_arg()
	# Process the second input argument.
	print "=	Process the second input argument." 
	op_filename = queue_ip_args.process_2nd_ip_arg()
	# Create a file object for reading.
	print "=	Create a file object for reading."
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	# Create a file object for writing.
	print "=	Create a file object for writing."
	op_file_obj = file_io_operations.open_file_object_write(op_filename)
	# Copy data from input BibTeX file to output BibTeX file.
	validate_url_field.data_copying_n_insertion(ip_file_obj,op_file_obj,ip_filename)
	# Close the file object for reading.
	print "=	Close the file object for reading."
	file_io_operations.close_file_object(ip_file_obj)
	# Close the file object for writing.
	print "=	Close the file object for writing."
	file_io_operations.close_file_object(op_file_obj)
	# Compare the input and output BibTeX files.
	if (validate_url_field.file_comparison(ip_filename,op_filename)):
		print "=	The input and output BibTeX files are EQUIVALENT!!!"
	else:
		print "=	The input and output BibTeX files are different."
	# Ensure that the DOI and URL fields exists, if appropriate.
	ip_file_obj = file_io_operations.open_file_object_read(op_filename)
	validate_url_field.ensure_doi_url(ip_file_obj,op_filename)
	file_io_operations.close_file_object(ip_file_obj)
	print "=	DOI and URL fields exist in appropriate places."
	# Delete the output BibTeX file.
#	os.remove(op_filename)

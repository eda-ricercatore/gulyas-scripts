#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to perform date and time
		processing/operations.

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	Notes/Assumptions:
	Assume that the following functions would be used together
		to validate the date/day of a month (and given year):
		+ date_time_operations.is_valid_31_day_month(dd,mm)
		+ date_time_operations.is_valid_30_day_month(dd,mm)
		+ date_time_operations.is_valid_date_in_Feb(dd,mm,yy))
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
import calendar


###############################################################
#	Module with methods that perform date & time processing/operations.
class date_time_operations:
	"""
		Create a dictionary (associative memories, or associative arrays)
			of (number, name) months.
	"""
	mth_number_name = {"1":"january", "2":"february", "3":"march", "4":"april", "5":"may", "6":"june", "7":"july", "8":"august", "9":"september", "10":"october", "11":"november", "12":"december"}
	# ============================================================
	##	Method to determine if the time is valid.
	#	@param hh - Hour of a time in numbers.
	#	@param mm - Minutes of a time in numbers.
	#	@param ss - Seconds of a time in numbers.
	#	@param us - Microseconds of a time in numbers.
	#	@return boolean True if the date is valid;
	#		else, return False.
	#	O(1) method.
	@staticmethod
	def is_valid_time(hh,mm,ss,us):
		# Check if the hour is valid: 0 <= tokens[3] <= 23.
		if (0>hh) or (23<hh):
			return False
		# Check if the minute is valid: 0 <= tokens[4] <= 59.
		if (0>mm) or (59<mm):
			return False
		# Check if the second is valid: 0 <= tokens[5] <= 59.
		if (0>ss) or (59<ss):
			return False
		# Check if the microsecond is valid: 0 <= tokens[6] <= 1000000.
		if (0>us) or (1000000<us):
			return False
		return True
	# ============================================================
	##	Method to determine if the year is valid.
    #	Check if the year is valid: 2014 <= yy <= 2100.
	#	@param yy - year of a date in numbers.
	#	@return boolean True if the year is valid;
	#		else, return False.
	#	O(1) method.
	@staticmethod
	def is_valid_year(yy):
		if (2014 > yy) or (2100 < yy):
			return False
		else:
			return True
	# ============================================================
	##	Method to determine if the month is valid.
	#	Check if the month is valid: 1 <= mm <= 12.
	#	@param mm - Month of a date in numbers.
	#	@return boolean True if the month is valid;
	#		else, return False.
	#	O(1) method.
	@staticmethod
	def is_valid_month(mm):
		if (1 > mm) or (12 < mm):
			return False
		else:
			return True
	# ============================================================
	##	Method to determine if the date/day of a 31-day month is valid.
	#	@param dd - Date/Day of a date (specifically 31-day month)
	#                   in numbers.
	#	@param mm - 31-day month of a date in numbers.
	#	@return boolean True if the date/day of a 31-day month is valid;
	#		else, return False.
	#	O(1) method.
	#
	#	Assume that the functions is_valid_30_day_month(dd,mm) and
	#		is_valid_date_in_Feb(dd,mm,yy) will determine the
	#		validity of the date for not-a-31-day months.
	@staticmethod
	def is_valid_31_day_month(dd,mm):
		if not date_time_operations.is_valid_month(mm):
			return False
		# Check if month has 31 days, 1 <= dd <= 31.
		if ((1 == mm) or (3 == mm) or (5 == mm) or (7 == mm) or (8 == mm) or (10 == mm) or (12 == mm)):
			if (1 > dd) or (31 < dd):
				return False
		"""
			Assume that the functions is_valid_30_day_month(dd,mm) and
				is_valid_date_in_Feb(dd,mm,yy) will determine the
				validity of the date for not-a-31-day months.
		"""
		return True
	# ============================================================
	##	Method to determine if the date/day of a 30-day month is valid.
	#	@param dd - Date/Day of a date (specifically 30-day month)
	#                   in numbers.
	#	@param mm - 30-day month of a date in numbers.
	#	@return boolean True if the date/day of a 30-day month is valid;
	#		else, return False.
	#	O(1) method.
	#
	#	Assume that the functions is_valid_31_day_month(dd,mm) and
	#		is_valid_date_in_Feb(dd,mm,yy) will determine the
	#		validity of the date for not-a-30-day months.
	@staticmethod
	def is_valid_30_day_month(dd,mm):
		if not date_time_operations.is_valid_month(mm):
			return False
		# Check if month has 30 days, 1 <= dd <= 30.
		if ((4 == mm) or (6 == mm) or (9 == mm) or (11 == mm)):
			if (1 > dd) or (30 < dd):
				return False
		"""
			Assume that the functions is_valid_31_day_month(dd,mm) and
				is_valid_date_in_Feb(dd,mm,yy) will determine the
				validity of the date for not-a-30-day months.
		"""
		return True
	# ============================================================
	##	Method to determine if the date in February is valid.
	#	@param dd - Date/Day of a date in February in numbers.
	#	@param mm - Month of a date (in February) in numbers.
	#	@param yy - Year of a date in numbers.
	#	@return boolean True if the date is valid;
	#		else, return False.
	#	O(1) method.
	#
	#	Assume that the functions is_valid_31_day_month(dd,mm)
	#		and is_valid_30_day_month(dd,mm) will determine the
	#		validity of the date for not-February months.
	@staticmethod
	def is_valid_date_in_Feb(dd,mm,yy):
		if not date_time_operations.is_valid_year(yy):
			return False
		if not date_time_operations.is_valid_month(mm):
			return False
		if (calendar.isleap(yy)) and (2 == mm):
			if ((1 > dd) or (29 < dd)):
				return False
			else:
				return True
		elif (not calendar.isleap(yy)) and (2 == mm):
			if ((1 > dd) or (28 < dd)):
				return False
			else:
				return True
		else:
			"""
				Assume that the functions is_valid_31_day_month(dd,mm)
					and is_valid_30_day_month(dd,mm) will determine the
					validity of the date for not-February months.
			"""
			return True
	# ============================================================
	##	Method to determine if the date is valid.
	#	@param dd - Date/Day of a date in numbers.
	#	@param mm - Month of a date in numbers.
	#	@param yy - Year of a date in numbers.
	#	@return boolean True if the date is valid;
	#		else, return False.
	#	O(1) method.
	#
	#	Assume that the following functions would be used together
	#		to validate the date/day of a month (and given year):
	#		+ date_time_operations.is_valid_31_day_month(dd,mm)
	#		+ date_time_operations.is_valid_30_day_month(dd,mm)
	#		+ date_time_operations.is_valid_date_in_Feb(dd,mm,yy))
	@staticmethod
	def is_valid_date(dd,mm,yy):
		return (date_time_operations.is_valid_month(mm) and date_time_operations.is_valid_year(yy) and date_time_operations.is_valid_31_day_month(dd,mm) and date_time_operations.is_valid_30_day_month(dd,mm) and date_time_operations.is_valid_date_in_Feb(dd,mm,yy))
	# ============================================================
	##	Method to tokenize the filename containing information
	#		about the date and time in which the output files are
	#		generated.
	#	@param filename - Name of a file.
	#	@return tokens if the filename containing the date and
	#		time placed in the DD-MM-YY-HR-MN-SS-US format is valid;
	#		else, return None.
	#	O(n) method, with respect to the number of characters in the
	#		filename argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	@staticmethod
	def get_date_time_tokens_of_filename(filename):
		if date_time_operations.check_filename_date_time_format(filename):
			# Remove the file extension from the filename.
			filename, filename_extension = os.path.splitext(filename)
			tokens = filename.split("-")
			return tokens
		else:
			return None
	# ============================================================
	##	Method to determine if the filename contains information
	#		about the date and time in which the output files are
	#		generated.
	#	@param filename - Name of a file.
	#	@return boolean True if the filename contains the date and
	#		time placed in the DD-MM-YY-HR-MN-SS-US format is valid;
	#		else, return False.
	#	O(n) method, with respect to the number of characters in the
	#		filename argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	@staticmethod
	def check_filename_date_time_format(filename):
		"""
			Cannot use the get_date_time_tokens_of_filename() method
				of this date_time_operations module/class, because it
				will result in infinite recursion.
			#tokens = date_time_operations.get_date_time_tokens_of_filename(filename)
		"""
		# Remove the file extension from the filename.
		filename, filename_extension = os.path.splitext(filename)
		tokens = filename.split("-")
		return (date_time_operations.is_valid_date(int(tokens[0]),int(tokens[1]),int(tokens[2])) and date_time_operations.is_valid_time(int(tokens[3]),int(tokens[4]),int(tokens[5]),int(tokens[6])))

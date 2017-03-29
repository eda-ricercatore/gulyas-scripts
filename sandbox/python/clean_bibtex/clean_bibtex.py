#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to clean
		BibTeX files of metadata and non-standard BibTeX
		fields.
	As for non-standard BibTeX entries, it shall change their
		BibTeX type to "misc".
	
	Synopsis:
	Remove non-standard BibTeX fields and correct non-standard
		BibTeX types.

	This script can be executed as follows:
	./clean_bibtex.py [BibTeX file]

	Parameters:
	[BibTeX file]: A BibTeX file to be processed.
"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


###############################################################
#	Import modules from The Python Standard Library.
import sys
import os



###############################################################
#	Module with methods that clean BibTeX files.
class Clean_BibTeX_DB:
	# ============================================================
	#	Method to provide information on how to run this script.
	@staticmethod
	def how_to_use_script():
		print "================================================="
		print "==>	This script cleans BibTeX files of non-standard"
		print "	BibTeX fields."
		print "	It also corrects non-standard BibTeX types."
		print ""
		print "This script can be executed as follows:"
		print "./clean_bibtex.py [BibTeX file]"
		print ""
		print "================================================="
		# Inform the user what went wrong.
		raise Exception("Error with input arguments.")

























###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print "==================================================="
	print "Cleaning the BibTeX file of non-standard BibTeX fields."
	print "	And, correcting non-standard BibTeX types."
	#	BLAH.
	Clean_BibTeX_DB.how_to_use_script()
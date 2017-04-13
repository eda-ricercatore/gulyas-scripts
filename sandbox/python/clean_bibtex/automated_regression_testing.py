#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to perform regression
		testing of his Python scripts to clean BibTeX databases.
	This includes validating non-standard BibTeX fields as well as
		BibTeX entries that are of non-standard BibTeX (entry) types.
	
	
	Synopsis:
	Carry out automated regression testing to see if
	"duplicate_BibTeX_entries.py" works as specified.
	
	
	
	This script can be executed as follows:
	./automated_regression_testing.py [dirty-BibTeX-file] [clean-BibTeX-file] [directory of LaTeX source files]
	
	Parameters:
	[dirty-BibTeX-file]
		A BibTeX file that may have the following:
		+ duplicated BibTeX entries.
		+ metadata in any BibTeX entry in the file.
		+ BibTeX entries that are not cited in the (working) document.
	[clean-BibTeX-file]
		A BibTeX file that should not have the following:
		+ duplicated BibTeX entries.
		+ metadata in any BibTeX entry in the file.
		+ BibTeX entries that are not cited in the (working) document.
	[directory of LaTeX source files]
		A directory where the LaTeX source files of a (working)
			document are located.
"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


###############################################################
#	Import modules from The Python Standard Library.

#	Get access to any command-line arguments.
import sys
#	To make system calls.
from subprocess import call
#	Import Python modules that I have developed.
#from build_sra_seq_db import Build_Seq_DB
#	Use any operating system dependent functionality.
import os

###############################################################
#	Test the script for input errors

print "##################################################"
print "==>>	Begin automated regression testing."

print "##################################################"
print "=	Testing: duplicate_BibTeX_entries.py"
print "-	-	-	-	-	-	-	-"
print "	=>	With no input arguments."
call("./duplicate_BibTeX_entries.py")
print "-	-	-	-	-	-	-	-"
print "	=>	With one input argument. Invalid path"
call(["./duplicate_BibTeX_entries.py","qwerty"])
print "-	-	-	-	-	-	-	-"
print "	=>	With one input argument: Valid path."
call(["./duplicate_BibTeX_entries.py","input/extra.bib"])
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: Invalid BibTeX entry types."
call(["./duplicate_BibTeX_entries.py","input/incorrect_bibtex_type.bib"])
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: Duplicate BibTeX entries exist."
call(["./duplicate_BibTeX_entries.py","input/duplicates_bibtex_keys.bib"])
"""
	print "-	-	-	-	-	-	-	-"
	print "	=>	With two input arguments: Invalid path + Valid path."
	call(["./duplicate_BibTeX_entries.py","qwerty","input/extra.bib"])
	print "-	-	-	-	-	-	-	-"
	print "	=>	With two input arguments: Invalid path + Invalid path."
	call(["./duplicate_BibTeX_entries.py","qwerty","poiuytre"])
	print "-	-	-	-	-	-	-	-"
	print "	=>	With two input arguments: Valid path + Valid path."
	call(["./duplicate_BibTeX_entries.py","input/one_bibtex_entry.bib","input/extra.bib"])
	print "-	-	-	-	-	-	-	-"
	print "	=>	With two input arguments: Valid path + Invalid path."
	call(["./duplicate_BibTeX_entries.py","input/one_bibtex_entry.bib","qwerty.bib"])
	#os.remove("qwerty.bib")
"""
print "-	-	-	-	-	-	-	-"
print "	=>	Input BibTeX File: 4/6 incorrect BibTeX entry types; 100010"
call(["./duplicate_BibTeX_entries.py","input/incorrect_bibtex_type.bib","y-1.bib"])
#os.remove("y-1.bib")
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: One BibTeX entry."
call(["./duplicate_BibTeX_entries.py","input/one_bibtex_entry.bib"])
print "-	-	-	-	-	-	-	-"
print "	=>	With >2 arguments: Valid path + Invalid path + ... (One BibTeX entry.)"
call(["./duplicate_BibTeX_entries.py","input/one_bibtex_entry.bib","asdfgh","3rdarg","4tharg","5tharg","6tharg","7tharg"])
#os.remove("asdfgh.bib")
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: No duplicates. Simple."
call(["./duplicate_BibTeX_entries.py","input/simple.bib","y-1.bib"])
#os.remove("y-1.bib")
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: No duplicates. Extensive."
call(["./duplicate_BibTeX_entries.py","input/no_duplicate_bibtex_keys.bib"])
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: Get Help (1)."
call(["./duplicate_BibTeX_entries.py","input/no_duplicate_bibtex_keys.bib","-h"])
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: Get Help (2)."
call(["./duplicate_BibTeX_entries.py","-h","input/simple.bib","y-1.bib"])
#os.remove("y-1.bib")
print "-	-	-	-	-	-	-	-"
print "	=>	Detect duplicate BibTeX keys: Get Help (3)."
call(["./duplicate_BibTeX_entries.py","-h"])

print "##################################################"
print "=	Testing: validate_url.py"
print "-	-	-	-	-	-	-	-"
print "	=>	With no input arguments."
call("./validate_url.py")
print "-	-	-	-	-	-	-	-"
print "	=>	With one INVALID input argument."
call(["./validate_url.py","qwerty"])
print "-	-	-	-	-	-	-	-"
fname = "input/one_bibtex_entry_op.bib"
print "	=>	With one valid input argument."
call(["./validate_url.py","input/one_bibtex_entry.bib"])
os.remove(fname)
print "-	-	-	-	-	-	-	-"
print "	=>	With 1 valid input argument, and 1 valid output argument."
dummy = "input/extra.bib"
call(["./validate_url.py","input/one_bibtex_entry.bib",dummy])
print "-	-	-	-	-	-	-	-"
print "	=>	With 1 valid input argument, and 1 invalid output argument."
dummy = "input/y-dummy.bib"
call(["./validate_url.py","input/one_bibtex_entry.bib",dummy])
#os.remove(dummy)
print "-	-	-	-	-	-	-	-"
print "	=>	Has Bdsk-Url-2, but not Bdsk-Url-1."
dummy = "input/x-dummy.bib"
call(["./validate_url.py","input/has_backup2_no_backup1.bib",dummy])
os.remove(dummy)

print "-	-	-	-	-	-	-	-"
print "	=>	Has missing DOIs and/or URLs."
call(["./validate_url.py","input/missing_doi_url.bib"])

print "-	-	-	-	-	-	-	-"
print "	=>	Extensive testing."
call(["./validate_url.py","input/no_duplicate_bibtex_keys.bib"])

#	rm input/missing_doi_url_op.bib input/no_duplicate_bibtex_keys_op.bib input/y-dummy.bib 
print "##################################################"
print "==>>	End automated regression testing."
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""

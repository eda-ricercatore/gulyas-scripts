#	General Information

This set of scripts is to clean up my BibTeX database.

My BibTeX database is a large set of BibTeX entries.
	Each BibTeX entry references a (research) publication.

It contains the following scripts:
+ duplicate-BibTeX-entries.py
	- Determine if duplicate BibTeX entries exist in my BibTeX
		database.
	- IMPORTANT
+ doi-validation.py
	- Validate the DOI field of BibTeX entries in my BibTeX database.
+ extract-citations.py
	- Extract the subset of BibTeX entries that are cited in a
		document that I wrote or co-authored.
+ not-defined-references.py
	- Check if this citation uses a undefined reference (BibTeX entry).
+ clean_bibtex.py
	- Remove metadata from each BibTeX entry.
	- Transform non-standard BibTeX entry types to standard BibTeX
		entry types.
	- Remove comments from LaTeX source files.
+ rm_bibtex_metadata.py
	- Remove metadata from each BibTeX entry.
+ standardize-bibtex-entries.py
	- Transform non-standard BibTeX entry types to standard BibTeX
		entry types.
+ uncomment-latex-src-files.py
	- Remove comments from LaTeX source files. Non importante.
+ altri-BibTeX-operazioni.py
	- Perform miscellaneous tasks to clean up the BibTeX file.
	- Check if the ampersand is surrounded by curly braces and set
		to the normal (non-Italics) font.
	- For each conference, check if its abbreviation is placed within
		round brackets after the title of the conference proceedings.
	  Check if there is no comma between the title and the
		abbreviation.
	- Write a script to extract the keywords from the BibTeX
		repository, arrange them in alphabetical order, and pipe them
		to an output file.
	- Check if the addresses of the publications have the U.S. states
		in capital letters.
		If I use abbreviations for states and territories in Australia
		and Canada, do likewise.
		For publications outside the U.S., (and Australia and Canada),
		ignore this.
	- Check if DOIs and/or URL fields are missing, if the following
		fields (metadata for BibDesk) exists:
		- "Bdsk-Url-1". 
+ automated_regression_testing.py
	- Perform regression testing on the Python scripts for validating
		and cleaning BibTeX files.















#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


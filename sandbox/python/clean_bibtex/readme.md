#	General Information

This set of scripts is to clean up my BibTeX database.

My BibTeX database is a large set of BibTeX entries.
	Each BibTeX entry references a (research) publication.

It contains the following scripts:
+ queue_ip_arguments.py
	- Not executed as a script. Part of my custom *Python* Library.
	- *Python* script to process input arguments for *Python* scripts.
+ file_io.py
	- Not executed as a script. Part of my custom *Python* Library.
	- *Python* script to perform input/output (I/O) operations on files. 
+ duplicate_BibTeX_entries.py
	- ./duplicate_BibTeX_entries.py [BibTeX file] [-h]
	- Determine if duplicate BibTeX entries exist in my BibTeX
		database.
	- No output required.
	- IMPORTANT
+ validate_url.py
	- ./validate_url.py [input BibTeX file] [output BibTeX file] [-h]
	- Validate the URL field of BibTeX entries in my BibTeX database.
	- If there exists backup URL and there does not exist any URL
		entry, add DOI entry.
	- No output required.
	- IMPORTANT
+ justify-doi.py
	- ./justify-doi.py [BibTeX file]
	- Validate the DOI field of BibTeX entries in my BibTeX database.
	- If there exists backup URL and there does not exist any DOI
		entry, add DOI entry.
	- No output required.
	- IMPORTANT
+ clean_bibtex.py
	- ./clean_bibtex.py [input BibTeX file] [output BibTeX file] [-h]
	- Remove metadata from each BibTeX entry.
	- Transform non-standard BibTeX entry types to standard BibTeX
		entry types.
	- Remove comments from LaTeX source files.
+ rm_bibtex_metadata.py
	- ./rm_bibtex_metadata.py [input BibTeX file] [output BibTeX file]
	- Remove metadata from each BibTeX entry.
+ standardize_bibtex_entries.py
	- ./standardize_bibtex_entries.py [input BibTeX file] [output BibTeX file]
	- Transform non-standard BibTeX entry types to standard BibTeX
		entry types.
+ extract_citations.py
	- ./extract_citations.py [LaTeX sources] [BibTeX output]
	- Produces an intermediate output, which is a set of BibTeX keys
		that uniquely identifies a matching BibTeX entry in my BibTeX
		database.
+ not_defined_references.py
	- ./not_defined_references.py  [LaTeX sources] [BibTeX input]
	- Check if this citation uses a undefined reference
	- No output required.
+ uncomment_latex_src_files.py
	- ./uncomment_latex_src_files.py [dirty LaTeX source files] [clean LaTeX source files]
	- Remove comments from LaTeX source files. Non importante.
+ z-altri-BibTeX-operazioni.py
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
	- ./automated_regression_testing.py
	- No input nor output required.
	- Perform regression testing on the Python scripts for validating
		and cleaning BibTeX files.
+ Additional filenames that I can use:
	- purify_bibtex.py













#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


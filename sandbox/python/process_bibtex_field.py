#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to process lines in
		BibTeX databases.
	A BibTeX database is a set of BibTeX entries.
	A BibTeX entry has a set of BibTeX fields, which may include the
		non-standard "Bdsk-Url-1" or "Bdsk-Url-2" BibTeX field.

	There exists no backup URL BibTeX field apart from the
		aforementioned two backup URL BibTeX fields.

	What works in this file will be used in my clean_BibTeX repository
		of Python scripts to "clean" my BibTeX databases of metadata,
		and non-standard BibTeX fields.

	This script can be executed as follows:
	./process_bibtex_field.py
"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

###############################################################
"""
	List of strings representing common lines in my BibTeX database
		that I have to process.
"""
# Backup URL field 1
backup_url_field1_not_last_line = "Bdsk-Url-1 = {https://elifesciences.org/content/5/e16800},"
backup_url_field1_not_last_line_doi = "Bdsk-Url-1 = {http://dx.doi.org/10.7554/eLife.13323},"
backup_url_field1_last_line = "Bdsk-Url-1 = {https://www.babble.com/relationships/lessons-learned-about-racial-tolerance-from-the-only-white-kid-on-this-step-team/}}"
backup_url_field1_last_line_doi = "Bdsk-Url-1 = {http://dx.doi.org/10.3386/w22347}}"
# Backup URL field 2
backup_url_field2_last_line_last_line_doi = "Bdsk-Url-2 = {http://dx.doi.org/10.7554/eLife.13323.001}}"
backup_url_field2_last_line_last_line = "Bdsk-Url-2 = {http://doi.acm.org/10.1145/270955.270970}}"
backup_url_field2_last_line = "Bdsk-Url-2 = {http://booksite.mkp.com/9780123838728/references.php}}"
backup_url_field2_last_line_doi = "Bdsk-Url-2 = {http://dx.doi.org/10.1007/b117041}}"

















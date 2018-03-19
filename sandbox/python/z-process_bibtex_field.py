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

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Apr 14, 2017'


###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from queue_ip_arguments import queue_ip_args
#import clean_bibtex.queue_ip_arguments.queue_ip_args
#import clean_bibtex.queue_ip_arguments
#from clean_bibtex.queue_ip_arguments import queue_ip_args

###############################################################

# ============================================================
#	Method to extract the URL from a backup URL field in the
#		BibTeX database.
#	@param a_str - A string containing/representing a line in
#		a BibTeX database.
#	@return a string representing the URL in the backup URL
#		field. Else, return None.
#	O(1) method.
def get_url(a_str):
	return_str = a_str
	# If the string starts with "Bdsk-Url-1",
	if(return_str.startswith(bdsk_url_1)):
		# Delete the initial substring "Bdsk-Url-1".
		return_str = return_str.replace(bdsk_url_1,'')
	# Else if the string starts with "Bdsk-Url-1",
	elif(return_str.startswith(bdsk_url_2)):
		# Delete the initial substring "Bdsk-Url-2".
		return_str = return_str.replace(bdsk_url_2,'')
	else:
		# Else, this string is not a URL.
		return None
	# If the string ends with "},",
	if(return_str.endswith(end_of_line)):
		# Delete the substring "},".
		return_str = return_str.replace(end_of_line,'')
		return return_str
	# Else if the string ends with "}}",
	elif(return_str.endswith(end_of_entry)):
		# Delete the substring "}}".
		return_str = return_str.replace(end_of_entry,'')
		return return_str
	else:
		# Else, this string does not contain a single-line
		#	backup URL field.
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
	if(a_str.startswith(bdsk_url_1)):
		return True
	elif(a_str.startswith(bdsk_url_2)):
		return True
	else:
		return False



###############################################################
"""
	List of strings representing common lines in my BibTeX database
		that I have to process.
"""
bdsk_url_1 = "	Bdsk-Url-1 = {"
bdsk_url_2 = "	Bdsk-Url-2 = {"
end_of_line = "},"
end_of_entry = "}}"
not_a_url = "This is not a URL (web address)."

# Backup URL field 1
backup_url_field1_not_last_line = "	Bdsk-Url-1 = {https://elifesciences.org/content/5/e16800},"
backup_url_field1_not_last_line_doi = "	Bdsk-Url-1 = {http://dx.doi.org/10.7554/eLife.13323},"
backup_url_field1_last_line = "	Bdsk-Url-1 = {https://www.babble.com/relationships/lessons-learned-about-racial-tolerance-from-the-only-white-kid-on-this-step-team/}}"
backup_url_field1_last_line_doi = "	Bdsk-Url-1 = {http://dx.doi.org/10.3386/w22347}}"
# Backup URL field 2
backup_url_field2_not_last_line = "	Bdsk-Url-2 = {http://doi.acm.org/10.1145/270955.270970},"
backup_url_field2_not_last_line_doi = "	Bdsk-Url-2 = {http://dx.doi.org/10.7554/eLife.13323.001},"
backup_url_field2_last_line = "	Bdsk-Url-2 = {http://booksite.mkp.com/9780123838728/references.php}}"
backup_url_field2_last_line_doi = "	Bdsk-Url-2 = {http://dx.doi.org/10.1007/b117041}}"

"""
	backup_url_field1_not_last_line
	backup_url_field1_not_last_line_doi
	backup_url_field1_last_line
	backup_url_field1_last_line_doi

	backup_url_field2_not_last_line
	backup_url_field2_not_last_line_doi
	backup_url_field2_last_line
	backup_url_field2_last_line_doi
"""

# Detect if the line begins with a given substring  
if(backup_url_field1_not_last_line.startswith(bdsk_url_1)):
	print "	backup_url_field1_not_last_line		starts with bdsk_url_1."
else:
	print "[string].startswith([another string]) implementation error!!! Test 1."

if(backup_url_field1_not_last_line_doi.startswith(bdsk_url_1)):
	print "	backup_url_field1_not_last_line_doi	starts with bdsk_url_1."
else:
	print "[string].startswith([another string]) implementation error!!! Test 2."

if(backup_url_field1_last_line.startswith(bdsk_url_1)):
	print "	backup_url_field1_last_line		starts with bdsk_url_1."
else:
	print "[string].startswith([another string]) implementation error!!! Test 3."

if(backup_url_field1_last_line_doi.startswith(bdsk_url_1)):
	print "	backup_url_field1_last_line_doi		starts with bdsk_url_1."
else:
	print "[string].startswith([another string]) implementation error!!! Test 4."
#	-----------------------------------------------------------
if(backup_url_field2_not_last_line.startswith(bdsk_url_2)):
	print "	backup_url_field2_not_last_line		starts with bdsk_url_2."
else:
	print "[string].startswith([another string]) implementation error!!! Test 5."

if(backup_url_field2_not_last_line_doi.startswith(bdsk_url_2)):
	print "	backup_url_field2_not_last_line_doi	starts with bdsk_url_2."
else:
	print "[string].startswith([another string]) implementation error!!! Test 6."

if(backup_url_field2_last_line.startswith(bdsk_url_2)):
	print "	backup_url_field2_last_line		starts with bdsk_url_2."
else:
	print "[string].startswith([another string]) implementation error!!! Test 7."

if(backup_url_field2_last_line_doi.startswith(bdsk_url_2)):
	print "	backup_url_field2_last_line_doi		starts with bdsk_url_2."
else:
	print "[string].startswith([another string]) implementation error!!! Test 8."

print "============================================================"

if(backup_url_field2_not_last_line.endswith(end_of_line)):
	print "backup_url_field2_not_last_line		ends with },"
else:
	print "[string].endswith([another string]) implementation error!!! Test 1."

if(backup_url_field2_last_line.endswith(end_of_entry)):
	print "backup_url_field2_last_line		ends with }}"
else:
	print "[string].endswith([another string]) implementation error!!! Test 1."

print "============================================================"

if(backup_url_field2_not_last_line.startswith(bdsk_url_2) and backup_url_field2_not_last_line.endswith(end_of_line)):
	print "Boolean comparison works for initial and final substring."
else:
	print "[string].endswith([another string]) implementation error!!! Test 1."

print "============================================================"

web_addr =  backup_url_field2_not_last_line.replace(end_of_line,'')
web_addr =  web_addr.replace(bdsk_url_2,'')

print	"	web_addr is now:"+web_addr 

print "============================================================"

print license
#license()
print credits
print copyright


if(is_bdsk_url(backup_url_field2_not_last_line)):
	print "=	This is a URL."

print "=	The URL is:::"+get_url(backup_url_field1_not_last_line)

print "============================================================"

set_of_BibTeX_fields = ["	Address = {", "	Annote = {", "	Author = {", "	Booktitle = {", "	Chapter = {", "	Crossref = {", "	Doi = {", "	Edition = {", "	Editor = {", "	Howpublished = {", "	Institution = {", "	Journal = {", "	Month = {", "	Note = {", "	Number = {", "	Organization = {", "	Pages = {", "	Publisher = {", "	School = {", "	Series = {", "	Title = {", "	Type = {", "	Url = {", "	Volume = {", "	Year = {"]

#print set_of_BibTeX_fields
for elem in set_of_BibTeX_fields:
	print elem

str = "	Edition = {Anniversary},"
for elem in set_of_BibTeX_fields:
	if(str.startswith(elem)):
		print "==="+str


str = "state-of-the-art SAT solvers can solve large and intractable problems"
for elem in set_of_BibTeX_fields:
	if(str.startswith(elem)):
		print str

print "============================================================"

fifo_queue = ["adhweuidh1", "bdhoweij1", "cwqhgdwqui1", "dewwe1", "edwede1", "frhwdjoqw1"]

while(1 < len(fifo_queue)):
	print fifo_queue.pop(0)
a_str  = fifo_queue.pop(0)
a_str = a_str[:-1] + "}"
print a_str

if(0 == len(fifo_queue)):
	print "List operations work."
else:
	print "List operations FAIL!!!"

print "============================================================"


esempio = "	Keywords = {industrial R&D, industry best practices, industry best practices awareness, industry standards},\n"
esempio = esempio.replace("	Keywords = {","")
esempio = esempio.replace("},\n","")
print "esempio is now:::"+esempio 
esempio = esempio.split(", ")
esempio2 = "coloring books, adult coloring books, academia, industry standards"
esempio2 = esempio2.split(", ")
esempio3 = esempio+esempio2
esempio4 = esempio3.append("qwerty")
esempio5 = list(set(esempio+esempio2))
esempio6 = sorted(esempio5)
print "------------------------------------------------------"
print "Finally, esempio is:::"
for elem in esempio:
	print elem
print "------------------------------------------------------"
for elem in esempio2:
	print elem
print "------------------------------------------------------"
for elem in esempio5:
	print elem
print "------------------------------------------------------"
for elem in esempio6:
	print elem

if not ("academia" in esempio3):
	print "esempio3 DOES NOT HAVE 'academia'."
else:
	print "esempio3 has 'academia'."

if not ("deiwh" in esempio3):
	print "esempio3 does not have 'deiwh'."
else:
	print "esempio3 HAS 'deiwh'."

print "------------------------------------------------------"

#print "size of esempio6 is:"+str(len(esempio6))
#print "size of esempio6 is:"+len(esempio6)._str_()

a_num = len(esempio6)
#a_str = str(a_num)
#print "size of esempio6 is:"+a_str
print "size of esempio6 is:",a_num

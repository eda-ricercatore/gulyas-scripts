#!/usr/bin/python

"""
	This is written by Zhiyang Ong to modify text (non-binary) files.
 
	Synopsis:
	Script to modify text (non-binary) files.
	
	Design choices:
		1)	Read the file.
			Modify currently enumerated line (writing process).
			Failed to work as of Nov 11, 2014 at 2200 hrs.

		2)	Read the file.
			Modify currently enumerated line as a temp string.
			Write the temp string to a temp file.
			Rename temp file to the target name file.
			
		3)	Create file objects for read and write separately
				(for the same input file).
			Read the file.
			Modify currently enumerated line.
			Write the modified line to the input file.
	
	I have attempted implementing methods 1 and 2 in vain.
	I will implement method two.
	
	
			
	References:
	Adam Pierce and Matthew Eager (Editor), Answer to "How do
		I modify a text file in Python?", in Stack Overflow,
		Stack Exchange Inc., New York, NY, September 24, 2008
		(Modified October 9, 2012).

	Revision History:
	1)	November 11, 2014. Initial working version.
 
 
 
 	The MIT License (MIT)
 
 	Copyright (c) <2014> <Zhiyang Ong>
 
 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""


#	Import packages and functions from the Python Standard Library.
import os.path, string, sys
from os.path import isfile
from os import remove
from string import find
#from tempfile import mkstemp
from shutil import move
#import codecs

#	Import my Python modules
from cons_tuple import cons_tuple


#	============================================================

#	Preliminaries: Set up the file objects/streams for processing.

#	Filename for input test file.
ip_file = "input-file.txt"
#	Path of input test file.
ip_fname = os.path.abspath(ip_file)
#	Is the specified input test file a valid file?
if not(isfile(ip_fname)):
	#	No. Raise an Error (i.e., Exception).
	print "==	Path to input file is:::" + ip_fname
	raise IOError("Input File does NOT exists.")
#	Create separate input and output file objects
ip_f_obj = open(ip_fname, "r");
#	Filename for output test file.
op_file = "output-file.txt"
op_f_obj = open(op_file, "w");

#	============================================================

#	Lists to generate data for the input test file.
#	List of universities that are good in EDA.
universities = ["Berkeley", "Stanford", "MIT", "UT Austin", "Carnegie Mellon", "Georgia Tech", "Columbia", "Northwestern", "Purdue", "UCSD", "UCLA"]
#	List of other universities in EDA.
other_unis = ["UIUC", "Brown", "Boston University", "UC Irvine", "UC Riverside", "UCSB", "USC", "University of Minnesota at Twin Cities", "Utah", "University of Wisconsin-Madison"]
#	List of VLSI topics.
vlsi_topics = ["RTL design", "TLM design", "processor design", "SRAM design", "DRAM design", "low-power VLSI design", "decoder design", "DFM", "VLSI verification", "VLSI design flow", "NoC", "asynchronous VLSI design", "VLSI architecture", "digitally-assisted analog IC design", "VLSI signal processing", "microarchitecture"]
#	List of EDA topics.
eda_topics = ["model checking", "equivalence checking", "high-level synthesis", "hardware/software partitioning", "hardware-accelerated emulation", "logic synthesis", "RTL synthesis", "static timing analysis", "statistical STA", "power optimization", "DVFS", "logic simulation", "fault saimulation", "ATPG", "DFT", "BIST", "memory compiler", "gate sizing", "threshold voltage assignment", "buffer insertion", "crosstalk analysis", "signal integrity analysis", "noise analysis", "thermal analysis", "floorplanning", "partitioning", "detailed placement", "detailed routing", "global placement", "global routing", "clock network synthesis", "power and ground routing", "layout compaction", "layout extraction", "parasitic extraction", "interconnect modeling", "design rule check", "layout versus schematic check", "electric rule check", "computational lithography", "optical proximity correction", "resolution enhancement technologies", "mask data preparation", "circuit simulation"]
#	Lists of numbers to be fixed.
list_of_hundreds = range(1500, 5000, 100)
list_of_10s = range(1234560, 1234767, 10)
#	References:
#	http://eecs_ece-and-cs.quora.com/Choosing-a-Graduate-Program-in-VLSI-Design-Related-Areas-Things-to-Consider
#	http://www.quora.com/What-are-the-best-VLSI-CAD-research-groups-in-US-universities

#	Write text to the input test file.
#f_object.write("Ciao Mondo")

#	Pointer to currently enumerated index of EDA topics.
ptr = 0

#	============================================================

"""
#	Experiments with "cons".
print "car is:%s" % ct.get_car()
print "cdr is:%s" % ct.get_cdr()
"""

#	Create a list of cons to store (original, updated) value pairs.
#list_cons = [cons_tuple("Stanford", "UIUC")]
ct = cons_tuple("Stanford", "UIUC")
list_cons = [cons_tuple("Stanford", "UIUC"), cons_tuple("Georgia Tech", "Utah"), cons_tuple("hardware-accelerated emulation", "resolution enhancement technologies"), cons_tuple("statistical STA", "interconnect modeling")]


#	============================================================

"""
for ln_num, cur_ln in enumerate(f_object):
	#print "<<		Currently enumerated line:" + cur_ln[ln_num]
	#print "<<		Currently enumerated line:" + str(ln_num)
	print "<<		Currently enumerated line:" + str(cur_ln)
	#if "Stanford" in ln:
	#if str(ln).find("Stanford"):
	#if str(cur_ln).find('Stanford'):
	if -1 < string.find(str(cur_ln),'Stanford'):
		print ">>	String with the term, Stanford, is found!"
		#str(cur_ln).replace("Stanford", "UCSB")
		#cur_ln.replace("Stanford", "UCSB")
		string.replace(str(cur_ln),"Stanford", "UCSB")
		#string.replace(cur_ln,"Stanford", "UCSB")
		#cur_ln[ln_num] = str(cur_ln)
		print "<<		Modified line:" + str(cur_ln)
"""
#print ">	Entering the FOR loop:"+str(ip_f_obj)
#lines = ip_f_obj.readline()

"""
if ip_f_obj is not None:
	print "ip_f_obj is NULL."
if lines is not None:
	print "lines is NULL."
if op_f_obj is not None:
	print "op_f_obj is NULL."
"""

#	Enumerate all lines of the input text file.
for ln_num, cur_ln in enumerate(ip_f_obj):
	print "<<		Currently enumerated line:" + cur_ln
	"""
	if -1 < string.find(cur_ln,'Stanford'):
		print ">>	String with the term, Stanford, is found!"
		string.replace(cur_ln,"Stanford", "UCSB")
		print "<<		Modified line:" + cur_ln
	"""
	temp_str = cur_ln
	#	Enumerate all cons_tuples.
	for c_instance in list_cons:
		if -1 < string.find(temp_str, c_instance.get_car()):
			print ">>	String with the term, "+c_instance.get_car()+", is found!"
			temp_str = string.replace(temp_str,c_instance.get_car(), c_instance.get_cdr())
			print "<<		Modified line:" + temp_str
	op_f_obj.write(temp_str)
	
	


#	============================================================
#	Close the input and output file objects.
ip_f_obj.close()
op_f_obj.close()
#move(op_file,ip_file)

#	============================================================
print ">>>	End of program.		<<<"


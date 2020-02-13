#!/usr/bin/python

"""
	This is written by Zhiyang Ong to modify text (non-binary) files.
 
	Synopsis:
	Script to modify text (non-binary) files.
	

 Revision History:
 1) November 11, 2014. Initial working version.
 
 
 
 	The MIT License (MIT)
 
 	Copyright (c) <2014> <Zhiyang Ong>
 
 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""

#	Import packages and functions from the Python Standard Library.
#from os import listdir, system
from os import system
#from os.path import isfile, join, splitext
#from os.subprocess import call
#import subprocess

#	============================================================

"""
	Create an output file object.
	
	Assume that the specified filename does not belong to an important file.
	Assume that the specified file can be overwritten.
"""
f_object = open("input-file.txt", "w");


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

#	Generate test data for the test input file.

#	Enumerate all universities that are good in EDA.
for gd_uni in universities:
	#temp_str = "%S %S %S", gd_uni, eda_topics[ptr], eda_topics[ptr+1]
	temp_str = gd_uni + "; " + str(list_of_hundreds[ptr]) + "; " + eda_topics[ptr]
	ptr = ptr + 1
	temp_str = temp_str + "; " + str(list_of_10s[ptr]) + "; " + eda_topics[ptr] + ".\n"
	if ptr < len(universities):
		ptr = ptr + 1
	f_object.write(temp_str)
	


temp_str = "Stanford" + "; " + "326748027" + "; " + "statistical STA"
temp_str = temp_str + "; " + "7289" + "; " + "hardware-accelerated emulation" + ".\n"
f_object.write(temp_str)
#	============================================================
#	Close the file object
f_object.close()


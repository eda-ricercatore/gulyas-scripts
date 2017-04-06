#!/usr/bin/python


"""
	This is written by Zhiyang Ong to store information as a cons.
	A cons is a 2-tuple, or double, that has a "left"/first element,
		car, and a "right"/second element, cdr.
	This class provides accessor and mutator functions to the
		elements of the cons.
 
	Synopsis:
	Class to contain 2 values as a cons.
	

	Revision History:
	1)	November 12, 2014. Initial working version.
 
 
 
 	The MIT License (MIT)
 
 	Copyright (c) <2014> <Zhiyang Ong>
 
 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""

#	==================================================================

#	Class definition.
class cons_tuple:

	#	Standard constructor
	def __init__(self,car_ip, cdr_ip):
		self.car = car_ip
		self.cdr = cdr_ip

	
	
	#	--------------------------------------------------------------
	
	#	Accessor methods.
	
	"""
		Function to access the "car" element of this instances of cons.
		@param - None.
		@return - The "car" element.
	"""
	def get_car(self):
		return self.car
	
	"""
		Function to access the "cdr" element of this instances of cons.
		@param - None.
		@return - The "cdr" element.
	"""
	def get_cdr(self):
		return self.cdr
	
	#	--------------------------------------------------------------
	
	#	Mutator methods.
	
	"""
		Function to set/modify the "car" element of this instances of cons.
		@param car_ip - The new value for car.
		@return - The "car" element.
	"""
	def set_car(car_ip):
		self.car = car_ip
	
	
	"""
		Function to set/modify the "cdr" element of this instances of cons.
		@param cdr_ip - The new value for cdr.
		@return - The "cdr" element.
	"""
	def set_cdr(cdr_ip):
		self.cdr = cdr_ip
	
	








#list_of_pairs = dict([('Stanford','UCSB'),('UT Austin','Utah'),('Georgia Tech','UIUC')])

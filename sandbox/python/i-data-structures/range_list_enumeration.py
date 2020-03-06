#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to test concepts with enumerating
		a list using the range() function.
"""

print("======================================")
print("=	Start Here	=")


#	============================================================
"""
	Beginning from this portion, we examine list generation to create
		an ascending list of powers of two (or any other base number).
"""
print("")
print("+++	Create an ascending list of powers of two.")


for i in range(10):
	print("The index is:",i,"=")

print("======================================")
for i in [8,16,32,64,128,256,512,1024]:
	print("Current power of 2 is:",i,"=")


print("======================================")

"""
	Reference:
	+ Matt Gilson, Answer to "How to return a list of numbers of the
		power of 2?", Stack Exchange Inc., New York, NY, June 23, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
			at: https://stackoverflow.com/a/13354695/1531728 and
			https://stackoverflow.com/questions/13354685/how-to-return-a-list-of-numbers-of-the-power-of-2/13354695#13354695;
			March 3, 2020 was the last accessed date.
	+ karakfa, Answer to "List comprehension of powers of 2 in Python
		fails with numpy array," Stack Exchange Inc., New York, NY,
		February 17, 2020.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/48843178/1531728 and
			https://stackoverflow.com/questions/48843102/list-comprehension-of-powers-of-2-in-python-fails-with-numpy-array/48843178#48843178;
			March 3, 2020 was the last accessed date.
	+ endolith, Answer to "For loop iterate over powers of 2,"
		Stack Exchange Inc., New York, NY, June 23, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
			at: https://stackoverflow.com/a/37980195/1531728 and
			https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37980195#37980195;
			March 3, 2020 was the last accessed date.
	+ Jorick Spitzen, Answer to "Raising elements of a list to a power,"
		Stack Exchange Inc., New York, NY, May 19, 2015.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/30323523/1531728 and
			https://stackoverflow.com/questions/30323439/raising-elements-of-a-list-to-a-power/30323523#30323523;
			March 3, 2020 was the last accessed date.
	+ \cite[from Section 6 "Expressions", and subsection 6.5 "The power operator"]{DrakeJr2016a}
		- Reference for the "**" power operator.
		- That is, x**y = $x^{y}$ in LaTeX.
"""

powers_of_two = [ 2**power for power in range(3,10+1)]

for i in powers_of_two:
	print("> Currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

for i in [ 2**power for power in range(3,10+1)]:
	print("= Currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

"""
	This solution is acceptable, since I can customize this in a
		function call using variables.
"""
start_point = 3
end_point = 10
for i in [ 2**power for power in range(start_point,end_point+1)]:
	print("using, variables, currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

"""
	TO-DO!!! TO BE COMPLETED!!!
	+ Implement and test this in the miscellaneous module of the
		utilities package of my boilerplate code.

	This solution is acceptable, since I can customize this in a
		function call using variables.

	The left shift operation should be faster than the pow() function
		to determine the value of 2^n, for "n" ranges from "start_point"
		to "end_point".

	Reference for using the left shift operation instead of the pow()
		function to determine the value of 2^n, for "n" ranges from
		start_point to end_point:
	+ Robert Olveira, Answer to "How to return a list of numbers of the
		power of 2?", Stack Exchange Inc., New York, NY, August 28, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/41462973/1531728 and
			https://stackoverflow.com/questions/13354685/how-to-return-a-list-of-numbers-of-the-power-of-2/41462973#41462973;
			March 3, 2020 was the last accessed date.
"""

for i in [1 << i for i in range(start_point, end_point+1)]:
	print("Shifted 2's power of i is:",i,"=")


print("======================================")


"""
	Reference:
	endolith, Answer to "For loop iterate over powers of 2,"
		Stack Exchange Inc., New York, NY, June 23, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/37980195/1531728 and
			https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37980195#37980195;
			March 3, 2020 was the last accessed date.
"""

from itertools import count, takewhile
for x in takewhile(lambda x: x <= 1024, (2**p for p in count(1))):
    print("x via functional programming is:",x,"=")


print("======================================")

"""
	Reference:
	+ AndrewSmiley, Answer to "For loop iterate over powers of 2," Stack Exchange Inc., New York, NY, June 20, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/37930871/1531728 and https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37930871#37930871;
			March 3, 2020 was the last accessed date.
	+ \cite[from section "Numeric and Mathematical Modules", subsection
		"math — Mathematical functions"]{DrakeJr2016b}
		- Available online from Python: The Python Standard Library:
			Numeric and Mathematical Modules: math — Mathematical functions at:
			https://docs.python.org/3/library/math.html#math.pow; March 2, 2020 was the last accessed date.
		- Also, see:
			* https://www.tutorialspoint.com/python/number_pow.htm
			* https://www.w3schools.com/python/ref_func_pow.asp
			* https://www.geeksforgeeks.org/pow-in-python/
"""

from math import log
from math import pow
import sys
#for i in map(lambda v : pow(2,v), range(0,int(log(sys.maxint, 2)))):
for i in map(lambda v : pow(2,v), range(0,int(log(sys.maxsize, 2)))):
	print("Power of two till log(sys.maxint, 2) is:",i,"=")



print("======================================")

"""
	Reference:
	Robert Calhoun, Answer to "For loop iterate over powers of 2,"
		Stack Exchange Inc., New York, NY, July 8, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/44988925/1531728 and
			https://stackoverflow.com/questions/30323439/raising-elements-of-a-list-to-a-power/44988925#44988925;
			March 3, 2020 was the last accessed date.
"""

numbers=[1,2,3,4]
powers_of_two=list(map(lambda x:pow(2,x),numbers))
print("powers_of_two are:",powers_of_two,"=")


print("- - - - - - - - - - - - - - - - - - -")

"""
	Reference:
	+ \cite{ParewaLabsStaff20XYd}
		- Parewa Labs staff, "Python Program To Display Powers of 2 Using
			Anonymous Function," from Programiz - Learn to Code for Free:
			Learn Python Programming: Python Examples, Parewa Labs Pvt. Ltd.,
			Kupondole, Lalitpur District, Province No. 3, Nepal, no date.
			Available online from Programiz - Learn to Code for Free:
				Learn Python Programming: Python Examples at:
				https://www.programiz.com/python-programming/examples/power-anonymous;
				March 3, 2020 was the last accessed date.
"""

"""
	range(10+1)
	=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	=> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
"""
powers_of_two=list(map(lambda x:pow(2,x),range(10+1)))
print("> powers_of_two are:",powers_of_two,"=")
"""
	range(1,10+1)
	=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	=> [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
"""
powers_of_two=list(map(lambda x:pow(2,x),range(1,10+1)))
print(">> powers_of_two are:",powers_of_two,"=")


print("======================================")


"""
	Reference:
	+ Tommy Carstensen, "Raising elements of a list to a power",
		Stack Exchange Inc., New York, NY, May 23, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/30324778/1531728 and https://stackoverflow.com/questions/30323439/raising-elements-of-a-list-to-a-power/30324778#30324778;
			March 3, 2020 was the last accessed date.
"""

import functools
bases = numbers = [1,2,3]
power = exponent = 3
cubed = list(map(functools.partial(pow, exponent), numbers))
print("cubed is:",cubed,"=")

print("======================================")

"""
	\cite["numpy.power", from section Routines, subsection (and subsubsection) Mathematical functions: Arithmetic operations]{TheSciPyCommunity2019c}
"""

import numpy as np
x1 = range(1,10+1)
x2 = np.power(2, x1)
print("x2 is:",x2,"=")
for index in x2:
	print("array element is:",index,"=")

#	==========================================================

"""
	Beginning from this portion, we examine list generation to create
		a list of ascending floating-point numbers with fixed increments.
"""

print("======================================")

print("")
print("+++	Create a list of ascending floating-point numbers with fixed increments.")

"""
	References for using the np.linspace() and np.arange() functions
		to generate a list of ascending floating-point numbers with
		fixed increments.


	Andrew Jaffe and Peter Mortensen and Cesar and
		"user2357112 supports Monica" and Brian Burns, Answer to
		"How to use a decimal range() step value?", Stack Exchange Inc.,
		New York, NY, February 10, 2020.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
			https://stackoverflow.com/a/477635/1531728 and
			https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/477635#477635;
			March 4, 2020 was the last accessed date.		
"""
import numpy as np

a = np.linspace(0.0,1.0,11)
print("np.linspace(0,1,11) is:",a,"=")
a = np.linspace(4.0,5.0,10,endpoint=False)
print("np.linspace(0,1,10,endpoint=False) - without endpoints - is:",a,"=")
print("- - - - - - - - - - - - - - - - - - -")
a = np.arange(3.5, 5.5, 0.25)
print("np.arange(3.5, 5.5, 0.25) is:",a,"=")
a = np.arange(3.5, 6.0, 0.25)
print("np.arange(3.5, 6.0, 0.25) is:",a,"=")
a = np.arange(3.5, 6.0, 0.25, list)
print("np.arange(3.5, 6.0, 0.25, list) is:",a,"=")
"""
	The following does not work:
[a] = np.arange(3.5, 6.0, 0.25)
print("[np.arange(3.5, 6.0, 0.25)] is:",a,"=")
"""


"""
	This returns a list containing the array() method call, instead of
		a NumPy array that can be transformed into a list.
	Hence, do not use this method.
"""
a = [np.arange(3.5, 6.0, 0.25)]
print("[np.arange(3.5, 6.0, 0.25)] is:",a,"=")

"""
	Convert the NumPy array into a (Python) list.
	This makes the NumPy.arrange() solution acceptable.

	Reference:
	+ user3654478, Answer to "How to use a decimal range() step value?,"
		Stack Exchange Inc., New York, NY, February 12, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
			at: https://stackoverflow.com/a/35362489/1531728 and
			https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/35362489#35362489;
			March 4, 2020 was the last accessed date.
"""
a = np.arange(3.5, 6.0, 0.25).tolist()
print("np.arange(3.5, 6.0, 0.25).tolist() is:",a,"=")
start_point = 4.5
end_point = 7.0
increments = 0.25
a = np.arange(start_point, end_point+increments, increments).tolist()
print("np.arange(start_point, end_point, increments).tolist() is:",a,"=")

print("======================================")

"""
	Reference:
	+ user25148, Answer to "How to use a decimal range() step value?,"
		Stack Exchange Inc., New York, NY, January 25, 2009.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
		at: https://stackoverflow.com/a/477513/1531728 and
		https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/477513#477513;
		March 4, 2020 was the last accessed date.
"""


"""
	Use 0.25 as the scaling factor, since range(0, 10) produces a list
		of integers.
"""
a = [3.5+0.25*x for x in range(0, 10)]
print("[3.5+0.25*x for x in range(0, 10)] is:",a,"=")
#a = [start_point+increments*x for x in range(0, 10)]
#print("[start_point+increments*x for x in range(0, 10)] is:",a,"=")







print("- - - - - - - - - - - - - - - - - - -")

"""
	TO-DO!!! TO BE COMPLETED!!!
	Implement this and test it.

	This solution is acceptable, since I can customize this in a
		function call using variables.
	It is easier to handle floating-point increments that use a
		multiplicative scale factor.
"""
bias = 4.5
scaling_factor = 0.25
start_point = 0
end_point = 10
a = [bias+scaling_factor*x for x in range(start_point, end_point+1)]
print("[bias+scaling_factor*x for x in range(start_point, end_point+1)] is:",a,"=")

print("======================================")



"""
	This solution is acceptable, since I can customize this in a
		function call using variables.
	Modified to handle floating-point increments that use a reciprocal
		scale factor or multiplicative inverse .


	cmsjr and Peter Mortensen, Answer to "How to use a decimal range()
		step value?," Stack Exchange Inc., New York, NY, February 1, 2015.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/477506/1531728 and
			https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/477506#477506;
			March 4, 2020 was the last accessed date.
"""
for i in range(0, 100, 10):
	print("for range(0, 100, 10), i/100.0 is:",i/100.0,"=")
print("- - - - - - - - - - - - - - - - - - -")
for i in range(0, 20, 2):
	print("for range(0, 20, 2), i/10.0 is:",i/10.0,"=")
print("- - - - - - - - - - - - - - - - - - -")
start_point = 0
end_point = 30
increments = 3
bias = 9
scale_factor = 10.0
a = [bias+i/scale_factor for i in range(start_point, end_point+1, increments)]
print("A list for bias+i/scale_factor is:",a,"=")






print("======================================")

"""
	Reference:
	+ Eric Myers, Answer to "How to use a decimal range() step value?",
		Stack Exchange Inc., New York, NY, February 16, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/42283283/1531728 and
			https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/42283283#42283283;
			March 4, 2020 was the last accessed date.
"""

dt = 0.2
#xdt = 12.5
t_max = 14
def xdt(n):
	return dt*float(n)
tlist  = map(xdt, range(int(t_max/dt)+1))
"""
	Reference to convert a map object to a list object in Python:
	+ Triptych, Answer to "TITLE," Stack Exchange Inc., New York, NY, MONTH DAY, YEAR.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at: URL; March 4, 2020 was the last accessed date.
"""
tlist_list = list(tlist)
print("tlist_list is:",tlist_list,"=")
print("- - - - - - - - - - - - - - - - - - -")
a = [dt*round(i/dt) for i in tlist_list]
print("dt*round(i/dt) for i in tlist is:",a,"=")
# The following does not work.
#tlist_list = [*tlist]
"""
	References to convert a map object to a list in Python:
	+ Israel Unterman, Answer to "Getting a map() to return a list in
		Python 3.x", Stack Exchange Inc., New York, NY, October 28, 2018.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/38702484/1531728 and
			https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x/38702484#38702484;
			March 4, 2020 was the last accessed date.
	+ Joshua Landau, Neil Girdhar, and Thomas Wouters, "Additional Unpacking Generalizations" as PEP 448,
		from Python: Python Developer's Guide: PEP 0 -- Index of Python
		Enhancement Proposals (PEPs), June 29, 2013.
		Available online from Python: Python Developer's Guide:
			PEP 0 -- Index of Python Enhancement Proposals (PEPs) as
			PEP 448 at: https://www.python.org/dev/peps/pep-0448/;
			March 4, 2020 was the last accessed date.
		- Elvis Pranskevichus and Yury Selivanov, "What’s New In Python 3.5",
			from Python: Python 3.8.2 documentation: What’s New in Python,
			Python Software Foundation, Wilmington, DE, September 13, 2015.
			Also available from Python: Python 3.8.2 documentation:
				What’s New in Python: What’s New In Python 3.5 at:
				https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-448;
				March 4, 2020 was the last accessed date.
"""
print("- - - - - - - - - - - - - - - - - - -")
tlist_list = [*map(xdt, range(int(t_max/dt)+1))]
print("tlist_list via [*tlist] is:",tlist_list,"=")



print("======================================")

"""
	Solution requires downloading the source code as a Python script
		from the following reference.

	Reference:
	+ Andrew Barnert, "Equally-spaced Numbers (linspace) (Python Recipe)"
		from ActiveState: ActiveState Code: Recipes,
		ActiveState Software Inc., Vancouver, British Columbia, Canada,
		January 12, 2015.
		Available online from at: https://www.python.org/dev/peps/pep-0448/;
			March 4, 2020 was the last accessed date.
"""

"""
print(linspace(0, 10, 5))
# linspace(0, 10, 5)
print(list(linspace(0, 10, 5)))
# [0.0, 2.5, 5.0, 7.5, 10]
"""


#	======================================
#print("======================================")


"""
	Added round() function to make the minor incremental floating-point
		errors negligible.
		This has no effect, and I am commenting out this option/modification.


	Reference:
	+ Santoso Wijaya ("Santa"), Answer to "How do get more control over
		loop increments in Python?", Stack Exchange Inc., New York, NY,
		February 8, 2011.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
			at: https://stackoverflow.com/a/4930482/1531728 and
			https://stackoverflow.com/questions/4930404/how-do-get-more-control-over-loop-increments-in-python/4930482#4930482;
			March 4, 2020 was the last accessed date.
"""
#for i in [6+round(float(j)) / 100 for j in range(0, 100, 5)]:
for i in [6+float(j) / 100 for j in range(0, 100, 5)]:
	print("i is:",i,"=")









print("======================================")


"""
	Alternatives:
	+ https://pypi.org/project/Franges/0.1.0/
	+ https://stackoverflow.com/questions/33257635/python-round-to-nearest-0-25
	

	References for Python rounding errors. such as 0.250000000002
		approximately equals 0.25 (or 0.250).
	+ https://mail.python.org/pipermail/python-list/2001-December/115350.html
	+ https://mail.python.org/pipermail/python-list/2001-December/071437.html
"""













print("=	End Here	=")
#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to test concepts with enumerating
		a list using the range() function.
"""

print("======================================")
print("=	Start Here	=")
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
	print("Currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

for i in [ 2**power for power in range(3,10+1)]:
	print("Currently enumerated power of 2 is:",i,"=")


print("- - - - - - - - - - - - - - - - - - -")

"""
	Robert Olveira, Answer to "How to return a list of numbers of the
		power of 2?", Stack Exchange Inc., New York, NY, August 28, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/41462973/1531728 and
			https://stackoverflow.com/questions/13354685/how-to-return-a-list-of-numbers-of-the-power-of-2/41462973#41462973;
			March 3, 2020 was the last accessed date.
"""

for i in [1 << i for i in range(10+1)]:
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
"""
	range(1,10+1)
	=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	=> [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
"""
powers_of_two=list(map(lambda x:pow(2,x),range(1,10+1)))
print("powers_of_two are:",powers_of_two,"=")


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


print("======================================")


"""
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
a = [np.arange(3.5, 6.0, 0.25)]
print("[np.arange(3.5, 6.0, 0.25)] is:",a,"=")
# Convert NumPy array into a (Python) list.
a = np.arange(3.5, 6.0, 0.25).tolist()
print("np.arange(3.5, 6.0, 0.25).tolist() is:",a,"=")


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
bias = 4.5
scaling_factor = 0.25
start_point = 0
end_point = 10
a = [bias+scaling_factor*x for x in range(0, 10)]
print("[bias+scaling_factor*x for x in range(0, 10)] is:",a,"=")

print("======================================")



"""
	cmsjr and Peter Mortensen, Answer to "How to use a decimal range()
		step value?," Stack Exchange Inc., New York, NY, February 1, 2015.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
		https://stackoverflow.com/a/477506/1531728 and
		https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/477506#477506;
		March 4, 2020 was the last accessed date.
"""
for i in range(0, 100, 10):
	print("for range(0, 100, 10), i/100.0 is:",i/100.0,"=")
print("- - - - - - - - - - - - - - - - - - -")
for i in range(0, 20, 2):
	print("for range(0, 20, 2), i/10.0 is:",i/10.0,"=")








print("======================================")
print("=	End Here	=")
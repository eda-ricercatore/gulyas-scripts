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
	AndrewSmiley, Answer to "For loop iterate over powers of 2," Stack Exchange Inc., New York, NY, June 20, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/37930871/1531728 and https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37930871#37930871;
			March 3, 2020 was the last accessed date.
"""

from math import log
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
squares=list(map(lambda x:pow(x,2),numbers))
print("squares are:",squares,"=")


print("- - - - - - - - - - - - - - - - - - -")

"""
	Reference:
	+ Parewa Labs staff, "Python Program To Display Powers of 2 Using
		Anonymous Function," from Programiz - Learn to Code for Free:
		Learn Python Programming: Python Examples, Parewa Labs Pvt. Ltd.,
		Kupondole, Lalitpur District, Province No. 3, Nepal, no date.
		Available online from Programiz - Learn to Code for Free:
			Learn Python Programming: Python Examples at:
			https://www.programiz.com/python-programming/examples/power-anonymous;
			March 3, 2020 was the last accessed date.
"""

squares=list(map(lambda x:pow(x,2),range(10+1)))
print("squares are:",squares,"=")


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
print("=	End Here	=")
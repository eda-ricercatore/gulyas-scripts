#!/usr/local/bin/python3

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
	+ karakfa, Answer to "TITLE," Stack Exchange Inc., New York, NY, MONTH DAY, YEAR.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/48843178/1531728 and https://stackoverflow.com/questions/48843102/list-comprehension-of-powers-of-2-in-python-fails-with-numpy-array/48843178#48843178;
			March 3, 2020 was the last accessed date.
	+ endolith, Answer to "For loop iterate over powers of 2," Stack Exchange Inc., New York, NY, June 23, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/37980195/1531728 and https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37980195#37980195;
			March 3, 2020 was the last accessed date.
"""

powers_of_two = [ 2**power for power in range(3,10+1)]

for i in powers_of_two:
	print("Currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

for i in [ 2**power for power in range(3,10+1)]:
	print("Currently enumerated power of 2 is:",i,"=")


print("======================================")


"""
	Reference:
	endolith, Answer to "For loop iterate over powers of 2," Stack Exchange Inc., New York, NY, June 23, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/37980195/1531728 and https://stackoverflow.com/questions/31872713/for-loop-iterate-over-powers-of-2/37980195#37980195;
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
for i in map(lambda v : pow(2,v), range(0,int(log(sys.maxint, 2)))):
    print("Power of two till log(sys.maxint, 2) is:",i,"=")




print("======================================")
print("=	End Here	=")
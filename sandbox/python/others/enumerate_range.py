#!/usr/local/bin/python3

print("======================================")
print("=	Start Here	=")
for i in range(10):
	print("The index is:",i,"=")

print("======================================")
for i in [8,16,32,64,128,256,512,1024]:
	print("Current power of 2 is:",i,"=")


print("======================================")

powers_of_two = [ 2**power for power in range(3,10+1)]

for i in powers_of_two:
	print("Currently enumerated power of 2 is:",i,"=")

print("- - - - - - - - - - - - - - - - - - -")

for i in [ 2**power for power in range(3,10+1)]:
	print("Currently enumerated power of 2 is:",i,"=")


print("======================================")

from itertools import count, takewhile
for x in takewhile(lambda x: x <= 1024, (2**p for p in count(1))):
    print("x via functional programming is:",x,"=")


print("======================================")

from math import log
import sys
for i in map(lambda v : pow(2,v), range(0,int(log(sys.maxint, 2)))):
    print("Power of two till log(sys.maxint, 2) is:",i,"=")




print("======================================")
print("=	End Here	=")
#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np

a = [int(i) for i in np.binary_repr(0b0111, 4)]
print("0b0111 is:",a,".")
a = [int(i) for i in np.binary_repr(0b000000111, 9)]
print("0b000000111 is:",a,".")
a = [int(i) for i in np.binary_repr(0b11010011, 4)]
print("0b11010011 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0100001, 7)]
print("0b0100001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0001, 4)]
print("0b0001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0000, 4)]
print("0b0000 is:",a,".")
a = [int(i) for i in np.binary_repr(0b1001, 4)]
print("0b1001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b10000000000, 11)]
print("0b10000000000 is:",a,".")
"""
print("--------------------------------------------------")
try:
	f = 0b834
except SyntaxError:
	print("A binary number, or integer in base 2, cannot contain numerical digits other than '0' and '1'.")
"""
print("--------------------------------------------------")
a = [int(i) for i in np.binary_repr(0b0111, 4)]
print("a is:",a,".")
aa = [int(i) for i in np.binary_repr(0b0111)]
print("aa is:",aa,".")
print("--------------------------------------------------")
b = "This is "
c = "a good way to benchmark circuits."
d = b+c
print("d is:",d,"=")
e = "This is a good way to benchmark circuits."
if e.find("benchmark"):
	print("Found benchmark.")
else:
	print("Benchmark is not found.")
print("--------------------------------------------------")
g = '%#o' % 10
print("g is:",g,"=")
h = '%o' % 10
print("h is:",h,"=")
i = format(10, '#o')
print("i is:",i,"=")
j = format(10, 'o')
print("j is:",j,"=")
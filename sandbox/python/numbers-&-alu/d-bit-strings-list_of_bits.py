#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3

import random
import numpy as np


#	This works!
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
	print("Even if I try to catch the 'SyntaxError' exception, it will still throw/raise the 'SyntaxError' exception.")
"""
print("--------------------------------------------------")
"""
	From \cite[SciPy.org: Numpy and Scipy Documentation: NumPy v1.17 Manual:
		NumPy Reference: Routines: Binary operations -- Output
		formatting]{Jones2018i}
	+ Updated NumPy Reference as Release 1.17, July 26, 2019.
	+ Available online from {SciPy.org}: {Numpy} and {Scipy} Documentation:
		{NumPy} v1.17 Manual: NumPy Reference: Routines: Binary
		operations -- Output formatting at: https://docs.scipy.org/doc/numpy/reference/generated/numpy.binary_repr.html;
		March 2, 2020 was the last accessed date
	+ If the optional "width" parameter that has been "[d]eprecated since
		version 1.12.0." is not provided, it will truncate the leading zero(s).
"""
a = [int(i) for i in np.binary_repr(0b0111, 4)]
print("a is:",a,".")
aa = [int(i) for i in np.binary_repr(0b0111)]
print("aa is:",aa,".")
print("--------------------------------------------------")
"""
	Use the "find()" method for the 'string' class to determine
		if a substring exists in a given/particular string.
"""
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
print("--------------------------------------------------")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 1",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 2",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 3",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 4",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 5",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 5",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 5",k,"=")
k = bin(random.getrandbits(7))
print("k = bin(random.getrandbits(n)) - 5",k,"=")
print("The bin(random.getrandbits(n)) method does not have 'n' bits for a n-bit binary string, since the leading zeros of the binary string are truncated.")
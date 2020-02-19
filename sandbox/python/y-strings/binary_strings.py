#!/Users/zhiyang/anaconda3/bin/python3


###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
"""
#import sys
import numpy as np



a = [int(i) for i in np.binary_repr(0b0111, 4)]
print("a is:",a,".")
b = "This is "
c = "a good way to benchmark circuits."
d = b+c
print("d is:",d,"=")
e = "This is a good way to benchmark circuits."
if e.find("benchmark"):
	print("Found benchmark.")
else:
	print("Benchmark is not found.")


bin_str = bin(83)
if isinstance(bin_str, str):
	print("bin_str is a string.")
else:
	print("bin_str is NOT a string!!!")
f = "{0:b}".format(7)
print("7 as a binary string:",f,"=")
g = "{0:8b}".format(7)
print("7 as an 8-bit binary string:",g,"=")
print("=	0-value bits are represented by character spaces, rather than 0-value bits.")
h = "{0:4b}".format(7)
print("7 as a 4-bit binary string:",h,"=")
try:
	bin_str = bin(7)
	j = [int(i) for i in np.binary_repr(bin_str, 5)]
	print("7 as a 5-bit binary string:",j,"=")
except TypeError:
	print("'bin()' method turns a number into a (binary) string, which cannot work with method.")


"""
	Reference:
	+ [noobar2017]
		- noobar, Answer to "Convert binary to list of digits Python",
			Stack Exchange Inc., New York, NY, March 14, 2017.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/42779009/1531728 and https://stackoverflow.com/questions/13081090/convert-binary-to-list-of-digits-python/42779009#42779009;
				February 18, 2020 was the last accessed date.
"""
a = [int(i) for i in np.binary_repr(0b011010101010, 12)]
print("a is:",a,".")
a = [int(i) for i in np.binary_repr(0b011010101010, 15)]
print("a is:",a,".")
try:
	a = [int(i) for i in np.binary_repr("9", 15)]
	print("a is:",a,".")
except TypeError:
	print("Cannot convert '9' to a list of 0-1 integers.")

try:
	a = [int(i) for i in np.binary_repr("1100", 15)]
	print("a is:",a,".")
except TypeError:
	print("Cannot convert '1100' to a list of 0-1 integers.")
# 1100 (in decimal) = 4+8+64+1024
a = [int(i) for i in np.binary_repr(1100, 15)]
print("a is:",a,".")
print("Converted number 1100 to a list of 0-1 integers.")
abb = 0b1100
if isinstance(abb, int):
	print("abb is an integer.")
else:
	print("abb is NOT an integer.")
ab = [int(i) for i in np.binary_repr(abb, 15)]
print("ab is:",ab,".")
print("Converted number 0b1100 to a list of 0-1 integers.")







try:
	bc = int(101011,2)
	print("= Can't event cast number into 'bc'")
	if 2 == bc.__index__():
		print("bc is a binary number.")
	else:
		print("bc is NOT a binary number!!!")
except TypeError:
	print("TypeError occurred. Primary/First input argument of int() has to be a string.")
# 1+2+8+32 = 43
bd = int("101011",2)
if 2 == bd.__index__():
	print("bd is a binary number.")
else:
	print("bd is NOT a binary number!!!")
	print("bd.__index__() is:",bd.__index__(),"=")


be = int("0b101011",2)
if 2 == be.__index__():
	print("be is a binary number.")
else:
	print("be is NOT a binary number!!!")
	print("be.__index__() is:",be.__index__(),"=")
bf = int(101011)


try:
	bg = int("7",2)
	if 2 == bg.__index__():
		print("bg is a binary number.")
	else:
		print("bg is NOT a binary number!!!")
		print("bf.__index__() is:",bg.__index__(),"=")
		print("bg is:",bg,"=")
except ValueError:
	print("ValueError! To express a number as a binary number, it has to be a string of '1's and '0's.")


try:
	ca = int("7",2)
	cb = int(101011,2)
	cc = int("101011",2)
	print("cc is:",cc,"=")
except ValueError:
	print("ValueError! Because of int('7',2).")
except TypeError:
	print("TypeError occurred. int(101011,2).")
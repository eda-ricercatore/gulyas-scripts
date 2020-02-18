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
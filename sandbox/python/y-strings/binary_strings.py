#!/Users/zhiyang/anaconda3/bin/python3


###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
"""
#import sys
import numpy as np


def binary_string_operations_1():
	a = [int(i) for i in np.binary_repr(0b0111, 4)]
	print("a is:",a,".")
	print("isinstance(a, str) is:",isinstance(a, list),"=")
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
		print("bin_str is a string:",bin_str,"=")
	else:
		print("bin_str is NOT a string!!!")
	f = "{0:b}".format(7)
	print("7 as a binary string:",f,"=")
	print("isinstance(f, str) is:",isinstance(f, str),"=")
	g = "{0:8b}".format(7)
	print("7 as an 8-bit binary string:",g,"=")
	print("isinstance(g, str) is:",isinstance(g, str),"=")
	print("=	0-value bits are represented by character spaces, rather than 0-value bits.")
	h = "{0:4b}".format(7)
	print("7 as a 4-bit binary string:",h,"=")
	print("isinstance(h, str) is:",isinstance(h, str),"=")
	try:
		bin_str = bin(7)
		j = [int(i) for i in np.binary_repr(bin_str, 5)]
		print("7 as a 5-bit binary string:",j,"=")
	except TypeError:
		print("'bin()' method turns a number into a (binary) string, which cannot work with method.")




def binary_string_operations_2():
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





def binary_string_operations_3():
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




def binary_string_operations_4():
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




def binary_string_operations_5():
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



def binary_string_operations_6():
	try:
		ca = int("7",2)
		cb = int(101011,2)
		cc = int("101011",2)
		print("cc is:",cc,"=")
	except ValueError:
		print("ValueError! Because of int('7',2).")
		try:
			cd = int(101011,2)
		except TypeError:
			print("TypeError occurred. int(101011,2) - 2.")
			ce = int("101011",2)
			print("ce is:",ce,"=")
	except TypeError:
		print("TypeError occurred. int(101011,2).")



def binary_string_operations_7():
	a = [int(i) for i in np.binary_repr(0b0111, 4)]
	print("a is:",a,".")
	aa = [int(i) for i in np.binary_repr(0b0111)]
	print("aa is:",aa,".")



def binary_string_operations_8():
	"""
		Integers cannot start with a zero.
		try-except block fails to work, since it causes an error with
			np.binary_repr(), prior to being used in int().
	"""
	try:
		#a = [int(i) for i in np.binary_repr(0111, 5)]
		#qwerty = np.binary_repr(0111, 5)
		qwerty = np.binary_repr(111, 5)
		print("qwerty is:",qwerty,".")
	except SyntaxError:
		a = [int(i) for i in np.binary_repr(111, 5)]
		print("a is:",a,".")



def binary_string_operations_9():
	# Integers cannot start with a zero.
	try:
		#a = 0836
		das = 4567
		print("das is:",das,".")
	except SyntaxError:
		a = 836
		print("a is:",a,".")







def binary_string_operations_10():
	dd1 = [int(i) for i in np.binary_repr(0b0111, 4)]
	print("dd1 is:",dd1,".")
	# Cannot assign a 0-begining integer value to a variable.
	#dd2 = [int(i) for i in np.binary_repr(0111, 4)]
	dd2 = [int(i) for i in np.binary_repr(9, 4)]
	print("dd2 is:",dd2,".")
	dd3 = [int(i) for i in np.binary_repr(9, 6)]
	print("dd3 is:",dd3,".")
	"""
		np.binary_repr() doesn't work for floating-point numbers.
	dd4 = [int(i) for i in np.binary_repr(1.25, 6)]
	"""
	dd4 = [int(i) for i in np.binary_repr(32, 6)]
	print("dd4 is:",dd4,".")




def binary_string_operations_11():
	ee = 0b0111
	ef = str(ee)
	print("ef is:",ef,"=")
	eg = bin(ee)
	print("eg is:",eg,"=")





def binary_string_operations_12():
	bin_str = bin(13)
	"""
		Turn binary string into an integer, in base 2, but stored
			as an integer in base 10 (decimal number).
	"""
	bin_str_as_int = int(bin_str,2)
	print("bin_str_as_int as:",bin_str_as_int,"=")














###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	binary_string_operations_1()
	binary_string_operations_2()
	binary_string_operations_3()
	binary_string_operations_4()
	binary_string_operations_5()
	binary_string_operations_6()
	binary_string_operations_7()
	binary_string_operations_8()
	binary_string_operations_9()
	binary_string_operations_10()
	binary_string_operations_11()
	binary_string_operations_12()
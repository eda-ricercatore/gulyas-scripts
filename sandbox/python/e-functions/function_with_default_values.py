#!/Users/zhiyang/anaconda3/bin/python3

"""
This Python script is written by Zhiyang Ong to try out ideas
	with Python functions that use default values for input
	arguments of the Python function.


References:
+ !!!Insert references!!!

Note:
+ I am writing this script from memory.
"""

def input_arguments_with_default_values(a=10,b=19,c=-8):
	return (a+b, a+c,b+c)




print("= Using default values.")
a_n_b, a_n_c, b_n_c = input_arguments_with_default_values()
print("	By default, a+b should be 29; it is:",a_n_b,"=")
print("	By default, a+c should be 2; it is:",a_n_c,"=")
print("	By default, b+c should be 11; it is:",b_n_c,"=")
if(29 == a_n_b and 2 == a_n_c and 11 == b_n_c):
	print("Test cases for default values:	Pass")
else:
	print("Test cases for default values:	Fail!!!")

print("= Using non-default values.")
a_n_b, a_n_c, b_n_c = input_arguments_with_default_values(4,6,-15)
print("	a+b should be 10; it is:",a_n_b,"=")
print("	a+c should be -11; it is:",a_n_c,"=")
print("	b+c should be -9; it is:",b_n_c,"=")
if(10 == a_n_b and -11 == a_n_c and -9 == b_n_c):
	print("Test cases for default values:	Pass")
else:
	print("Test cases for default values:	Fail!!!")








#!/Users/zhiyang/anaconda3/bin/python3


###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
"""
import sys

my_string = ""

if not my_string:
	print("my_string is empty:",my_string,"=")
else:
	print("The string is:",my_string,"=")

my_string = "Hello World"

if not my_string:
	print("my_string is empty:",my_string,"=")
else:
	print("The string is:",my_string,"=")

print("= length of input arguments to the program:",len(sys.argv),"=")
if 1 < len(sys.argv):
	print("the first argument is:",sys.argv[1],"=")

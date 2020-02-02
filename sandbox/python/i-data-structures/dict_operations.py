#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		a Python dictionary.
	
	References:
	+ See references cited in the source code.
"""


# ============================================================
# Import packages and modules from Python libraries.
import pandas as pd



# Create a dictionary of physical constants and their values.
dict_of_reference_values = {"c":299792458, "standard acceleration due to gravity":9.80665, "standard atmosphere":101325}

if 299792458 == dict_of_reference_values["c"]:
	print("'c' is: 299792458")
else:
	print("The value of 'c' cannot be accessed.")
	

if 9.80665 == dict_of_reference_values["standard acceleration due to gravity"]:
	print("'g' is: 9.80665")
else:
	print("The value of 'g' cannot be accessed.")

if 101325 == dict_of_reference_values["standard atmosphere"]:
	print("'std atm' is: 101325")
else:
	print("The value of 'std atm' cannot be accessed.")

try:
	unknown = dict_of_reference_values["random string"]
	print("unknown is:", unknown,".")
except KeyError:
	


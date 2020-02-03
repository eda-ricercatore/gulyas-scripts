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
print("The dictionary is:",dict_of_reference_values,".")

if 299792458 == dict_of_reference_values["c"]:
	print("'c' is: 299792458")
else:
	print("The value of 'c' cannot be accessed!!!")
	

if 9.80665 == dict_of_reference_values["standard acceleration due to gravity"]:
	print("'g' is: 9.80665")
else:
	print("The value of 'g' cannot be accessed!!!")

if 101325 == dict_of_reference_values["standard atmosphere"]:
	print("'std atm' is: 101325")
else:
	print("The value of 'std atm' cannot be accessed!!!")

if 101325 == dict_of_reference_values.get("standard atmosphere"):
	print("'std atm' via get() is: 101325")
else:
	print("The value of 'std atm' cannot be accessed via get()!!!")

try:
	unknown = dict_of_reference_values["random string"]
	print("unknown is:", unknown,".")
except KeyError:
	print("Accessing the dictionary with an invalid key.")


# Change 'g' to 9.81.
print("Changing the value associated with 'standard acceleration due to gravity'.")
dict_of_reference_values["standard acceleration due to gravity"] = 9.81
if 9.81 == dict_of_reference_values["standard acceleration due to gravity"]:
	print("	'g' is: 9.81")
else:
	print("The value of 'g'=9.81 cannot be accessed!!!")

print("Enumerating all key names in the dictionary.")
for x in dict_of_reference_values:
	print("	",x)
	
print("Enumerating all values in the dictionary.")
for x in dict_of_reference_values:
	print("	",dict_of_reference_values[x])

print("Enumerating all keys and values in the dictionary, using the items() function.")
for x, y in dict_of_reference_values.items():
	print("	", x, y)


if "standard acceleration due to gravity" in dict_of_reference_values:
	print("'g' is one of the keys in the dictionary.")

print("Number of elements in the dictionary is:", len(dict_of_reference_values),".")

print("Add a (key, value) pair = ('initial year', 2020) to the dictionary.")
dict_of_reference_values["initial year"] = 2020 
if 2020 == dict_of_reference_values["initial year"]:
	print("	'initial year' is: 2020.")
else:
	print("The value of 'initial year'=2020 cannot be accessed!!!")

print("Remove a (key, value) pair = ('g', 9.81) from the dictionary.")
dict_of_reference_values.pop("standard acceleration due to gravity")
try: 
	print(dict_of_reference_values["standard acceleration due to gravity"])
except KeyError:
	print("	The (key, value) pair = 'g'=9.81 is removed!!!")

print("Remove (from the dictionary) the most recent (key, value) pair added to the dictionary.")
dict_of_reference_values.popitem()
try: 
	print(dict_of_reference_values["initial year"])
except KeyError:
	print("	The (key, value) pair = 'initial year'=2020 is removed!!!")

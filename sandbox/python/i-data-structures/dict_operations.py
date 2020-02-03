#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		a Python dictionary.
	
	References:
	+ Refsnes Data staff, "Python Dictionaries", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/python_dictionaries.asp;
			February 3, 2020 was the last accessed date.
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
print("	Enumerate all key names in the dictionary again.")
x1 = dict_of_reference_values.values()
print(x1)


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
	print("	The (key, value) pair = 'g'=9.81 is removed.")

print("Remove (from the dictionary) the most recent (key, value) pair added to the dictionary.")
dict_of_reference_values.popitem()
try: 
	print(dict_of_reference_values["initial year"])
except KeyError:
	print("	The (key, value) pair = 'initial year'=2020 is removed.")

print("The dictionary is currently:",dict_of_reference_values,".")
print("Remove a (key, value) pair = ('c', 299792458) from the dictionary.")
del dict_of_reference_values["c"]
try: 
	print(dict_of_reference_values["c"])
except KeyError:
	print("	The (key, value) pair = 'c'=299792458 is removed.")
print("The dictionary is currently:",dict_of_reference_values,".")
print("Delete the dictionary.")
del dict_of_reference_values
try: 
	print("The dictionary is currently:",dict_of_reference_values,".")
except NameError:
	"""
		The variable 'dict_of_reference_values' is not 
	"""
	print("	The dictionary is deleted.")

print("Recreate the dictionary.")
dict_of_reference_values = {"c":299792458, "standard acceleration due to gravity":9.80665, "standard atmosphere":101325}
print("	The dictionary is:",dict_of_reference_values,".")
print("Clear the dictionary, by emptying its contents.")
dict_of_reference_values.clear()
print("	The empty dictionary is:",dict_of_reference_values,".")

print("Copy the dictionary to the variable 'a'.")
dict_of_reference_values = {"c":299792458, "standard acceleration due to gravity":9.80665, "standard atmosphere":101325}
a = dict_of_reference_values.copy()
print("	The dictionary 'a' is:",a,".")

print("Make another copy of the dictionary to the variable 'b'.")
b = dict(dict_of_reference_values)
print("	The dictionary 'b' is:",b,".")


print("Created nested dictionaries: a dictionary of dictionaries.")
myfamily = {
	"child1" : {
	"name" : "Emil",
	"year" : 2004
	},
	"child2" : {
	"name" : "Tobias",
	"year" : 2007
	},
	"child3" : {
	"name" : "Linus",
	"year" : 2011
	}
}
print("	Print nested dictionaries",myfamily,".")

print("Created another set of nested dictionaries: a dictionary of dictionaries.")
c1 = {
	"name" : "Emil",
	"year" : 2004
}
c2 = {
	"name" : "Tobias",
	"year" : 2007
}
c3 = {
	"name" : "Linus",
	"year" : 2011
}
mfamily = {
	"child-1" : c1,
	"child-2" : c2,
	"child-3" : c3
}
print("	Print other nested dictionaries",mfamily,".")

print("Create the dictionary using the standard constructor for dictionaries.")
a_dict = dict(c=299792458, standard_acceleration_due_to_gravity=9.80665, standard_atmosphere=101325)
print("	dictionary is:",a_dict,".")


print("Create a sample dictionary to test the update() method.")
car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
print("	Car is:",car,".")
print("	Update the sample dictionary using the update() method.")
car.update({"color": "White"})
print("	Updated car is:",car,".")

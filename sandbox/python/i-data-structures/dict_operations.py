#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		a Python dictionary.
	
	References:
	+ Refsnes Data staff, "Python Dictionaries", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/python_dictionaries.asp;
			February 3, 2020 was the last accessed date.
	+ Refsnes Data staff, "Python Dictionary values() Method", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/ref_dictionary_values.asp;
			February 3, 2020 was the last accessed date.
	+ Refsnes Data staff, "Python Dictionary keys() Method", from W3Schools Online Web Tutorials: Python Tutorial, Refsnes Data, no address, 2020.
		Available online from W3Schools Online Web Tutorials: Python Tutorial at:
			https://www.w3schools.com/python/ref_dictionary_keys.asp;
			February 3, 2020 was the last accessed date.
	+ \cite[Section/Chapter 5, Data Structures]{Brandl2017a}
	+ See references cited in the source code.
"""


# ============================================================
# Import packages and modules from Python libraries.
import pandas as pd


print("# ===================================================")
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
x1 = dict_of_reference_values.keys()
print("=	",x1)



print("Enumerating all values in the dictionary.")
for x in dict_of_reference_values:
	print("	",dict_of_reference_values[x])
print("	Enumerate all key names in the dictionary again.")
x2 = dict_of_reference_values.values()
print("=	",x2)


print("Enumerating all keys and values in the dictionary, using the items() function.")
for x, y in dict_of_reference_values.items():
	print("	:", x,"=&=", y,".")


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


print("Dictionary cannot be created with duplicate keys.")
"""
	Duplicate keys detected at run-time by the Python Virtual Machine,
		when the dict() constructor is used.
		This results in the following error:
			SyntaxError: keyword argument repeated.
	Keywords, or dictionary keys, cannot be expressions.
		Else, it will result in a SyntaxError, since the keyword
		wwcan't be an expression
	
"""
nba_team = dict(
		LA = "Lakers",
		#LA = "Clippers",
		Boston = "Celtics",
		Chicago = "Bulls",
		Utah = "Jazz"
	)
print("	The NBA teams are:",nba_team,"=")
nba_team = {
	"LA" : "Lakers",
	"LA" : "Clippers",
	"Boston" : "Celtics",
	"Chicago" : "Bulls",
	"Utah" : "Jazz"
	}
print("The NBA teams are:",nba_team,"=")
print("	The 2nd entry for LA overwrote the 1st entry.")
print("	For duplicate keys, the dict() constructor will throw a SyntaxError at run-time.")
print("	For duplicate keys, the {}-based dictionary constructor will overwrite the previous key-value mapping at run-time.")

"""
	The keys of the dictionary are treated as strings.
	Hence, I need to enclose these keys with double/single
		quotes, when using the "string" keys.
	Else, a NameError would result as follows:
		"NameError: name 'Boston' is not defined"
"""
#print("	Value of NBA team[Boston]=:",nba_team[Boston],"=")
print("	Value of NBA team['Boston']=:",nba_team["Boston"],"=")

kv_mapping = {
	6325532 : 0,
	5225421 : -23425,
	1252362 : 43,
	3745305 : 336466
	}
print("Dictionary with numerical keys and values:",kv_mapping,"=")
print("	Dictionaries declared and instantiated with numerical keys or string keys require the curly brackets, or (curly) braces, '{}' to avoid the following error: 'SyntaxError: keyword can't be an expression'")



ascending_order_kv_mapping = {
	1252362 : 43,
	3745305 : 336466,
	5225421 : -23425,
	6325532 : 0
	}
print("Ascending order dictionary with numerical keys and values:",ascending_order_kv_mapping,"=")

descending_order_kv_mapping = {
	6325532 : 0,
	5225421 : -23425,
	3745305 : 336466,
	1252362 : 43
	}
print("Descending order dictionary with numerical keys and values:",descending_order_kv_mapping,"=")
print("	Dictionaries are printed with their (key,value) pairs in the order of addition.")


empty_dict = {}
print("Print an empty dictionary:",empty_dict,"=")


"""
	From \cite{Sturtz2020}:
	Basic data types can be used as dictionary keys.
	They include:
	+ tuples
	+ integers
	+ floats
	+ strings
	+ boolean
	
	Hence, lists, dictionaries, and sets cannot serve as
		dictionary keys. 
"""
print("Dictionary keys have to belong to a basic data type.")
print("	Hence, immutable tuples (tuple is a basic data type) can be dictionary keys.")
my_dict_with_tuples = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print("	dictionary my_dict_with_tuples:",my_dict_with_tuples,".")
print("	Accessing dict[(1,1)]:",my_dict_with_tuples[(1,1)],".")
print("	Accessing dict[(2,1)]:",my_dict_with_tuples[(2,1)],".")


my_dict_with_floats = {2.3: 'a', 3.45: 'b', 6.78: 'c', 9.12: 'd'}
print("dictionary my_dict_with_tuples:",my_dict_with_floats,".")
print("	Accessing dict[3.45]:",my_dict_with_floats[3.45],".")

my_dict_with_bool = {True: "Ciao tutti!", False: "Buona serata!"}
print("dictionary my_dict_with_tuples:",my_dict_with_bool,".")
print("	Accessing dict[False]:",my_dict_with_bool[False],".")
print("	Accessing dict[3<5]:",my_dict_with_bool[3<5],".")

try:
	print("Creating a dictionary with lists as dictionary keys.")
	my_dict_with_lists = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
	print("	dictionary my_dict_with_lists:",my_dict_with_lists,".")
	print("	Accessing dict[[1,1]]:",my_dict_with_lists[(1,1)],".")
except TypeError:
	# TypeError: unhashable type: 'list'
	print("	Lists cannot be used as dictionary keys.")


try:
	print("Creating a dictionary with a dictionary as a dictionary key.")
	kb = { "Kobe Bryant": 24 }
	my_dict_with_dicts = { kb: 8 }
	print("	dictionary my_dict_with_dicts:",my_dict_with_dicts,".")
	print("	Accessing dict[kb]:",my_dict_with_dicts[kb],".")
except TypeError:
	# TypeError: unhashable type: 'dict'
	print("	Dictionaries cannot be used as dictionary keys.")





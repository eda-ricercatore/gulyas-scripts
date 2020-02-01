#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to scale
		a list by a scalar factor (or, scaling factor, or scale
		factor).
	
	References:
	+ See references cited in text.
"""


# ============================================================
# Import packages and modules from Python libraries.
import pandas as pd




"""
	range() method does not work as expected to produce a list.
	The range() method needs to be used within a loop.
	The range() method returns a range() object. 
"""
incremental_list = range(10)
print("incremental_list is:",incremental_list,".")
#scaled_incremental_list = incremental_list * 5

incre_list = []
for i in range(10):
	incre_list.append(i)
print("incre_list is:",incre_list,".")

scale_factor = 5

# List*n merely repeats the list "n" times.
scaled_incre_list = incre_list * scale_factor
print("scaled_incre_list is:",scaled_incre_list,".")

"""
	From https://stackoverflow.com/questions/26446338/how-to-multiply-all-integers-inside-list/26446349#comment41535602_26446349
	List comprehension results in faster operations
		than explicit "for" loops;
		last accessed January 17, 2020 at 15:34 U.S. CST.
	
	Reference:
	+ [2Ring2014]
		PM 2Ring, Comment about an answer to `How to multiply all integers inside list [duplicate]', Stack Exchange Inc., New York, NY, October 19, 2014.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/26446338/how-to-multiply-all-integers-inside-list/26446349#comment41535602_26446349 (or comment to the answer, https://stackoverflow.com/a/26446349/1531728); January 31, 2020 was the last accessed date.
"""
scaled_incre_list = [x * scale_factor for x in incre_list]
print("scaled_incre_list is:",scaled_incre_list,".")


scale_factor = 6
"""
	Use lambda function to obtain an object representing the list.
"""
scaled_incre_list = map(lambda x: x * scale_factor, incre_list)
print("scaled_incre_list is:",scaled_incre_list,".")
scaled_incre_list = list(scaled_incre_list)
print("scaled_incre_list is:",scaled_incre_list,".")


# https://stackoverflow.com/questions/26446338/how-to-multiply-all-integers-inside-list/26446349
def times_scale_factor(x):
	return x * scale_factor

# The map() function returns a sequence as an object.
scaled_incre_list = map(times_scale_factor, incre_list)
print("scaled_incre_list is:",scaled_incre_list,".")
# Cast the object from calling map() into a list. 
scaled_incre_list = list(scaled_incre_list)
print("scaled_incre_list is:",scaled_incre_list,".")



"""
	Resource for using functional programming to do this.
		https://stackoverflow.com/a/55491809/1531728
"""



scale_factor = 3
# Using Pandas
s = pd.Series(incre_list)
scaled_incre_list = (s*scale_factor).tolist()
print("scaled_incre_list is:",scaled_incre_list,".")

print("#	==============================================")

"""
	References:
	+ [Satyaprasad 2019]
		Sham Satyaprasad and Martijn Pieters, Answer to
			'Checking if type == list in python',
			Stack Exchange Inc., New York, NY, July 15, 2019.
			Available online from Stack Exchange Inc.:
				Stack Overflow: Questions at:
				https://stackoverflow.com/a/26544117/1531728;
				January 31, 2020 was the last accessed date.
	+ [Garg 20XY]
		Akshat Garg, "Python | Check if a given object is
			list or not", GeekstoGeeks, Noida, Uttar Pradesh,
			India, no date.
			Available online from Stack Exchange Inc.:
				Stack Overflow: Questions at:
				https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
				January 31, 2020 was the last accessed date.
"""

# From [Satyaprasad 2019] and [Garg 20XY].
print("= Check if an object is a list, via isinstance() method.")
a = [-221, 247, 0, 576372.32604]
if isinstance(a, list):
	print("=	a is a list.")
else:
	print("=	a is not a list.")
a = []
if isinstance(a, list):
	print("=	a is an empty list.")
else:
	print("=	a is not a list; a should be an empty list.")
a = None
if not isinstance(a, list):
	print("=	a is a None object!")
else:
	print("=	a is a list??? When it should be a None object.")
a = "dwefw"
if not isinstance(a, list):
	print("=	a is a string object!")
else:
	print("=	a is a list??? When it should be a string object.")
a = ""
if not isinstance(a, list):
	print("=	a is an empty string object!")
else:
	print("=	a is a list??? When it should be an empty string object.")


"""
	From [Garg 20XY]. This is a lousy method, and is not reliable.
	Avoid it.
	
	For more information and references, see:
	https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-classes
"""
print("= Check if an object is a list, via type() method \cite{Garg20XY}.")
a = [-221, 247, 0, 576372.32604]
if type(a) is list:
	print("=	a is a list.")
else:
	print("=	a is not a list.")
a = []
if type(a) is list:
	print("=	a is an empty list.")
else:
	print("=	a is not a list; a should be an empty list.")
a = None
if not type(a) is list:
	print("=	a is a None object!")
else:
	print("=	a is a list??? When it should be a None object.")
a = "dwefw"
if not type(a) is list:
	print("=	a is a string object!")
else:
	print("=	a is a list??? When it should be a string object.")
a = ""
if not type(a) is list:
	print("=	a is an empty string object!")
else:
	print("=	a is a list??? When it should be an empty string object.")


print("= Test if an object is a number object.")
print("isinstance(10, (int, float, complex):",isinstance(10, (int, float, complex)),".")
print("isinstance(float('NaN'), (int, float, complex)):",isinstance(float('NaN'), (int, float, complex)),".")
print("isinstance(float('nan'), (int, float, complex)):",isinstance(float('nan'), (int, float, complex)),".")
print("isinstance(float('inf'), (int, float, complex)):",isinstance(float('inf'), (int, float, complex)),".")
print("isinstance(float('-inf'), (int, float, complex)):",isinstance(float('-inf'), (int, float, complex)),".")
print("isinstance(True, (int, float, complex)) and not isinstance(True, bool):",isinstance(True, (int, float, complex)) and not isinstance(True, bool),".")
print("NaN, nan, inf, and -inf cannot be cast into integer objects.")
print("isinstance(complex('5-9j'), (int, float, complex)):",isinstance(complex('5-9j'), (int, float, complex)),".")
print("isinstance(complex('5-9j'), (int, float)):",isinstance(complex('5-9j'), (int, float)),".")

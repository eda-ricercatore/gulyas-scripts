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

print("--------------------------------------------------")
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
print("--------------------------------------------------")
b = [23, 34, 45, 56, 67, 78, 89]
c = [2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
d = [1.3, 2.4, 3.5, 4.6, 5.7, 6.8, 7.9]
for index, elem in enumerate(b):
	print("	index is:", index,"and elem is:", elem,"=")
print("--------------------------------------------------")
low_and_high_values = [(-1,0.5), (-1,1), (-0.5,0.5), (-0.5,1), (0,1)]
for elem in low_and_high_values:
	if isinstance(low_and_high_values, tuple):
		print("	elem is:",elem,"=")
	else:
		print("	elem is:",elem,"=. It is NOT a tuple!!!")
print("--------------------------------------------------")
"""
	References:
	+ url[section Built-in Functions]{DrakeJr2016b}
		- https://docs.python.org/3/library/functions.html#enumerate
		- Available online at: https://docs.python.org/3/library/functions.html#enumerate;
			February 24, 2020 was the last accessed date.
"""
for index, (car, cdr) in enumerate(low_and_high_values):
	if isinstance(low_and_high_values, tuple):
		print("	tuple index", index," (car",car," and cdr ",cdr,") is a tuple.")
	else:
		print("	tuple index", index," (car",car," and cdr ",cdr,") is NOT a tuple.")
print("--------------------------------------------------")
"""
	References:
	+ url[section Built-in Functions]{DrakeJr2016b}
		- https://docs.python.org/3/library/functions.html#enumerate
		- Available online at: https://docs.python.org/3/library/functions.html#enumerate;
			February 24, 2020 was the last accessed date.
"""
for index, cur_tuple in enumerate(low_and_high_values):
	if isinstance(low_and_high_values, tuple):
		print("	tuple index is", index," cur_tuple is",cur_tuple,"=")
	else:
		print("	tuple index is", index," cur_tuple is",cur_tuple,"=")
print("--------------------------------------------------")
"""
	Reference:
	+ [Shadowfax2016]
		- \cite{Shadowfax2016}
		- Sha{\d}o{\omega}fa{\chi}, Answer to "Iterate a list with indexes in Python",
		from Stack Exchange Inc.: Stack Overflow: Questions, Stack Exchange
		Inc., New York, NY, February 16, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/35429590 and https://stackoverflow.com/questions/126524/iterate-a-list-with-indexes-in-python/35429590#35429590;
			February 24, 2020 was the last accessed date.
"""
for i, (bi,ci,di) in enumerate(zip(b,c,d)):
	print("index", i, "elem 1:",bi, "elem 2:",ci, "elem 3:", di)
print("--------------------------------------------------")
embedded_lists = [[[[["embedded list"]]]]]
print("embedded_lists is:",embedded_lists,"=")
for index, cur_list in enumerate(embedded_lists):
	print("	index is:", index,"and currently enumerated list is:", cur_list,"=")
	for idx2, em_list2 in enumerate(cur_list):
		print("	idx2 is:", idx2,"and currently embedded2 list is:", em_list2,"=")
		for idx3, em_list3 in enumerate(em_list2):
			print("	idx3 is:", idx3,"and currently embedded3 list is:", em_list3,"=")
			for idx4, em_list4 in enumerate(em_list3):
				print("	idx4 is:", idx4,"and currently embedded4 list is:", em_list4,"=")
				for idx5, em_list5 in enumerate(em_list4):
					print("	idx5 is:", idx5,"and currently embedded5 list is:", em_list5,"=")
print("With embedded lists, I can define a list of a list of a list of a list...")
print("	Can't do that with embedded tuples.")


print("--------------------------------------------------")
"""
Reference:
+ https://stackoverflow.com/a/4406399/1531728 or https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension/4406399#4406399
	- user225312 and tscizzle, April 17, 2015
		Answer to "if else in a list comprehension [duplicate]"
		Last accessed August 25, 2020.
		April 17, 2015 (last date of edit)
	- user225312 and tscizzle, Answer to "if else in a list comprehension [duplicate]", Stack Exchange Inc., New York, NY, April 17, 2015. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/4406399/1531728 or https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension/4406399#4406399; March 7, 2020 was the last accessed date.
"""
list_1 = [22, 13, 45, 50, 98, 69, 43, 44, 1]
list_2 = [x+1 if x >= 45 else x+5 for x in list_1]
print(list_1)
print(list_2)
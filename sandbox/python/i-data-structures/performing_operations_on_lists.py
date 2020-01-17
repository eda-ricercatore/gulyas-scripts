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

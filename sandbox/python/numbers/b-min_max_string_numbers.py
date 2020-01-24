#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s



# Python code to illustrate  
"""
min()	built-in function to determine the minimum number of
			a list (of numbers).

max()	built-in function to determine the maximum number of
			a list (of numbers).
"""

# List of numbers 
a = [32, 236, 8, 329, 32677862485, 724, 32, 975]
print("list a is:",a,".")
print('minimum number of list a is:', min(a),".")
print('maximum number of list a is:', max(a),".")

"""
	Ways to generate a list of numbers
	
	References:
	+ 
"""

# Option 1: For loop
a = []
for i in range(3,9):
	a.append(i)
print("list a is:",a,".")

"""
	Option 2: list comprehension and range()
	
	References:
	+ https://docs.python.org/2.3/whatsnew/section-slices.html
		- A. M. Kuchling, "What's New in Python 2.3", as
			Release 1.01, from Python Documentation (Release 2.3.5),
			Python Software Foundation, Beaverton, OR,
			February 8, 2005.
			Available online at: https://docs.python.org/2.3/whatsnew/section-slices.html;
				January 24, 2020 was the last accessed date
		- [Kuchling 2005]
"""
a = [item for item in range(30)]
b = a[3:18:2]
print("list a is:",a,".")
print("list b is:",b,".")
# From [Kuchling 2005]
a = [i for i in range(30)[slice(3,18,2)]]
print("list a is:",a,", after slicing range().")

b = [i for i in range(11,20)]
print("list b is:",b,".")
c = [i for i in range(121,130)]
print("list c is:",c,".")
# Append the lists "b" and "c" together.
d = b + c
print("list d is:",d,".")




"""
	Option 3: list and range()
	
	References:
	+ https://docs.python.org/2.3/whatsnew/section-slices.html
		- A. M. Kuchling, "What's New in Python 2.3", as
			Release 1.01, from Python Documentation (Release 2.3.5),
			Python Software Foundation, Beaverton, OR,
			February 8, 2005.
			Available online at: https://docs.python.org/2.3/whatsnew/section-slices.html;
				January 24, 2020 was the last accessed date
		- [Kuchling 2005]
	+ https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
		- Smitha Dinesh Semwal and Manas Chhabra, "Create list of numbers with given range",
			from GeeksforGeeks, Noida, Uttar Pradesh, India, no date.
			Available from https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/;
				January 24, 2020 was the last accessed date.
"""
b = list(range(34,52))
print("list b is:",b,".")

"""
	Option 4: NumPy's arange()
	
	References:
	+ https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
		- Smitha Dinesh Semwal and Manas Chhabra, "Create list of numbers with given range",
			from GeeksforGeeks, Noida, Uttar Pradesh, India, no date.
			Available from https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/;
				January 24, 2020 was the last accessed date.
"""
b = np.arange(34,52)
print("list b is:",b,", NumPy's arange().")
print("b[4] is:",b[4],".")

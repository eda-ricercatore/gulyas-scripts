#!/usr/local/bin/python3



"""
	This is written by Zhiyang Ong to demonstrate how to scale
		a list by a scalar factor (or, scaling factor, or scale
		factor).
	
	References:
	+ See references cited in text.
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.


	Additional resources:
	+ https://runestone.academy/runestone/books/published/fopp/Sequences/SplitandJoin.html
	+ https://www.pitt.edu/~naraehan/python3/split_join.html
	+ https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php
	+ https://docs.python.org/3/reference/lexical_analysis.html#delimiters
"""

#	===================================================================

"""
	A string that I want to delimit and tokenize each full name into
		an element of a list.
"""
string_of_names = "Min Chen and Sergio Gonzalez and Athanasios Vasilakos and Huasong Cao and Victor C. M. Leung"


"""
	The following method works.

	Earlier problems in trying to get it to work resulted from treating
		the delimiter " = " as equivalent to " and ".
	I made this mistake when I was writing the program while being sleepy.




	
	References:
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.
"""
#list_of_names = string_of_names.split(' and ')
list_of_names = string_of_names.split(" and ")
print("list_of_names is:",list_of_names,"=")
print("string_of_names.split(' and ') is:",string_of_names.split(" and "),"=")

#	===================================================================


list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll"]

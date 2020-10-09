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
	+ Wikipedia contributors, ``Regular expression,'' in {\it Wikipedia, The Free Encyclopedia: Pattern matching}, Wikimedia Foundation, San Francisco, CA, Pattern matching 7, 2020.
Available online at: \url{https://en.wikipedia.org/wiki/Regular_expression}; last accessed on October 9, 2020.


context-free

	Additional resources:
	+ https://runestone.academy/runestone/books/published/fopp/Sequences/SplitandJoin.html
	+ https://www.pitt.edu/~naraehan/python3/split_join.html
	+ https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php
	+ https://docs.python.org/3/reference/lexical_analysis.html#delimiters
"""

# Import regular expressions package.
import re

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


list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam"]

"""
	My solution.

	Reference:
	+ https://docs.python.org/3/library/re.html
		Subsection: re — Regular expression operations
		Section: Text Processing Services
		Document: The Python Standard Library
		From: Python 3.9.0 documentation
"""
for current_name in list_of_names:
	print("Full name is:",current_name,"=")
	tokens = current_name.split(" ")
	tokens = re.split("\{??\}| ",current_name)
	for current_token in tokens:
		print("	current token is:",current_token,"=")


"""
	
	Reference:
	+ https://stackoverflow.com/a/58656637/1531728
		https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python/58656637#58656637
	+ https://stackoverflow.com/a/38999682/1531728
		https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python/38999682#38999682

"""
s = "name(something)"
na, so = re.match(r"(.*)\((.*)\)" ,s).groups()
print("na is:",na,"=")
print("so is:",so,"=")

for current_name in list_of_names:
	print("Full name is:",current_name,"=")
	#tokens = current_name.split(" ")
	#tokens = re.match(r'\((.*)\)',current_name).group(1)
	#tokens = re.match(r'\((.*)\)',current_name)
	#tokens = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2,tokens_3,tokens_4,tokens_5,tokens_6 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2,tokens_3 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens = re.match(r"(.*)\((.*)\)",current_name).groups()
	tokens = re.match(r"(.*)\((.*)\)",current_name)
	for current_token in tokens:
		print("	current token is:",current_token,"=")

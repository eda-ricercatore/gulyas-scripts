#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		Python sets.
	
	References:
	+  https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html   
		- 2015, Jakub Przywóski. Revision 9a3b94e7.
		- Section:Subsection
			* Comprehensions and Generator Expression: {} set comprehension
		- Title: Python Reference (The Right Way) - DRAFT
		- Jakub Przyw{\'{o}}ski, "\{\} set comprehension," in Python Reference (The Right Way) - {DRAFT}: Comprehensions and Generator Expression, Revision 9a3b94e7, Read the Docs, Inc., Portland, OR, 2015.
			Available online from {\it Read the Docs, Inc.} as Revision 9a3b94e7 at: \url{https://python-reference.readthedocs.io/en/latest/}; February 1, 2020 was the last accessed date
"""


# ============================================================
# Import packages and modules from Python libraries.
import pandas as pd



"""
	A Python object to test performing an addition operation
		between a Python object that is not a basic data type
		and a number.
"""
class my_object:
	property = 678


# Method implemented with set comprehension
"""
def remove_suffix(my_str,set_of_substr):
	return 
"""

###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	my_string = "This is an substring that I want to eliminate from my sentence."
	set_of_substrings = {"substring that I ", "to eliminate from", "non-existent"}
	"""
		Note that the order of elements in the set that selected for
			processing varies between execution of this Python script.
	"""
	for x in set_of_substrings:
		print("=	substring:",x)
		if x in my_string:
			print("substring exists in my_string.")
		else:
			print("substring is not found in my_string.")
		
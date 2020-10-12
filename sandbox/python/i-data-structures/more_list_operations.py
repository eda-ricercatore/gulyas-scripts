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
	+ Wikipedia contributors, ``Regular expression,'' in Wikipedia, The Free Encyclopedia: Pattern matching, Wikimedia Foundation, San Francisco, CA, Pattern matching 7, 2020. Available online at: https://en.wikipedia.org/wiki/Regular_expression; last accessed on October 9, 2020.
		- Regular expressions cannot process text that requires
			context-free grammar (CFG).
			* That is, it is based on regular grammar, rather than
				context-sensitive grammar (CSG).
	+ Wikipedia contributors, ``Parsing expression grammar,'' in Wikipedia, The Free Encyclopedia: Formal languages, Wikimedia Foundation, San Francisco, CA, September 21, 2020. Available online at: https://en.wikipedia.org/wiki/Parsing_expression_grammar; last accessed on October 9, 2020.
		- parsing expression grammar (PEG) is similar to
			context-free grammar (CFG), and cannot be ambiguous.



	Additional resources:
	+ https://runestone.academy/runestone/books/published/fopp/Sequences/SplitandJoin.html
	+ https://www.pitt.edu/~naraehan/python3/split_join.html
	+ https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php
	+ https://docs.python.org/3/reference/lexical_analysis.html#delimiters
	+ https://note.nkmk.me/en/python-split-rsplit-splitlines-re/
"""

# Import regular expressions package.
import re

print("=========================================================")

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

print("=========================================================")


list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam", "Albert-L{\'{a}}szl{\'{o}} Barab{\'{a}}si"]

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


"""
	From above:
	list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam"]
"""
for i in list_of_names:
	print("	current name is:",i,"=")
	list_of_tokens = re.match(r"(.*)\{(.*)\}| " ,s)
	#list_of_tokens = re.match(r"(.*){(.*)}| " ,s)
	print("	list_of_tokens is:",list_of_tokens,"=")

print("===	Test code on \{\}, instead of \(\) or ().")
list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric (von Hippel)", "Donata (von der Leyen)", "Wolff (van Sintern)", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam"]
for nn in list_of_names:
	print("	current name is:",nn,"=")
	"""
		The function re.match() will return a match object
			if the regular expression has matches in the given string. 
		+ https://docs.python.org/3/library/re.html
		+ https://docs.python.org/3/library/re.html#match-objects

		Match objects are different from regular expression objects
			(regex objects).
		+ https://docs.python.org/3/library/re.html#regular-expression-objects
		+ egular Expression HOWTO: https://docs.python.org/3/howto/regex.html#regex-howto
		+ https://docs.python.org/3/library/re.html#match-objects


		Reference:
		+ Python contributors, "re — Regular expression operations," from Python: Python 3.9.0 documentation: The Python Standard Library (or, Library Reference): Text Processing Services, Python Software Foundation, October 10, 2020. Available online at: https://docs.python.org/3/library/re.html; last accessed on October 10, 2020.
	"""
	list_of_tokens = re.match(r"(.*)\((.*)\)| " ,nn)
	print("	list_of_tokens is:",list_of_tokens,"=")
	"""
	if list_of_tokens is not None:
		for tt in list_of_tokens:
			print("	Its tokens are:",list_of_tokens,"=")
	"""
"""
	Implement this in the check_names() function for my
		BibTeX management software.


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
"""

print("=========================================================")


s = "<alpha.Customer[cus_Y4o9qMEZAugtnW] active_card=<alpha.AlphaObject[card]\
 ...>, created=1324336085, description='Customer for My Test App',\
 livemode=False>"

"""
	Reference:
	+ David Alber, https://stackoverflow.com/a/8569256/1531728
		December 20, 2011.
"""
val = s.split('[', 1)[1].split(']')[0]
print("David Alber val is:",val,"=")
tokens = s.split('[')[1].split(']')[0]
"""
	The following does not work since it requires selecting the
		specific token in the initial tokenized result.

	tokens = s.split('[').split(']')
"""
print("tokens is:",tokens,"=")

"""
	Reference:
	+ srgerg and D K, https://stackoverflow.com/a/8569258/1531728
		December 20, 2011.
"""
tokens = re.search(r"\[([A-Za-z0-9_]+)\]", s)
print("srgerg tokens is:",tokens,"=")

tokens = re.search(r"\[(\w+)\]", s)
print("srgerg tokens is:",tokens,"=")


"""
	Reference:
	+ Samuele Santi / redShadow, https://stackoverflow.com/a/8569270/1531728
		December 20, 2011.
"""
tokens = re.match(r"[^[]*\[([^]]*)\]", s).groups()[0]
print("redShadow tokens is:",tokens,"=")

"""
	Reference:
	+ OmaL, https://stackoverflow.com/a/38871907/1531728
		August 10, 2016 and May 23, 2017 (edited by Community moderator)
"""
tokens = s[s.find("[") + 1:s.find("]")]
print("OmaL tokens is:",tokens,"=")


"""
	This method can find all instances of pattern matches.
	Use this method!!!

	Reference:
	+ Brandon Keith Biggs, https://stackoverflow.com/a/31358563/1531728
		July 11, 2015 and May 23, 2017
"""
tokens = re.findall(r"\[([A-Za-z0-9_]+)\]", s)
print("Brandon Keith Biggs tokens is:",tokens,"=")
"""
	"Use re.findall or re.finditer instead."
	"re.findall(pattern, string) returns a list of matching strings."
	"re.finditer(pattern, string) returns an iterator over MatchObject objects."


	To-do:
	+ test with Albert-L{\'{a}}szl{\'{o}} Barab{\'{a}}si



	Reference:
	+ Amber Yust / Amber and Mike Fogel, https://stackoverflow.com/a/4697884/1531728
		January 15, 2011 and January 21, 2020.
"""



"""
	Mr. Jean-Fran{\c{c}}ois Fabre claims that regular expressions
		cannot handle nested brackets (or, "parenthesis nesting")
	+ https://stackoverflow.com/a/42070578/1531728
		- February 6, 2017.

	Hence, we should use the PyPi regex module instead.
	However, Wiktor Stribi{\.{z}}ew claims that it is buggy, and
		should not be used in production code.


	Reference:
	+ Wiktor Stribi{\.{z}}ew, https://stackoverflow.com/a/42073084/1531728
		February 6, 2017

	Also, the method from Ohad Eytan
"""


print("=========================================================")

# Find the number of characters in a string.


"""
	References:
	+ [Striver 2019]
		- Striver, Shubham Singh, and Nidhi, "Python String | count()," GeekstoGeeks, Noida, Uttar Pradesh, India, September 30, 2019.
			Available online from GeektoGeeks at: https://www.geeksforgeeks.org/python-string-count/; October 11, 2020 was the last accessed date.
	+ Roy, Answer to the question "Python: How to count number of letters in a string?", in Codecademy: Codecademy Forums, New York, NY, March 17, 2020.
		Available online from Codecademy: Codecademy Forums at: https://discuss.codecademy.com/t/python-how-to-count-number-of-letters-in-a-string/78055/4; October 11, 2020 was the last accessed date.





	Resources that I look at:
	+ https://www.geeksforgeeks.org/python-string-length-len/
	+ https://www.tutorialspoint.com/python/string_len.htm
	+ https://www.educative.io/edpresso/how-to-find-the-length-of-a-string-in-python
	+ https://www.guru99.com/python-string-length-len.html
	+ https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
	+ https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
	+ https://discuss.codecademy.com/t/python-how-to-count-number-of-letters-in-a-string/78055/4

"""

# Trying method len().
one_letter_string = "x"
two_letter_string = "xy"
ten_letter_string = "abcdefghij"

if 1 == len(one_letter_string):
	print("one_letter_string has 1 letter:",one_letter_string,"=")
if 2 == len(two_letter_string):
	print("two_letter_string has 2 letters:",two_letter_string,"=")
if 10 == len(ten_letter_string):
	print("ten_letter_string has 10 letters:",ten_letter_string,"=")


print("=========================================================")

# Determine if an object is in a list.


"""
	Reference:
	+ [Baumstark 2017]
		- Niklas Baumstark, Chris Rands, and Rich "Drise" Moll, 
			https://stackoverflow.com/a/9542768/1531728
			March 3, 2012 and December 14, 2017


	Notes:
	+ If the BibTeX type is "@conference{", raise an error.
		- This is because we should use the equivalent "@inproceedings{"
			to avoid redundant BibTeX types.
"""

# Method 1: Checking if something is inside [Baumstark 2017]
bibtex_types = ["@book{", "@misc{", "@phdthesis{", "@article{", "@inproceedings{", "@incollection{", "@manual{", "@proceedings{", "@techreport{", "@booklet{", "@inbook{", "@mastersthesis{", "@unpublished{"]


current_bibtex_entry_type = "@incollection{"
if current_bibtex_entry_type in bibtex_types:
	print("The current BibTeX entry type @incollection is valid in bibtex_types.")

current_bibtex_entry_type = "@random{"
if current_bibtex_entry_type not in bibtex_types:
	print("The current BibTeX entry type @random is not valid in bibtex_types.")

current_bibtex_entry_type = "@phdthesis{"
if current_bibtex_entry_type in bibtex_types:
	print("The current BibTeX entry type @phdthesis is valid in bibtex_types.")
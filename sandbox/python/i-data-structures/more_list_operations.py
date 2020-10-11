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

# ====================================================================


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
	Reference:
	+ Amber Yust / Amber and Mike Fogel, https://stackoverflow.com/a/4697884/1531728
		
"""
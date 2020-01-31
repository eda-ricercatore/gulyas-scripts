#!/Users/zhiyang/anaconda3/bin/python3


###############################################################
"""
	Import modules from The Python Standard Library.
	sys:		Get access to any command-line arguments.
	
	Finishing referencing publication used in this script!!!
	
	
	References:
	+ https://docs.python.org/3/library/tokenize.html
		- "tokenize" for tokenization.
	+ https://realpython.com/convert-python-string-to-int/
		- Convert numbers to different bases, such as binary
			and hexadecimal.
"""
import sys

csv_string = "nome cognome, 45678996545678654, 73.237, 82.167, 98.234, 72983.627"
# Use "," as a delimiter to tokenize "csv_string".
tokenized_csv_string = csv_string.split(",")
print("tokenized_csv_string:",tokenized_csv_string,".")
whitespace_delimited_tokenized_csv_string = []





# Convert a number string into an integer.
actual_number = 45678996545678654
string_number_with_whitespace = "	  45678996545678654  	"
if actual_number == int(string_number_with_whitespace):
	print("Can covert strings with leading and trailing whitespace to integers.")
else:
	print("Error!!! Cannot covert strings with leading and trailing whitespace to integers!")
string_number_with_whitespace = "  	  45678996545678654"
if actual_number == int(string_number_with_whitespace):
	print("Can covert strings with leading whitespace to integers.")
else:
	print("Error!!! Cannot covert strings with leading whitespace to integers!")
string_number_with_whitespace = "45678996545678654	  	"
if actual_number == int(string_number_with_whitespace):
	print("Can covert strings with trailing whitespace to integers.")
else:
	print("Error!!! Cannot covert strings with trailing whitespace to integers!")






actual_number = 7328.32879708
string_number_with_whitespace = "	  7328.32879708  	"
if actual_number == float(string_number_with_whitespace):
	print("Can covert strings with leading and trailing whitespace to floating-point numbers.")
else:
	print("Error!!! Cannot covert strings with leading and trailing whitespace to floating-point numbers!")
string_number_with_whitespace = "  	  7328.32879708"
if actual_number == float(string_number_with_whitespace):
	print("Can covert strings with leading whitespace to floating-point numbers.")
else:
	print("Error!!! Cannot covert strings with leading whitespace to floating-point numbers!")
string_number_with_whitespace = "7328.32879708	  	"
if actual_number == float(string_number_with_whitespace):
	print("Can covert strings with trailing whitespace to floating-point numbers.")
else:
	print("Error!!! Cannot covert strings with trailing whitespace to floating-point numbers!")

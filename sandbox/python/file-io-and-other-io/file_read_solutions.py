#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to try out different solutions for
		file input.




	Notes:
	+ File objects within a *with statement* cannot be closed yet.
	+ However, they will be closed automatically when all the code
		in the code block has finished executing.
	+ Use the file object attribute "closed" to determine if a
		file I/O object/stream is closed.
		- [DrakeJr2016b], as "io — Core tools for working with streams",
			in Python 3.9.1 Documentation: The Python Standard Library: Generic Operating System Services.
	+ Use file objects, file streams, and file-like objects
		interchangeably/synonymously
		- [DrakeJr2016b], as "io — Core tools for working with streams",
			in Python 3.9.1 Documentation: The Python Standard Library: Generic Operating System Services.


	

	References:
	+ [DrakeJr2016b].





	Citations/references that use the LaTeX/BibTeX notation are taken from my BibTeX database
		(set of BibTeX entries).

	If these citations are not found in this list of references, information about them can be found in my BibTeX database.

	+ 


"""



# Import Python libraries and modules.
#import io






# Absolute path to the input file.
input_file = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/file-io-and-other-io/dummy-files/topics.md"

#	=================================================================

"""
	References for Method 1:
	+ \cite{Mohtashim2017}
		"Python - Files I/O": https://www.tutorialspoint.com/python/python_files_io.htm
		- to open and close an input file stream.
	+ \cite{Krishna2020}
		from {\it Guru99: Web: Python: Python Tutorial for Beginners -- Learn Python Programming in 7 Days -- Python File Handling}
		"Python File Handling: How to Create, Open, Append, Read, Write": https://www.guru99.com/reading-and-writing-files-in-python.html
		- to open and close an input file stream.
		- to read all the contents of the file at once.
	+ \cite{Bader2018a}
		from "Working With File I/O in Python" at: https://dbader.org/blog/python-file-io
		- to open and close an input file stream.
		- to read all the contents of the file at once.
"""


"""
	Create an input file object to process the input file.
	+ \cite{Mohtashim2017}
	+ \cite{Krishna2020}
	+ \cite{Bader2018a}
"""
ip_file_obj = open(input_file, "r+")


"""
	Read all the contents of the input file at once.
	+ \cite{Krishna2020}
	+ \cite{Bader2018a}
"""
contents = ip_file_obj.read()
print("Method 1: Contents are...")
print(contents)
print("Method 1: Finished processing input file.")

"""
	Close the input file object that has processed the input file.
	+ \cite{Mohtashim2017}
	+ \cite{Krishna2020}
	+ \cite{Bader2018a}
"""
ip_file_obj.close()

"""
	References for using the file object attribute "closed" to
		determine if a file I/O object/stream is closed:
	+ \cite{DrakeJr2016b}
"""
if True == ip_file_obj.closed:
	print("Method 1: Input file stream is closed: ip_file_obj.")
else:
	print("Method 1: Input file stream for ip_file_obj is NOT closed.")

#	=================================================================

"""
	References for Method 2:
	+ [abccd2017]
		- abccd, Answer to ``How to read/print the ( _io.TextIOWrapper) data?,'' Stack Exchange Inc., New York, NY, April 16, 2017. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/43438389/1531728 and https://stackoverflow.com/questions/43438303/how-to-read-print-the-io-textiowrapper-data/43438389#43438389; March 7, 2020 was the last accessed date.
	+ \cite{Bader2018a}
		from "Working With File I/O in Python" at: https://dbader.org/blog/python-file-io
		- to open and close an input file stream.
		- to read all the contents of the file at once.
	+ 
"""
with open(input_file, "r+") as ip_file_obj:
	"""
		Read all the contents of the input file at once.
		+ \cite{abccd2017}
		+ \cite{Krishna2020}
		+ \cite{Bader2018a}
	"""
	contents = ip_file_obj.read()
	print("Method 2: Contents are...")
	print(contents)
	print("Method 2: Finished processing input file.")
	"""
		References for using the file object attribute "closed" to
			determine if a file I/O object/stream is closed:
		+ \cite{DrakeJr2016b}
	"""
	if False == ip_file_obj.closed:
		print("Method 2: inside with statement: Input file stream for ip_file_obj is not closed yet.")
	else:
		print("Method 2: inside with statement: Input file stream IS CLOSED: ip_file_obj!!!")
"""
	References for using the file object attribute "closed" to
		determine if a file I/O object/stream is closed:
	+ \cite{DrakeJr2016b}
"""
if True == ip_file_obj.closed:
	print("Method 2: outside with statement: Input file stream is closed: ip_file_obj.")
else:
	print("Method 2: outside with statement: Input file stream for ip_file_obj is NOT closed.")

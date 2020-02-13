#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	References for handling the "__file__" attribute.
	+ https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
"""


import os

print("= Perform split() operation.")
path_prefix, last_pathname_component = os.path.split('/my/path/to/whatever/somefile.ext')
print(path_prefix)
print(last_pathname_component)

print("= Perform splitext() operation.")
filename, file_extension = os.path.splitext('/some/path/to/somefile.ext')
print(filename)
print(file_extension)

print("= Perform splitext() operation again.")
filename, file_extension = os.path.splitext('fosca.battati')
print(filename)
print(file_extension)


print("= Perform splitext() operation yet another time.")
filename, file_extension = os.path.splitext('daniela-stefanescu')
print(filename)
print(file_extension)



print("= Perform splitext() operation on multiple file extensions.")
filename, file_extension = os.path.splitext('ansu_mani.tar.gz')
print(filename)
print(file_extension)
f_name, f_extension = os.path.splitext(file_extension)
print(f_name)
print(f_extension)
f_name1, f_extension1 = os.path.splitext(filename)
print(f_name1)
print(f_extension1)



"""
	References and notes:
	+ \cite[From section "File and Directory Access", subsection "os.path — Common pathname manipulations"]{DrakeJr2016b}
		Available online from "The Python Standard Library: File and Directory Access: os.path — Common pathname manipulations" at: https://docs.python.org/3/library/os.path.html#os.path.expanduser;
			February 12, 2020 was the last accessed date.
		- Information about the "os.path.expanduser(path)" command
			replaces relative paths starting from the current
			user's home directory (starting with "~" or "~user").
			* Hence, if the path does not start with "~" nor
				"~user", or if the path cannot be expanded,
				the 'path' remains unchanged.
	+ \cite[From section "Generic Operating System Services", subsection "os — Miscellaneous operating system interfaces"]{DrakeJr2016b}
		Available online from "The Python Standard Library: Generic Operating System Services: os — Miscellaneous operating system interfaces" at: https://docs.python.org/3/library/os.html#os.getcwd;
		February 12, 2020 was the last accessed date.
	+ [Dias2016] Russell Dias and Mark Amery, Answer to "Find current
		directory and file's directory [duplicate]", from
		Stack Exchange Inc.: Stack Overflow: Questions,
		Stack Exchange, Inc., New York, NY, July 31, 2016.
		Available online from Stack Exchange Inc.: Stack
			Overflow: Questions at: https://stackoverflow.com/a/5137509/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory/5137509#5137509;
			February 12, 2020 was the last accessed date.
	+ John Howard and Mark Amery, "Find current
		directory and file's directory [duplicate]", from
		Stack Exchange Inc.: Stack Overflow: Questions,
		Stack Exchange, Inc., New York, NY, July 31, 2016.
		Available online from Stack Exchange Inc.: Stack
			Overflow: Questions at: https://stackoverflow.com/q/5137497/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
			February 12, 2020 was the last accessed date.
"""
valid_path = os.path.expanduser("./")
print("valid_path is:",valid_path,"=")
"""
	See \cite[From section "File and Directory Access", subsection "os.path — Common pathname manipulations"]{DrakeJr2016b}
		for reasons why the "os.path.expanduser(path)" command
		does not work with the paths "./" nor ".".
"""
valid_path = os.path.expanduser(".")
print("New valid_path is:",valid_path,"=")
"""
	See \cite[From section "Generic Operating System Services", subsection "os — Miscellaneous operating system interfaces"]{DrakeJr2016b}.
"""
current_wking_dir = os.getcwd()
print("New current_wking_dir is:",current_wking_dir,"=")

# \cite{Dias2016}
full_path = os.path.realpath("./")
print("full_path is:",full_path,"=")
full_path = os.path.realpath(".")
print("Now full_path is:",full_path,"=")

absolute_path = os.path.abspath("./")
print("absolute_path is:",absolute_path,"=")
absolute_path = os.path.abspath(".")
print("Now absolute_path is:",absolute_path,"=")


"""
	Get the name of the current directory, and the path
		to the current directory.
	Reference:
	+ StormShadow, Answer to "Find current directory and file's directory [duplicate]," Stack Exchange Inc., New York, NY, October 9, 2013.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19269546/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory/19269546#19269546
			February 13, 2020 was the last accessed date.
"""
current_folder_path, current_folder_name = os.path.split(os.getcwd())
print("current_folder_path is:",current_folder_path,"=")
print("current_folder_name is:",current_folder_name,"=")

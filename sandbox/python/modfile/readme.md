Scripts for String Processing in Text Files
===========================================

Scripts for string processing, such as replacing substrings, in text files are located here.


Organization of the Directory
-----------------------------

This directory is organized as follows:

cons_tuple.py			Script to store cons (i.e., pair of values).
get-expr-version.py		Script to remove print statements from C++ files.
__init__.py				Empty file required for importing Python classes.
input-file.txt			Input for testing "mod-file.py".
*.cpp					Inputs for testing "get-expr-version.py".
makefile				For build automation, using Make.
mod-file.py				Script to replace substrings in a text file.
output-file.txt			Output of testing "mod-file.py".
readme.md				README file for explaining contents of this project/directory.
string_processing.py	Script to test concepts in string processing.
test_ip_gen.py			Script to generate test input for "mod-file.py".
z-cpp-inputs			C++ files for testing "get-expr-version.py".



Make Targets and Main Scripts
-----------------------------

make test
	1) Run script to generate input test data.
	2) Run script to replace substrings in input test data.


make clean
	1) Remove temporary files.


make cpp
	1) Remove print statements from C++ source files.



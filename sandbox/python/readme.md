#	Contents


This is a sandbox, for trying out different concepts with "throwaway" scripts, for *Python* scripts for:
+ [*BibTeX* database processing](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/clean_bibtex)
	- superceded by an ongoing [*BibTeX* analytics project](https://github.com/eda-ricercatore/bibtex-analytics)
+ [data structures, and data types](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/i-data-structures)
	- [enumerating multiple arrays concurrently](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/i-data-structures/enumerate_multiple_arrays-concurrently.py)
	- [enumerating ordered dictionaries, and lists of tuples (i.e., each list is a list tuples)](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/i-data-structures/ordered_dict_color_enumeration.py)
	- [performing operations on lists, using functional programming and otherwise](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/i-data-structures/performing_operations_on_lists.py)
		* includes an example on [list comprehension](https://en.wikipedia.org/wiki/List_comprehension), which is exploited in functional programming (for monad comprehension, set comprehension, dictionary comprehension, parallel list comprehension)
		* "List comprehension results in faster operations than explicit *for* loops"
+ [data visualization](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/b-visualization)
	- bar charts to compare experimental/simulation from different solutions for each category/benchmark
		* https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/b-visualization/barchart_3_groups.py
		* https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/b-visualization/barchart.py
+ [database management](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/database-management)
+ [dump](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/x-dump)
	- [*Python* script to remove duplicate entries in a *BibTeX* database](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/x-dump/duplicate_BibTeX_entries.py).
+ [error management and exception handling](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/h-error-management)
	- [printing error messages to standard error, and providing warning messages](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/h-error-management/e-print-error-output.py)
	- [exception handling](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/h-error-management/my_exception_handling.py)
	- [catching warnings just like catching exceptions, by squelching/suppressing/silencing warnings in the standard output](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/h-error-management/catch_and_process_warnings.py)
		* [catching warnings just like catching exceptions, by squelching/suppressing/silencing warnings in the standard output -- ***cleaner solution without Python statements/commands that do not suppress/silence warnings***](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/h-error-management/catch_and_process_warnings_3.py)
		* [solution that fails to catch warnings just like catching exceptions, by squelching/suppressing/silencing warnings in the standard output](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/h-error-management/catch_and_process_warnings_2.py)
+ [file input/output (I/O) operations and other I/O operations](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/file-io)
	- [file formats](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/file-io/q-file-formats)
		* [JSON file operations](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/file-io/q-file-formats/json-files)
			+ For operations with files using the JavaScript Object Notation (JSON) format.
	- [file modifications, or reading a file, modifying its contents, saving the file modifications in a temporary file, and renaming the file to the filename of the original input file](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/file-io/modfile)
	- [Squelching standard output and standard error output](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/file-io-and-other-io/squelching_std_op_and_std_err_op.py)
+ [*Google Colab*, or *Google Colaboratory*](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/google-colab)
	- Uploading code
	- Importing pacakges and modules
		* from uploaded source code to *Google Drive*
		* from *Git*-based cloning of *GitHub* repositories.
+ [linear algebra](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/linear_algebra)
+ [navigating file systems](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/a-navigating-file-systems)
	- enumerating subdirectories
	- [operations involving file extensions](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/a-navigating-file-systems/a_os_path_methods.py)
+ [numbers](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/numbers)
	- [comparing numbers to determine if they are approximately equal](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/numbers/approximately_equal.py)
		* explores different techniques for doing so, and my success and failures in implementing them
	- [comparisons using "p == q" and "p is q"](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/numbers/miscellaneous.py)
	- [min(), max(), and list operations](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/numbers/b-min_max_string_numbers.py)
	- [Multiplying a list of numbers (or numbers in a list) with a scalar constant (or, scaling factor, or scale factor)](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/numbers/scaling_factor.py)
	- [Usage of the scientific notations](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/numbers/scientific_notation.py)
	- Terminated/Aborted attempts:
		* Good representations of recurring/repeating decimals that enables arithmetic operations, just like the default (i.e., typical) floating-point representation in *Python*.
			+ See https://docs.python.org/3/tutorial/floatingpoint.html \cite[Section 15, Floating Point Arithmetic: Issues and Limitations]{Brandl2017a}
			+ See https://docs.python.org/3/library/fractions.html \cite[From Numeric and Mathematical Modules: fractions -- Rational numbers]{Brandl2017a}
		* Representations and operations with continued fractions, especially finite continued fraction (or terminated continued fraction) that are used in filter design.
			+ Note that infinite continued fractions cannot lead to practical circuit implementations of filters.
			+ Generalized continued fractions can represent the structure of circults for filtering out noise.
			+ [Filter circuits](https://en.wikipedia.org/wiki/Leapfrog_filter) include:
				- leapfrog filter, active-ladder, or multiple feedback filter; an example of an active circuit electronic filter.
				- passive electronic ladder filter.
				- See https://en.wikipedia.org/wiki/Electronic_filter_topology#Ladder_topologies for ladder filters.
		* Creating a range of numbers using *n..m*. This works with [*Ruby*](https://en.wikipedia.org/wiki/For_loop#1995:_Ruby) though.
+ [porting *Python 2.x* source code to *Python 3.y* source code](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/porting-Py2-to-Py3)
+ [*Python* functions](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/e-functions)
	- [*Python* functions that return multiple values](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/e-functions/function_multiple_return_values.py)
+ [*Python* strings](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/y-strings)
	- [common string operations](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/y-strings/strings_tutorial.py)
	- [strings from each line parsed from a comma-separated values (CSV) file](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/y-strings/csv_strings.py) 
		* Information about [comma-separated values (CSV) files](https://en.wikipedia.org/wiki/Comma-separated_values)
	- [substring replacement](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/y-strings/string_processing.py)
+ [statistics, statistical analysis, stochastic modeling/optimization](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/statistics)
+ [utilities package for my *Python* code base](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/utilities)
	- [current time measurement methods -- ***code that is used by my Python programs/software/scripts***](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/utilities/timing_measurements)
		* [script in the *Python* sandbox directory to test the current time measurement methods](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/test.py)
		* [additional scripts to try concepts related to date and time processing](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/time-processing)
			+ [Script demonstrating that methods of timing measurements should not be combined to find elapsed time](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/a_combined_measurement_techniques.py)
				- "Acceptable" combinations are:
					* perf_counter and monotonic
					* perf_counter_ns and monotonic_ns
				- All other combinations are not acceptable.
				- In general, avoid combining methods of timing measurements.
+ [version control, revision control, and software configuration management](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/revision-ctrl)
+ [VLSI design](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/vlsi)
	- [*n*-bit adders](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/vlsi/adder.ipynb)
	











#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


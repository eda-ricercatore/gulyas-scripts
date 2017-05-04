#	Notes About *GNU Octave*

##	Basic Operations for *GNU Octave*

See [GNU Octave script executing basic operations](../sandbox/gnu-octave/h-basic-operations.m).

Some basic operations that are shown in the script are:
+ How to declare a variable as a range.
+ How to declare a variable as a complex number.
+ How to determine the type of a variable.
+ List of predefined constants of *GNU Octave*.
+ List of environment variables of *GNU Octave*.
	- E.g., EDITOR, LOADPATH, and INFO_FILE.
	- See [GNU Octave script executing basic operations](../sandbox/gnu-octave/h-basic-operations.m).
+ How to cast a number from a data type to another data type.
+ How to represent missing data explicitly using the
	'Not Available' (NA) function.
+ How to determine if a variable is a null value or empty string.
+ Show a list of variables that are currently defined.
+ Show a detailed list of variables that are currently defined.
+ Determine if a "name" is used for an existing "variable, function,
	file, directory, or class"
	\cite[\S7.3 Status of Variables]{Abbott2016,Eaton2016}
+ Note #1: The number of columns per row of an array cannot be
	mismatched. Else, it would cause an error to be thrown during
	interpretation/compilation/execution.


Interesting functions regarding the status of variables
	\cite[\S7.3 Status of Variables]{Abbott2016,Eaton2016}:
+ pack()
	- "Consolidate workspace memory in MATLAB."
	- "This function is provided for compatibility, but does nothing
		in Octave."
	- Deprecated
+ type
	- "Display the contents of name which may be a file,
		function (m-file), variable, operator, or keyword."
+ which
	- "Display the type of each name."
+ what
	- "List the Octave specific files in directory dir."


Functions to find elements and check conditions
	\cite[\S16.1 Finding Elements and Checking Conditions]{Abbott2016,Eaton2016}:
+ any(x)
	- any(x, dim)
	- "For a vector argument, return true (logical 1) if any element
		of the vector is nonzero."
	- "For a matrix argument, return a row vector of logical ones
		and zeros with each element indicating whether any of the
		elements of the corresponding column of the matrix
		are nonzero."
+ all(x)
	- all(x, dim)
	- "For a vector argument, return true (logical 1) if all elements
		of the vector are nonzero."
	- "For a matrix argument, return a row vector of logical ones and
		zeros with each element indicating whether all of the
		elements of the corresponding column of the matrix
		are nonzero."
+ xor(x, y)
	- xor(x1, x2,...)
	- "Return the exclusive or of x and y."
+ diff(x)
	- diff(x, k)
	- diff(x, k, dim)
	- "If x is a vector of length n, diff (x) is the vector of first
		differences x(2) - x(1), …, x(n) - x(n-1)."
+ isinf(x)
	- "Return a logical array which is true where the elements of x
		are infinite and false where they are not."
+ isnan(x)
	- "Return a logical array which is true where the elements of x
		are NaN values and false where they are not."
+ isfinite(x)
	- "Return a logical array which is true where the elements of x are finite values and false where they are not."
+ [err,y1,...] = common_size(x1,...)
	+ "Determine if all input arguments are either scalar or of
		common size."
+ idx = find(x)
	- idx = find(x, n)
	- idx = find(x, n, direction)
	- [i, j] = find (...)
	- [i, j, v] = find (...)
	- "Return a vector of indices of nonzero elements of a matrix,
		as a row if x is a row vector or as a column otherwise."
+ idx = lookup(table, y)
	- idx = lookup(table, y, opt)
	- "Lookup values in a sorted table."


###	Suggestions for Research Activities

Some suggestions for research activities in science and engineering,
	or any activity that requires reproducible (experimental or
	computational) and replicable results
	\cite{Mailund2017,Gandrud2015,Liberman2015,Gandrud2014,Stodden2014,Geier20XY}
	and data analysis are:
+ *`diary` [on | off | filename]* \cite[\S2.4.8, Diary & Echo Commands, pp. 34]{Eaton2016a}
	- Function to record executed commands and their output in a
		separate file named *diary* or *filename* (if specified by
		the user). 
	- When called without any input arguments, the current *on/off*
		diary state is toggled.
	- Essentially, it is similar to the "script" function in some
		UNIX-like operating systems.
+ *`echo [on | off] [all]`* \cite[\S2.4.8, Diary & Echo Commands, pp. 34]{Eaton2016a}
	- Function to display commands that are executed, or to mute
		their display.
	- Its input arguments are optional.
	- Without input arguments, it toggles between displaying the
		commands and muting their display.
	- The [on | off] input argument enables/disables the display of
		the commands, respectively.
	- The [all] input argument is used to indicate the display of
		commands in all script files and functions.

Note that reproducible research enables published experimental
	results to be reproduced from raw data.
	A stronger notion is replicable research that requires the
	experiment and experimental data analyses to be repeated multiple
	times \cite{Mailund2017,Gandrud2015,Liberman2015,Gandrud2014,Stodden2014,RunMyCodeAssociationMembers2013,Geier20XY}.










##	Build Automation for *GNU Octave*

###	Using *Makefile* for Build Automation

For *Makefile*-based build automation for executing/running 
	*GNU Octave* scripts, I have to do the following:
+ ./[*filename*]
	- Requires adding the *UNIX* shebang for *GNU Octave*
	- Requires using *chmod* (*UNIX* command) to change the file
		permission, so that the script(s) can be executed via the
		Terminal as a *UNIX* command/process.

And avoid doing the following:
+ octave [*filename*]

Notes for using *Makefile* for build automation; that is, using *Makefile* to execute/run *GNU Octave* scripts:
+ Only the main script that would be called by the *Makefile*, or executed via the command line of the *Terminal* application, need to have its file permissions set by *chmod*.
+ The main script also needs to have the *UNIX* shebang in its first line.
+ Other scripts, containing a function per script, form a library of *GNU Octave* scripts.
+ The aformentioned library of *GNU Octave* scripts need not have the *UNIX* shebang in their first line.
+ The aformentioned library of *GNU Octave* scripts need not have their file permissions set by *chmod*.

Experimentally/Empirically demonstrated in the execution of the
	*Make* target *torture*. See: [link to sandbox/gnu-octave](../sandbox/gnu-octave).

















##	Functions

Each *GNU Octave* script can only contain one function.

If more than one function is defined in a script, all the functions
	(except the first function) cannot be recognized by other
	*GNU Octave* scripts. 

For a function-specific script:
+ The name of the function must match its file name.
+ The name of the function must match the name of the function
	used in a function call.
	- E.g., to call function *foo* in a script, the function
		specified in the file named *foo.m* must be named *foo*.  

When I make a function call, I can use more arguments than specified
	as function parameters.
	The extra arguments are ignored.


Experimentally/Empirically demonstrated in the execution of the
	*Make* target *torture*. See: [link to sandbox/gnu-octave](../sandbox/gnu-octave).

###	Handling Input Arguments/Parameters

The variable *nargin* stores the number of input arguments that are
	used in the function call.
	That is, when a function is called, *nargin* determines the
	number of input arguments in the function call
	\cite[\S11.2, pp. 173]{Eaton2016a}.
	
However, if *varargin* is specified as the last argument to a
		function, *nargin()* (or *nargin(function_name)*) would
		return a negative value \cite[\S11.2, pp. 173]{Eaton2016a}.


### Concepts Experimentally/Empirically Demonstrated, But Unrecorded

Concepts that are experimentally/empirically demonstrated, but not
	stored in the repository as commented code fragments:
+ Mismatch between the name of the specified function and the filename
	of the function-specific script is not allowed. 
+ Mismatch between function name used in a function call and the name
	of the specified function (in the function-specific script) is
	not allowed. 
+ If the number of arguments used in the function is less than the
	number of arguments specified in the function, an error will be
	raised in the execution of the script. 
	- **Example of creating an error.**
+ If a script file contains multiple functions, only the first
	function defined can be called.
	- The remaining functions can not be called.
	- Each unique function shall be specified in a unique file/filename.





###	Function files (and Script Files)

A function file (or script file) should only contain one function.




###	Function Handles, Anonymous Functions, and Inline Functions








##	Pseudo-Random Number Generation (PRNG) in *GNU Octave*

To reset the seed of the function for pseudo-random number generation
	(PRNG), do the following: rand("seed","reset") 
	\cite[Function File: Function Reference -- rand]{OctaveForgeContributors2016}.
	
Note: Do not assign *rand("seed","reset")* to any variable. 
	This will cause an error in executing/interpreting the
	*GNU Octave* script, since this function does not return a value
	or matrix (or any other mathematical object).
+ **Example of creating an error.**















##	Error Management

*GNU Octave* does not have exceptions, which *C++* and *Java* have.

Instead, *GNU Octave* uses errors to terminate execution of the
	*GNU Octave* program, when abnormalities are detected. 

In addition, *GNU Octave* can also raise warnings about things that
	are undesirable, but not problematic such that the *GNU Octave* 
	program should terminate.
	If the program can still run or be completed correctly, warnings
	can be raised instead of throwing exceptions to terminate the
	program.


Errors reported by *GNU Octave* for error-causing programs
	\cite[\S2.5, pp. 35]{Eaton2016a}.
+ Parse errors; that is, syntax errors.
	- Usually, a caret ('^') is used to indicate the source of the
		syntax/parse error.
+ Run-time errors, or evaluation errors.
	- To debug these run-time errors, examine error messages generated
		from the innermost error provide a traceback of function calls
		and enclosing expressions.

###	Guidelines On Using Errors and Warnings

Error and warning messages can be used to judiciously inform the user
	of abnormal conditions \cite[\S12, pp. 205]{Eaton2016a}.

Adopt "a set of contractual guidelines" \cite{WikipediaContributors2016f}
	to support reasoning on errors, just like exception safety
	guarantees in *C++* 
	\cite{Abrahams1998,Abrahams2001,WikibooksContributors2016,WikipediaContributors2016f}.

In descending order of safety guarantees, the levels of exception
	safety (or rather, error safety) are \cite{Abrahams1998,Abrahams2001,WikibooksContributors2016,WikipediaContributors2016f}:
+ no throw guarantee, or failure transparency: "Best level of exception safety."
+ strong exception safety, commit/rollback semantics, or no-change guarantee
+ basic exception safety
+ minimal exception safety, no-leak guarantee
+ no exception safety: "No guarantees are made. (Worst level of exception safety)"  

These levels of error/exception safety can be partially handled, and the
	use of guards/invariants is strongly recommended for making the code
	exception safe.

In addition, judiciously consider what to do with the semipredicate
	problem \cite{WikipediaContributors2016e}.

### *unwind_protect* Technique \cite[\S10.8, pp. 168]{Eaton2016a}

+ Warnings cannot be handled by *unwind_protect*.
	- When a warning occurs, the *unwind_protect_cleanup* block can
		make corrections to (i.e., mitigate) the trigger of
		the warning.
	- The execution of the script does not terminate when warnings
		are generated in the *unwind_protect* block.
+ When no warning nor error is generated, the
	*unwind_protect_cleanup* block is executed anyway.
	- Cleanup of *unwind_protect* is executed regardless of whether
		errors/warnings are generated.
+ When an error is caught (and handled), the
	*unwind_protect_cleanup* block is executed before the
	program/script is terminated.
	- The remainder of the program, after the
		*unwind_protect_cleanup* block would not be executed. 
+ Only errors are handled with *unwind_protect*.

###	*try-catch-block* Technique \cite[\S10.9, pp. 168-169]{Eaton2016a}

+ Warnings cannot be caught.
+ Only errors are caught.
+ For normal operations that do not produce an error or warning,
	the catch block is not executed.

###	Raising Errors

The syntax for raising an error is: *error(id, template, ...)*
	\cite[\S12.1.1, pp. 205]{Eaton2016a}.  

The first argument *id* is: the value/number associated with the
	output stream
	\cite[\S12.1.1, pp. 205; \S14.1.3, pp. 242; \S14.1.1.1, pp. 236]{Eaton2016a}.

The second argument *template* is: the string containing the
	error message \cite[\S12.1.1, pp. 205; \S14.2.4, pp. 253]{Eaton2016a}..

A raised error would diplay an error message, which is stored in
	*template* (if *template* is not terminated by a newline
	character) or a "traceback of function calls leading to the
	error" \cite[\S12.1.1, pp. 205-206]{Eaton2016a}.

If *template* "does not end with a newline character, a traceback
	of function calls leading to the error" is printed in the
	standard error stream \cite[\S12.1.1, pp. 205-206]{Eaton2016a}.

If *template* ends with a newline character, the error message
	*template* is printed without the aforementioned traceback
	\cite[\S12.1.1, pp. 206]{Eaton2016a}. 

If *template* is "a null string ("")," the script/program would
	continue execution. The raised error would be treated as a
	NOP ("no operation") statement
	\cite[\S12.1.1, pp. 206]{Eaton2016a}.

	
###	Difficulties Faced

I cannot raise an error with an identifier. I have tried using
	a string or a number in vain.

After multiple errors are raised, I cannot increment the value of
	beep_on_error(), via beep_on_error(new_error_value).
Before an error occurs, the error value is zero.
Subsequently, it is raised to one.

I have problems using the onCleanup() correctly, without causing
	errors due to my poor understanding of its function arguments.
		 


###	Catching Specific Errors

Specific errors can be caught, if only one potentially error raising
	operation is placed within the *try* block.
While **lasterr** and **lasterror** can help me obtain information
	about it, if I assign that error to a name in the specification
	of the *catch* block, I can access information about that
	specific error later \cite[\S10.9, pp. 169]{Eaton2016a}.



### Default Error and Warning Messages

In \cite[\S12.2.1, pp. 214-218]{Eaton2016a}, a list of default warning messages from
	*GNU Octave* is provided. 

















## Debugging

Make use of the "built-in debugger" \cite[\S13, pp. 219]{Eaton2016a}
	while developing programs/scripts in *GNU Octave*.

Features of the "built-in debugger" include
	\cite[\S13, pp. 219]{Eaton2016a}: 
+ Interrupting the execution of the *GNU Octave* script at
	certain points (e.g., line number).
+ Interrupting the execution of the *GNU Octave* script during
	certain conditions.

When the execution of the *GNU Octave* script is interrupted, the
	["process", or execution of the program/script] switches (from
	the execution mode) into the debug mode.
This allows the symbol table at the point/condition of interruption
	to be examined, and modified for error location and correction
	\cite[\S13, pp. 219]{Eaton2016a}. 

**I am skipping the subsections on "Breakpoints" and "Call Stack"
	for the time being.**

###	Debug Mode Difficulties

I can enter the debug mode using *debug_on_interrupt()*, when I
	interrupt execution of the *GNU Octave* program/script using
	*Ctrl-C* on the *Terminal*.

However, I cannot enter the debug mode using warnings, or errors, yet.

###	Profiling

**I am skipping the subsection on "Profiling" for the time being.**















##	Data Types, Including Strings

`typeinfo(expr)` is used to determine the type of the
	expression `expr`, which is returned as a `string`.
"If `expr` is omitted," "a cell array containing all the currently"
	defined (and added) data types \cite[\S3, pp. 39]{Eaton2016a}.

`class(obj)` returns the class of the object `obj`
	\cite[\S3.1, pp. 39]{Eaton2016a}.
 
`class(s, id, p, ...)` creates a class with the fields of structure
	`s` and the name (string) `id`, and inherits
	attributes/properties and behavior (functions) 
	\cite[\S3.1, pp. 39]{Eaton2016a} [WikipediaContributors2016a].

`isa(obj, classname)` returns true if `obj` is an object of the
	class `classname` or the following class categories
	\cite[\S3.1, pp. 39-40]{Eaton2016a}: 
+ "float": 'double', or 'single'
+ "integer": (u)int8, (u)int16, (u)int32, and (u)int64
+ "numeric": either a floating point or integer value

If `classname` in `isa(obj, classname)` "is a cell array of string,"
	return a logical array (i.e., boolean array) of the same size.
The array would contain true for each class that `obj` belongs to
	\cite[\S3.1, pp. 40]{Eaton2016a}.

###	Numeric Constants

Forms of *numeric constants* \cite[\S4, pp. 47]{Eaton2016a}:
+ scalar
	- integer
	- decimal fraction
	- number in scientific/exponential notation
	- complex number
+ vector
+ matrix

By default, numeric constants are internally represented in
	*GNU Octave* "in double-precision floating point format," and
	complex constants are internally represented as "pairs of
	double-precision floating point values"
	\cite[\S4, pp. 47]{Eaton2016a}.

The imaginary part of a complex constant requires the `i` to be
	appended to the number representing the magnitude of the
	complex number, without white space between them
	\cite[\S4, pp. 47]{Eaton2016a}.

`double(x)` converts x to the data type with double-precision
	floating point format \cite[\S4, pp. 47]{Eaton2016a}.  

`complex(re,im)` returns the complex number *(re)* + *(im)*i.
	If the second input argument *(im)* is not provided, the
	result is a real number with the magnitude *(re)*
	\cite[\S4, pp. 47]{Eaton2016a}.








###	Built-in Data Types

List of built-in data types \cite[\S3 and \S3.1, pp. 39]{Eaton2016a}: 
+ real scalars
	- \cite[\S4.4, pp. 54-57]{Eaton2016a} provides a list of functions
		to deal with the *Integer* data type.
+ complex scalars
+ real matrices
+ complex matrices
+ ranges
	- A range is "a row vector with evenly spaced elements."
	- Its format is: *base*:*increment*:*limit*.
	- The increment is an optional number.
	- To turn a range into the *row vector* (i.e., matrix) data type,
		place the range within square brackets.
	- E.g., [*base*:*increment*:*limit*].
	- Note that if it is important to include the endspoints of
		range, and the number of elements is known, use the
		`linspace` function instead.
	- Note that the optional *increment* must be a non-zero number.
	- See \cite[\S4.2, pp. 52-53]{Eaton2016a}.
+ character strings (i.e., strings)
	- A character string is a "sequence of characters" enclosed
		in single- or double- quote marks.
		It is stored internally by *GNU Octave* as matrices of
		characters \cite[\S3.1.3, pp. 43]{Eaton2016a}.
		See [script that determines the data type of various variables](../sandbox/gnu-octave/h-basic-operations.m).
+ *struct*, a data structure type:
	Currently, implemented as "an associative array with indices
	limited to strings" \cite[\S3.1.4, pp. 43]{Eaton2016a}.
+ "an array that can contain all data types"
+ cell arrays
	- A "general array that can hold any number of" elements, which
		can be of any data type \cite[\S3.1.3, pp. 43]{Eaton2016a}. 

Matrix objects are not limited by language-specific size constraints,
	"and can be dynamically reshaped and resized"
	\cite[\S3.1.1, pp. 42]{Eaton2016a}.
That said, there is a limit for "the maximum number of elements in
	a matrix."
This is determined by various factors, such as the size of the
	physical memory (or main memory) of my computer.
The value of this limit can be found via invoking the function
	`sizemax`.
Therefore, its returned value "is slightly smaller than" the
	theoretical maximum value reported by `intmax` (of the class
	`int64`) \cite[\S4.1, pp. 49]{Eaton2016a}.

The maximum and minimum values of "built-in floating-point
	numeric data," which are "currently stored as double precision
	numbers," are given by \cite[\S3.1.1, pp. 43]{Eaton2016a}.:
+ `realmin`
+ `realmax`
+ `eps`

\S3.3 has a list of functions in *GNU Octave* to determine the size
	of objects.
That is, these functions determine the number of elements in that
	set of objects/elements, or the size of a given dimension of the
	matrix \cite[\S3.3, pp. 44-46]{Eaton2016a}.

Notes:
+ \cite[\S4.1, pp. 49-51]{Eaton2016a} has functions to modify the
	standard output display. E.g., the display of the elements of
	a huge matrix can be modified, so that it is more readable. 
	- See \cite[\S4.1.1, pp. 51-52]{Eaton2016a} to find out how to
		display huge empty matrices.
+ \cite[\S4.5, pp. 57-60]{Eaton2016a} provides a list of functions
	for bit manipulations.
+ \cite[\S4.6, pp. 60-61]{Eaton2016a} provides a list of functions
	for logical reasoning, based on boolean algebra.
+ \cite[\S4.8, pp. 62-65]{Eaton2016a} provides a list of predicates
	for numeric objects. These support run-time type checking.



### Developer-Defined Specialized Data Types

Specialized data types can be defined with some *C++* code 
	\cite[\S3, pp. 39]{Eaton2016a}.

Such code can be integrated into *GNU Octave*
	via \cite[\S3, pp. 39]{Eaton2016a}:
+ Recompiling *GNU Octave* to add the new data type(s).
+ Dynamically load the new data type(s) "while *GNU Octave*
	is running." 






###	Casting Into A Data Type
`cast(val, "type")` converts `val` in its current data type to the
	data type specified by `"type"` \cite[\S3.1, pp. 40]{Eaton2016a}.
	
The numeric classes that can be used for `val`
	are \cite[\S3.1, pp. 40]{Eaton2016a}:
+ "double"
+ "single"
+ "logical"
+ "char"
+ "int8"
+ "int16"
+ "int32"
+ "int64"
+ "uint8"
+ "uint16"
+ "uint32"
+ "uint64"

Note that this can change the value of `val`, so that its value
	can fit within the range of the data type `"type"`
	\cite[\S3.1, pp. 40]{Eaton2016a}.


###	Casting Into A Class

`y = typecast(x, "class")` interprets the data of `x` in memory as
	data of the numeric class `"class"`, and returns a new array `y`
	containing values from the interpretation
	\cite[\S3.1, pp. 40-41]{Eaton2016a}. 

The classes that `x` and `"class"` belong to are restricted to the
	following "built-in numeric classes"
	\cite[\S3.1, pp. 40-41]{Eaton2016a}:
+ "logical"
+ "char"
+ "int8"
+ "int16"
+ "int32"
+ "int64"
+ "uint8"
+ "uint16"
+ "uint32"
+ "uint64"
+ "double"
+ "single"
+ "double complex"
+ "single complex"





###	Missing Data Representation

Missing data can be explicitly represented in *GNU Octave* as
	`"NA(n,m,k, ...)"` and `"NA(class)"`.
These functions return a scalar, matrix, or N-dimensional array
	containing elements that "are all equal to the special constant
 	used to designate missing values `NA` (i.e., "Not Available").
When the input argument(s) of `"NA(n,m,k, ...)"` are/is
	\cite[\S3.1.2, pp. 43]{Eaton2016a}:
+ empty (i.e., no input arguments), return the scalar value `NA`.
+ one (`n`), return a square matrix with the same dimensions as `n`.
+ >1 (`(n, m)` or `(n, m, k, ...)`), return a `i`-dimensional matrix,
	where the size/cardinality of the `j`th dimension is specificed
	by the `j`th input argument \cite[\S3.1.2, pp. 43]{Eaton2016a}.

Note that the optional argument `class` in `NA(..., class)`
	specifies the return type as *"double"* or *"single"*
	\cite[\S3.1.2, pp. 43]{Eaton2016a}.

Note that `NA != NA`, hence I could not compare the equality of	`NA`
	values using `==` or `!=`.
Instead, I should use the `isna(x)` function
	\cite[\S3.1.2, pp. 43]{Eaton2016a}.

`isna(x)` returns a boolean array that indicates which elements of
	`x` are `NA` (missing) values. If `x[i]` is a `NA` value, then
	the `i`th element of the returned boolean array would indicate
	`true`; else, the `i`th element would return `false`
	\cite[\S3.1.2, pp. 43]{Eaton2016a}.




###	Strings

A string constant, or character string \cite[\S3.1.3, pp. 43]{Eaton2016a},
	[is composed of / contains / "consists of"] "a sequence of
	characters" that are enclosed in quotation
	(single/double quote(s)) \cite[\S5, pp. 67]{Eaton2016a}.

Essentially, its representation is an array (of a one-dimensional
	matrix) of characters, which are represented by their ASCII values
	in the array \cite[\S5.2, pp. 68]{Eaton2016a}.

By convention, each row of characters is a string in *GNU Octave*,
	while a column of such strings (of the same length) form a string
	array \cite[\S5.2, pp. 68]{Eaton2016a}.

In *GNU Octave*, a string is a character vector, rather than merely a
	character matrix.
	Hence, use the *`ischar(x)`* and *`isvector(x)`* functions to
	determine if a variable is a character array/matrix or a character
	vector \cite[\S5.2, pp. 68]{Eaton2016a}.

It is recommended to use double quotes to denote strings, since a
	single quote is used as the operator for matrix transpose 
	\cite[\S5, pp. 67]{Eaton2016a}.





####	String Creation and Concatenation

Use matrix notation to enable string concatenation;
	e.g., *`[string1, string2]`* (or *`[string1 string2]`*)  concatenates *string1* and *string2*
	together \cite[\S5, pp. 67]{Eaton2016a}.





####	Conversion Between Strings and Numerical Data

Conversion between strings and numerical data can be done by the
	following functions \cite[\S5.3.2, pp. 73-75]{Eaton2016a}:
+ *`mat2str(x,n)`*:
	- `mat2str(x,n, "class")`
+ *`num2str(x)`*:
	- *`num2str(x, precision)`*
	- *`num2str(x, format)`*
+ *`int2str(n)`*

*`sprinf(template, ...)`* provides more flexibility to display
	numerical data as strings. 


####	String Comparison

Functions for string comparison, which requires character by
	character comparison of strings (can't be done by using "=="),
	are \cite[\S5.4, pp. 76-77]{Eaton2016a}:
+ *`strcmp(s1,s2)`*
+ *`strncmp(s1,s2,n)`*
+ *`strcmpi(s1,s2)`*
+ *`strncmpi(s1,s2,n)`*


####	String Manipulation

Functions for string manipulation are found in 
	\cite[\S5.5, pp. 77-91]{Eaton2016a}:
+ Remove whitespace \cite[\S5.5, pp. 77-78]{Eaton2016a}:
	- *`deblank(s)`*
	- *`strtrim(s)`*
	- *`strtrunc(s,n)`*
+ Modify whitespace \cite[\S5.5, pp. 90-91]{Eaton2016a}:
	- *`untabify (t)`*
	- *`untabify (t, tw)`*
	- *`untabify (t, tw, deblank)`*
+ Substring search operations, including the use of regular
	expressions (regex) and string matching
	\cite[\S5.5, pp. 78-80, 87-90]{Eaton2016a}:
	- *`findstr(s,t)`*
	- *`findstr(s,t,overlap)`*
	- *`idx = strchr (str, chars)`*
	- *`idx = strchr (str, chars, n)`*
	- *`idx = strchr (str, chars, n, direction)`*
	- *`[i, j] = strchr (...)`*
	- *`index (s, t)`*
	- *`index (s, t, direction)`*
	- *`rindex (s, t)`*
	- *`idx = strfind (str, pattern)`*
	- *`idx = strfind (cellstr, pattern)`*
	- *`idx = strfind (..., "overlaps", val)`*
	- *`substr (s, offset)`* \cite[\S5.5, pp. 87]{Eaton2016a}.
	- *`substr (s, offset, len)`* \cite[\S5.5, pp. 87]{Eaton2016a}.
	- *`[s, e, te, m, t, nm, sp] = regexp (str, pat)`* \cite[\S5.5, pp. 87-89]{Eaton2016a}.
	- *`[...] = regexp (str, pat, "opt1", ...)`* \cite[\S5.5, pp. 87-89]{Eaton2016a}.
	- *`[s, e, te, m, t, nm, sp] = regexpi (str, pat)`* \cite[\S5.5, pp. 89]{Eaton2016a}.
	- *`[...] = regexpi (str, pat, "opt1", ... )`* \cite[\S5.5, pp. 89]{Eaton2016a}.
	- *`outstr = regexprep (string, pat, repstr)`* \cite[\S5.5, pp. 90]{Eaton2016a}.
	- *`outstr = regexprep (string, pat, repstr, "opt1", ... ) `* \cite[\S5.5, pp. 90]{Eaton2016a}.
+ String set operations \cite[\S5.5, pp. 80]{Eaton2016a}:
	- *`str = strjoin (cstr)`*
	- *`str = strjoin (cstr, delimiter)`*
+ String comparison operations \cite[\S5.5, pp. 80-81]{Eaton2016a}:
	- *`strmatch (s, A)`*
	- *`strmatch (s, A, "exact")`*
+ String tokenization \cite[\S5.5, pp. 81-84]{Eaton2016a}:
	- *`[tok, rem] = strtok (str)`*
	- *`[tok, rem] = strtok (str, delim)`*
	- *`[cstr] = strsplit (str)`*
	- *`[cstr] = strsplit (str, del)`*
	- *`[cstr] = strsplit (..., name, value)`*
	- *`[cstr, matches] = strsplit (...)`*
	- *`[cstr] = ostrsplit (s, sep)`*
	- *`[cstr] = ostrsplit (s, sep, strip_empty)`*
+ String input operations + parsing \cite[\S5.5, pp. 84-86]{Eaton2016a}: 
	- *`[a, ...] = strread (str)`*
	- *`[a, ...] = strread (str, format)`*
	- *`[a, ...] = strread (str, format, format_repeat)`*
	- *`[a, ...] = strread (str, format, prop1, value1, ... )`*
	- *`[a, ...] = strread (str, format, format_repeat, prop1, value1, ...)`*
+ (Sub-)String replacement operations \cite[\S5.5, pp. 86]{Eaton2016a}:
	- *`newstr = strrep (str, ptn, rep)`*
	- *`newstr = strrep (cellstr, ptn, rep)`*
	- *`newstr = strrep (..., "overlaps", val)`*
+ String operations regarding regular expressions (regex), and do not
	involve substring search operations nor string matching
	\cite[\S5.5, pp. 90]{Eaton2016a}:
	- *`regexptranslate (op, s)`*


Notes based on experiential analysis:
+ Calling the function *`index(s,t,direction)`* with an invalid
	direction (i.e., not "first" nor "last") will result in a
	thrown error \cite[\S5.5, pp. 78-79]{Eaton2016a}.
	See [script](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-strings.m).



####	String Conversions

Functions for string conversions are found in 
	\cite[\S5.6, pp. 91-96]{Eaton2016a}.
	They convert between representations, such as ASCII, decimal,
	string (including left/right justification), binary, double,
	hexadecimal, single/double precision numbers/vector, and numbers
	of another base.
	They can also convert strings to upper case or lower case.
	In addition, they can convert between escape sequences/forms to
	their corresponding representations (as special characters).
+ *`bin2dec (s)`*
+ *`dec2bin (d, len)`*
+ *`dec2hex (d, len)`*
+ *`hex2dec (s)`*
+ *`dec2base (d, base)`*
+ *`dec2base (d, base, len)`*
+ *`base2dec (s, base)`*
+ *`s = num2hex (n)`*
+ *`n = hex2num (s)`*
+ *`n = hex2num (s, class)`*
+ *`str2double (s)`*
+ *`strjust (s)`*
+ *`strjust (s, pos)`*
+ *`x = str2num (s)`*
+ *`[x, state] = str2num (s)`*
+ *`toascii (s)`*
+ *`tolower (s)`*
+ *`lower (s)`*
+ *`toupper (s)`*
+ *`upper (s)`*
+ *`do_string_escapes (string)`*
+ *`undo_string_escapes (s)`*



####	Accessor Functions: Character Class Functions

Character class functions are a category of accessor functions that
	determine if a string array contains elements of a specific/given
	character class.
	That is, are the elements of the string alphanumeric, alphabetic,
	numeric (in decimal or hexadecimal), lower case, upper case,
	punctuation characters, whitespace characters, control characters,
	printable characters, or ASCII characters
	\cite[\S5.7, pp. 96-98]{Eaton2016a}:
+ *`isalnum (s)`*
+ *`isalpha (s)`*
+ *`isletter (s)`*
+ *`islower (s)`*
+ *`isupper (s)`*
+ *`isdigit (s)`*
+ *`isxdigit (s)`*
+ *`ispunct (s)`*
+ *`isspace (s)`*
+ *`iscntrl (s)`*
+ *`isgraph (s)`*
+ *`isprint (s)`*
+ *`isascii (s)`*


It also includes an accessor function to determine the charactes
	class property of a string; see *`isstrprop(str, prop)`*
	\cite[\S5.7, pp. 98]{Eaton2016a}.













###	Escape Sequences for Strings

With single-quoted strings, the backslash character is not treated as
	a special character \cite[\S5.1, pp. 67]{Eaton2016a}.

However, with double-quoted strings, the backslash character introduces
	an escape sequence to represent other characters, such as
	\cite[\S5.1, pp. 67-68]{Eaton2016a}:
+ backslash character, *literal representation* 
+ double-quote character, *literal representation*
+ single-quote character, *literal representation*
+ newline character
+ horizontal tab 










##	Information About The Workspace

For information about the workspace, including a list of defined variables
	and their properties, see \cite[\S7.3, pp. 127]{Eaton2016a}.










##	Data Containers and Data Structures

Two mechanism used by *GNU Octave* to contain arbitrary data types in
	a variable are \cite[\S6, pp. 99]{Eaton2016a}:
+ Structures:
	- "C-like."
	- "Indexed with named fields."
+ Cell arrays:
	- "Each element of the array can have a different data type annd/or
		shape."


###	Structures

A structure in *GNU Octave* is implemented as an associative array,
	which indices are limited to strings.
	Its syntax is similar to similar to structures in *C* (or "C-style
	structures") \cite[\S6.1, pp. 99]{Eaton2016a}. 


####	Structure Usage

To access/modify a field *f* of a structure *s*, concatenate the name
	of the structure with the name of the field with a period
	between them.
	E.g., *s.f* \cite[\S6.1.1, pp. 99]{Eaton2016a}.

The value of a structure can be printed on the console/terminal of
	*GNU Octave*, stating the structure's variable name would suffice.
	However, the order in which the fields are listed when printing
	a structure is random
	\cite[\S6.1.1, pp. 99]{Eaton2016a}.

The structure can be copied just like variables of data types.
	That is, its content would be copied into another variable
	\cite[\S6.1.1, pp. 99-100]{Eaton2016a}.

Structures are "treated" as values.
	Hence, fields/elements of a structure can "reference other
	structures" \cite[\S6.1.1, pp. 100]{Eaton2016a}.

Note that printing the value of a nested structure, which has
	structures embedded in a (i.e., top-level) structure, would only
	print the content of the first few-level (e.g., three) levels.
	The remaining embedded/nested levels are printed/represented as
	a *struct* array with its dimensions (but not content) specified
	\cite[\S6.1.1, pp. 100-101]{Eaton2016a}.

The *`function struct_levels_to_print()`* is used to determine or set
	the number of levels (of the nested structure) to print.
	*`val = struct_levels_to_print()`* is used to find out the
		number of levels (of the nested structure) to print. 
	*`old_val = struct_levels_to_print(new_val)`* is used to set the
		number of levels (of the nested structure) to print.
	*`struct_levels_to_print(new_val, "local")`* is used to set the
		number of levels (of the nested structure) to print locally,
		such that only the function and called subroutines are
		affected \cite[\S6.1.1, pp. 101]{Eaton2016a}.

Use the function *`print_struct_array_contents ()`* to determine or
	set the boolean flag that specifies whether to print the contents
	of the *struct* array.
	If the boolean flag is set to true, the contents of *struct* arrays
		would be printed \cite[\S6.1.1, pp. 101]{Eaton2016a}.
	*I have problems using the function
		`print_struct_array_contents()` correctly.*


Structures can be returned by functions as their output
	\cite[\S6.1.1, pp. 101-102]{Eaton2016a}.

To enumerate all elements of a structure, use a special form of the
	*`for`* statement for a variable (named *`expression`*)
	\cite[\S10.5.1, pp. 165-166]{Eaton2016a}.

	for [val, key ] = expression
		body
	endfor

The content of 2-D *struct*s are displayed/accessed via rows first,
	then columns during enumeration of such *structs*.
	That is, for 2-D *struct*s, rows are incremented before columns 
	are incremented.
	Alternatively, elements in 2-D *struct*s are accessed via
	(row,column) enumeration. 

In general, for *n*-D *struct*s, which entries are indexed as
	[i,j,k, ..., n], the elements are accessed in the following order:
+ increment i only
+ increment i and j 
+ increment i, j, and k
...
+ increment n only

The fields of a *struct* are enumerated/traversed in order.

####	Structure Arrays

A structure array is a subset of structures, and each of its fields
	"is [be] represented by a cell array." 
	Since these cell arrays have the same dimensions, a structure
	array can also be recognized as an array of structures, where
	each of these structures has identifical field.
	Alternatively, index and print the field/element of the structure.
	That is, use the vectors as indices to the structure array.
	Similarly, elements of a structure array can be deleted by
	assigning them to an empty matrix
	\cite[\S6.1.2, pp. 103]{Eaton2016a}.

To delete elements of a structure array by assigning each of these
	elements to an empty matrix \cite[\S6.1.2, pp. 104]{Eaton2016a}.



#####	Difficulties Faced

When I called the function size(x), on a nested *struct* "x", it always
	returns the array [1 1] as the size of the nested *struct*.
	It does not return a set of values that correctly/"correctly"
	indicates the size of the nested structure.
	See [h-structures.m](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/h-structures.m).

####	Structure Creation

Structures can be created using \cite[\S6.1.3, pp. 104]{Eaton2016a}:
+ the index operator *`.`*
+ the *`struct`* function
	- The functions accepts pairs of arguments (fieldname, and scalar or
		cell array) \cite[\S6.1.3, pp. 105-106]{Eaton2016a}
+ dynamic naming *`(var)`*, by using the variable's string value (or
	arbitrary string) as the field name \cite[\S6.1.3, pp. 104-105]{Eaton2016a}...
	Arbitrary strings can be used, in addition to "valid *Octave*
	identifiers"; this is not true for *MATLAB* scripts. 



The string used in dynamic naming does not have to be a valid
	*GNU Octave* identifier.
	Note that *MATLAB* does not allow dynaming naming to use arbitrary
	strings \cite[\S6.1.3, pp. 104-105]{Eaton2016a}.

The *`struct`* function requires pairs of arguments
\cite[\S6.1.3, pp. 104-107]{Eaton2016a}.

When elements of a *struct* are a mixture of scalar and cell arrays,
	the scalar arguments are expanded to form a structure array that
	has a consistent dimension \cite[\S6.1.3, pp. 104-105]{Eaton2016a}.

"To create a *struct* "that has/contains "a cell array as an individual
	field", wrap it in another cell array
	\cite[\S6.1.3, pp. 106]{Eaton2016a}.
	From personal experimentation in [h-structures.m](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/h-structures.m), when I specify the cell
		array using square brackets, an instance of the cell array is
		assigned to each field; curly braces are needed to assign
		each element in the cell array to each field of the *struct*;
		in the cell array, each element in the cell array is
		delimited/delineated by a comma (or white space).
	Also, from personal experimentation in [h-structures.m](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/h-structures.m), the cardinality/dimension 
		of cell arrays in each field should match; if there is only
		one value for a field, while the other fields have multiple
		values, that value is repeated *n* times (dimensionality of
		the cell array); else, an error is called when the
		dimensionality of this cell array does not match the
		dimensionalities of the other cell arrays.

**Note that the fields of a (ordinary scalar) *struct* should have fields
	that have the same cardinality/size/dimension. Else, the *struct*
	could contain contain false/erroneous information.**  

Use the function `isstruct(x)` to determine if `x` is a structure
	(or structure array). 
	If `x` is a structure or structure array, a boolean true is
	returned. Else, a boolean false is returned
	\cite[\S6.1.3, pp. 106]{Eaton2016a}.




####	Structure Manipulation 

Functions to control the fields of a structure, which can be a nested
	structure, are \cite[\S6.1.4, pp. 107-111]{Eaton2016a}:
+ *`numfields(s)`* returns the number of fields in the *struct* *s*. 
+ *`fieldnames(s)`* returns the names of fields in *s*, which can be
	a *struct* or an Octave (/Java) object, in a cell array.
+ *`isfield(x,"field_name")`* returns true if *field_name* is a field
	of *x*.
+ *`isfield(x,field_names)`* returns a bit vector indicating if each
	field name in *field_names* is a field of *x*.
+ *`new_struct = setfield (s, field[i], val[i], field[i+1], val[i+1], ...)`*
	copies the *struct* *s* to *struct* *new_struct*, and for each pair
	of field[i] and val[i], it will assign val[i] to field[i].
	If a field (e.g., 'field[n]') is provided without a corresponding
	value (i.e., 'value[n]'), an error will be called for the
	mismatching number of fields and values.
	**Note: I have a problem using `setfield()` for structure arrays.
	March 6, 2017: Abandon mission to learn how to do this.**
	For a single element of a structure array, I can use the normal
	`setfield()` function.
	The technical debt for not knowing how to use `setfield()` for
	structure arrays is when I have to enumerate elements in a
	structure array.
+ *`val = getfield (s, field)`* is an access method to obtain the
	value of the field *field* in the *struct* *s*.
+ *`val = getfield (s, sidx1, field1, fidx1,...)`*
	**Note: Currently, I have not learnd how to use `getfield()` for
	structure arrays. March 6, 2017; Technical debt: not being able
	to easily enumerate elements of a structure array, and the fields
	of each *struct* in the structure array.**
+ *`sout = rmfield(s, "f")`* removes the field *f* in the structure
	(or nested structure) *s*.
	If *f* is not a valid field of the (nested) structure *s*, an
	error is called.
+ *`sout = rmfield(s, f)`* removes the fields specified in the cell
	array of strings, *f*, from the structure (or nested structure)
	*s*.
+ *`[copy, p] = orderfields()`* for various function signatures.
	For function signature *`(s1)`*, the fields of *s* are arranged
	lexicographically.
	For function signature *`(s1,s2)`*, the fields of *s1* are
	arranged according to the order of fields of *s2*; *s1* and *s2*
	must have the same number and names of fields, else an error is
	called.
	For function signature *`(s1,{cellstr})`*, the fields of *s1* are
	arranged according to the order of strings in the cell array of
	strings *{cellstr}*.
	For function signature *`(s1,p)`*, the fields of *s1* are
	arranged according to the permutation vector *p*.
	The second output argument *p* is optional, and is a permutation
	vector that converts the old order to the new order.

#####	Difficulties Faced

I cannot use the function *`substruct()`*. Also, I cannot use 
	getfield() nor setfield().


####	Structure: Data Processing for Its Fields

Data in a structure can be enumerated as follows
	\cite[\S6.1.5, pp. 111-112]{Eaton2016a}: 
+ Use a *`for`* loop to enumerate the elements of a structure.
+ Use the *`structfun`* function to create user-defined functions
	for each field of a structure.
	- E.g., [\S19.3 Function Application](https://www.gnu.org/software/octave/doc/v4.0.1/Function-Application.html)
		or \cite[\S19.3 Function Application]{Eaton2016}
	- **[To Be Continued]**
+ Use another type of container to process the data; i.e., convert
	the *struct* into a cell array, followed by data processing.


The fields/elements of a *struct* are processed from the first to the
	last, or "right" to "left".



###	Cell Arrays

A cell array is a container that can contain variables of different
	sizes or types. 
	A cell array can be used just like $N$-dimensional arrays with
	the exception of the using curly braces as operators for allocation
	and indexing \cite[\S6.2, pp. 112]{Eaton2016a}. 

####	Cell Array Usage

A cell array can have fields/variables of different sizes.
	These fields/variables can be indexed, added/inserted, overwritten
	using curly braces \cite[\S6.2.1, pp. 112]{Eaton2016a}.
	
**[Note: I do not know if cell arrays (or *struct*s) can include
	functions in their containers.]**

A nested cell array is hierarchically displayed via *`celldisp()`*,
	and referenced by their index \cite[\S6.2.1, pp. 113]{Eaton2016a}.


*`celldisp(c)`* recursively displays the contents of the call
	array *c*. 
	Alternatively, *`celldisp(c, b)`* also recursively displays the
	contents of the cell array *c*, but indicates its name as *b*,	
	instead of *c* \cite[\S6.2.1, pp. 113]{Eaton2016a}.

*`iscell(x)`* determines if *x* is a cell array object.
	A boolean *true* is returned if *x* is a cell array object.
	Else, return boolean *false* \cite[\S6.2.1, pp. 113]{Eaton2016a}.

The script [h-multi-dimensionall-cell-array.h](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/h-multi-dimensionall-cell-array.h) indicates that embedded
	elements are displayed first, before visiting next cell/field.
	This demonstrates that the elements of multi-dimensional matrices
	are processed from the right-most dimension to the left-most
	dimension.


####	Cell Array Creation

A cell array can be created using currently available variables.
	It can also be created with empty matrices.
	The empty matrices contained in the cell array can be subsequently 
	filled with data \cite[\S6.2.2, pp. 114]{Eaton2016a}.

A multi-dimensional cell array can be created using the cell function
	with a set of positive integers, or a vector of positive integers,
	that describes its size/dimensions
	\cite[\S6.2.2, pp. 114]{Eaton2016a}.

Functions that describe the size of an object can also be used to
	describe the size of a cell array
	\cite[\S6.2.2, pp. 114]{Eaton2016a}:
+ size(x)
+ length(x)
+ numel(x)
+ rows(x)
+ columns(x)

*`cell(m,n,k,...)`*, or *`cell([m n k ...])`*, are functions to create
	new cell array objects, with the dimensions *N\*M\*K*.
	The set of positive integers do not have to be listed as a vector
	\cite[\S6.2.2, pp. 114]{Eaton2016a}.

Functions to transform numerical arrays, such as matrices, into cell
	arrays \cite[\S6.2.2, pp. 114-116]{Eaton2016a}:
+ *`c = num2cell(A)`* transforms numerical matrix *A* into cell
	array *c* \cite[\S6.2.2, pp. 115]{Eaton2016a}.
+ *`c = mat2cell(A,m,n)`*, or *`c = mat2cell(A,d1,d2,...)`*, are
	functions to transform a matrix *A* into a cell array *c*.
	Here, *d1,d2, ...* are dimensional arguments corresponding to the
	dimensions of *A* \cite[\S6.2.2, pp. 115-116]{Eaton2016a}.
+ *`c = cellslices(x,lb,ub,dim)`* maps an array *x* to a cell array
	of slices based on the index vectors *lb* and *ub*, for lower
	and upper bounds, respectively.
	The optional input argument *dim* determines the position of the
	index. If *dim* is not specified, slice along the first
	non-singleton [WikipediaContributors2017] dimension
	\cite[\S6.2.2, pp. 116]{Eaton2016a}.



####	Indexing Cell Arrays

Extract elements from cell arrays using the *'{'* and *'}'* operators.
	These operators enable access to elements of a cell array
	\cite[\S6.2.3, pp. 116]{Eaton2016a}.

However, "extract or access subarrays, which are still cell
	arrays," using the *'('* and *')'* operators.
	These operators enable access to a subarray of a cell array.
	They enable indexing cell arrays to be like indexing
	multi-dimensional arrays \cite[\S6.2.3, pp. 116-117]{Eaton2016a}.

Use the empty matrix *'[]'* to delete elements from a cell array,
	just like *struct* arrays and numerical arrays.
	This also deletes the *"vector"*/memory??? space for them, in
	addition to removing the contents of the cell array elements.
	That said, elements of a cell array can have their contents
	deleted/removed, without deleting the *"vector"*/memory??? space
	for them \cite[\S6.2.3, pp. 118]{Eaton2016a}.

These indexing operations operate on the cell array, rather than the
	objects within the cell array \cite[\S6.2.3, pp. 118]{Eaton2016a}.

The function *`y = cellindexmat(x, varargin)`* allows objects within
	each cell array entry to be indexed, via matrix indexing
	\cite[\S6.2.3, pp. 118]{Eaton2016a}.




####	Cell Array of Strings

The storage of multiple strings in a cell array, in comparison to
	that of character matrices, has the advantage of storing strings
	of varying lengths.
	Character matrices require its strings to be of the same length
	\cite[\S6.2.4, pp. 118]{Eaton2016a}.

Functions to convert between a cell array of strings and a character
	matrix are \cite[\S6.2.4, pp. 118-119]{Eaton2016a}:
+ *`char`* and/or *`strvcat`* can transform a cell array of strings
	into a character matrix \cite[\S6.2.4, pp. 118]{Eaton2016a}. 
+ *`cstr = cellstr(strmat)`* can transform a character matrix into
	a cell array of strings.
	This transforms each row of the character matrix *strmat* into
	an element in *cstr*, while deleting trailing white space in each
	element \cite[\S6.2.4, pp. 118-119]{Eaton2016a}. 

Since "most functions for string manipulations, provided by default
	in stable versions of *GNU Octave*, support cell arrays of
	strings, it is recommended to manipulate a collection/set of
	strings using cell arrays instead of character matrices
	\cite[\S6.2.4, pp. 119]{Eaton2016a}. 

By default, stable versions of *GNU Octave* provide support for the
	following string manipulation functions
	\cite[\S6.2.4, pp. 119]{Eaton2016a}:
+ *`strcmp(string, cell array of strings)`*
+ *`char`*
+ *`deblank`*
+ *`regexp`*
+ *`regexpi`*
+ *`str2double`*
+ *`strcat`*
+ *`strcmp`*
+ *`strcmpi`*
+ *`strfind`*
+ *`strmatch`*
+ *`strncmp`*
+ *`strncmpi`*
+ *`strtrim`*
+ *`strtrunc`*
+ *`strvcat`*

*`iscellstr(cell)`* is a function that returns *true* if each element
	of the cell array is a character string
	\cite[\S6.2.4, pp. 119]{Eaton2016a}.



####	Data Processing with Cell Arrays

Data in a cell array can be enumerated using
	\cite[\S6.2.4, pp. 119]{Eaton2016a}.:
+ *`for`* loops.
+ "*`cellfun`* function that calls a user-specified function on all
	elements of a cell array"
+ Convert data into a different container, such as a matrix or
	a *struct* \cite[\S6.2.4, pp. 119-120]{Eaton2016a}
	- *`m = cell2mat(c)`* concatenates all elements of the cell array
		*c* in its transformation into a hyperrectangle.
		Elements of *c* must be concatenable by the function *`cat`*
		and can be either of the following types:
		* numeric
		* logical 
		* character matrix
		* cell arrays
		* *struct*s
	- *`cell2struct(cell, fields, dim)`* and
		*`cell2struct(cell, fields)`* transforms a cell array *cell*
		into a strucure *struct*.
		The cardinality of *fields* (number of fields) and the
		cardinality of *cell* (its number of elements along dimension
		*dim*) should match.
		*`numel(fields) == size(cell, dim)`*
		By default, the optional argument/parameter *dim* has a
		value of 1.



### Lists

####	Comma Separated Lists

For all *GNU Octave* functions, a comma separated list (or *cs-list*)
	is a fundamental input/return argument type.
	That is, the set of input arguments and the set of return
	arguments are both *cs-list*s
	\cite[\S6.3, pp. 120]{Eaton2016a}.

*cs-list*s can also appear on either side (left or right) of an
	asignment statement \cite[\S6.3, pp. 120]{Eaton2016a}.

During the initialization/creation of an array (with *[]*) or cell
	array  (with *{}*), *cs-list*s are also used
	\cite[\S6.3, pp. 120]{Eaton2016a}.

That said, *cs-list*s cannot be directly manipiulated by users, but
	can be implicitly manipulated via structure arrays and cell arrays
	before their conversion into *cs-list*s
	\cite[\S6.3, pp. 121]{Eaton2016a}.

Transform element of a cell array into a *cs-list* by placing the
	*`{}`* operators around the cell array
	\cite[\S6.3.1, pp. 121-122]{Eaton2016a}.

Transform a *cs-list* into a cell array by placing the *`[]`*
	operators around the *cs-list*.
	This "concatenates" the elements of the *cs-list* into a cell
	array, by treating with element in the *cs-list* as a
	field/variable (or cell element) in the cell array
	\cite[\S6.3.1, pp. 121-122]{Eaton2016a}. 

Cell elements of a cell array can be an input argument of a function.
	Hence, a list of such cell elements can be passed as an input
	argument to the given function.
	This is no different from calling the function with each cell
	element passed to the function as an individual/separate argument
	\cite[\S6.3.1, pp. 121-122]{Eaton2016a}.  

Transform a structure array, *struct*, into a *cs-list* via dynamic
	naming with the function *`struct`*. Its dynamic names can be
	used to retrieve information from the elements of the *cs-list*
	\cite[\S6.3.2, pp. 122]{Eaton2016a}.






####	Variable-length argument lists

Self-explanatory.

####	Variable-length return lists

Self-explanatory.













## Object-Oriented Programming



















##	Performance Improvement

Techniques for performance improvement
	\cite[Slide 48, ``Techniques for improving performance'']{Zucchelli2011}:
+ Vectorization
	- "Brute force vectorization"
		* cellfun
		* structfun
		* arrayfun
		* **[To Be Continued]**
	- Use libraries
		* BLAS
		* LAPACK
+ "Preallocation: Minimize changing variable class".
+ "Mexing: compiled code"










##	Miscellaneous

###	Formatted Output

Conversion specifications \cite[\S14.2.4 Formatted Output]{Abbott2016}:
+ '%d': scalar argument, decimal notation
+ '%s': string argument
+ '%o': integer argument, octal radix
+ '%u': integer argument, decimal radix
+ '%x': integer argument, hexadecimal radix
+ '%c': character value 
+ '%f': fixed-point notation
+ '%e': exponential notation
+ '%g': fixed-point or exponential notation

For these aforementioned specific conversion specifications \cite[\S14.2.4 Formatted Output]{Abbott2016}:
+ Specific modifiers can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.
+ Specific flags can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.
+ These aforementioned flags and modifiers can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.  

### Terminal Output

To change the number of significant figures displayed in the terminal output, use the command *format[options]*, where the options are indicated as follows \cite[14.1.1 Terminal Output]{Abbott2016}:
+ *short*: Fixed point format with 5 significant figures in a field that is a maximum of 10 characters wide. (default).
+ *long*: Fixed point format with 15 significant figures in a field that is a maximum of 20 characters wide.



###	Block Comments

Block comments are enclosed "between matching '#{' and '#}' (or '%{' and '%}') markers" \cite[\S2.7.2, Block Comments, pp. 37-38]{Eaton2016a}

###	Continuation Lines \cite[\S10.10, pp. 169]{Eaton2016a}

By default, statements terminate with the newline character.

To continue a statement over multiple lines, use the ellipsis ("...")
	to list a fragment of a statement in a line that would be
	continued in the next line.

To continue a string over multiple lines, use the backslash ("\") to
	to list a fragment of a string in a line that would be
	continued in the next line.

Mathematical expressions that are contained within a pair of
	parentheses can be continued over multiple lines without using
	any continuation markers, such as the aforementioned ellipsis
	or backslash. 

###	Copy Functions

The function `deal(a)` is used to reproduce/copy data/information from
	"the input parameters [to] the corresponding output parameters"
	\cite[Definition of deal]{OctaveForgeContributors2017a}.



###	Documentation Generation

To automatically generate documentation for *GNU Octave*
	scripts/programs, use [Texinfo](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/texinfo.md).



###	Executable and Self-Contained *GNU Octave* Scripts

To execute self-contained *GNU Octave* scripts, use the UNIX shebang
	\cite[\S2.6, pp. 36]{Eaton2016a} \cite{WikipediaContributors2017a}
	at the start of the script, so that the rest of the script's
	initial line would be parsed as an interpreter directive.
	It runs the specified interpreter program, command-line
	*GNU Octave*, instead.

That is, the first line of an executable, self-contained *GNU Octave*
	script should contain the following:

	#![location of the command-line GNU Octave] [-qf]

The file permissions of such a script in *UNIX*-like operating systems
	should be changed to make the script executable, using the
	*`chmod`* command \cite[\S2.6, pp. 36]{Eaton2016a}.

The optional *`-qf`* option disables printing of the normal startup
	message.
	It also provides some form of standard behavior/performance across
	different installations of *GNU Octave*, which can be customized
	via the *`.octaverc`* file in the home directory.
	\cite[\S2.6, pp. 36]{Eaton2016a}.

Executable, self-contained *GNU Octave* scripts enable batch
	processing of data sets \cite[\S2.6, pp. 36]{Eaton2016a}.

Use the built-in function *`argv`* to retrieve the command line
	arguments passed to the executable *GNU Octave* script
	\cite[\S2.6, pp. 37]{Eaton2016a}.
	
E.g., the following is entered in the command line.

	./[name-of-GNU-Octave-script].m [ip_arg1] [ip_arg2] ... [ip_argN]

The input arguments to the aforementioned execution of the script
	*`./[name-of-GNU-Octave-script].m`* are:
	*`[ip_arg1] [ip_arg2] ... [ip_argN]`*.


###	Variables

A variable name is a sequence of alphanumeric characters and
	underscores, which does not begin with a digit.
	It is case sensitive \cite[\S7, pp. 123]{Eaton2016a}.


Generally, variable names that begin and end with two consecutive
	underscores ('__') are reserved for GNU Octave's internal usage.
	They are used "to access documented internal variables and
	built-in symbolic constants" of *GNU Octave*
	\cite[\S7, pp. 123]{Eaton2016a}.

When the result of the previous/last computation (or "most recently
	computed result")  is not assigned to a variable, it is assigned
	to the built-in variable '***ans***'
	\cite[\S7, pp. 123]{Eaton2016a}.

Like other popular scripting languages, such as *Ruby* and *Python*,
	*GNU Octave* uses static typing.
	That is, each "variable in *GNU Octave*" has no fixed type
	\cite[\S7, pp. 123]{Eaton2016a}.

Some functions concerning variables are
	\cite[\S7, pp. 123-124]{Eaton2016a}:
+ *`isvarname(nome)`*
	- Function that returns a boolean *True* value, if the input
		argument *nome* is a valid variable name.
		Else, return *False*.
+ *`varname = genvarname (str, [exclusions])`* and
	*`eval([varname " = [numeric value]])`* are used to create (a)
	valid unique variable name(s) from *str*, and define them
	with numeric value(s) (*[numeric value]*).
	Any sequence of characters in *str* that is not alphanumeric nor
	an underscore would be replaced with an underscore. 
	If *str* begins with a digit, the character *'x'* is added to the
	beginning of *str * as a prefix. 
	Also, the function *`genvarname (str, [exclusions])`* would not
		generate variable names that begin and end with two
		consecutive underscores ('__'), nor variable names that match
		keywords or function names.
	*[exclusions]* is an optional string or cell array of strings.  
+ *`namelengthmax()`* returns maximum length of a variable name.
	This function is compatible with *MATLAB*, is considerably less
		than the maximum length of strings in *GNU Octave*, which is
		(2^{31} - 1).

####	Global Variables

Declare a global variable by placing the keyword *global* before the
	variable name(s) \cite[\S7.1, pp. 124-125]{Eaton2016a}.

E.g., global variable_name1 variable_name2 variable_name3.

E.g., global variable_name4 = [a number].

A global variable cannot be initialized to different values on
	multiple occasions.
	A global variable will retain the first value that it is
		initialized to.
	Use the command *`clear all`* to allow the global variable to be
		initialized to a different variable \cite[\S7.1, pp. 125]{Eaton2016a};
		this would also delete all local and global user-defined
		variables, and functions, from the symbol table
		\cite[\S7.3, pp. 131]{Eaton2016a}.
	In general, a global variable can be changed to a different value
	you assign a new value to the global variable, without redeclaring
	it as a global variable again; see [script to show various usage of global variables](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m).
	After the initial assignment of a global variable, subsequent
	assignment of a global variable to other values must not invoke
	use of the keyword *'global'* (in these reassignment statements).


When a global variable is passed as an input argument during a
	function call, a local copy of the global variable will be made
	within the scope of the function call.
	The local copy, which is a local variable, can be initialized to
	a value different from the global variable; the global variable
	has a value that remains unchanged.
	The global variable can be changed to a different value when it
	is declared as a global variable in the body of a function;
	see [script to show various usage of global variables](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m)
	\cite[\S7.1, pp. 125]{Eaton2016a}.

The function *`isglobal(name)`* returns *True* if *name* is a global
	variable; else, it returns *False* \cite[\S7.1, pp. 125]{Eaton2016a}.


####	Persistent Variables

Declaring a variable as persistent inside a function allows it to
	keep its value between calls to the aforementioned functions. 
	This persistent variable is local in scope to the aforementioned
	function, and is not accessible elsewhere.
	It cannot be initialized multiple times.
	When initialized multiple times with the 'persistent' keyword,
	only its first instance counts.
	The value of a persistent variable can be changed, when the
	'persistent' keyword is not used in the statement that changes
	its value.
	If it is "not initialized to a specific value, it will contain an
	empty matrix."
	Hence, before using a persistent variable, it would be prudent
	to judiciously test if it is an empty matrix before using it.
	Its value is only reset to its first initialized value, or to an
	empty matrix, if it is cleared from memory via the *`clear`*
	function, such as *`clear all`* or *`clear [name_of_persistent_variable]`*.
	Its behavior is equivalent to that of a static variable in *C*,
	*C++*, and *Java*
	\cite[\S7.2, pp. 126-127]{Eaton2016a}.

The *`mlock`* function should be used to retain the value of a
	persistent variable after the function containing it has been
	cleared from memory \cite[\S7.2, pp. 126-127]{Eaton2016a}.


####	Status of Variables

There are several functions to determine the status of variables: 
+ *`who`* function, and its siblings *`whos`* and *`whos_line_format`*
	inform the user different information about data in the memory
	\cite[\S7.3, pp. 127-130]{Eaton2016a}.
	- *`who [option] [list of patterns]`* is a function that carries
		out pattern matching, using the given *[list of patterns]* in
		the optional input argument, on the set of currently defined
		variables (in memory).  
		This function only accepts zero or one option, and does not
		accept multiple options.
		For each pattern in the *[list of patterns]* optional input
		argument, it can be described using a simple (formal) grammar
		for regular expressions (regex), including the use of special
		characters \cite[\S7.3, pp. 131]{Eaton2016a}.
		If patterns are not given as input arguments during a
		function call of *`who`*, all variables would be listed.
		Calling the function *`who`* only displays the local variables
		in the current scope.
		To list global and local variables, use the *[global]* option.
		Use the *[-regexp]* option to process the each pattern as a
		regular expression; the syntax for patterns based on regular
		expression is equivalent to that for the *`regexp`* function.
		The *[-file]* option treats the next (optional) input argument 
		as a filename. Consequently, the specified file is parsed
		and all of its variables are listed. When this option is
		invoked, it does not process any input pattern. 
		\cite[\S7.3, pp. 128]{Eaton2016a}.
	- *`whos [option] [list of patterns]`* is a function that provides
		information about the list of "currently defined variables"
		that matches the specified patterns *[list of patterns]*,
		which is/are provided as (an) optional input argument(s).
		Its optional input arguments defined according to their
		equivalent counterparts of the *`who [option] [list of
		patterns]`* function.
		Information presented about the variables fall into the
		following categories:
		* Atrribute
		* Name
		* Size
		* Bytes
		* Class
		This information is presented in a tabular form
		\cite[\S7.3, pp. 128-129]{Eaton2016a}.
	- *`whos_line_format([new_value],["local"])`* is a function that
		queries or specifies the format and alignment of the tabular
		representation of information of variables for the
		*`whos [option] [list of patterns]`* function
		\cite[\S7.3, pp. 129-130]{Eaton2016a}.
+ Use the function *`exist(name,[type])`* to determine if *name* is
	declared to be of the type *[type]*. If it is, return *True*.
	Else, return *False*.
	The input argument *[type]* is optional. If it is not specified
	by the user as an input argument, the *GNU Octave* interpreter
	would check if any variable, built-in function, oct-file, 
	directory, file (function file specifying a custom function), or
	class is declared with the name *name* (or is named *name*)
	\cite[\S7.3, pp. 130-131]{Eaton2016a}.
+ The following functions allow memory to be manually managed, in case
	if *GNU Octave*'s automatic garbage collection (or memory
	management) fails to provide enough memory space for computation
	\cite[\S7.3, pp. 131]{Eaton2016a}:
	- The function *`clear [options] [list of patterns]`* allows specified variables (as input
		arguments), or all variables, to be removed manually from
		memory \cite[\S7.3, pp. 131-132]{Eaton2016a}.
		For each pattern in the *[list of patterns]* optional input
		argument, it can be described using a simple (formal) grammar
		for regular expressions (regex), including the use of special
		characters \cite[\S7.3, pp. 131]{Eaton2016a}.
		If no pattern is provided as an input argument to the function
		*`clear`*, *GNU Octave* removes "all user-defined variables
		(local and global)" "from the symbol table"  
		\cite[\S7.3, pp. 131]{Eaton2016a}.
		When at least one pattern is specified as an input argument to
		the function *`clear`*, *GNU Octave* removes only visible
		user-defined variables and funtions
		\cite[\S7.3, pp. 131]{Eaton2016a}.
		The options allow users to have more control in pattern
		matching using regular expressions
		\cite[\S7.3, pp. 131-132]{Eaton2016a}.
	- The function *`pack`* consolidates memory in *MATLAB*'s
		workspace, but does nothing in *GNU Octave*, and is provided
		as a built-in function for compatibility purposes
		\cite[\S7.3, pp. 132]{Eaton2016a}.
+ The following functions allow users to determine certain information
	about functions, variables, operators, keywords, and files.
	Typically, such functions are more valuable during software
	development of *GNU Octave*-based programs/scripts than to provide
	certain information for the *GNU Octave*-based programs/scripts
	to use during execution \cite[\S7.3, pp. 132]{Eaton2016a}.
	- The function *`type [-q] [list of names]`* displays the content
		of a variable, function, file, or directory that has a name
		matching any name in the *[list of names]*.
		If the user declares the name *name* to be of different types
		throughout the *GNU Octave*-based program/script, the visble
		user-defined variable/function would used/processed.
		If any of the names in the *[list of names]* does not match
		an existing variable, function, operator, keyword, or file,
		it is undefined and it will cause an error to be thrown at
		run time. See [("commented out") implementation of this in this hyperlinked script](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m)





[Repeat]
Use the command *`clear all`* to allow the global variable to be
		initialized to a different variable \cite[\S7.1, pp. 125]{Eaton2016a};
		this would also delete all local and global user-defined
		variables, and functions, from the symbol table
		\cite[\S7.3, pp. 131]{Eaton2016a}





###	Expressions




###	Statements













##	Compatibility with *Matlab*

For compatibility between *GNU Octave* and *Matlab*, see the section "Differences between Octave and MATLAB" [TheUniversityOfTexasAtAustinStaff2016].

Some information to note are [TheUniversityOfTexasAtAustinStaff2016]: 
+ Loading files
	- Use absolute path; use relative paths otherwise.
	- Files are loaded differently in *GNU Octave* and *Matlab*.
+ Use "C-style autoincrement and assignment operators" in *GNU Octave*
	but not in *Matlab*.
+ *GNU Octave* and *Matlab* have compute the product of
	boolean values differently.
	- *GNU Octave* usues "prod," and *Matlab* does not.
+ *GNU Octave* fucntions and variables that do not exist in *Matlab*:
	- nargin
+ *GNU Octave* allows an array of varying-length strings,
	while *Matlab* does not.
	
	*GNU Octave* enables left single quotes to surround a string, and 
		right single quotes to surround a string.
+ *GNU Octave* does not allow empty files to be loaded, but *Matlab*
	does allow empty files to be loaded.
+ *GNU Octave* allows *"printf"* to print a string to standard output,
	but *Matlab* does not; for *Matlab*, use *"printf"* to print
	a string to standard output or to a file (via a "file-handle").
	array	"MATLAB has no fputs function."
+ *GNU Octave* allows whitespace before the transpose operator, but
	*Matlab* does not.
+ *GNU Octave* does not require the use of ellipses for line continuation
	but *Matlab* does.
	 
	Use a backslash "\" to indicate line continuation.
+ *GNU Octave*'s e operators may be rendered unacceptable by
	*Matlab*.
+ *GNU Octave* have toolboxes for different applications, just like
	*Matlab*'s toolboxes.

	In *GNU Octave*, the "system data structure" (i.e., system model)
		requires the installation of the Octave Controls System Toolbox.
+ Comment, for single lines:
	- *Matlab*: percent sign
	- *GNU Octave*: pound sign, or percent sign
+ Exponentiation:
	- *Matlab*: "^"
	- *GNU Octave*: "^" or "**" 
+ String delimiters:
	- *Matlab*: "'"
	- *GNU Octave*: "'" or """
+ For **ends**:
	- *Matlab*: requires **end**
	- *GNU Octave*: use "end{if,for, ...}"














#	Enabling Seamless Interoperability Between Programming Languages

See [Interoperability Between Programming Languages](interoperability-between-programming-languages.md).

##	Integrating *GNU Octave* Code Into *C++* Code

To integrate *GNU Octave* code into a *C++* codebase, include the header file *"octave/oct.h"*.

That is, use:

	#include \<octave/oct.h\>

See [C++ integration; including *GNU Octave* code into a *C++* codebase](https://en.wikipedia.org/wiki/GNU_Octave#C.2B.2B_integration) [WikipediaContributors2016].


##	Integrating *C++* Code Into *GNU Octave* Code

To integrate *C++* code into a *GNU Octave* codebase, create
	*oct* files and use them in my codebase.

Alternatively, I can create *Matlab*-compatible *MEX* files
	and use them in my codebase. 

See [C++ integration; including *GNU Octave* code into a *C++* codebase](https://en.wikipedia.org/wiki/GNU_Octave#C.2B.2B_integration) [WikipediaContributors2016].

###	Creating *oct* Files

Use the *mkoctfile* function to compile the C, C++, or Fortran
	source code into either of the following, based on the options
	used with the *mkoctfile* function 
	[TheUniversityOfTexasAtAustinStaff2016]:
+ Compiled code that can be called within *GNU Octave*
+ Stand-alone *GNU Octave* application

Call the *mkoctfile* function from the shell prompt of the "Terminal"
	application or the *GNU Octave* prompt 
	[TheUniversityOfTexasAtAustinStaff2016]
















#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).
 
+ [WikipediaContributors2016]
	
	Wikipedia contributors, "GNU Octave," in {\it Wikipedia, The Free Encyclopedia: Free mathematics software}, Wikimedia Foundation, San Francisco, CA, October 16, 2016.
	
	Available online at: \url{https://en.wikipedia.org/wiki/GNU_Octave}; last accessed on October 25, 2016.

+ [WikipediaContributors2016a]
	
	Wikipedia contributors, "Class (computer programming)," in {\it Wikipedia, The Free Encyclopedia: Programming constructs}, Wikimedia Foundation, San Francisco, CA, December 1, 2016.
	
	Available online at: \url{https://en.wikipedia.org/wiki/Class_(computer_programming)}; last accessed on December 4, 2016.

+ [WikipediaContributors2017]
	
	Wikipedia contributors, "Singleton (mathematics)," in {\it Wikipedia, The Free Encyclopedia: Basic concepts in set theory}, Wikimedia Foundation, San Francisco, CA, January 7, 2017.
	
	Available online at: \url{https://en.wikipedia.org/wiki/Singleton_(mathematics)}; last accessed on April 16, 2017.

+ [TheUniversityOfTexasAtAustinStaff2016]

	The University of Texas at Austin staff, "Sysnet's Documentation," in {\it Institute for Computational Engineering and Sciences}, Institute for Computational Engineering and Sciences, Cockrell School of Engineering and College of Natural Sciences, The University of Texas at Austin, Austin, TX, October 6, 2016.
	
	Available online at: \url{https://www.ices.utexas.edu/sysdocs/}; last accessed on October 26, 2016.
	















#	Author Information

The MIT License (MIT)

Copyright (c) <2016-2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


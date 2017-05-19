#	Notes About *GNU Octave*

+ [Basic Operations for *GNU Octave*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#basic-operations-for-gnu-octave)
+ [Build Automation for *GNU Octave*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#build-automation-for-gnu-octave)
+ [Functions](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#functions)
+ [Pseudo-Random Number Generation (PRNG) in *GNU Octave*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#pseudo-random-number-generation-prng-in-gnu-octave)
+ [Error Management](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#error-management)
+ [Debugging](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#debugging)
+ [Data Types, Including Strings](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#data-types-including-strings)
+ [Information About The Workspace](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#information-about-the-workspace)
+ [Data Containers and Data Structures](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#data-containers-and-data-structures)
+ [Object-Oriented Programming](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#object-oriented-programming)
+ [Performance Improvement](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#performance-improvement)
+ [Miscellaneous](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#miscellaneous)
+ [Compatibility with *Matlab*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#compatibility-with-matlab)
+ [Enabling Seamless Interoperability Between Programming Languages](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#enabling-seamless-interoperability-between-programming-languages)
+ [References](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#references)
+ [Author Information](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#author-information)









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
	*GNU Octave* scripts, we have to do the following:
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

When we make a function call, we can use more arguments than specified
	as function parameters.
	The extra arguments are ignored.


Experimentally/Empirically demonstrated in the execution of the
	*Make* target *torture*. See: [link to sandbox/gnu-octave](../sandbox/gnu-octave).


Functions in *GNU Octave* can return multiple values.
	The values returned from a function call can be assigned to
	a list of expressions, specifically a list of variable names or
	index expressions, via a multiple assignment expression
	\cite[\S8.1.1, pp. 137]{Eaton2016a}.


A function can be implemented such that only a subset of the return
	variables have return values.
	If this is the case, the return variables without return values
	would cause a warning \cite[\S11.3, pp. 176]{Eaton2016a}.


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




###	Variable-length argument lists

Use a special parameter name *vargin*, instead of a fixed set of
	parameters, to contain a list of input arguments of variable
	length.
	*vargin* is a cell array that contains all the input arguments,
	which can be of varying length
	\cite[\S11.4, pp. 182-183]{Eaton2016a}.




###	Ignoring Input Arguments and Output/Return Variables

Ignore input arguments and output/return variables by placing a tilde
	symbol *'~'* as a placeholder where the input variable, or
	output/return variable should be during the function call.
	This allows such input arguments and/or output/return variables
	to be ignored during the computation of this function
	\cite[\S11.5, pp. 184]{Eaton2016a}.



###	Variable-length return lists

To allow the return list to be of variable length, use a special
	parameter name *varargout*, instead of a fixed set of parameters,
	to contain a cell array of return/output variables.
	*varargout* is a cell array that contains all the return/output
	arguments, which can be of varying length
	\cite[\S11.6, pp. 184-185]{Eaton2016a}.

The function *`[r1,r2,...,rn] = deal(a1,a2,...,an)`* and
	*`[r1,r2,...,rn] = deal(a)`* copies the input arguments to the
	corresponding return/output variables.
	For the first function call, *`ri = ai`*, where
	*i \in {1,2,...,n}*.
	For the second function call, *`r1 = r2 = ... = rn = a`*.
	With comma separated lists, cell arrays, or structures, avoid
	the function call overhead by using the operator *':'* to
	select/specify entire rows/columns
	\cite[\S11.6, pp. 185]{Eaton2016a}.

###	Returning from a Function

A return statement for a user-defined function only consists of the
	keyword *`return`*. 
	It returns control to the caller of the function/script immediately.
	When called at the top level, it is ignored.
	It is assumed that a return statement exists "at the end of every
	function definition"
	\cite[\S11.7, pp. 185-186]{Eaton2016a}.


###	Default Arguments for Functions

Default values for input arguments of functions can be assigned in
	the function definition. 
	In the declaration of input parameters, default values can be
	assigned to input parameters (in the input argument list).
	E.g., *`function function_name(arg1=val1,arg2=val2,...)`* assigns
	the values of *val1* and *val2* to *arg1* and *arg2*, respectively. 
	During the function call of *`function_name(...)`*, if the caller
	did not provide values for all input arguments, because of the use
	of *`:`* or missing input arguments, the default values for *arg1*
	and *arg2* are used instead
	\cite[\S11.8, pp. 186-187]{Eaton2016a}.





###	Function files

Function files should only contain one function each
	\cite[\S11.1, pp. 171]{Eaton2016a}.
	It begins with the keyword *`function`*, which is a requirement
	for a function file.
	The scope of variables in the function file is local, and
	restricted only to other variables in this function
	\cite[\S11.10, pp. 198]{Eaton2016a}.

The function *`ignore_function_time_stamp("all")`* causes the time
	stamps for all function files to be ignored
	\cite[\S11.9, pp. 187,189]{Eaton2016a}.
	When this function is called with the *"none"* flag, *GNU Octave*
	would determine if function files need to be recompiled due to
	changes with the time stamp of files
	\cite[\S11.9, pp. 189]{Eaton2016a}.

####	Load Path Access and Modification

A list of functions for accessing and modifying the load path is
	provided in \cite[\S11.9.1, pp. 189-192]{Eaton2016a}.


####	Subfunctions

Subfunctions are secondary functions that the primary/first function
	in a function file would call.
	Its scope is limited to functions in that function file 
	\cite[\S11.9.2, pp. 192]{Eaton2016a}.
	Here is an example of a [function in a function file](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/j-main.m)
	calling [subfunctions](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/j_subfunctions.m).


####	Private Functions

My [implementation](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/gnu-octave/z-dir) of private functions was **unsuccessful**.
	Similarly, my [test case for private functions](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/gnu-octave/y-dir) **failed**, too.

####	Nested Functions

Usage of nested functions are strongly discouraged
	\cite[\S11.9.4, pp. 193]{Eaton2016a}.

Also, do not use rge *`eval()`* function together with nested
	functions \cite[\S11.9.4, pp. 194]{Eaton2016a}.

####	Overloading and Autoloading

*GNU Octave* supports function overloading by allowing functions of
	the same name to have different sets of input arguments.
	It is strongly encouraged to use object-oriented programming to
	overload functions \cite[\S11.9.5, pp. 195]{Eaton2016a}.

Use the *`builtin()`* function to call the base function of the
	overloaded function for the given function signature (set of
	input arguments) 

*GNU Octave* supports function autoloading to allow users to
	specify/define where a given function can be found.
	This enables functions in dynamically linked files to be found,
	even if the operating system in use does not support symbolic
	links.
	Use the *`autoload`* function to do this
	\cite[\S11.9.5, pp. 195]{Eaton2016a}.

####	Function Locking

A function can be locked into memory, so that its location in memory
	would not be affected by the operating system.
	It is recommended for usage with dynamically linked functions, or
	functions in dynamically linked files
	\cite[\S11.9.6, pp. 196-197]{Eaton2016a}.


####	Function Precedence

The precedence of functions used in a given scope is provided in
	\cite[\S11.9.7, pp. 197-198]{Eaton2016a}.






####	Side Notes About Function Files

When *GNU Octave* encounters an undefined identifier during execution,
	it will look up the symbol table to search for variables and
	compiled functions prior to search searching directories specified
	in its load path \cite[\S11.10, pp. 198]{Eaton2016a} for a
	function file corresponding to that undefined identifier.
	*GNU Octave* may reload the file when the time stamp on the file
	changes or when the current working directory is modified/changed
	\cite[\S11.9, pp. 187]{Eaton2016a}.








###	Script Files

A *GNU Octave* script file is a regular file containing a list/sequence
	of *GNU Octave* commands.
	That is, it does not begin with the keyword *`function`*, which is
	a requirement for a function file.
	The scope of variables in the script file is not restricted to
	being local.
	The script file can have definitions for multiple functions, and
	can load all of them at once; however, only one function can
	execute at any given instance \cite[\S11.10, pp. 198]{Eaton2016a}.


Use the *`path`* function to determine if the script file is in the
	load path of *GNU Octave* \cite[\S11.10, pp. 198]{Eaton2016a}.

The command *`source([filename])`* allows commands from the file
	*[filename]* to be parsed and executed
	\cite[\S11.10, pp. 199]{Eaton2016a}.


###	Function Handles

"A function handle is a pointer to another function," and can be
	defined as *`function_handle = @function_name`*
	\cite[\S11.11.1, pp. 199]{Eaton2016a}.

Functions to query if a variable is a function handle or provide
	information about a function handle are described in
	\cite[\S11.11.1, pp. 200]{Eaton2016a}.

###	Commands

Commands belong to a special category/class of functions that requires
	all of its input arguments to be strings.
	A command can also be called without parentheses 
	\cite[\S11.12, pp. 203]{Eaton2016a}.

The following are equivalent \cite[\S11.12, pp. 203]{Eaton2016a}:

	cmd arg1 arg2 ...

	cmd(arg1,arg2,...)

Note that when invoking/calling commands with string variables,
	parentheses have to be used so that the variable name does not
	get treated as a string
	\cite[\S11.12, pp. 203]{Eaton2016a}.

###	Library of *GNU Octave* Functions: Provided by default

The organization of *GNU Octave* functions, which is provided by
	default in the *GNU Octave* library, is shown in
	\cite[\S11.13, pp. 203-204]{Eaton2016a}.

















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

For preconditions, check the number and type of input parameters
	\cite[\S9.1, pp. 156]{Eaton2016a}.

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

We cannot raise an error with an identifier. We have tried using
	a string or a number in vain.

After multiple errors are raised, we cannot increment the value of
	beep_on_error(), via beep_on_error(new_error_value).
Before an error occurs, the error value is zero.
Subsequently, it is raised to one.

We have problems using the onCleanup() correctly, without causing
	errors due to my poor understanding of its function arguments.
		 


###	Catching Specific Errors

Specific errors can be caught, if only one potentially error raising
	operation is placed within the *try* block.
While **lasterr** and **lasterror** can help me obtain information
	about it, if we assign that error to a name in the specification
	of the *catch* block, we can access information about that
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

**We are skipping the subsections on "Breakpoints" and "Call Stack"
	for the time being.**

###	Debug Mode Difficulties

We can enter the debug mode using *debug_on_interrupt()*, when we
	interrupt execution of the *GNU Octave* program/script using
	*Ctrl-C* on the *Terminal*.

However, we cannot enter the debug mode using warnings, or errors, yet.

###	Profiling

**We are skipping the subsection on "Profiling" for the time being.**















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

Note that `NA != NA`, hence we could not compare the equality of	`NA`
	values using `==` or `!=`.
Instead, we should use the `isna(x)` function
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
	*We have problems using the function
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

When we called the function size(x), on a nested *struct* "x", it always
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
	From personal experimentation in [h-structures.m](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/h-structures.m), when we specify the cell
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
	**Note: We have a problem using `setfield()` for structure arrays.
	March 6, 2017: Abandon mission to learn how to do this.**
	For a single element of a structure array, we can use the normal
	`setfield()` function.
	The technical debt for not knowing how to use `setfield()` for
	structure arrays is when we have to enumerate elements in a
	structure array.
+ *`val = getfield (s, field)`* is an access method to obtain the
	value of the field *field* in the *struct* *s*.
+ *`val = getfield (s, sidx1, field1, fidx1,...)`*
	**Note: Currently, we have not learnd how to use `getfield()` for
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

We cannot use the function *`substruct()`*. Also, we cannot use 
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
	
**[Note: We do not know if cell arrays (or *struct*s) can include
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

[Summarize my thoughts on adopting object-oriented programming in
	GNU Octave]

###	Class Creation

To create a class in *GNU Octave* named *class-name*,  create a
	directory named *`@class-name`*.
	The *'@'* symbol must be a prefix for the name of the directory
	representing a class in *GNU Octave*
	\cite[\S34.1, pp. 721]{Eaton2016a}.

The constructor for the class should have the same name as the class
	name *class-name*; i.e., *`@class-name/class-name.m`* 
	\cite[\S34.1, pp. 721-722]{Eaton2016a}.

Use the function *`isobject([obj])`* to determine if *obj* is an
	object, and *`isa([variable_name],[class_name])`* is a function
	that determines if a variable *[variable_name]* is an object
	instance of the class *[class_name]*
	\cite[\S34.1, pp. 722]{Eaton2016a}.

The function *`[mthds] = methods([obj])`* returns a cell array
	containing the method names for the class that the object *[obj]*
	is an instance of.
	Similarly, the function *`[mthds] = methods([class_name])`*
	returns a cell array containing the method names for the class
	*[class_name]* \cite[\S34.1, pp. 723]{Eaton2016a}.

The function *`ismethod([obj],[mthd])`* queries if *[mthd]* is a
	method of the class the the object *[obj]* belongs to
	\cite[\S34.1, pp. 723]{Eaton2016a}.

Methods/Functions for the class can be defined via function files
	in the directory named *`@class-name`*
	\cite[\S34.1, pp. 722]{Eaton2016a}.


###	Class Manipulation

###	Basic Accessor and Mutator Class Methods

Basic class methods for access and modification/update are
	 \cite[\S34.2, pp. 723-725]{Eaton2016a}:
+ *`display([obj])`*
	+ Access method
	+ "Display the contents of [the] object" *[obj]*.
+ *`get([obj],[property_name])`*
	+ Access method
	+ Determine if *[property_name]* is a property of the object named
		*[obj]*.
+ *`get([obj])`*
	+ Access method
	+ List all the properties of the object named *[obj]*.
+ *`set([obj],[property_value_pairs])`*
	+ Access method
	+ For the object named *[obj]*, set the values of its properties
		using the (property, value) pairs found in
		*[property_value_pairs]*. 

	+ Return the modified object *[obj]* as the updated object. 
		E.g., *`p = set([obj],[property_value_pairs])`*
	+ \cite[\S34.2, pp. 725]{Eaton2016a}:














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
+ [Advanced indexing](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#advanced-indexing);
	not only does this improve performance (i.e., execution time),
	it can also improve memory management
	\cite[\S8.1.1, pp. 136-137]{Eaton2016a}.
+ [Broadcasting](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/gnu-octave.md#arithmetic-operators)
	- Broadcasting can handle binary operators and functions when
		their size differ.
		From *GNU Octave 3.6.0*, for arrays/matrices that are of
		different sizes, "broadcast" the smaller array/matrix across
		the larger array/matrix.
		"Broadcasting" enforces the compatible shape rule, such that
		corresponding array dimensions are equal or one of these
		dimensions is one.
		If "corresponding array dimensions are equal", carry out
		"ordinary element-by-element arithmetic".
		Else, copy the array with the singleton dimension along that
		dimension until their shapes are compatible (i.e., this
		dimension of this array matches that dimension in that array).
		This copying operation is cosmetic/superficial, so that the
		binary operator/function can be carried out; no actual
		copying of data is done in memory.
		For scalar arrays, broadcast all of its dimensions.
		For functions without broacasting semantics, use the function
		*`bsxfun`* for forced broadcasting.
		The preconditions for broadcasting are: two different
		dimensions and no singleton dimension exists.
		Broadcasting is known as binary singleton expansion in
		*MATLAB*, recycling in *R*, replication, or single-instruction
		multiple data (SIMD)
		\cite[\S19.2, pp. 491-494]{Eaton2016a}.






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
		user-defined variable/function would used/processed
		\cite[\S7.3, pp. 132]{Eaton2016a}.
		If any of the names in the *[list of names]* does not match
		an existing variable, function, operator, keyword, or file,
		it is undefined and it will cause an error to be thrown at
		run time. See [("commented out") implementation of this in this hyperlinked script](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m)
		By default, calling the function *`type`* displays a header
		line printing the *name* being processed and a short
		description of its category (such as 'function' or 'variable').
		Printing of the aforementioned header can be suppressed by
		using the *[-q]* option.
		If the output of calling this function *`type`* is not
		assigned to an output variable, as a cell array of strings,
		the output is printed to standard output (i.e., the
		'Terminal' application) \cite[\S7.3, pp. 132]{Eaton2016a}.
	- The function *`which [list of names]`* displays the type of
		each name in the *[list of names]*
		\cite[\S7.3, pp. 132]{Eaton2016a}.
		If the name is undefined, calling the function *`which`* will
		produce no output; see [its implementation in this *GNU Octave* script](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m).
		That said, we am unable to call the function *`which`*
		successfully with a "name defined [in] a function file",
		which should result in displaying the filename, too; this
		remains untested as of now.
	- The function *`what [path to a directory]`* displays the *GNU
		Octave* files that are in the directory *[path to a directory]*. 
		*GNU Octave* files are *GNU Octave* scripts (or function files).
		If this function is called without input arguments, it will
		display *GNU Octave* files in the current working directory.  
		See [its implementation in this *GNU Octave* script](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-variables.m)
		\cite[\S7.3, pp. 132-133]{Eaton2016a}.





###	Expressions

In *GNU Octave*, an expression is a fundamental component of
	statements \cite[\S8, pp. 135]{Eaton2016a}.

The value that an expression evaluates to can be
	\cite[\S8, pp. 135]{Eaton2016a}:
+ Printed
+ Tested, in control statements
+ Stored in variables
+ Passed to functions, in function calls.
+ Used with an assignment operator to assign a new value to a variable. 



Components, or building blocks, of expressions in *GNU Octave*
	\cite[\S8, pp. 135]{Eaton2016a}: 
+ Variables
+ Array references
+ Constants
+ Function calls
+ Combinations of these and operators

####	Index Expressions

Use an index expression to \cite[\S8.1, pp. 135]{Eaton2016a}:
+ Reference selected elements of a matrix/vector
+ Extract selected elements of a matrix/vector

Building blocks, or components, or an index expression
	\cite[\S8.1, pp. 135]{Eaton2016a}:
+ Scalar
+ Vector
+ Range
+ Operator *':'* to select entire rows/columns


When using a single index expression, we can index
	\cite[\S8.1, pp. 135]{Eaton2016a}:
+ Vectors, and
+ Multi-dimensional arrays/matrices

We can use *N* indices to index a higher-dimensional (up to *N*
	dimensions) matrix/array.
	Semicolons are used as delimiters to separate columns from each
	other, while colons are used to indicate columns or range of
	numbers along a column \cite[\S8.1, pp. 135]{Eaton2016a}. 

When we use a single index expression to index a higher-dimensional
	matrix/array, it would process the matrix/array elements in a
	column-first order \cite[\S8.1, pp. 135]{Eaton2016a}.

It is not uncommon for multiple index expressions to be equivalent
	\cite[\S8.1, pp. 135]{Eaton2016a}.

Use the keyword *end* to refer to the last entry of a given dimension
	of a matrix/array; when this is used in ranges, we do not need to
	call size()/length() to determine the bounds of the array before
	indexing \cite[\S8.1, pp. 135]{Eaton2016a}.

When an index expression has three numbers separated from each other
	by colons *start:increment/decrement:end*, it can be used to
	indicate ranges, such as odd/even elements or the reverse order
	of a vector/array \cite[\S8.1, pp. 135]{Eaton2016a}. 

#####	Advanced Indexing

To index an *n*-dimensional array with a set of *m*-index tuple, the
	Cartesian product of the index vectors/ranges/scalars is used
	to determine the indexed matrix/array element (or range thereof).

Indexing can be used for the following types of operations, so that
	performance (i.e., execution time) and memory management can be
	improved \cite[\S8.1.1, pp. 136-137]{Eaton2016a}:
+ Creating an array, or a matrix, filled with the same value.
	Using indexing saves the need for multiplication operation.
	This results in a performance improvement.
+ It also allows a range to be stored more efficiently in memory,
	since it needs to store a tuple of *(starting value, increment,
	end value, and total number of values) instead of a vector/matrix
	that has more than four elements. 
	This results in better memory management.
	In addition, its range representation allows the *GNU Octave*
	interpreter to use more performance-efficient algorithm than
	its vector/matrix representation
	\cite[\S8.1.1, pp. 136-137]{Eaton2016a}.
	- Use the function *`repmat`* to replicate smaller arrays into
		larger arrays, so that more efficient algorithms can be used
		on them, rather than slower algorithms for matrix computations
		\cite[\S8.1.1, pp. 137]{Eaton2016a}.
+ Substitute certain loops with indexing, since this replacement
	allows fast indexing operations to be done instead of slower
	looping operations \cite[\S8.1.1, pp. 137]{Eaton2016a}.
+ For procedures that involve matrix/array resizing, substitute loops
	for such resizing with indexing, since this replacement allows
	fast indexing operations to be done instead of slower
	resizing operations \cite[\S8.1.1, pp. 137]{Eaton2016a}.
+ The functions *`ind = sub2ind(dims,s1,s2,...,sN)`* and
	*`[s1,s2,...,sN] = sub2ind(dims,ind)`* are dual functions that
	convert subscripts of a N-dimensional matrix into a series of
	linear indices, and to convert a series of linear indices into
	subscripts of a N-dimensional matrix, respectively
	\cite[\S8.1.1, pp. 137]{Eaton2016a}.

The function *`isindex(ind,[n])`* is a function that determines if *ind*
	is a valid index.
	The optional input argument *[n]* is the maximum value of *ind*,
	which must be a positive integer of the real type, or a logical
	array.
	If *ind* is a string, it is converted to a double value before
	checking if it is a valid index. As long as the string does not
	contain the *'NULL'* character, it is a valid index
	\cite[\S8.1.1, pp. 137]{Eaton2016a}.




######	Side Note on Advanced Indexing

I do not understand the material in the second paragraph of \S8.1.1,
	Advanced Indexing, on page 137, where each index is less than the 
	size of the array in the *i*^{th} dimension.

For the case of *(m>n)*, I have experimentally determined that it will
	result in a array/matrix "index out of bounds" error; see
	[this script for its implementation](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/gnu-octave/i-expressions.m).





####	Function Calls
#####	Function Calls: Call by Value

Currently, functions arguments/parameters cannot be passed by
	reference.
	Hence, they have to be passed by value; local copies of such
	arguments (i.e., variables) are processed by the function, rather
	than the actual variables.
	Thus, for passing "constants" as input arguments to functions, we
	do not have to be concerned if the function would change the value
	of the "constants" (i.e., variables with fixed values).
	Also, variables pass as input arguments to functions are not
	copied, unless the functions have to modify them
	\cite[\S8.2.1, pp. 140]{Eaton2016a}.

"Octave does not implement pass by reference"
	\cite[\S34.2, pp. 725]{Eaton2016a}.


#####	Function Calls: Recursion

*GNU Octave* supports recursive function calls, with the exception of
	some built-in *GNU Octave* functions (such as *`lsode()`*).
	Call recursive functions directly or indirectly
	\cite[\S8.2.2, pp. 141]{Eaton2016a}.

Note that each recursive function should have a base case, so that it
	can terminate (i.e., not run indefinitely).
	When a recursive function ends up in infinite recursion, the
	*GNU Octave* process associated with it must be terminated.




####	Arithmetic Operators

\S8.3 includes a list of arithmetic operators that work on scalars
	and matrices \cite[\S8.3, pp. 141-142]{Eaton2016a}.
	It includes:
+ "element-by-element" operators and functions broadcast to handle
	arithmetic operations on matrices with different sizes.
	- Broadcasting can handle binary operators and functions when
		their size differ.
		From *GNU Octave 3.6.0*, for arrays/matrices that are of
		different sizes, "broadcast" the smaller array/matrix across
		the larger array/matrix.
		"Broadcasting" enforces the compatible shape rule, such that
		corresponding array dimensions are equal or one of these
		dimensions is one.
		If "corresponding array dimensions are equal", carry out
		"ordinary element-by-element arithmetic".
		Else, copy the array with the singleton dimension along that
		dimension until their shapes are compatible (i.e., this
		dimension of this array matches that dimension in that array).
		This copying operation is cosmetic/superficial, so that the
		binary operator/function can be carried out; no actual
		copying of data is done in memory.
		For scalar arrays, broadcast all of its dimensions.
		For functions without broacasting semantics, use the function
		*`bsxfun`* for forced broadcasting.
		The preconditions for broadcasting are: two different
		dimensions and no singleton dimension exists.
		Broadcasting is known as binary singleton expansion in
		*MATLAB*, recycling in *R*, replication, or single-instruction
		multiple data (SIMD)
		\cite[\S19.2, pp. 491-494]{Eaton2016a}.

####	Comparison Operators

Comparison operators use relational operators to determine the
	relationship between numeric values for equality (or otherwise).
	If the comparison is *True*, return one. Else, return zero.
	For matrix comparison, the comparison is done on an
	element-by-element basis
	\cite[\S8.4, pp. 145]{Eaton2016a}.

String comparison is done with the function *`strcmp`* instead of the
	binary comparison operators \cite[\S8.4, pp. 145]{Eaton2016a}.






####	Boolean Expressions

*GNU Octave* does not support the ternary operator *`?:`*
	\cite[\S8.5.2, pp. 149]{Eaton2016a}.

#####	Binary Element-by-Element Boolean Operators

Use boolean operators, and nesting via parentheses, to form an
	element-by-element boolean expression
	\cite[\S8.5.1, pp. 146]{Eaton2016a}.

Broadcasting rules apply for boolean expressions containing matrix
	of differing sizes, or for applying a binary operator to an
	expression involving a scalar and a matrix
	\cite[\S8.5.1, pp. 147]{Eaton2016a}.

"For the binary element-by-element boolean operators" "to work for
	matrix-valued operands," subexpressions are evaluated before
	the expression involving the boolean operator and two
	subexpressions are evaluated \cite[\S8.5.1, pp. 147]{Eaton2016a}.

E.g., the expression *`(subexpression #1) & (subexpression #2)`* is
	evaluated after *(subexpression #1)* and *(subexpression #2)*
	are evaluated individually.

When the boolean operators *and(x1,x2,...)* and *or(x1,x2,...)* are
	applied to multiple matrices, they are applied cumulatively to
	the input argument list from left to right
	\cite[\S8.5.1, pp. 147-148]{Eaton2016a}.


#####	Short-Circuit Boolean Operators

For certain uses of boolean expressions, to terminate evaluation of 
	a boolean expression when the "overall truth value can be 
	determined," use short-circuit boolean operators instead of 
	element-by-element boolean operators.
	The overall truth value for the expression of a short-circuit
	boolean operator can be determined before evaluating both
	operands of the short-circuit boolean operator
	\cite[\S8.5.2, pp. 148-149]{Eaton2016a}.

E.g.,  the *&&* and *||* operators are short-circuit boolean operators
	that perform the conjunction and disjunction operations on a set
	of operators.


The functions *`merge(mask, tval, fval)`* and
	*`merge(mask, tval, fval)`* implements the *if-else* block for
	*mask*.
	If *mask* is *True*, it returns *tval*; else, it returns *False*
	\cite[\S8.5.2, pp. 149]{Eaton2016a}.

####	Assignment Expressions

An assignment expression is an expression that allocates a value
	*val* to a variable *var*.
	This gives the variable *var* a value of *val*.
	The sign *'='* is the assignment operator, which causes a variable
	to be assigned to a (new) value
	\cite[\S8.6, pp. 149-150]{Eaton2016a}.

The type of a given variable can be changed; the current type of the
	variable depends on the type of its current value
	\cite[\S8.6, pp. 150]{Eaton2016a}.

To delete rows and/or columns in matrices and vectors, assign the
	empty matrix *'[]'* to the row/column (specified with the *':'*)
	\cite[\S8.6, pp. 150]{Eaton2016a}.

Multiple assignments can be concatenated.
	E.g., the expression *`a = b = c = d = e = 12345`* assigns the
	value of *12345* to the variables *a*, *b*, *c*, *d*, and *e*.
	Expressions for multiple assignments are processed from right
	to left.
	In the above example, assign *12345* to *e*, followed
	by assigning *e* to *d*, and so on; it eventually ends with
	assigning *b* to *a*.
	When evaluating an assignment expression between two sets of
	variables (left and right), the number of variables/values on the
	left-hand side (LHS) cannot exceed the number of variables/values
	on the right-hand side (RHS); else the excess variables on the
	LHS would be undefined in the return list.
	That said, the cardinality of the LHS set of variables can be
	smaller than the cardinality of the RHS set of variables.
	If I do not need to use a given return variable of a function, I
	can use a placehold *`~`* in its place among the return variables
	on the LHS.
	Using the placeholder avoids the usage of dymmy variables, which
	makes the code looker cleaner and is more memory efficient
	\cite[\S8.6, pp. 150-151]{Eaton2016a}.

Use the expression of the form *`(expr1) (op)= (expr2)`* as a shortcut
	to perform the evaluation of *`(expr1) = (expr1) (op) (expr2)`*.
	Here, the operator *`(op)=`* can be *`+=`*, *`-=`*, *`*=`*, or
	*`/=`*.
	Note that the variable in *(expr1)* has to be defined; e.g.,
	*`(expr1) = [value]`* assigns the value *`[value]`* to *(expr1)*.
	If the variable in *(expr1)* is undefined, it will cause an
	undefined error to occur at run time.
	Also, note that the following is grammatically not correct, since
	it will cause a *'parse error'*:
	*`(expr1) (op)= (expr2) (op)= (expr3)`*.
	Note that the following is legal:
	*`(expr1) (op)= ((expr2) (op) (expr3))`*
	\cite[\S8.6, pp. 151]{Eaton2016a}.

Note that when assignment expressions are included in a boolean
	expression or comparison expression, it can be confusing to read
	\cite[\S8.6, pp. 151]{Eaton2016a}.


####	Increment Operators

Use increment/decrement operators to alter the value of a variable by
	*`±1`* before (pre- increment/decrement, *`(op)(var)`*) or after
	(post- increment/decrement, *`(var)(op)`*) the assignment.
	Here, *`(op)`* can be *`++`* or *`--`*.
	The pre- increment/decrement is equivalent to
	*`(var) = (var) (±) 1`*, which is the new value of *(var)*.
	The post- increment/decrement is equivalent to
	*`(var) = (var) (±) 1`*, and the value of the *(var)* is the old
	value of *(var)* prior to the increment/decrement operation
	\cite[\S8.7, pp. 152]{Eaton2016a}.


####	Operator Precedence

The operator precedence for *GNU Octave* is listed in 
	\cite[\S8.8, pp. 152-153]{Eaton2016a}.
	Also, note that parentheses can be used to modify operator
	precedence during evaluation of an expression (from left to right,
	with the exception of assignment operators).
	Explicit parentheses make the source code more readable
	\cite[\S8.8, pp. 152]{Eaton2016a}.



###	Evaluation

Use the function *`eval([try], [catch])`* to evaluate the string
	*'[try]'* as a command; should the string *'[try]'* fail to
	execute as a command, the string *'[catch]'* would be executed
	as a command.
	The use of *try-catch* blocks and *unwind_protect/unwind_protect_protect*
	is recommended as error handling mechanism, instead of
	*`eval([try], [catch])`* \cite[\S9, pp. 155]{Eaton2016a}.


If a given variable *fn_name* cannot be determined to be "a function
	handle, function name in a string, or inline function," the
	function *`feval([fn_name])`* can be used for safer evaluation
	of *fn_name* \cite[\S9, pp. 155]{Eaton2016a}.

Functions that allow arguments to be passed by name (i.e.,
	pass-by-name style), is analogous to pass-by-reference
	\cite[\S6.1, pp. 16-19]{Ong2017} in *C++* (and similar languages).
	They allow variables to be modified in my own context; i.e., I get
	to decide which symbol table would be used by expressions in
	functions of the pass-by-name style
	\cite[\S9.2, pp. 157-158]{Eaton2016a}.

The function *`fail(code, "warning", pattern)`* is explained in
	\cite[\SB.1, pp. 863]{Eaton2016a}.










###	Statements

Types of statements \cite[\S10, pp. 159]{Eaton2016a}:
+ (simple constant) expressions
+ (list of nested) loops
	- *`while`* loops
	- *`do-until`* loops
	- *`for`* loops
		* This can be applied to structures (via a *[value,key]* pair)
			and cell arrays, in parallel.
			Also, the conditional expression for the *`for`* loop to
			keep iterating can be "a range, a row vector, or a
			scalar."
			\cite[\S10.5, pp. 164-165]{Eaton2016a}. 
+ conditional statements
	- *`if`* statements
	- *`switch`* statements
		* Duplicate cases (with the same *label* expressions) in
			switch statements cannot be detected by the *GNU Octave*
			interpreter.
			Also, only the list of statements associated with the
			first case would be executed.
			The *otherwise* case is optional
			If the label for a case is a cell array, if the expression
			for the switch statement matches any element of the cell
			array, execute the list of statements associated with
			that case.
			The label for any case in the *switch* statement can be
			\cite[\S10.2, pp. 162]{Eaton2016a}.
		* \cite[\S10.2.1, pp. 162-163]{Eaton2016a} has important
			notes for implementing *`switch`* statements.
			Cases for the *`switch`* statement are exclusive; and,
			consequently, each case in the *`switch`* statement must
			have a non-empty list of statements to execute.
+ other statements
	- *`break`* statements
	- *`continue`* statements
	- *`unwind_protect`* statements
	- *`try`* and *`try-catch`* statements
	- continuation lines
		* ellipsis (*'...'*) for statements
		* The backslash character '\\' is used for "double-quoted
			string constants."

Control statements in *GNU Octave* programs change/modify the flow
	of execution.
	Control statements include loops and conditional statements.
	A control statement can be nested inside another control statement.
	A control statement begins and ends with special keywords.
	The body of the control statement is the list of statements
	between its beginning and end \cite[\S10, pp. 159]{Eaton2016a}.

For evaluation of matrices as conditions in conditional statements,
	the matrices must be non-empty and contain only non-zero elements
	\cite[\S10.1, pp. 159]{Eaton2016a}.


















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
+ *GNU Octave* functions and variables that do not exist in *Matlab*:
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
+ *GNU Octave* allows whitespace before the transpose operator, but
	*Matlab* does not.
+ *GNU Octave* does not require the use of ellipses for line continuation
	but *Matlab* does.
+ "MATLAB has no fputs function. Call fprintf instead."
	 
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

Alternatively, we can create *Matlab*-compatible *MEX* files
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


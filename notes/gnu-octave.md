#	Notes About *GNU Octave*

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
	number of input arguments in the function call.  


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
	use of guards is strongly recommended for making the code
	exception safe. 

In addition, judiciously consider what to do with the semipredicate
	problem \cite{WikipediaContributors2016e}.

### *unwind_protect* Technique

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

###	*try-catch-block* Technique

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
	specific error later.



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

###	Continuation Lines

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
	
	"MATLAB has no fputs function."
+ *GNU Octave* allows whitespace before the transpose operator, but
	*Matlab* does not.
+ *GNU Octave* does not require the use of ellipses for line continuation
	but *Matlab* does.
	 
	Use a backslash "\" to indicate line continuation.
+ *GNU Octave*'s logical operators may be rendered unacceptable by
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


##	Integrating *GNU Octave* Code Into *C++* Code

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

+ [TheUniversityOfTexasAtAustinStaff2016]

	The University of Texas at Austin staff, "Sysnet's Documentation," in {\it Institute for Computational Engineering and Sciences}, Institute for Computational Engineering and Sciences, Cockrell School of Engineering and College of Natural Sciences, The University of Texas at Austin, Austin, TX, October 6, 2016.
	
	Available online at: \url{https://www.ices.utexas.edu/sysdocs/}; last accessed on October 26, 2016.
	







#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


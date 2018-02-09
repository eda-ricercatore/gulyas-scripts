#	Notes About *Python*

##	Differences between *Python 3.x* and *Python 2.y*

The `print` statement in *Python 2.y* has been replaced by the
	`print()` function in *Python 3.x*.
	A pair of parentheses, or round brackets, are used in the `print()`
	function to print the string within the parentheses.
	The `print` statement needs to be appended by a string, and these
	tokens (the `print` statement and the string) are whitespace
	delimited \cite{vanRossum2017}.

Comparing *Python* 3.x to *Python* 2.y, the former has significant
		differences in printing information (to standard output)
		\cite{vanRossum2017}.
	This can cause compatibility problems between different versions
		of *Python* in a given *Python* software. 

Definitions of classes between *Python 3.x* and *Python 2.y* are different
	\cite[Chapter 4, pp. 103]{Alchin2010}.




##	Design Decisions

Use either keyword arguments or positional arguments in my
	implementation of *Python* methods to process input parameters
	\cite[Chapter 3, pp. 53]{Alchin2010}.






##	Syntax Rules Regarding Identifiers

*Python* identifiers for variables, functions, classes, and modules
	have to be alphanumeric and can include underscores
	\cite[from \S *Python* Basic Syntax]{Mohtashim2017}
	\cite[\S2.3 Identifiers and keywords]{DrakeJr2016f}
	\cite[\S2.3 Identifiers and keywords]{DrakeJr2016a}.
	Otherwise, the *Python* interpreter would report a syntax error,
	since the syntax is invalid.
	These identifiers are case sensitive and cannot be *Python*
	keywords [ParewaLabsPvtLtdStaff20XY, \S "*Python* Keywords and Identifier"].

They should not include dashes. Else, an interpreting/compiling error
	would result.





##	Importing *Python* Classes, Modules, and Packages

Tasks that I can do:
+ Create and define a class, and use static methods in the class
	(within the same script). 
+ Use static methods of a class, from another *Python* script.
+ Create, define, and use my own *Python* modules, from any *Python*
	script.
+ Create, define, and use my own *Python* packages, from any *Python*
	script.
	Determine the importance and usefulness packages, with respect to
	modules.

See [example to import *Python* modules and classes](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/sandbox/python/s-import).



Tasks that I want to do, but can't yet (or have yet to try):
+ BLAH






Note: "A module is a file containing *Python* definitions and statements."
	\cite[\S6 Modules]{Brandl2017a} \cite[\S6 Modules]{Brandl2017}
	\cite[Importing Modules: Module? What's a Module?]{Thurlow2012}.
	**This is different from how I define modules in *C++* and *Java*.**


Pages in \cite[Beginning *Python*]{Hetland2005} that deal with importing
	*Python* classes and modules:
+ Abstraction of classes and modules, pp. 109--158, 173--202
+ Modules and The Standard Library, pp. 203--254
+ Summaries: pp. 547--574




Pages in \cite[Expert *Python* Programming]{Ziade2008} that deal with
	importing *Python* classes and modules (Not helpful):
+ Naming, (pp. 91--116
	- Application of naming to (pp. 92): 
		* Variables: constants and public/private variables
		* Functions and methods
		* Properties
		* Classes
		* Modules
		* Packages
+ Packages, (pp. 117--165)
+ Documentation, (pp. 223--250)



With regards to importing *Python* modules, circular dependencies is
	forbidden/discouraged during interpretation of *Python* programs.
	That is, don't import a *Python* module *A*, which imports another
		*Python* module *B* that imports *Python* module *A*.
	Or rather, **if *Python* module *A* imports *Python* module *B*, *Python*
		module *B* should not import *Python* module *A*.**

A *Python* package is a collection of *Python* modules, and is effectively a
	subdirectory of *Python* modules that includes a file named *\_\_init\_\_.py*;
	the file *\_\_init\_\_.py* can be an empty file.

To import a module *B* from a package *A*, try: *import A.B*.  

To import a class *C* from module *B* that belongs to package *A*, try:
	*from A.B import C*.

Use the error *ImportError* to catch errors associated with importing modules
	that have been moved or renamed.
	Provide fallback imports, so that in the *try-catch* block, we can provide
		another statement to import the module from its old/new location
		(or with its old/new name);
	if the *try* block uses the old location/name, the *catch* block shall use
		the new location/name, and vice versa;
	if the module is not critical to the function of the software, it is recommended
		to assign the module to *None* (i.e., *[module name] = None*)
	\cite[Chapter 2, pp. 45-46]{Alchin2010}.

In the transition period from upgrading old locations/names to new
	locations/names, use the special module **\_\_module\_\_** to make the
	import of non-critical modules conditional \cite[Chapter 2, pp. 46-47]{Alchin2010}.

Explicit module imports, by specifying the module (and package) names are
	preferred over implicit imports of all (or a subset of) modules within a
	package \cite[Chapter 2, pp. 47-48]{Alchin2010}.

Relative imports are supported by providing relative paths to modules that are
	being imported \cite[Chapter 2, pp. 48-49]{Alchin2010}.









## *Python* Classes


Notes on *Python* Classes:
+ A class is a particular type of object has a logical group of functions, and
	"encapsulates the behavior of an object" \cite[Chapter 4, pp. 103]{Alchin2010}. 
+ "An instance of the class represents the data for the object"
	\cite[Chapter 4, pp. 103]{Alchin2010}.
+ Difference instances of a class has different sets of data, but have the same
	behavior that is determined by the class definition;
	this behavior can be defined, extended, or altered 
	\cite[Chapter 4, pp. 103]{Alchin2010}. 
+ Inheritance allows a derived/child class to have a different fundamental
	behavior from its base class \cite[Chapter 4, pp. 103]{Alchin2010}. 
+ The built-in type **object** is "a foundation type that underpins the entire
	system \cite[Chapter 4, pp. 103]{Alchin2010}.
+ Codify relationships between packages, modules, and classes to represent
	actual/real relationships between (concrete or abstract) nouns
	\cite[Chapter 4, pp. 105]{Alchin2010}.
+ *Python* supports multiple inheritance, and enables each class to be build
	as another component of the software \cite[Chapter 4, pp. 105]{Alchin2010}. 
	- Multiple inheritance enables mixins, or support classes, to provide minor
		add-on features that can be used by a variety of classes. 
		\cite[Chapter 4, pp. 105]{Alchin2010}.
		* **Compare mixins with traits.**
		* "[A mixin does] not provide full functionality on [its] own."
+ Method resolution order (MRO) determines "the order in which *Python*
	resolves which method to use" in software that uses "multi-level or multiple
	inheritance" \cite[Chapter 4, pp. 106]{Alchin2010}.
	- Since Python does not know the class hierarchy, it has "to account for all
		the possibilities" \cite[Chapter 4, pp. 108]{Alchin2010} in which it
		determines which method to use.
+ **\_\_init\_\_()** is a class, when it shoud be considered as an instance object
	(**self**), which inherits from **type** \cite[Chapter 4, pp. 122]{Alchin2010}.
+ The (software) plugin framework allows software plugins and plugin systems
	to be additively added to it \cite[Chapter 4, pp. 122]{Alchin2010}.




	









Chapter 4,5-6,8.



\cite{Alchin2010}



+ \cite{Hall2009b}
	- Chapter 9,10
	- For *Python 3,* not *Python 2*.

+ \cite{Hetland2005}
	- Chapters 6-9???/10??
	- Chapters 17-19


### *Python* Functions

Notes on *Python* functions:
+ By default, *Python* functions return *None* \cite[Chapter 1, pp. 15]{Alchin2010}.
+ No *Python* function is given special privileges over other *Python* functions
	\cite[Chapter 3, pp. 53]{Alchin2010}.
+ *Python* functions encapsulate code into individual units, which facilitates
	code reuse \cite[Chapter 3, pp. 53]{Alchin2010}.
+ *Python* treats functions as full-fledged objects, so that they can be
	\cite[Chapter 3, pp. 53]{Alchin2010}:
	- stored and transferred via data structures
	- "wrapped [around by] other functions"
	- "replaced by new implementations"
+ Arguments of a *Python* function:
	- positional arguments (or order-based arguments)
		\cite[Chapter 3, pp. 53]{Alchin2010} are grouped in an immutable tuple
		\cite[Chapter 3, pp. 56]{Alchin2010}.
	- keyword arguments \cite[Chapter 3, pp. 53]{Alchin2010} are placed in
		a mutable dictionary \cite[Chapter 3, pp. 56]{Alchin2010}.
	- It is recommended that arguments of a given *Python* function have
		default values \cite[Chapter 3, pp. 53]{Alchin2010}.
	- Keyword arguments are explicitly specified during function calls,
		and are favored over positional arguments that are implictly specified
		during function calls \cite[Chapter 3, pp. 54]{Alchin2010}.
		* Keyword arguments also *Python*ic in terms of coding style
			\cite[Chapter 3, pp. 56]{Alchin2010}.
	- Develop code that supports overriding via flexibility
		\cite[Chapter 3, pp. 54]{Alchin2010}.
	- Types of arguments listed in order of precedence/priority
		\cite[Chapter 3, pp. 56-59]{Alchin2010}:
		* required arguments (ensures/guarantees that required positional
			arguments are processed before optional arguments are processed)
		* optional arguments (ensures/guarantees that optional arguments are
			processed before variable arguments)
		* variable positional arguments (ensures/guarantees that variable
			positional arguments are processed before variable keyword
			arguments);
			**all the variable positional arguments of a function have to be
				group into one set**;
			multiple sets of variable positional arguments have to be group into
				one set
		* variable keyword arguments;
			**all the variable keyword arguments of a function have to be
				group into one set**;
			multiple sets of variable keyword arguments have to be group into
				one set
	- "Preloading arguments" (or"Partial application of a function") occurs when it "preload[s] some of the
		arguments in advance", so that fewer arguments have to be assigned
		values later \cite[Chapter 3, pp. 60]{Alchin2010}.
	- Currying in functional programming is subtly different from preloading
		arguments \cite[Chapter 3, pp. 60]{Alchin2010};
		* A pure curried function shall be called repeatedly till all the arguments
			are assigned values -- the number of unassigned arguments is
			reduced as the pure curried function is iteratively called till all
			arguments are assigned values, before the most recently
			returned/created function (for which all of its arguments are
			assigned) is executed;
		* Partial application will return a function that can be subsequently
			executed, regardless of whether it has any unassigned arguments
			-- note that executing a function with unassigned arguments will
			result in raising a *TypeError*.
+ Types of *Python* functions \cite[Chapter 3]{Alchin2010}:
	- decorators
	- function annotations \cite[Chapter 3, pp. 78]{Alchin2010}.
		* Attach an expression to each input argument and the return value. 
	- generators
		* A generator has the "flexibility of a function and the performance of
			an iterator";
			it uses the **yield** statement to enable a value to be read externally,
				and it is analogous to the **return** statement \cite[Chapter 3, pp. 94]{Alchin2010}.
	- lambdas
		* Has a return value in the body of a lambda, and omits any explicit
			return statement;
			only allows a single expression \cite[Chapter 3, pp. 97]{Alchin2010}. 
	- introspection
		* Any access/examination of information at run-time, such as
			\cite[Chapter 3, pp. 97]{Alchin2010}:
			+ object attributes
			+ module contents
			+ documentation
			+ generated bytecode
+ A decorator is a technique for obtaining a (new) function from passing a
	function (function to be decorated) into another function (decorator)
	\cite[Chapter 3, pp. 61,68]{Alchin2010};
	- It is used to support preloading arguments (or partial application of a
		function) \cite[Chapter 3, pp. 61]{Alchin2010};
	- Use a decorator to execute boilerplate code in a set of input functions
		before/after the execution of the returned function
		\cite[Chapter 3, pp. 68]{Alchin2010}.
	- Use decorators to avoid boilerplate code and simplify the functions
		\cite[Chapter 3, pp. 77]{Alchin2010}. 
	- Applications of decorators \cite[Chapter 3, pp. 67-68]{Alchin2010}:
		* access control
		* cleanup of temporary objects
		* error handling
		* caching
		* logging
	- A closure is a function, which is defined in another function, and can be
		passed to another function as an object
		\cite[Chapter 3, pp. 69]{Alchin2010}.
		* It can involve \cite[Chapter 3, pp. 69]{Alchin2010}:
			+ lexical scope
			+ free variables
			+ upvalues
			+ variable extent
		* A function *A* passed into another function *B* cannot be the closure
			of function *B*, since *A* is not defined in *B*
			\cite[Chapter 3, pp. 70]{Alchin2010}.
	- A wrapper is a function contained within another function and additional
		behavior executed before or/and after the execution of the wrapped
		function \cite[Chapter 3, pp. 71]{Alchin2010}.
		* To call the wrapper "as if it [was] the original function," pass variable
			positional arguments and keyword arguments together (for
			"maximum flexibility") internally into the original function
			\cite[Chapter 3, pp. 71]{Alchin2010}.
		* Execute the wrapper within a *try-except* block to catch any raised
			error;
			if an error is raised, implicitly return **None**;
			a value (or **None**) is returned to the original function
			\cite[Chapter 3, pp. 71]{Alchin2010}.
		* Information lost by the wrapped function can be obtained by the
			*wrap* decorator in the *functools* module;
			here, a decorator is used inside another decorator to avoid
				code duplication
			\cite[Chapter 3, pp. 71]{Alchin2010}.
	- A decorator with arguments is implemented by the "original" function
		having extra arguments that are passed to the wrapper, which returns
		the decorator \cite[Chapter 3, pp. 72]{Alchin2010}.
	- Beware of side effects of decorators \cite[Chapter 3, pp. 75]{Alchin2010}.
	- A decorator enables memoization by storing the result of a function;
		this is carried out by the argument list as a key to automatically cache
		the result \cite[Chapter 3, pp. 75]{Alchin2010}.
	- Factoring out the boilerplate code \cite[Chapter 3, pp. 86]{Alchin2010}:
		* An annotation determines "if [a] value is appropriate, and raises an
			exception" for inappropriate values.
		* Use a decorator to factor out the boilerplate code as a new function,
			connect it to the rest of the code, and process the annotation for each
		value \cite[Chapter 3, pp. 86]{Alchin2010}.
	- A decorator can make use of annotation for type coercion
		\cite[Chapter 3, pp. 88]{Alchin2010}.
		- Either require an argument to accept values of a specific type, or
			coerce an input value to the required type
			\cite[Chapter 3, pp. 88]{Alchin2010}.
		* **The robustness principle allows input arguments to accept values
			of a small range of types, which can be converted to the
			required types prior to further processing;
			hence, the type of the return value would always be consistent
			with the type expected by external code, so that
			postconditions would be satisfied.**
	- Provide an annotation directly to the code that needs it, and/or use a
		decorator with input argument to annotate the code
		\cite[Chapter 3, pp. 90]{Alchin2010}.
	- Stacking multiple decorators "together on a function" provides "a built-in
		way to manage each corresponding framework";
		each decorator has a corresponding framework
		\cite[Chapter 3, pp. 90]{Alchin2010}.
+ A flexible function can be customized into a simpler and less flexible function
	so that its reduced flexibility can be handled by existing API/libraries
	\cite[Chapter 3, pp. 61]{Alchin2010}.
+ The transparency of *Python* allows different aspects of *Python* objects,
	including functions, to be examined/inspected at run-time
		\cite[Chapter 3, pp. 61]{Alchin2010};
	- the *inspect* module from *The Python Standard Library* has introspection
		features that enable the examination/inspection of function arguments  
		-- "a named tuple of information about [a] function's arguments" is
		returned from processing the input function
		\cite[Chapter 3, pp. 61]{Alchin2010};
	- argument values of a function's arguments can be identified and be used to
		generate argument lists \cite[Chapter 3, pp. 62]{Alchin2010}.
	- call a function with another function, a tuple of its positional arguments, and
		a dictionary keyword arguments \cite[Chapter 3, pp. 62]{Alchin2010}.
	- exploit the transparency of *Python* while refactoring functions to make
		the functions more concise \cite[Chapter 3, pp. 62]{Alchin2010}.
	- perform argument validation to reduce the risk of raising errors due to
		unassigned arguments by checking if arguments are assigned values
		and if all arguments are known (i.e., "Are there any unknown
		arguments?") \cite[Chapter 3, pp. 66]{Alchin2010}.
	- argument validation assigns default values to optional arguments, and
		returns a dictionary of required arguments (such that each
		unassigned argument has a message indicating that it needs to be
		assigned a value or that it is an unknown argument)
		\cite[Chapter 3, pp. 66-67]{Alchin2010}.
+ Aspects of a function that is code invariant
	\cite[Chapter 3, pp. 78]{Alchin2010}:
	- name of function
	- set of input arguments
	- optional docstring 






 







## *Python*-based Software Development

Try to use a *Python*ic approach to software development.
	This can facilitate the design and implementation of software (architectures)
		that can be refactored easily \cite[Chapter 1]{Alchin2010}.

Use a **list comprehension** to perform a conditional operation iteratively on
	a collection of elements \cite[Chapter 2, pp. 35]{Alchin2010}.
	Similarly, a **generator expression** implicitly creates an iterable object to
		iterate over a list/collection of elements and perform an operation on
		each enumerated item/element;
		a generator expression needs to be surrounded by parentheses,
			which can belong to a function (or an operation) performed on the
			collection of objects \cite[Chapter 2, pp. 35-37]{Alchin2010}.
	Likewise, a **set comprehension** performs the built-in set() function on a
		a collection of unsorted elements \cite[Chapter 2, pp. 37]{Alchin2010}.
	Comparably, a **dictionary comprehension** is an unordered linear
		("1-D") collection of (key,value) pairs, such that each pair is donoted
		by *key: value* \cite[Chapter 2, pp. 37-38]{Alchin2010}.
		Compare this to **ordered dictionaries** \cite[Chapter 2, pp. 38]{Alchin2010}.


+ Try to follow the *Don't Repeat Yourself* principle during software development
	\cite[Chapter 4, pp. 120]{Alchin2010}.



+ \cite[Chapters 8-11]{Alchin2010}.
+ \cite[Appendices A and B]{Langtangen2006}.
+ \cite[Appendices A and B]{Langtangen2009}.
+ \cite[Chapter 21]{Lutz2011}.
	- No information on object-oriented programming.
+ \cite[Chapter 15]{Lutz2013}.
+ \cite{Younker2008}.
	- No information on object-oriented programming.


### *Python*ic Coding Style


\cite{vanRossum2013} describes *Python*ic software development, including
	how to program in a *Python*ic coding style.
	Note that the term "coding style" can be used interchangeably with "coding
		scheme", "coding standard", "coding style guide",
		and "programming style".

Note that \cite{Franca2014} mentions that modern *C++1X*, such as *C++11*,
	*C++14*, and *C++17*, is becoming more like *Python*;
	that is, modern *C++1X* has become *Python*ic.   


### Input/Output Operations

\cite[Chapter 2, pp. 23]{Alchin2010} shows how to log errors that have been
	raised during input/output operations.
	They can be recorded/stored by the *logging* module from *The Python
		Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}


###	Modules in *The Python Standard Library*

The following modules in *The Python Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}
	can be useful in developing *Python* software .
+ *itertools*
	Enables a set/chain of functions to be performed on each element in a
		collection \cite[Chapter 2, pp. 38]{Alchin2010}. 
	- The *zip()* function enables multiple iterables to be combined
		together \cite[Chapter 2, pp. 38]{Alchin2010};
		an iterable is a collection "object" that can generate an iterator to
			iterate over each element in the collection \cite[Chapter 5, pp. 155]{Alchin2010}.






####	Built-in Collections

From \cite[Chapter 2, pp. 39]{Alchin2010}
+ lists
+ tuples
+ sets \cite[Chapter 2, pp. 39]{Alchin2010}
	- Disallow duplicates
	- The standard constructor accepts the following as inputs:
		* sequences
		* lists
		* tuples
		* dictionary keys
		* custom iterable objects
	- Unordered data structure that is only concerned about membership.
	- Has the following operations \cite[Chapter 2, pp. 40-43]{Alchin2010}:
		* *{element}* in *{set}*
		* *{set}*.add(*{element}*)
		* *{set}*.update(*{element}*)
		* *{set}*.remove(*{element}*)
		* *{set}*.discard(*{element}*)
		* *{set}*.pop(*{element}*)
		* *{set}*.clear(*{element}*)
		* OR operation, disjunction: *{set 1} | {set 2}*, *{set 1}.union({set 2})*
		* AND operation, disjunction: *{set 1} & {set 2}*, *{set 1}.intersection({set 2})*
		* difference operation, *{set 1} - {set 2}*, *{set 1}.difference({set 2})*
		* symmetric difference operation, *{set 1} ^ {set 2}*, *{set 1}.symmetric_difference({set 2})*
		* *{set 1}*.issubset(*{set 2}*)
		* *{set 1}*.issuperset(*{set 2}*)
		* ({set 1} - {set 2}); Or, not ({set 1} - {set 2})
	- Use *set()* to represent the empty set, so that it can be differentiated from
		an empty dictionary *{}* \cite[Chapter 2, pp. 41]{Alchin2010}.
+ named tuples \cite[Chapter 2, pp. 43]{Alchin2010}
	- The *factory* function, namedtuple(), from the *collections* module in
		*The Python Standard Library* returns a new class that is
		customized for a given set of named fields, rather than a "named tuple"
		object with named fields.
	- For functions that return multiple values, named tuples can be used to
		return these sets of values.
		They allow the returned values to be accessible by named fields, just
			like dictionaries. 
+ dictionaries \cite[Chapter 2, pp. 44]{Alchin2010}
	- unordered data structure
+ ordered dictionaries \cite[Chapter 2, pp. 44]{Alchin2010}
	- ordered data structure
	- Has all the features of a dictionary, while having a reliable ordering of keys
		for its *(key,value)* pairs. 
+ dictionaries with defaults \cite[Chapter 2, pp. 44-45]{Alchin2010}
	- A dictionary with defaults is assumed to have (optimal) default values for
		keys that cannot be found in the mapping.
	- Lambda functions can be used to create and process dictionaries with
		defaults.











##	Exception Handling

\cite[Chapter 2, pp. 23-28,29-30]{Alchin2010} shows how to catch multiple
	errors that have been raised.









#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).

+ [ParewaLabsPvtLtdStaff20XY]

	Parewa Labs Pvt. Ltd. staff, "Learn Python Programming," Parewa Labs Pvt. Ltd., Kupondole, Lalitpur, Lalitpur District, Nepal.
	
	Available online from {\it Programming Tutorial, Articles and Examples -- Programiz} at: \url{https://www.programiz.com/python-programming/}; last accessed on April 1, 2017.



## Object-Oriented *Python* Programming

+ \cite{Alchin2010}
	- Chapter 4,5-6,8.
	- Software development/engineering \cite[Chapters 8-11]{Alchin2010}.
	- Marty Alchin, "Pro Python: Advanced Coding Techniques and Tools," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2010. DOI: https://dx.doi.org/10.1007/978-1-4302-2758-8.
+ \cite{Hall2009b}
	- Chapter 9,10,11, 8 (pp. 165).
	- Tim Hall and J.-P. Stacey, "Python 3 for Absolute Beginners: All you will ever need to start programming Python," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2009. DOI:https://dx.doi.org/10.1007/978-1-4302-1633-9.
+ \cite{Hetland2005}
	- Chapters 6-8,9,11,13,16,17,18,19.
	- Magnus Lie Hetland, "Beginning Python: From Novice to Professional," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, New York, NY, 2005. DOI:https://dx.doi.org/10.1007/978-1-4302-0072-7.
+ \cite{Langtangen2006}
	- Chapter 8.6,8.8,8.10.
	- Software development/engineering \cite[Appendices A and B]{Langtangen2006}.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Second edition, Texts in Computational Science and Engineering, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2006. DOI:https://dx.doi.org/10.1007/3-540-31269-2.
+ \cite{Langtangen2009}
	- Chapter 3, 7, 9.
	- Software development/engineering \cite[Appendices A and B]{Langtangen2009}.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Third edition, in the Texts in Computational Science and Engineering series, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-540-73916-6.
+ \cite{Langtangen2009a}
	- Chapter 8.3,8.6,8.8,8.10, Appendix B.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-642-02475-7. 
+ \cite{Langtangen2011}
	- Chapter 4, 6, 7, 9.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Second edition, in Springer-Verlag Berlin Heidelberg series, Texts in Computational Science and Engineering, Volume 6, Heidelberg, Germany, 2011. DOI:https://dx.doi.org/10.1007/978-3-642-18366-9.
+ \cite{Langtangen2012}
	- Chapter 4, 6, 7, 9.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Third edition, in Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2012. DOI:https://dx.doi.org/10.1007/978-3-642-30293-0.
+ \cite{Lee2011b}
	- Chapter 4, 7.
	- Kent D. Lee, "Python Programming Fundamentals," in Undergraduate Topics in Computer Science, Springer-Verlag London, London, U.K., 2011. DOI:https://dx.doi.org/10.1007/978-1-84996-537-8.
+ \cite{Lutz2009}
	- Chapter 4,15,16-20,21-24,25-28,30-31,32-35,37,38,39.
	- Mark Lutz, "Learning Python: Powerful Object-Oriented Programming," Fourth edition, O'Reilly Media, Sebastopol, CA, 2009.
+ \cite{Lutz2010}
	- pp. 60-61, 85-88, 183-187.
	- Mark Lutz, "Python Pocket Reference: Python in your pocket," Fourth edition, O'Reilly Media, Sebastopol, CA, 2010.
+ \cite{Lutz2013}
	- Chapter 4,16-21, 22-25, 26-29, 31-32, 33-36, 39-41.
	- Software development/engineering \cite[Chapter 15]{Lutz2013}.
	- Mark Lutz, "Learning Python: Powerful Object-Oriented Programming," Fifth edition, O'Reilly Media, Sebastopol, CA, 2013.
+ \cite{Pilgrim2009}
	- Chapter 6-7, 8, 9, 10.
	- Mark Pilgrim, "Dive Into Python 3," Apress, Berkeley, CA, 2009. DOI:https://dx.doi.org/10.1007/978-1-4302-2416-7.
+ \cite{Ucoluk2012}
	- Chapter 7.
	- Gokturk Ucoluk and Sinan Kalkan, "Introduction to Programming Concepts with Case Studies in Python," Springer-Verlag Wien, Vienna, Austria, 2012. DOI:https://dx.doi.org/10.1007/978-3-7091-1343-1.






























## Domain Applications of *Python* Programming

+ Algorithm analysis.
	- \cite{Hetland2010}.
+ Data structures.
	- \cite{Lutz2011,Lutz2013,Sweigart2015,Ucoluk2012}.
	- **Read this!!!**
+ **Database management**.
	- \cite{Hetland2005,Lutz2010,Lutz2011,Sileika2010,Younker2008}.
+ Functional programming.
	- \cite{Lutz2009,Lutz2013}.
	- **Read this!!!**
+ GUI development.
	- \cite{Gift2008,Hall2009b,Hetland2005,Langtangen2009,Lee2011b,Lutz2010,Lutz2011,Vaingast2009}.
+ **Machine learning**.
	- \cite{Unpingco2016}.
+ Network programming.
	- \cite{Goerzen2004,Hetland2005,Lutz2011,Rhodes2010,Sileika2010}.
+ **Numerical methods, or numerical computing**.
	- \cite{Langtangen2006,Langtangen2009,Langtangen2009a,Langtangen2011,Langtangen2012,Linge2016}. 
+ **Parallel programming**.
	- \cite{Gift2008,Lutz2011}.
+ **Scientific computing, computational science, and computational engineering**.
	- \cite{Langtangen2006,Langtangen2009}.
	- \cite{Langtangen2009a,Langtangen2011,Langtangen2012}
	- \cite{Vaingast2009}
+ **Software development** and **software engineering**.
	- \cite[Chapters 8-11]{Alchin2010}.
	- \cite[Appendices A and B]{Langtangen2006}.
	- \cite[Appendices A and B]{Langtangen2009}.
	- \cite[Chapter 21]{Lutz2011}.
	- \cite[Chapter 15]{Lutz2013}.
	- \cite{Younker2008}.
+ **Statistical analysis**.
	- \cite{Saha2015,Sileika2010,Unpingco2016}.
+ Task automation.
	- \cite{Sweigart2015}
+ UNIX/Linux system administration.
	- \cite{Gift2008,Sileika2010,Sweigart2015}.
+ Web development.
	- \cite{Hetland2005,Langtangen2006,Langtangen2009,Pilgrim2009,Rhodes2010,Sileika2010,Younker2008}.
















## Mixed-Language Software Development

+ \cite{Langtangen2006}
	- Chapter 5,10, Appendix B.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Second edition, Texts in Computational Science and Engineering, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2006. DOI:https://dx.doi.org/10.1007/3-540-31269-2.
+ \cite{Langtangen2009}
	- Chapter 5,10, Appendix B.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-642-02475-7.
+ \cite{Lutz2011}
	- Chapter 20.
	- Mark Lutz, "Programming Python: Powerful Object-Oriented Programming," Fourth edition, O'Reilly Media, Sebastopol, CA, 2011.








#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


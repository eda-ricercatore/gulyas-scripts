#	Notes About *Python*

##	Table of Contents

+ [Differences between *Python 3.x* and *Python 2.y*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#differences-between-python-3x-and-python-2y)
+ [Design Decisions](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#design-decisions)
+ [Syntax Rules Regarding Identifiers](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#syntax-rules-regarding-identifiers)
+ [Importing *Python* Classes, Modules, and Packages](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#importing-python-classes-modules-and-packages)
+ [*Python* Classes](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-classes)
	- [*Python* Functions](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-functions)
+ [*Python*-based Software Development](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-based-software-development)
	- [*Python*ic Coding Style](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#pythonic-coding-style)
	- [*Python* Documentation](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-documentation)
	- [Input/Output Operations](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#inputoutput-operations)
	- [Modules in *The Python Standard Library*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#modules-in-the-python-standard-library)
		* [Built-in Collections](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#built-in-collections)
	- [Software Testing](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#software-testing)
+ [*Python* Strings](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-strings)
+ [Exception Handling](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#exception-handling)
	- [Ancillary Note](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#ancillary-note)
+ [*Python* Virtual Machine (PVM)](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-virtual-machine-pvm)
+ [Miscellaneous](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#miscellaneous)
+ [References](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#references)
	- [Object-Oriented *Python* Programming](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#object-oriented-python-programming)
	- [Domain Applications of *Python* Programming](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#domain-applications-of-python-programming)
	- [Mixed-Language Software Development](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#mixed-language-software-development)
	- [Books Covered](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#books-covered)
+ [Random](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#random)
+ [Author Information](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#author-information)








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

Unlike *Python 3.x*, properties in *Python 2.y* do not have mutator methods
	\cite[Chapter 4, pp. 129]{Alchin2010}.

When a function descriptor on a class is accessed, the function descriptor
	returns itself and shows up as any function in *Python 3.x*;
	however, in *Python 2.y*, this returns an instance method object
	\cite[Chapter 4, pp. 129]{Alchin2010}.  

*Python 3.x* and *Python 2.y* represent boolean values differently, **True** and
	**False** as opposed to **0** and **1** \cite[Chapter 4, pp. 143]{Alchin2010}.

Unlike *Python 2.y*, the **round()** method in *Python 3.x* would return a number
	of the same type \cite[Chapter 5, pp. 154]{Alchin2010}.

Backward compatibility support for *Python 2.y* in *Python 3.x*:
+ implement the **\_\_next\_\_()** method to call the **next()** method
	\cite[Chapter 5, pp. 156]{Alchin2010}.










##	Design Decisions

Use either keyword arguments or positional arguments in my
	implementation of *Python* methods to process input parameters
	\cite[Chapter 3, pp. 53]{Alchin2010};
	don't use both (keyword and positional arguments) of these types.






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
	\cite[Importing Modules: Module? What's a Module?]{Thurlow2012}
	\cite[Chapter 11, pp. 241]{Hall2009b}.
	**This is different from how I define modules in *C++* and *Java*.**


Pages in \cite{Hetland2005} that deal with importing
	*Python* classes and modules:
+ Abstraction of classes and modules, pp. 109--158 (Chapters 6-7), 173--202
	(Chapter 9)
+ Modules and The Standard Library, pp. 203--254 (Chapter 10) 
+ Summaries: pp. 547--573 (Appendices A-C)



+ \cite{Hetland2005}
	- Chapters 7-9???/10??
	- Chapters 17-19
	- Appendices A-C
Finished???
Appendix ???
\cite[Chapters 17, pp. ]{Hetland2005}








Pages in \cite{Ziade2008} that deal with
	importing *Python* classes and modules (Not helpful):
+ Naming, (pp. 91--116)
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
		module *B* should not import *Python* module *A* **
		"\cite[Chapter 11, pp. 241]{Hall2009b}"

A *Python* package is a collection of *Python* modules \cite[Chapter 11, pp. 241]{Hall2009b},
	and is effectively a subdirectory of *Python* modules that includes a file
	named **\_\_init\_\_.py** \cite[Chapter 11, pp. 252]{Hall2009b};
	the file **\_\_init\_\_.py** can be an empty file \cite[Chapter 11, pp. 252]{Hall2009b}.
	That is, a *Python* package is a "hierarchical directory structure" of
		*Python* files \cite[Chapter 11, pp. 252]{Hall2009b}.

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

Use the internal method **\_\_import\_\_** to conditionally import modules
	\cite[Chapter 11, pp. 245]{Hall2009b}.

A module can be imported under another name
	\cite[Chapter 11, pp. 245]{Hall2009b}.

Import statements should be placed at the top of each *Python* file
	\cite[Chapter 11, pp. 246]{Hall2009b}.

Importing *Python* submodules \cite[Chapter 11, pp. 253-254]{Hall2009b}:
+ Explicitly with an empty **\_\_init\_\_.py** file
	\cite[Chapter 11, pp. 253]{Hall2009b}.
	- **from pirate import \*** does not allow all submodules of **pirate** to be
		imported.
+ Implicitly 
	-  Using **\_all\_** as the list variable, which is comparable to using an
		import statement with the wildcard **\***.
		* Enables the use of import statements such as
			**from [*pirate import*] \***
	- Execute import statements in the **\_\_init\_\_.py** file.
		* To reload any module imported in the **\_\_init\_\_.py** file, explicitly
			reload those modules.
		* The **\_\_init\_\_.py** file can contain *Python* code just like any
			*Python* script.
















A **weakly internal** variable is a variable with a leading underscore,
	**_[variable name]**, that is explicitly imported
	\cite[Chapter 11, pp. 246]{Hall2009b}. 



While literate programming
	\cite{Knuth1984,Knuth1992a,McConnell2004,Subramaniam2006,Schach2007,Oram2007,MullerHannemann2010}
	is recommended, self-documenting code would suffice
	\cite[Chapter 11, pp. 246-247]{Hall2009b}. 

If the functionality of an imported module is changed/modified and updated, use
	the *imp* module from *The Python Standard Library*
	\cite{DrakeJr2016e,DrakeJr2016b} to clear "*Python*'s internal cache of
	[certain] imported modules" \cite[Chapter 11, pp. 249-250]{Hall2009b} and
	reload the cache with the update modules;
	this is useful when modules have to be created again or recompiled during
		program execution \cite[Chapter 11, pp. 249-250]{Hall2009b}.


When a *Python* script imports a module, it \cite[Chapter 11, pp. 250]{Hall2009b}:
+ Locates the *Python* script/file containing the module.
	- **PYTHONPATH** is a set of relative or absolute paths of *Python* modules,
		and *The Python Standard Library*, which helps the *Python*
		interpreter/compiler and the operating system locate *Python* modules
		\cite[Chapter 11, pp. 251]{Hall2009b}.
+ Loads the *Python* module into memory, and creates an internal representation
	for the *Python* module
	- *Python* compiles the *Python* modules into *Python* byte code, which
		are saved in *.pyc* files (the "c" in ".pyc" refers to compiled), for
		faster execution \cite[Chapter 11, pp. 251]{Hall2009b}.
+ Executes the aforementioned internal representation.














In the transition period from upgrading old locations/names to new
	locations/names, use the special module **\_\_module\_\_** to make the
	import of non-critical modules conditional \cite[Chapter 2, pp. 46-47]{Alchin2010}.

Explicit module imports, by specifying the module (and package) names are
	preferred over implicit imports of all (or a subset of) modules within a
	package \cite[Chapter 2, pp. 47-48]{Alchin2010}.

Relative imports are supported by providing relative paths to modules that are
	being imported \cite[Chapter 2, pp. 48-49]{Alchin2010}.

*Python* modules allow *Python* software to be modularized, which improves
		support for code reuse \cite[Chapter 11, pp. 241]{Hall2009b}.







## *Python* Classes


Notes on *Python* Classes:
+ Concepts in object-oriented programming for
	\cite[Chapters 7, pp. 139]{Hetland2005}  
	- ***polymorphism***
	- ***encapsulation***
	- methods
	- attributes
	- superclasses
	- ***inheritance***
	- constructors
+ A class is a particular type of object has a logical group of functions, and
	"encapsulates the behavior of an object" \cite[Chapter 4, pp. 103]{Alchin2010}.
	- A *Python* class definition is a template for custom data types that contain
		data (i.e., attributes, or object-specific variables
		\cite[Chapters 7, pp. 144]{Hetland2005}) and commands (i.e., methods,
		or functions belonging to this *Python* class)
		\cite[Chapter 9, pp. 181]{Hall2009b}.  
+ "An instance of the class represents the data for the object"
	\cite[Chapter 4, pp. 103]{Alchin2010} \cite[Chapter 9, pp. 183]{Hall2009b}.
	- Encapsulation enables the treatment of an object as a black box
		\cite[Chapter 9, pp. 183]{Hall2009b} to hide its details "from
		the outside world" \cite[Chapters 7, pp. 139]{Hetland2005}.
		* This is similar to polymorphism, because encapsulation and
			polymorphism are concepts/principles of abstraction;
			however, polymorphism can exist without encapsulation 
			\cite[Chapters 7, pp. 143]{Hetland2005}.
		* Encapsulation enables the usage of objects without knowing the
			details of how these objects are constructed
			\cite[Chapters 7, pp. 143]{Hetland2005}.
	- **self** refers to the instance object that the instance methods are
		operating with \cite[Chapter 9, pp. 183]{Hall2009b}.
	- **dir(*[instance object]*)** shows a list of attributes and methods
		supported by the ***[instance object]*** within its namespace 
		\cite[Chapter 9, pp. 184]{Hall2009b}.
	- Each instance object is associated with an unique identity (number), which
		can be obtained with **id(*[instance object]*)**.
		This identity (number) is an integer (or, positive integer)
			\cite[Chapter 9, pp. 184]{Hall2009b}.
	- The namespace of an object can be implemented by a dictionary object,
		and has the organization of a family tree or directory structure
		\cite[Chapter 9, pp. 185]{Hall2009b}.
	- Name binding is used to map/connect a name to an object
		\cite[Chapter 9, pp. 184]{Hall2009b}.
	- The state of an instance object is determined by the values of its
		attributes/properties/fields/characteristics
		\cite[Chapter 9, pp. 185]{Hall2009b}
		\cite[Chapters 7, pp. 145]{Hetland2005}.
	- Note that in \cite[Chapter 7, pp. 145; Chapter 9, pp. ???]{Hetland2005},
		properties are distinguished from attributes.
	- An attribute is private to objects of a class
		\cite[Chapters 7, pp. 145]{Hetland2005}. 
+ Difference instances of a class has different sets of data, but have the same
	behavior that is determined by the class definition;
	this behavior can be defined, extended, or altered 
	\cite[Chapter 4, pp. 103]{Alchin2010}.
+ Inheritance allows a derived/child class to have a different fundamental
	behavior from its base/parent class \cite[Chapter 4, pp. 103]{Alchin2010}
	\cite[Chapter 9, pp. 181]{Hall2009b}.
	- Inheritance allows specialized classes of objects to be created from
		general classes of objects \cite[Chapters 7, pp. 139]{Hetland2005}.
	- Duck typing enables developers to modify and manipulate objects, which
		are related via class inheritance, while ensuring type safety
		\cite{WikipediaContributors2018a}.
	- Polymorphism allows operators to be overloaded with *special methods*
		\cite{DrakeJr2016a} (which are known as "magic methods" in
		\cite{Hall2009b}) \cite[Chapter 9, pp. 184]{Hall2009b}.
	- Polymorphism enables type/class -dependent functions to be performed 
		on an object \cite[Chapters 7, pp. 140]{Hetland2005}.
		* That is, polymorphism not only allows objects of child classes
			(subclasses, or derived classes) to inherit functions from parent
			classes (superclasses, or base classes) but also customizes them
			for the child classes \cite[Chapters 7, pp. 140]{Hetland2005}.
		* This type of *Pythonic* programming exploits "duck typing"
			\cite[Chapters 7, pp. 143]{Hetland2005}.
		* Polymorphism enables the usage of an object' methods without
			detailed information about what it is (i.e., its type/class)
			\cite[Chapters 7, pp. 143]{Hetland2005}.   
		* An object of a child class is also an instance of the parent class;
			hence, using the **isinstance()** method for type/class checking
			is an inadequate solution \cite[Chapters 7, pp. 140]{Hetland2005}.
		* Polymorphism applies to \cite[Chapters 7, pp. 142]{Hetland2005}:
			+ methods
			+ built-in operators
			+ built-in functions
		* The advantages/benefits of polymorphism are mitigated/negated with
			type checking functions \cite[Chapters 7, pp. 143]{Hetland2005}:
			+ **type()**
			+ **isinstance()**
			+ **issubclass()**
		* Instead of type checking (or checking the class), ask if the object is
			behaving according to what I want
			\cite[Chapters 7, pp. 143]{Hetland2005}.
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
	- Since *Python* does not know the class hierarchy, it has "to account for all
		the possibilities" \cite[Chapter 4, pp. 108]{Alchin2010} in which it
		determines which method to use.
+ **\_\_init\_\_()** is a class, when it shoud be considered as an instance object
	(**self**), which inherits from **type** \cite[Chapter 4, pp. 122]{Alchin2010}
	\cite[Chapter 7, pp. 102-103]{Pilgrim2009}.
+ The (software) plugin framework allows software plugins and plugin systems
	to be additively added to it \cite[Chapter 4, pp. 122]{Alchin2010}.
	- The plugin framework allows easy access to plugins and plugin systems
		in use \cite[Chapter 4, pp. 122]{Alchin2010}.
	- A plugin extends a base class by using Python's extension features, such
		as the built-in subclass syntax and the support "for common plugin
		needs", so that it can complement the functionality of the base class
		\cite[Chapter 4, pp. 123]{Alchin2010}. 
	- An example of support "for common plugin needs" would be input
		validation \cite[Chapter 4, pp. 123]{Alchin2010}:
	- The plugin, or plugin system, should be well documented, in terms of its
		expectations and assumptions \cite[Chapter 4, pp. 123]{Alchin2010}.
	- The plugin can be extended by more specialized plugins as subclasses
		(also known as derived classes and child classes)
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- Provide an iterator to enumerate plugins mounted to the plugin
		framework's plugin mount point \cite[Chapter 4, pp. 124]{Alchin2010}.
	- The metaclass for the plugin framework should register/connect plugins
		to the plugin mount class by adding the plugin objects to the plugin list
		(list of plugins) for subsequent access
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- The plugin mount class needs to have a switch to enable or disable the
		plugin mount (or plugin framework)
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- An individual/standard plugin inherits from the metaclass, and obtains its
		plugin behavior automatically \cite[Chapter 4, pp. 125]{Alchin2010}.
	- Use the metaclass **\_\_prepare\_\_()** to prepare a class declaration for
		immediate processing \cite[Chapter 4, pp. 125]{Alchin2010}.
	- An instantiated object stores data via an instance-specific namespace
		dictionary that can be accessed by the attributes if the instantiated
		object;
		access these attributes with "a trio of functions"
		\cite[Chapter 4, pp. 125]{Alchin2010}.
+ Define a property using the built-in @property decorator function, so that it
	can allow attributes to be assessed by methods
	\cite[Chapter 4, pp. 127]{Alchin2010}.
+ A descriptor of an assigned class allows an object definition to behave just
	like the properties of the assigned class \cite[Chapter 4, pp. 129]{Alchin2010}. 
	- Since a descriptor cannot use the namespace dictionary of the instance
		object, the descriptor has to use a dictionary to access instance objects
		\cite[Chapter 4, pp. 131]{Alchin2010}.
+ A method is a function belonging to a class \cite[Chapter 4, pp. 131]{Alchin2010}.
	- That is, a method is a function that is bound to object attributes (or,
		attributes of an object/class) \cite[Chapters 7, pp. 141]{Hetland2005}
		\cite[Chapters 7, pp. 144]{Hetland2005}.
	- Unlike functions that do not belong to a class, a method can access class
		information \cite[Chapter 4, pp. 131]{Alchin2010}.
	- Categories of methods \cite[Chapter 4, pp. 131]{Alchin2010}:
		* unbound methods
		* bound methods
	- A function also serves as a descriptor of a class
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- Like descriptors, a class and its instances can access a method
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- An unbound method is a method that is accessed by a class, which is
		received by the descriptor \cite[Chapter 4, pp. 131]{Alchin2010}. 
	- A bound method requires an instance of a class to for access
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- When an unbound method on a class is accessed, a function object for
		the unbound method is returned \cite[Chapter 4, pp. 131]{Alchin2010}.
	- A function can support bound and unbound methods;
		a bound method uses the instance object, which is
			passed as a positional argument, of the class to receive the first
			argument;
		hence, the positional argument does not need to be **self**
		\cite[Chapter 4, pp. 132]{Alchin2010}.
	- To implement method binding with an unbound method, explicitly use an
		 instance objects in the first argument to mimic/imitate bound methods;
		 this can be helpful "when passing functions around as callbacks"
		\cite[Chapter 4, pp. 133]{Alchin2010}.
	- To use a method without instantiating a class, use either of the following
		\cite[Chapter 4, pp. 133-135]{Alchin2010}:
		* Class methods
		* Static methods
	- A class method is a method that needs access to the attached class, and
		the built-in *@classmethod* decorator supports it
		\cite[Chapter 4, pp. 133-135]{Alchin2010}.
	- An "unbound" class method is a bound instance method that accepts an
		instance object as the first positional argument
		\cite[Chapter 4, pp. 133]{Alchin2010}.
	- A method can be defined on a metaclass, since a class is an instance of a
		metaclass \cite[Chapter 4, pp. 134]{Alchin2010}.;
		hence, each instance of a class can access that method, just like any
			bound method of that class \cite[Chapter 4, pp. 134]{Alchin2010};
		however, a class instance can call unclass methods, but not bound
			class methods \cite[Chapter 4, pp. 134]{Alchin2010};
		a bound class method can only be called by the class itself.
			\cite[Chapter 4, pp. 134]{Alchin2010}.
	- While a metaclass-based class method has less visibility by instances of
		a class than standard decorated class methods, it allows
		metaclass-using applications to add class methods to classes that use
		the metaclass \cite[Chapter 4, pp. 134]{Alchin2010};
		this avoids the need for a separate/extra class just to contain the
		aforementioned class methods (and nothing else)
		\cite[Chapter 4, pp. 134]{Alchin2010}.
	- A static method enables a method to interact with properties of the class,
		and other static methods of the class, without requiring an instance
		object of the class to perform various operations and functions
		\cite[Chapter 4, pp. 134]{Alchin2010};
		this also avoids the need to implement a function at the module level,
			without being embedded in any *Python* class
			\cite[Chapter 4, pp. 134]{Alchin2010};
		a static method shall be defined within a *Python* class with the
			**static method** decorator \cite[Chapter 4, pp. 134]{Alchin2010}.
+ There exists various ways to instantiate/create, modify, or invalidate *Python*
	instance objects \cite[Chapter 4, pp. 135]{Alchin2010}.
	- Creating *Python* instance objects via instantiation of a *Python* class
		 \cite[Chapter 4, pp. 136]{Alchin2010}:
		* Use **\_\_new\_\_()** to instantiate/create an object of a *Python*
		 	class \cite[Chapter 4, pp. 137]{Alchin2010}. 
		* Use **\_\_init\_\_()** to initialize an object of a *Python* class to
			implement behavior (i.e., perform functions and operations) that is
		 	specific/unique to that *Python* instance object;
		 	that is, use the constructor **\_\_init\_\_()** to initialize instance
				variables of the class as a basic setup of the instance object
				and to perform common tasks for each instance object of the
				class (such as file input operations, validation of
				initial/preliminary user input, or to collect information
				regarding a given running process)
			\cite[Chapter 4, pp. 136]{Alchin2010}.
		* Default values for instance variables of the class serve as placeholders
			until they will be updated \cite[Chapter 4, pp. 136]{Alchin2010}.
		* For a given *Python* instance object, the **\_\_new\_\_()** method
			should be called before the **\_\_init\_\_()** method
			\cite[Chapter 4, pp. 137]{Alchin2010}.
	- Accessing and modifying attributes of a *Python* class
		\cite[Chapter 4, pp. 138]{Alchin2010} \cite[Chapter 9, pp. 197]{Hall2009b}:
		* The name of an attribute of an instance object can be accessed or
			modified directly via *instance.attribute* \cite[Chapter 4, pp. 138]{Alchin2010};
			other methods for accessing or modifying *instance.attribute* can
				provide more control \cite[Chapter 4, pp. 138]{Alchin2010}. 
		* Use the **\_\_getattr\_\_()** function to obtain the value of an attribute
			(of the instance object) \cite[Chapter 4, pp. 138]{Alchin2010};
			e.g., use the **getattr(instance, attribute_name)** to obtain the
				name of the attribute \cite[Chapter 4, pp. 138]{Alchin2010}.
		* Also, use the **\_\_getattr\_\_()** function to control implicitly (or
			rather, not explicitly) managed attributes
			\cite[Chapter 4, pp. 138]{Alchin2010}.
		* For requests to access undefined attributes, and if the
			**\_\_getattr\_\_()** function is defined, call the **\_\_getattr\_\_()**
			function \cite[Chapter 4, pp. 138]{Alchin2010}.
		* For defined attributes that exists with an instance object of the class,
			use the **\_\_getattribute\_\_()** function, which takes the same
			set of input arguments as the **\_\_getattr\_\_()** function
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use the **\_\_setattr\_\_()** function, with the input arguments **self**,
			**name**, and **value** to assign the **value** to the attribute
			called **name** for the instance object **self** (of a class)
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* For defined attributes, they can be modified with the function
			**setattr()** \cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use **del** to delete an attribute from an object;
			however, it does not work for fake attributes that are controlled by
			special methods
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use the **\_\_delattr\_\_()** function to handle/manage fake attributes
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Overridden attributes may have errors or exceptions that when
			raised may indicate another exception (for an overridden or a fake
			attribute) \cite[Chapter 4, pp. 140]{Alchin2010}.  
	- A string representation of an instance object is provided by the
		implementation of the **\_\_str\_\_()** method to coerce the instance
		object to a string \cite[Chapter 4, pp. 140]{Alchin2010}.
		* The implementation of the **\_\_str\_\_()** method should list the
			list of attributes and their corresponding values to enable users to
			create a clone of that instance object
			\cite[Chapter 4, pp. 141-142]{Alchin2010}.
		* Alternatively, the **\_\_repr\_\_()** method can provide more
			information about the instance object
			\cite[Chapter 4, pp. 141-142]{Alchin2010}.
+ Access specifiers (or access modifiers):
	- In *C++*, access specifiers are: public, protected, and private
		\cite[Chapter 12]{Deitel2012} \cite[Chapter 11]{Deitel2014}
		\cite[Chapter 7, pp. 392]{Gaddis2011} \cite[\S7.2, pp.. 349]{Lippman2013}.
		\cite[Chapters 5-6]{Sutherland2015} \cite{Gregoire2014}
	- In *Java*, access specifiers are also: public, protected, and private
		\cite[Chapter 2, pp. 23; Chapter 7, pp. 138]{Schildt2007}
		\cite[pp. 20, 145, & 153]{Eckel2006}
	- *Python* does not directly support keyword-based access specifiers (or
		access modifiers) \cite[Chapters 7, pp. 145]{Hetland2005};
		however, an attribute or method can be set to be private by adding the
			prefix "\_\_" (i.e., two underscores)
			\cite[Chapters 7, pp. 145-146]{Hetland2005}.










Protocols masked by *Python* syntactic sugar
	\cite[Chapter 5, pp. 143]{Alchin2010}:
+ Use the built-in **bool()** method to implement the **\_\_bool\_\_()** method
	to check if the attributes of a class complies with certain class invariants
	(e.g., assertions) are satisfied \cite[Chapter 5, pp. 143]{Alchin2010}.
+ To perform arithmetic operations via arithmetic operators, they require custom
	implementations of the certain methods \cite[Chapter 5, pp. 145]{Alchin2010}:
	- Arithmetic operations \cite[Chapter 5, pp. 145]{Alchin2010}:
		* addition
		* subtraction
		* multiplication
		* division
		* modulo operation \cite[Chapter 5, pp. 146-147]{Alchin2010}
		* exponentiation \cite[Chapter 5, pp. 147]{Alchin2010}
	- arithmetic operators \cite[Chapter 5, pp. 145]{Alchin2010}:
		* **+**
		* **-**
		* **\***
		* **/**
		* **//** \cite[Chapter 5, pp. 146]{Alchin2010}
		* **%** \cite[Chapter 5, pp. 146]{Alchin2010}
		* **\*\*** \cite[Chapter 5, pp. 147]{Alchin2010}
	- Customized implementations of the following methods
		\cite[Chapter 5, pp. 145]{Alchin2010}:
		* **\_\_add\_\_()**
		* **\_\_sub\_\_()**
		* **\_\_mul\_\_()**
		* **\_\_truediv\_\_()** (true division)
		* **\_\_floordiv\_\_()** (floor division) \cite[Chapter 5, pp. 146]{Alchin2010}
		* **\_\_mod\_\_()** (for "perform[ing] standard variable interpretation")
			\cite[Chapter 5, pp. 146]{Alchin2010}
		*  **\_\_divmod\_\_()** (floor division with modulo operation, which is
			called by the **divmod()** method) \cite[Chapter 5, pp. 147]{Alchin2010}
		* **\_\_pow\_\_()** (exponentiation, which is called by the built-in
			**pow()** function) \cite[Chapter 5, pp. 147]{Alchin2010}
	- True division returns the numerical value of the division operation
		\cite[Chapter 5, pp. 145]{Alchin2010}.
	- Floor division returns the lower of the two operands, if the true division of
		these operands lie between the operands on the number line
		\cite[Chapter 5, pp. 146]{Alchin2010}.
+ Bitwise operations \cite[Chapter 5, pp. 148-152]{Alchin2010}
	- **<<**, supported by **\_\_lshift()\_\_** implementation
	- **>>**, supported by **\_\_rshift()\_\_** implementation
	- Bitwise comparison operations \cite[Chapter 5, pp. 149-150]{Alchin2010}:
		* **&**, AND operation or conjunction, implemented by **\_\_and\_\_()**
		* **|**, OR operation or disjunction, implemented by **\_\_or\_\_()**
		* **^**, exclusive OR operation (XOR), implemented by **\_\_xor\_\_()**
		* **~**, inversion operation, implemented by **\_\_invert\_\_()**;
			the **\_\_invert\_\_()** method only works with two's-complement
			encoding \cite[Chapter 5, pp. 150]{Alchin2010}
		* See the table at the bottom of \cite[Chapter 5, pp. 151]{Alchin2010}
			and the top of \cite[Chapter 5, pp. 152]{Alchin2010} for alternate
			ways to place custom objects (e.g., on the right-hand side, and
			in-line via in-place operators) 
+ Additional Operations with Numbers
	- Use the **\_\_index\_\_()** method to use an instance object as an index
		in a sequence (e.g., list) \cite[Chapter 5, pp. 152]{Alchin2010}.
	- To round off numbers, use methods such as **floor()** (or rather,
		**\_\_floor\_\_()**) method and **ceil()** (or rather, **\_\_ceil\_\_()**)
		method \cite[Chapter 5, pp. 153]{Alchin2010}.
	- Use the method **round()** (or rather, **\_\_round\_\_(self, number of
		significant figures)**) to round numbers to the nearest number (with
		the specified number of significant figures, which is an optional
		argument) \cite[Chapter 5, pp. 153]{Alchin2010}.
	- For sign operations, use the **\_\_neg\_\_()** to negate the sign of a value,
		and **\_\_abs\_\_()** to obtain the absolute value of the number
		\cite[Chapter 5, pp. 154]{Alchin2010}.
	- For comparison operations that return either **True** or **False**
		\cite[Chapter 5, pp. 154]{Alchin2010}
		\cite[Chapter 9, pp. 197, Table 9.2]{Hall2009b}:
		* **is**, can compare known constants (e.g., **None**)
		* **is not**, can compare known constants (e.g., **None**)
		* **==**, or **\_\_eq\_\_()**
		* **!=**, or **\_\_ne\_\_()** (i.e., not equal)
		* **<**, or **\_\_lt\_\_()**
		* **>**, or **\_\_gt\_\_()**
		* **<=**, or **\_\_lte\_\_()**
		* **>=**, or **\_\_gte\_\_()**
		* Default method for comparison **\_\_cmp\_\_()** compares **self**
			with **other** \cite[Chapter 5, pp. 155]{Alchin2010} 
+ Iterables \cite[Chapter 5, pp. 155]{Alchin2010}:
	- To determine if an object is iterable, use the built-in **iter()** function (or
		rather, **\_\_iter\_\_()**) to obtain an iterator;
		if an iterator is returned, the object is iterable
		\cite[Chapter 5, pp. 155]{Alchin2010}.
	- The **\_\_iter\_\_()** method, which includes the **\_\_init\_\_()** method
		to instantiate the iterator and returns **self** \cite[Chapter 5, pp. 155]{Alchin2010};
		an iterator is itself iterable \cite[Chapter 5, pp. 155]{Alchin2010}.
	- The **\_\_next\_\_()** is another required method, which retrieves a value
		from the iterator for use (by the caller of the **\_\_next\_\_()** method)
		\cite[Chapter 5, pp. 155]{Alchin2010};
		the **\_\_next\_\_()** method terminates at the end of enumerating all
			elements of a collection, due to the raised **StopIteration**
			exception \cite[Chapter 5, pp. 156]{Alchin2010};
		this is because **None** is a valid object, and the iterator cannot
			compare the instance object pointed to by itself to **None**
			\cite[Chapter 5, pp. 156]{Alchin2010}.
	- If the **\_\_iter\_\_()** method is not implemented, the **\_\_getitem\_\_()**
		method is used to access the element at the current position of the
		iterator \cite[Chapter 5, pp. 157]{Alchin2010}. 
+ *Python* supports sequences, such as lists, tuples, sets, and strings
	\cite[Chapter 5, pp. 159]{Alchin2010}:
	- Each type of these sequences \cite[Chapter 5, pp. 159]{Alchin2010}:
		* has a specialized type of iterator
		* can provide information regarding attributes about the sequence
		* has behaviors that can be performed on the sequence
		* E.g., determine the size/length of the sequence \cite[Chapter 5, pp. 159]{Alchin2010},
			or traverse the sequence in reverse order \cite[Chapter 5, pp. 160]{Alchin2010}.
		* **\_\_len\_\_()**, **\_\_setitem\_\_()**, **\_\_append\_\_()**,
			**\_\_insert\_\_()**, **del sequence[index]**, **\_\_delitem\_\_()**,
			and **\_\_contains\_\_()**
+ A mapping is a set of individual pairs, where each pair has a key and a
	corresponding value \cite[Chapter 5, pp. 164]{Alchin2010}.
	- The ordering of the pairs by their keys is not important, since a map is
		typically not traversed/enumerated.
	- For a given key, it enables instant access to a the key's corresponding
		value (which is referenced by its key).
	- Use the **key()** method to enumerate each key/pair in the mapping,
		without paying attention to its ordering.  
	- Use the **items()** method to obtain the set of all *(key,value)* pairs in the
		mapping \cite[Chapter 5, pp. 165]{Alchin2010}.
+ Callable functions and classes \cite[Chapter 5, pp. 165]{Alchin2010}
	- The **\_\_call\_\_()** method calls the class itself, using **self** as the first
		argument
+ Context manager \cite[Chapter 5, pp. 166]{Alchin2010}
	- Use objects as context managers with the **with** statement (which
		includes the **as** clause), so that they can set things up
		(preprocessing), do some processing within the context, and clean up
		after the processing (or post-processing)
		\cite[Chapter 5, pp. 166]{Alchin2010}.
	- Examples of contexts include:
		* file handling \cite[Chapter 5, pp. 166]{Alchin2010}
	- Set things up (preprocessing):
		* **\_\_enter\_\_()** method
	- Clean up after the processing (or post-processing):
		* **\_\_exit\_\_()** method
			+ When exceptions terminate the processing, this **\_\_exit\_\_()**
				method would receive information about the exception for
				post-processing and debugging (or troubleshooting)
				\cite[Chapter 5, pp. 166]{Alchin2010}.
			+ When no exceptions are raised during processing, and clean up
				proceeds as expected, it would receive **None** objects
				instead of information for debugging (or troubleshooting)
				\cite[Chapter 5, pp. 167]{Alchin2010}.
+ Multiple protocols can be used simultaneously, since they are not mutually
	exclusive \cite[Chapter 5, pp. 168]{Alchin2010}.




Object management:
+ In the object-oriented programming (OOP) paradigm, an object (or an instance
	of a class) has a set of methods (member functions) and attributes (i.e.,
	fields or data members) that enable manipulation (or control) of its behavior
	\cite[Chapter 6, pp. 169]{Alchin2010} \cite[Chapter 9, pp. 181]{Hall2009b}.
	- Methods; also known as functions belonging to an object, or member
		functions. These capture the behavior of the objects.
	- Attributes; also known as fields, data members, or instance variables and
		static variables. These capture the data of the objects.
+ In *Python*, an object is a combination of the following
	\cite[Chapter 6, pp. 169]{Alchin2010}:
	- identity, which is its unique address in memory; it is constant in its lifetime;
		this can be determined by "the built-in **id()** function".
	- type, which is defined by its class and parent class (or supporting base
		classes); an object has a reference to the class that it is an instance
		of (or belongs to).
	- value(s) of its attributes, which distinguishes objects of a class from each
		other.
		* Use the method **super()** to access the overridden method in the
			parent class \cite[Chapter 6, pp. 170]{Alchin2010}.
		* Use the **\_\_init\_\_()** method and the **\_\_new\_\_()** method to
			set up the default values \cite[Chapter 6, pp. 170]{Alchin2010}.
+ Guidelines about using mixins:
	- The use of **super()** may not allow us to control the mixin's class and
		base class \cite[Chapter 6, pp. 171]{Alchin2010};
		resolve this problem using the method **\_\_new\_\_()**, so that a
			new dictionary can be created for each encountered class.
	- Note that if a dictionary is created within a **cachedproperty()** function,
		each property would have its own private namespace;
		this results in memory leaks
		\cite[Chapter 6, pp. 176]{Alchin2010}.   
+ *Python* has automatic garbage collection \cite[Chapter 6, pp. 176]{Alchin2010}
	\cite[Chapter 5, pp. 103]{Hetland2005}.
	- Effective garbage collection depends on
		\cite[Chapter 6, pp. 176]{Alchin2010}:
		* ability to reliably identify/recognize an object as garbage that will
			cause memory leaks in the *Python* application
		* ability to remove garbage from (main) memory
	- Techniques for garbage collection \cite[Chapter 6, pp. 177]{Alchin2010}:
		* Reference counting
		* Cyclical references, which is inefficient but leads to more consistent
			and reliable outcomes \cite[Chapter 6, pp. 178-179]{Alchin2010}
		* Weak references \cite[Chapter 6, pp. 180-181]{Alchin2010}
+ The **pickle** module in *The Python Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}
	enables data stored in *Python* objects to be exported to external software
	as strings \cite[Chapter 6, pp. 182]{Alchin2010}.
	- Its "pickling" process serializes a *Python* object structure by converting
		a *Python* object hierarchy into a byte stream \cite{DrakeJr2016e,DrakeJr2016b}.
	-  "Unpickling" is the inverse operation of "pickling";
		it de-serializes a *Python* object structure by converting a byte stream
		into a *Python* object hierarchy \cite{DrakeJr2016e,DrakeJr2016b}.
	- Picking is also known as serialization, marshalling, or flattening
		\cite{DrakeJr2016e,DrakeJr2016b}.
	- The functions for performing pickling are **dump()** and **dumps()**
		\cite[Chapter 6, pp. 182]{Alchin2010}, and the functions for unpickling
		are **load()** and **loads()** \cite[Chapter 6, pp. 183]{Alchin2010}.
+ Objects can be copied using a shallow copy or deep copy method
	\cite[Chapter 6, pp. 186-189]{Alchin2010}.
	- Perform shallow copying with **copy()** to get a shallow copy of an object;
		the copy object has the same data values (of the same type), but with a
		new identity, and modifying the copy object would not modify the
		original object \cite[Chapter 6, pp. 187]{Alchin2010}.  
	- One-level deep copying, which is considered shallow copying, only
		provides a copy of the references, and does not copy the objects
		\cite[Chapter 6, pp. 188]{Alchin2010};
		"a namespace is a mapping from names to objects"
		\cite{Brandl2017,Brandl2017a}
+ To make a deep copy, use the **deepcopy()** method to copy the structure
	and objects referenced by the original object;
	modification of the deep copy does not affect the original copy, and vice
		versa \cite[Chapter 6, pp. 188]{Alchin2010}.





































Chapter 3, 7, 9.
\cite[Appendices A and B]{Langtangen2009}.




\cite{Langtangen2009a}
Chapter 7,9, Appendix D,E.

\cite{Langtangen2012}
Chapter 4, 6, 7, 9.
Appendices A and B



\cite{Lee2011b}
Chapter 4, 7.

\cite[Chapter 21]{Lutz2011}.




\cite{Lutz2013}
Chapter 4,16-21, 22-25, 26-29, 31-32, 33-36, 39-41.
\cite[Chapter 15]{Lutz2013}.

\cite{Lutz2010}

\cite{Pilgrim2009}
\cite{Ucoluk2012}




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
+ From *Python* 2.2 onwards, scopes in *Python* programs can be nested
	  \cite[Chapter 6, pp. 128]{Hetland2005}.
	- That is, we can nest a function definition within another function definition.
	- Alternatively, a function can be embedded within another function.  
	- When the outer function gets called, the inner function is redefined, and
		the outer function "returns the inner function" by returning the return
			value of the inner function.
	- The outer local scope (i.e., local scope of the outer function) is accessible
		within the inner function (i.e., local scope of the inner function).
	- That is, the following are equivalent:
		* outer_function(*param_1*)(*param_2*)
		* The following pair of statements:
			+ temp_function = outer_function(*param_1*)
			+ temp_function(*param_2*) 
+ *Python* supports "functional programming" via the
	following functions \cite[Chapter 6, pp. 133]{Hetland2005}:  
	- **map** \cite[Chapter 6, pp. 133-134]{Hetland2005}:
		* Maps a sequence to another sequence of equivalent length, via the
			application of a function to each element in the input sequence.
		* E.g., **map(***[lambda expression]*, input_sequence **)**.
		* E.g., **map(***[a function that accepts a sequence as its input parameter]*, input_sequence **)**.
	- **filter** \cite[Chapter 6, pp. 133-135]{Hetland2005}:
		* The **filter** function returns a subset of the input sequence by
			applying a function, which has a boolean return value, on each
			element in the input sequence.
		* The input parameters for the **filter** function are:
			an explicitly specified input function for the input sequence,
			and an input sequence;
			note that the explicitly specified input function would be applied to
				each element in the input sequence, and must return a
				boolean value.
		* E.g., **map(** *[lambda expression]*, input_sequence **)**.
		* E.g., **map(** *[input function]*, input_sequence **)**.
	- **reduce** \cite[Chapter 6, pp. 135-137]{Hetland2005}:
		* The **reduce** function performs an explicitly specified input function
			with the first two elements in the input sequence, and the outcome
			and the next available element, till the input sequence has been
			processed/enumerated \cite[Chapter 6, pp. 135]{Hetland2005}.
		* E.g., **reduce(** *[lambda expression]*, input_sequence **)**.
		* E.g., **reduce(** *[an input function]*, input_sequence **)**.
		* A **for** loop can implement any **reduce** function
			\cite[Chapter 6, pp. 135-137]{Hetland2005}.
		* Using a **for** loop instead of the **reduce** function can improve
			the comprehensibility of the source code.
	- **apply** \cite[Chapter 6, pp. 137]{Hetland2005}:
		* The **apply** function calls the explicitly specified input function,
			which is provided as an input argument.
		* E.g., **apply(** *[input function]* **)**.
		* E.g., **apply(** *[input function]*, *[tuple of positional arguments]* **)**.
		* E.g., **apply(** *[input function]*, *[dictionary of keyword arguments]* **)**.
		* E.g., *[input function]*(\**[dictionary of keyword arguments]*).
		* E.g., *[input function]*(\**[tuple of positional arguments]*).
		* Note that \**[dictionary of keyword arguments]* unpacks the dictionary
			of keyword ararguments.
		* Note that \**[tuple of positional arguments]* unpacks the tuple of
			positional ararguments.
	- lambda expressions \cite[Chapter 6, pp. 134]{Hetland2005}:
		* small, unnamed functions that contains an expression, which value is
			returned.
		* Note that the term **lambda** is a reserved word (or keyword) in
			*Python*.
		* **lambda** [parameters, delimited by a comma] : [an expression]
		* Also, note that full-fledged functions with names facilitate
			self-documention;
			lambda expressions can make the code difficult to read and
				understand.
	- Note on **map**, **filter**, and list comprehension
		\cite[Chapter 6, pp. 134-135]{Hetland2005}:
		* A list comprehension can implement any **filter** or **map**
			\cite[Chapter 6, pp. 135]{Hetland2005}.
		* Using list comprehensions, instead of **map**s or **filter**s, can
			improve the comprehensibility of the source code
			\cite[Chapter 6, pp. 135]{Hetland2005}.
		* Note that using **map**s or **filter**s, instead of list comprehensions,
			would result in faster execution (i.e., better performance)
			\cite[Chapter 6, pp. 135]{Hetland2005}.









 







## *Python*-based Software Development

Try to use a *Python*ic approach to software development.
	This can facilitate the design and implementation of software (architectures)
		that can be refactored easily \cite[Chapter 1]{Alchin2010}.

Use a **list comprehension** to perform a conditional operation iteratively on
	a collection of elements \cite[Chapter 2, pp. 35]{Alchin2010}.

Similarly, a **generator expression** implicitly creates an iterable object to
	iterate over a list/collection of elements and perform an operation on each
	enumerated item/element \cite[Chapter 2, pp. 35-37]{Alchin2010};
	a generator expression needs to be surrounded by parentheses, which can
		belong to a function (or an operation) performed on the collection of
		objects \cite[Chapter 2, pp. 35-37]{Alchin2010}.

Likewise, a **set comprehension** performs the built-in set() function on a
	collection of unsorted elements \cite[Chapter 2, pp. 37]{Alchin2010}.

Comparably, a **dictionary comprehension** is an unordered linear ("1-D")
	collection of (key,value) pairs, such that each pair is donoted by *key: value*
	\cite[Chapter 2, pp. 37-38]{Alchin2010}.

Compare this to **ordered dictionaries** \cite[Chapter 2, pp. 38]{Alchin2010}.


+ Try to follow the *Don't Repeat Yourself* principle during software development
	\cite[Chapter 4, pp. 120]{Alchin2010}.



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


Use documentation generators to produce documentation for the [software
	(library) \cite{WikipediaContributors2018b}](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md#python-documentation),
	from the comments in the code.


### *Python* Documentation

Use the **\_\_doc\_\_** attribute of modules, classes, and functions to access
	docstrings \cite[Chapter 8, pp. 209]{Alchin2010}.

Guidelines on what to include in docstrings \cite[Chapter 8, pp. 209]{Alchin2010}:
+ "Describe the function[/method]"
+ "Explain the arguments"
+ "Don't forget the return value"
+ "Include any expected exceptions" \cite[Chapter 8, pp. 210]{Alchin2010}

Endeavor to provide additional documentation for the following
	\cite[Chapter 8, pp. 210]{Alchin2010}:
+ Information about the installation, configuration, and execution of the software.
+ Tutorials on how to use the software.
+ "Reference documents"

\cite[Chapter 2, pp. 16]{Hall2009b} suggests the following *Python* docstring to
	provide built-in documentation for the *Python* software:
+ Usage: [*How to execute/run this program?*] \cite[Chapter 9, pp. 201]{Hall2009b}
+ Options: [*Options that are supported by this program.*]
+ Problem/Purpose: [*What does the **Python** software do?*]
+ Target Users: [*People who want to perform data analytics or other operations
	on their **BibTeX** databases.*]
+ Target Systems: [*UNIX-like operating systems.*] \cite[Chapter 9, pp. 201]{Hall2009b}
+ Interface: [*Command-line.*] \cite[Chapter 9, pp. 201]{Hall2009b}
+ Functional Requirements: \cite[Chapter 9, pp. 202]{Hall2009b}
	- [*Input **BibTeX** file.*]
	- [*Perform data processing on the **BibTeX** file.*]
	- [*Perform statistical analysis, or data analytics operations, on the **BibTeX**
		file.*]
	- [*Validate the integrity of the **BibTeX** file.*]
+ Maintainer(s): [*Zhiyang Ong*]
+ Expected Results: [*Perform tasks to address the problem statement.*]
+ Testing methods/modules: [*List of methods and modules used to test software.*] \cite[Chapter 9, pp. 202]{Hall2009b}
+ Test values: [*Values used to test software.*]
+ Limitations: [*Limitations of the software.*] \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\_version\_\_ = 0.1 \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\status\_\_ = "Prototype" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\_date\_\_ = "March 19, 2018" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\maintainer\_\_ = "Zhiyang Ong" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\credits\_\_ = "Thanks to everyone."


Produce documentation using documentation generators, such as:
+ *Javadoc*
+ *Doxygen*
+ *Sphinx* \cite{WikipediaContributors2018b}
+ *pydoc*

The command **help(*[Python module]*)** enables a user to read documentation
	about the *[Python module]* that is automatically produced by documentation
	generators, such as *pydoc* \cite[Chapter 11, pp. 248]{Hall2009b}.
	This documentation is extracted from the comments in the *[Python module]*
		\cite[Chapter 11, pp. 248]{Hall2009b}. 










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








###	Software Testing


+ Unit testing \cite[Chapter 9, pp. 217]{Alchin2010}
+ Test-driven development \cite[Chapter 9, pp. 217]{Alchin2010} 
+ Doctests
	- \cite[Chapter 9, pp. 218-221]{Alchin2010}
	- \cite[Chapter 1, pp. 5--6]{Pilgrim2009}
+ **unittest** module \cite[Chapter 9, pp. 221-230]{Alchin2010}











## *Python* Strings

In *Python* 3.x:
+ *exec("ls -al")* does not work.
	- *exec()* only executes *Python* code, in a *Python* environment
		\cite[Chapter 8, pp. 172]{Hall2009b}.
+ ***exec()* and *eval()* pose software security threats**, if they execute
	malicious *Python* code \cite[Chapter 8, pp. 173]{Hall2009b}.













##	Exception Handling


An exception stops the execution of the *Python* software/program due to
	an encountered error \cite[Chapter 10, pp. 221]{Hall2009b}.

Use **try...except...else...finally** statements to handle exceptions
	\cite[Chapter 10, pp. 221]{Hall2009b}. 

Exception chaining is a method of tracebacks that enable exceptions raised
	during exception handling to be differentiated from the original
	raised/thrown exception \cite[Chapter 10, pp. 235-236]{Hall2009b}. 





\cite[Chapter 2, pp. 23-28,29-30]{Alchin2010} shows how to catch multiple
	errors that have been raised.


###	Ancillary Note

The philosophy of "look before you leap" (LBYL) discourages exception handling
	\cite[Chapter 10, pp. 238]{Hall2009b}.

The Pythonic philosophy of "easier to ask forgiveness than permission" (EAFP)
	encourages trying something, and use exception handling to deal with
	uncommon outcomes/circumstances \cite[Chapter 10, pp. 238]{Hall2009b}.
















##	*Python* Virtual Machine (PVM)

Notes about the *Python* Virtual Machine (PVM):
+ \cite{Pattis2016}


















##	Miscellaneous





Notes on global and local variables: 
+ A global variable (e.g., "*x*") would be shadowed by a local variable (e.g., "*x*")
	of the same name \cite[Chapter 6, pp. 127]{Hetland2005}. 
	- To access the aforementioned global variable (e.g., "*x*"), try:
		*globals()['x']*
+ To rebind a global variable (e.g., "*x*") in a function, which assigns a new value
	to the global variable, explicitly state that the global variable is global
	\cite[Chapter 6, pp. 127]{Hetland2005}.
	- E.g., including this statement ***global x*** in a function enables all instances
		of "*x*" to become a global variable after this explicit declaration.
+ The use of global variables reduces the comprehensibility and robustness of the
	software \cite[Chapter 6, pp. 128]{Hetland2005}.
+ Local variables support abstraction and encapsulation, which improves the
	comprehensibility and robustness of the software
	\cite[Chapter 6, pp. 128]{Hetland2005}.
+ Note the existence of non-local variables \cite{WikipediaContributors2017a2}. 



The primary built-in object types in *Python*
	\cite[Chapters 7, pp. 139]{Hetland2005}:
+ numbers
+ strings
+ lists
+ tuples
+ dictionaries
















#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).

**If these citations/references are not found in this list of references, information
	about them can be found in my *BibTeX* database.** 

+ [ParewaLabsPvtLtdStaff20XY]

	Parewa Labs Pvt. Ltd. staff, "Learn Python Programming," Parewa Labs Pvt. Ltd., Kupondole, Lalitpur, Lalitpur District, Nepal.
	
	Available online from {\it Programming Tutorial, Articles and Examples -- Programiz} at: \url{https://www.programiz.com/python-programming/}; last accessed on April 1, 2017.

	**[Note in my *BibTeX* database.]**

+ [WikipediaContributors2018a]

	Wikipedia contributors, "Duck typing," in *Wikipedia, The Free Encyclopedia: Type theory*, Wikimedia Foundation, San Francisco, CA, January 10, 2018.

	Available online from *Wikipedia, The Free Encyclopedia: Type theory* at: \url{https://en.wikipedia.org/wiki/Duck_typing}; March 19, 2018 was the last accessed date.

+ [WikipediaContributors2018b]

	Wikipedia contributors, "Comparison of documentation generators," in *Wikipedia, The Free Encyclopedia: Software comparisons*, Wikimedia Foundation, San Francisco, CA, February 24, 2018.

	Available online from *Wikipedia, The Free Encyclopedia: Software comparisons* at: \url{https://en.wikipedia.org/wiki/Comparison_of_documentation_generators}; March 25, 2018 was the last accessed date.

+ [WikipediaContributors2017a2]

	Wikipedia contributors, ``Non-local variable,'' in *Wikipedia, The Free Encyclopedia: Programming language theory*, Wikimedia Foundation, San Francisco, CA, September 24, 2017.

	Available online from *Wikipedia, The Free Encyclopedia: Programming language theory* at: \url{https://en.wikipedia.org/wiki/Non-local_variable}; last accessed on March 29, 2018.










## Object-Oriented *Python* Programming

+ \cite{Alchin2010}
	- Chapter 4,5-6,8.
	- Software development/engineering \cite[Chapters 8-11]{Alchin2010}.
	- Marty Alchin, "Pro Python: Advanced Coding Techniques and Tools," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2010. DOI: https://dx.doi.org/10.1007/978-1-4302-2758-8.
+ \cite{Hall2009b}
	- Chapter 9,10,11, 8 (pp. 165).
	- Tim Hall and J.-P. Stacey, "Python 3 for Absolute Beginners: All you will ever need to start programming Python," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2009. DOI:https://dx.doi.org/10.1007/978-1-4302-1633-9.
+ \cite{Hetland2005}
	- Chapters 6-8,9,11,13,16-19.
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
	- Table of common computational complexities cite[\S5.1.1, pp. 157]{Ucoluk2012}
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




##	Additional *Python* Resources

Additional *Python* resources from my *BibTeX* database:
+ \cite{Brandl2017a}

	Georg Brandl and Benjamin Peterson and Senthil Kumaran and Guido {van Rossum} and Chris Jerdonek and Andrew Kuchling, "The *Python* Tutorial," Python Software Foundation, Beaverton, OR, March 26, 2017.

	Available online from *Welcome to Python.org: Python 3.6.1 documentation* at: https://docs.python.org/3/tutorial/; April 4, 2017 was the last accessed date.

+ \cite{DrakeJr2018a}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "Python/C API Reference Manual," Python Software Foundation, Beaverton, OR, April 1, 2018.

	Available online from *Welcome to Python.org: Python 3.6.5 documentation* at: https://docs.python.org/3/c-api/; April 2, 2018 was the last accessed date.

+ \cite{DrakeJr2018}
	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "Extending and Embedding the *Python* Interpreter," Python Software Foundation, Beaverton, OR, April 1, 2018. 

	Available online from *Welcome to Python.org: Python 3.6.5 documentation* at: https://docs.python.org/3/extending/; April 2, 2018 was the last accessed date.

+ \cite{DrakeJr2017c}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "*Python* 3.6.1 documentation," Python Software Foundation, Beaverton, OR, March 31, 2017.

	Available online at: https://docs.python.org/3/; March 31, 2017 was the last accessed date.

+ \cite{DrakeJr2016b}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "The *Python* Standard Library," Python Software Foundation, Beaverton, OR, March 23, 2016.

	Available online from *Python 3.5.1 documentation* at: https://docs.python.org/3/library/; April 1, 2016 was the last accessed date.

+ \cite{DrakeJr2016a}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "The *Python* Language Reference," Python Software Foundation, Beaverton, OR, March 31, 2016.

	Available online from *Python 3.5.1 documentation* at: https://docs.python.org/3/reference/index.html; April 1, 2016 was the last accessed date.

+ \cite{Thurlow2012}

	Steven Thurlow, "A Beginner's Python Tutorial," GitHub, Inc., San Francisco, CA, March 30, 2012.

	Available online from *Steven Thurlow's GitHub repository* at: https://github.com/stoive/pythontutorial; self-published; April 4, 2017 was the last accessed date.

+ \cite{Ziade2008}

	Tarek Ziade, "Expert *Python* Programming," Packt Publishing, Birmingham, West Midlands, England, U.K., 2008.









##	Books Covered

+ \cite{Alchin2010}
+ \cite{Hall2009b}



# Random

+ https://www.tutorialspoint.com/python/python_if_else.htm
+ https://dev.to/ogwurujohnson/distinguishing-instance-variables-from-class-variables-in-python-81
+ https://softwareengineering.stackexchange.com/questions/340383/assigning-instance-variables-in-function-called-by-init-vs-function-called
+ http://www.dummies.com/programming/python/working-with-variables-in-python/
+ https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-2-8e0db3ddd531
+ https://www.tutorialspoint.com/python/python_classes_objects.htm
+ https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1_Basics.html
+ http://kronosapiens.github.io/blog/2014/05/10/from-ruby-to-python.html
+ https://docs.python.org/3.5/tutorial/classes.html?highlight=inheritance#inheritance
+ https://softwareengineering.stackexchange.com/questions/254576/is-it-a-good-practice-to-declare-instance-variables-as-none-in-a-class-in-python
+ https://syntaxdb.com/ref/python/class-variables
+ https://docs.python.org/2/tutorial/classes.html
+ https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3
+ https://www.python-course.eu/python3_class_and_instance_attributes.php
+ http://home.wlu.edu/~lambertk/pythontojava/InstanceVariables.htm
+ https://timothyawiseman.wordpress.com/2012/10/06/class-and-instance-variables-in-python-2-7/






#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


#	Notes About *Unified Modeling Language*

This document is my summary, or cheat sheet, about the Unified Modeling
	Language (UML).


##	Author's note


Use this set of terms, Set #1, interchangeably \cite{WikipediaContributors2018d}:
+ class instance
+ class object
+ instance
+ instance object
+ object instance




##	Class Diagrams

In UML, the class diagram statically represents the software architecture of a
	software.

The class diagram depicts the elements, such as classes and packages, and the
	static relationships (not dynamic interactions) between them
	\cite{WikipediaContributors2018d}.

For each class in the class diagram, it has three compartments that are described
	as follows \cite{WikipediaContributors2018d}: 
+ top compartment
	- Name of the class
	- Center aligned
	- In bold font
	- Captialize the first letter of each word
		* If the class name is a concatenation of words, the first letter of each
			word in this concatenation shal be capitalized.
		* That is, write the first letter of each word in upper case.
			\cite{WikipediaContributors2018g}.
		* Or, use the camel case \cite{WikipediaContributors2018f,WikipediaContributors2018g}.
		* Or, use the Hungarian notation \cite{WikipediaContributors2018e}.
+ middle compartment
	- Class attributes.
	- Left aligned.
	- Write each attribute (entirely) in lower case \cite{WikipediaContributors2018g}.
		* Use of the snake case is strongly recommended \cite{WikipediaContributors2018g}.
+ bottom compartment
	- Operations (i.e., functions or methods) that "the class can execute."
	- Left aligned.
	- Write each operation (entirely) in lower case \cite{WikipediaContributors2018g}.
		* Use of the snake case is strongly recommended \cite{WikipediaContributors2018g}.



###	Notes about Classes and Objects

Additional notes about classes:
+ A class member is an attribute or method/operation of a given class
	 \cite{WikipediaContributors2018d}.





Additional notes about objects:
+ The state of an object is determined by the set of attributes and their
	corresponding values. 















###	Visibility and Scope of Class members

Visibility of class members \cite{WikipediaContributors2018d}:
+ "+": public
+ "-": private
+ "#": protected
+ "/": derived
	- Can be combined with another type of visibility
+ "~": package
+ "\*": random



Types of scope for class members \cite{WikipediaContributors2018d}:
+ classifier members; or, static members
	- *Underline the name of each classifier member.*
	- The scope of a classifier member specified by the scope of the class
		owning it.
	- The value of a classifier attribute should be the same for all instances of
		the class.
	- Invoking/invocating a classifier method shall not affect the state of any class
		instance (or instance of the class);
		invoking a classifier method should not modify any instance attribute
			of any object. 
+ instance members
	- Assume each member of a class to be an instance member, unless its
		name is underlined;
		a class member that has an underlined name is an classifier member.
	- The scope of an instance member is restricted to a specific object instance
		of the class.
	- The value of an instance attribute can vary between instances of the class.
	- Invoking/invocating an instance method can affect the state of any class instance
		(or instance of the class);
		invoking an instance method can modify the value of any instance
			attribute of any object. 








###	Types of instance-level relationships


Notes about the types of instance-level relationships
	\cite{WikipediaContributors2018d}:
+ dependency
+ association
+ aggregation
+ composition

Difference between compoition and aggregation:
+ 
+ 
















###	Class-level relationships

+ generalization/inheritance
+ realization/implementation
+ general relationship
	- dependency
	- multiplicity













###	Analysis of stereotypes















#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken from my
	*BibTeX* database (set of *BibTeX* entries).














#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


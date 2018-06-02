#	Notes About *Unified Modeling Language*

This document is my summary, or cheat sheet, about the Unified Modeling
	Language (UML).

##	Table of Contents

+ [Author's note](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#authors-note)
+ [Types of UML Diagrams](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#types-of-uml-diagrams)
+ [Class Diagrams](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#class-diagrams)
	- [Notes about Classes and Objects](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#notes-about-classes-and-objects)
	- [Visibility and Scope of Class members](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#visibility-and-scope-of-class-members)
	- [Types of instance-level relationships](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#types-of-instance-level-relationships)
	- [Class-level relationships](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#class-level-relationships)
	- [Analysis of stereotypes](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#analysis-of-stereotypes)
+ [References](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/uml.md#references)









##	Author's note


Use this set of terms, Set #1, interchangeably \cite{WikipediaContributors2018d}:
+ class instance
+ class object
+ instance
+ instance object
+ object instance













##	Types of UML Diagrams


This figure shows the hierarchical categorization of UML diagrams
	\cite{WikipediaContributors2018h}.

![Figure 1 Hierarchical categorization of UML diagram](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/pics/UML_diagrams_overview.png)

The categories of *UML 2.x* are also listed, and briefly described, below
	\cite{WikipediaContributors2018h}:
+ structural diagrams, which "represent structural information"
	- **class diagrams**
	- component diagrams
	- composite structure diagrams
	- deployment diagrams
	- object diagrams
	- package diagrams
	- profile diagrams
+ behavioral diagrams, which "represent general types of behavior" and
	different aspects of interactions
	- **activity diagrams**
	- **state machine diagrams**
	- **use case diagrams**
	- **interaction diagrams**, which represent "different aspects of interactions"
		* communication diagrams
		* interaction overview diagrams
		* **sequence diagrams**
		* **timing diagrams**

















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
	- Note that I use methods and member functions interchangeably
		\cite{WikipediaContributors2017a3}.


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
	- A unidirectional association from the dependent element (or client or
		source) to the	 independent element (or supplier, server, target).
	- If there exists a change in the independent element, there exists a change
		to the dependent element.
+ association
	- A family of links that connects any number of classes.
	- It represents a "has-a" relationship.
	- It can be named.
	- We can label an end of an association with its properties, such as:
		* role name
		* ownership indicator
		* multiplicity
		* visibility
	- Types of association:
		* bidirectional
		* unidirectional
		* aggregation:
			- Includes composition aggregation
		* reflexive
	- The most common types of association are bidirectional and unidirectional.
	- A binary association connects two elements.
	- A ternary association connects three elements.
+ aggregation
	- "Represent[s] a software or database relationship"
	- "When the container is destroyed, the contents are usually not destroyed"
	- Characterized as a "catalog containment."
	- It represents a "part-whole," or "part-of," relationship.
	- An aggregation is a variant of the association relationship.
	- An aggregation is more specific than the association relationship.
	- It describes a structural relationship, rather than a behavioral relationship;
		it specifies how objects of different classes connect to each other;
		or how objects of a class (i.e., requesting objects) causes objects of
			another class (i.e., controlled objects) to perform an action on its
			behalf by "sending a message" to, "invoking a method" on, or
			"calling a member function" of "the controlled object"
		\cite{WikipediaContributors2017a3}.
	- In an aggregation relationship, each object (requesting object and
		controlled object) has a role;
		this "role[s] describe the public aspects of [the] object[s]" in the context
			of the association
		\cite{WikipediaContributors2017a3}.
	- It can be named.
	- We can label an end of an association with its properties, such as:
		* role name
		* ownership indicator
		* multiplicity
		* visibility
	- An aggregation involves only two classes, as a binary association.
	- **Since the difference between an aggregation and an association is
		insignificant during implementation, class diagrams can ignore
		aggregations and simply replace them with associations.**
	- Aggregation can describe the relationship between a collection, or
		container, and each element in the collection/container;
		note that destroying the container does not destroy the
			elements/contents of the container;
			hence, classes representing the elements in the container "do not
				have a strong lifecycle dependency on the container."
+ composition
	- "Represent[s] real-world whole-part relationships"
	- "When the container is destroyed, the contents are also destroyed" 
	- Characterized as a "physical containment."


Difference between composition and aggregation
	\cite{WikipediaContributors2018d}:
+ "The aggregation relationship is often 'catalog' containment to distinguish it
	from composition's 'physical' containment."

















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


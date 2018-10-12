#	Notes About Databases and Information Systems


##	Table of Contents





##	Database Management Systems

A database is a collection of data that is systematically organized
	for access, storage, and processing
	\cite{DictionaryDotComStaff2018,WikipediaContributors2018r}.

A "general-purpose" database management system (DBMS) is a software system that enables people to create, maintain, and access databases \cite{WikipediaContributors2018r}.

The main functions of DBMS are \cite{WikipediaContributors2018r}:
+ data definition, data is organized according to definitions of
	relationships between the data; these definitions need to be created,
	modified, and deleted
+ update, which allows data to be added, modified, or removed from
	the database
+ retrieval, which allows data to be accessed
+ administration, which involves registering people to access the
	database and monitoring them, and implementing techniques for data
	security and data integrity, performance monitoring, concurrency
	control, and data/information recovery

A data model (or datamodel) is a description of how data is organized
	and related to each other, and the relationships between data and
	entities in the real world \cite{WikipediaContributors2018x};
We can create data models using entities, attributes, relations, and
	tables \cite{WikipediaContributors2018x}.
In enterprise modeling, a function model complements a data model
	\cite{WikipediaContributors2018x}.
The main categories of data model instances are
	\cite{WikipediaContributors2018x}:
+ conceptual data model, which is a technology-independent description
	of the semantics of a specific domain (in the information context
	\cite{WikipediaContributors2018y}) and defines the scope of the
	model
+ logical data model (or logical schema \cite{WikipediaContributors2018y}),
	which describes the semantics of a conceptual model for "a
	particular data manipulation technology", in terms of (relational)
	tables, columns, object-oriented classes, and XML tags;
	a logical data model is a detailed reflection of a conceptual data
		model's domain-specific semantics, and is independent of the
		physical data model ("particular database management product or
		storage technology" \cite{WikipediaContributors2018y});
	it is a representation of a domain-specific abstract structure
		(or, they "represent the abstract structure of a domain of
		information") \cite{WikipediaContributors2018y};
	use the logical data model to create databases, and use it as the
		basis of a physical data model \cite{WikipediaContributors2018y}
+ physical data model, which describes how data is physically stored
	in terms of partitions, processors, and tablespaces.


WikipediaContributors2018w

A database model is an abstract model (specifically, a data model) that
	describes the logical structure of a database, such.
	\cite{WikipediaContributors2018w}


A query language, or data query languages (DQL), is a computer language for
	making queries on databases and information systems \cite{WikipediaContributors2018v}.

The main categories of query languages are \cite{WikipediaContributors2018v}:
+ database query languages
+ information retrieval query languages


##	Database Design

cite this!!!

+ Database design is the process of organizing data/information, using a
	database model.
+ Database design involves creating the ontology of the desired data set:
	- Data classification
		* Deciding what/which data to store.
	- Identifying the relationships between the data.
+ The types of ontology are:
	- domain ontology (or domain-specific ontology)
	- upper ontology (or foundation ontology)
		* A model of common objects, and common relationships between these
			objects, that can be applies to a set of domain ontologies.
	- hybrid ontology
		* A combination of domain ontology and upper ontology.
	- Reference: https://en.wikipedia.org/wiki/Ontology_(information_science)
		* ontology visualization techniques
		* ontology engineering (or ontology building), part of knowledge
			engineering


object-relational mapping

##	Database Models


##	Categories of Databases

###	Object Databases



###	SQL

Relational databases
+
+ relational database management systems
	- database servers
		* MySQL
		* PostgreSQL
			+ Supports ODBC
		* SQLite
		* Firebird (database server)
	- database clients
		* SQuirrel SQL client



###	NoSQL

####	Key-Value Store

####	NoSQL Database Management Systems

+ HBase
+ Cassandra
+ MongoDB



Document-oriented database (= document store)
+ Use document-oriented information (= semi-structured data)
+ Examples:
	- XML database

###	NewSQL




##	Distributed Databases for Big Data


+ Hive
+ Spark
+ Kafka
+ Flume


Apache Ignite???


###	Distributed Databases Based on MapReduce

Apache Hadoop (and HDFS):
+ Pig




##	Database Data Formats

Data formats for databases \cite{WikipediaContributors2018r}:
+ SQL
+ ODBC, Open Database Connectivity \cite{WikipediaContributors2018t}
	- API to access DBMS
	- There exists ODBC-to-JDBC (ODBC-JDBC) and JDBC-to-ODBC
		(JDBC-to-ODBC) bridges.
	- Also, see *unixODBC* and Microsoft Windows ODBC
		\cite{WikipediaContributors2018u} for the ODBC data API for
		associated operating systems.
+ JDBC, Java Database Connectivity.
	- API based on *Java* to access/modify a database
		\cite{WikipediaContributors2018s}.
+ GDA, GNU Data Access \cite{WikipediaContributors2017a5}
	- *GNOME-DB* is a *GNOME*-based database management systems.
	- It supports access to persistent data (in databases).
	- GDA, GNU Data Access, is its data management API.
		* Compared to JDBC and ODBC, it provides a larger set of
			features, and is considered as a complete architecture
			for databases.
		* "*Libgda* is a database access library", which serves
			as "a database and abstraction layer".


Use ODBC, JDBC, and GDA wrappers for database management systems
	of my choice \cite{WikipediaContributors2017a5}.



#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).

**If these citations/references are not found in this list of references,
	information about them can be found in my *BibTeX* database.**





#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

#	Notes About Databases and Information Systems


##	Table of Contents





##	Definitions of Database, Database Management System, and Related Concepts

A **database** is a collection of data that is systematically organized
	for access, storage, and processing
	\cite{DictionaryDotComStaff2018,WikipediaContributors2018r}.

A "general-purpose" **database management system** (**DBMS**) is a software system that enables people to create, maintain, and access databases \cite{WikipediaContributors2018r}.

The main functions of DBMS are \cite{WikipediaContributors2018r}:
+ **data definition**, data is organized according to definitions of
	relationships between the data; these definitions need to be created,
	modified, and deleted
+ **update**, which allows data to be added, modified, or removed from
	the database
+ **retrieval**, which allows data to be accessed
+ **administration**, which involves registering people to access the
	database and monitoring them, and implementing techniques for data
	security and data integrity, performance monitoring, concurrency
	control, and data/information recovery

A **database model** is an abstract model (specifically, a data model) that
	describes the logical structure of a database, and how to store,
	organize, and manipulate data \cite{WikipediaContributors2018w}.

A **data model** (or **datamodel**) is a description of how data is organized
	and related to each other, and the relationships between data and
	entities in the real world \cite{WikipediaContributors2018x};
We can create data models using entities, attributes, relations, and
	tables \cite{WikipediaContributors2018x}.
In enterprise modeling, a **function model** complements a data model
	\cite{WikipediaContributors2018x}.
The main categories of data model instances are
	\cite{WikipediaContributors2018x}:
+ **conceptual data model**, which is a technology-independent description
	of the semantics of a specific domain (in the information context
	as abstract structures \cite{WikipediaContributors2018y}) and
	defines the scope of the model
	- "Includes high-level data constructs" that are used to create
		architectural descriptions in layperson terms
		\cite{WikipediaContributors2018y}.
	- Avoids technical names to facilitate understanding of the
		architectural description's data basis
		\cite{WikipediaContributors2018y}.
	- "May not be normalized" \cite{WikipediaContributors2018y}.
+ **logical data model** (or **logical schema**
	\cite{WikipediaContributors2018y}),
	which describes the semantics of a conceptual model for "a
	particular data manipulation technology", in terms of (relational)
	tables, columns, object-oriented classes, and XML tags
	- A logical data model is a detailed reflection of a conceptual data
		model's domain-specific semantics, and is independent of the
		physical data model ("particular database management product or
		storage technology" \cite{WikipediaContributors2018y})
	- It is a representation of a **domain-specific abstract structure**
		(or, they "represent the abstract structure of a domain of
		information") \cite{WikipediaContributors2018y};
	- Use the logical data model to create databases, and use it as the
		basis of a physical data model \cite{WikipediaContributors2018y}
	- types of logical data models \cite{WikipediaContributors2018y}
		* **hierarchical data model** \cite{WikipediaContributors2018w}.
		* **network data model** \cite{WikipediaContributors2018w}
		* **relational model** \cite{WikipediaContributors2018w}
		* **object-oriented data model**, **object model**, and
			**objective database** \cite{WikipediaContributors2018w}
		* **entity-relationship model** \cite{WikipediaContributors2018w}
			+ **enhanced entity-relationship model**
				\cite{WikipediaContributors2018w}
		* **document model** \cite{WikipediaContributors2018w}
		* **entity-attribute-value model** \cite{WikipediaContributors2018w}
		* **star schema** \cite{WikipediaContributors2018w}
		* **object-relational database** \cite{WikipediaContributors2018w}
			+ An object-relational database is a combination of the object
				model and the relational model.
	- rationale/justifications for creating logical data model
		\cite{WikipediaContributors2018y}:
		* Facilitates understanding of business data elements and requirements.
		* Provides the basis for database design.
		* Facilitates the avoidance of data redundancy, data inconsistency,
			and business transaction inconsistency;
			avoidance of the latter pair is dependent on avoiding data
				redundancy.
		* Facilitates re-use and sharing of data.
		* Facilitates the reduction of time and effort/cost in developing
			and maintaining the database.
		* Verifies the logical process models.
		* Facilitates impact analysis.
	- Includes entities (tables), attributes (columns/fields), and
		relationships (keys) \cite{WikipediaContributors2018y}
	- Uses defined (and specific) business names, and less generic names,
		for entities and attributes \cite{WikipediaContributors2018y}.
	- Is technology independent, and is based on platforms and DBMSes
		\cite{WikipediaContributors2018y}.
	- "Is normalized to the fourth normal form (4NF)"
		\cite{WikipediaContributors2018y}.
+ **physical data model**, which describes how data is physically stored
	in terms of partitions, processors, and tablespaces.
	- Involves using specific database management technology
		\cite{WikipediaContributors2018y}.
	- "Includes tables, columns, keys, data types, validation rules,
		database triggers, stored procedures, domains, and access
		constraints" \cite{WikipediaContributors2018y}.
	- Uses more defined (and specific) business names, for entities and
		attributes, subject to limitations of DBMS and company defined
		standards \cite{WikipediaContributors2018y};
		e.g., abbreviated column names \cite{WikipediaContributors2018y}.
	- "Includes primary keys and indices for fast data access"
		\cite{WikipediaContributors2018y}.
	- If the database is for "**online transaction processing** (**OLTP**) or
		**Operational Data Store** (**ODS**), it is usually not de-normalized";
		else, de-normalize the physical data model to meet performance
			requirements of the database (context-dependent).
	- Examples:
		* inverted index \cite{WikipediaContributors2018w}
		* flat file \cite{WikipediaContributors2018w}

Other **database models** (or **data models**) \cite{WikipediaContributors2018w}:
+ **associative model**
+ **correlational model**
+ **multi-dimensional model**
+ **multi-value model**
+ **semantic model**
+ **XML database**
+ **named graph**
+ **triplestore**

WikipediaContributors2018z
WikipediaContributors2018w

The **relational data model** is the most popular database model (and data
	model);
	it uses the **table-based format** \cite{WikipediaContributors2018w}.

##	Ancillary Definitions






A **storage record** is a group of fields, data, or words
	\cite{WikipediaContributors2016m}
+ A **record** is "a self-contained collection of information about a single
	object", or a collection of distinct items
	\cite{WikipediaContributors2016m}.
+ A **row** (or **tuple**) "represents a single, implicitly structured data item
	in a table," or "a set of related data" \cite{WikipediaContributors2018a15}
	- Each row in a table (or relational database) has the same structure
		\cite{WikipediaContributors2018a15}.
	- Each row in a table represents a set of related data
		\cite{WikipediaContributors2018a15}.
	- The implicit structure and significance of a row implies a sequence
		of data values (or a sequence of sets of data values) such that
		each column in that row has a value (or a set of data values)
		\cite{WikipediaContributors2018a15}.
	- A row is a relvar that is comprised of a set of two-tuples, where each
		two-tuple consist of the name of the appropriate column and the value
		associated with this row for that column
		\cite{WikipediaContributors2018a15}.
	- Each column of a row/table requires data value(s) of a specific
		data type \cite{WikipediaContributors2018a15}.

"A **database segment** is a database object that occupies physical space,
	such as table data and indexes/indices" \cite{WikipediaContributors2018z}.

A **tablespace** is a storage location of the actual data underlying database
	objects (database storage locations) \cite{WikipediaContributors2018z}.
+ it provides a layer of abstraction between the logical and physical
	data models \cite{WikipediaContributors2018z};
+ it allocates storage for all data segments managed by the DBMS
	\cite{WikipediaContributors2018z};
+ when creating database segments, we can refer to the tablespace by name
	\cite{WikipediaContributors2018z};
+ it does not store the logical database structure;
	- for a given logic schema, an unique object in the schema has a
		unique tablespace \cite{WikipediaContributors2018z};
	- for a given tablespace, it allows multiple database segments to
		refer to it \cite{WikipediaContributors2018z};
	- for a given tablespace, use it to specify a database model that
		forms a bond between logical and physical data
		\cite{WikipediaContributors2018z};
	- use a tablespace to optimize performance of database access/modification
		and decide where to store indexes/indices and tables
		\cite{WikipediaContributors2018z};
	- a tablespace can store its data in a file in the file system
		\cite{WikipediaContributors2018z};
	- a file cannot be associated with multiple tablespaces
		\cite{WikipediaContributors2018z};
	- a DBMS allows the direct configuration of a tablespace over device
		entries of an operating system (i.e., raw devices), in order to
		gain a performance speedup "by avoiding OS file system overheads"
		\cite{WikipediaContributors2018z}.

In *UNIX*-like operating systems, a **raw device** is a special logical device
	that is associated with **character device files**
	\cite{WikipediaContributors2018a3,Bovet2006}, and enables/allows
	direct access by a **storage device** (e.g., hard disk drive)
	\cite{WikipediaContributors2017a6}.
+ that is, the raw device allows software applications to use storage
	devices directly, without using the page caches
	\cite{WikipediaContributors2018a4} and buffers of the operating
	system - although the **disk buffer** \cite{WikipediaContributors2018a2,WikipediaContributors2016l}
		of the **tertiary storage devices** would still be used
		\cite{WikipediaContributors2017a6}.

In *UNIX*-like operating systems, a **device file** (or **special file**) is an
	interface to a device driver, and appears in a file system as an
	ordinary file \cite{WikipediaContributors2018a3}.
+ Using I/O system calls for the application, users can interact with
	its device driver \cite{WikipediaContributors2018a3}.
+ It is managed by the virtual file system \cite{WikipediaContributors2018a3};
	- the controlling daemon "monitors hardware addition and removal
		at run time" and modifies the device file system (if the device
		file system has not been modified by the kernel)
		\cite{WikipediaContributors2018a3}.

A "**character device (driver)**, or **character special file**, provides
	unbuffered, direct access to the hardware device"
	\cite{WikipediaContributors2018a3};
+ it can also request for read and write operations to align to block
	boundaries (or otherwise) \cite{WikipediaContributors2018a3};
+ block-based hardware typically requires software to read/write aligned
	blocks \cite{WikipediaContributors2018a3}.

A **block device**, or **block special file**, provides software with buffered
	access to hardware devices with restrictions on size or alignment
	\cite{WikipediaContributors2018a3};
+ however, it has no guarantee on performance nor order of data between any
	character, byte, nor block, due to the buffering
	\cite{WikipediaContributors2018a3}.

An operating system can represent hardware devices, such as hard
	disks, as **character/block devices** \cite{WikipediaContributors2018a3}.

A **device node** corresponds to a resource allocated by the kernel of the
	operating system \cite{WikipediaContributors2018a3}.

A **pseudo-device** is a **device node** in UNIX-like systems that do not
	correspond to a **physical device** \cite{WikipediaContributors2018a3}.

The ***mknod*** system call, which is a service request made from a computer
	program on the OS kernel, creates nodes in the file system tree
	\cite{WikipediaContributors2018a3};
	such nodes can be moved or deleted using file system system calls
		and commands \cite{WikipediaContributors2018a3}.



A **query language**, or **data query languages** (**DQL**), is a computer
	language for making queries on databases and information systems
	\cite{WikipediaContributors2018v}.

The main categories of query languages are \cite{WikipediaContributors2018v}:
+ **database query languages**
+ **information retrieval query languages**


"A **table** is a collection of related data" stored in a database, using
	a structured format consists of (horizontal) rows and (vertical) columns
	(identifiable by name) \cite{WikipediaContributors2018a5,WikipediaContributors2018a15};
+ the number of columns are specified (and fixed), and the table can
	have any number of rows \cite{WikipediaContributors2018a5};
+ for any {row, column} entry, it can have multiple values
	\cite{WikipediaContributors2018a5};
+ a table is defined for relational databases and flat-file databases
	\cite{WikipediaContributors2018a5}.
+ A **table** can be used to describe a **relation**, which is a set without
	duplicates \cite{WikipediaContributors2018a5};
	- however, most tables are **multisets** (or **bags**)
		\cite{WikipediaContributors2018a5}.
+ A table can have **associated metadata**, such as constraints on the table
	or values for certain columns \cite{WikipediaContributors2018a5}.

A **view** can function as a relational table, although its data would be
	computed/calculated at **query time** \cite{WikipediaContributors2018a5};
+ an **external table** can be considered as a view
		\cite{WikipediaContributors2018a5}.

For the **relational model of database**, a **table** can be considered as a
	**relation**, even though they are not strictly equivalent
	\cite{WikipediaContributors2018a5}.

In a **hierarchical database**, which is a **non-relational system**, a
	**table** has a distant counterpart known as **structured file**, which can
	have repeating information in a row (i.e., the **child data segments**)
	\cite{WikipediaContributors2018a5};
+ "data are stored [as a] sequence of physical records"
	\cite{WikipediaContributors2018a5}.

A **primary key** is a specific choice of columns that can uniquely
	identify rows \cite{WikipediaContributors2018a5} (or identify
	a tuple in a relation \cite{WikipediaContributors2018a6}).
+ For "the relational model in databases, a primary key is a specific
	choice of a minimal set of attributes (columns) that uniquely
	specify a tuple (row) in a relation (table)"
	\cite{WikipediaContributors2018a6};
+ Mathematically, "a primary key is a choice of **candidate key** (i.e.,
	a **minimal superkey**), and other candidate keys are **alternate keys**
	\cite{WikipediaContributors2018a6}.
+ Assign an unique index to each alternate key, so that we can use the
	unique index to determine if duplicates (of alternate keys) exist
	\cite{WikipediaContributors2018a6};
	- use this to prevent insertion/addition of duplicate alternate keys
		\cite{WikipediaContributors2018a6}; and
	- unique columns in databases cannot include duplicates
		\cite{WikipediaContributors2018a6}.
	- for a single-table select, or filtering in a *where* [command/] clause,
		we can use alternate keys as primary keys
		\cite{WikipediaContributors2018a6}.
	- However, alternate keys cannot be used as primary keys
		\cite{WikipediaContributors2018a6}.













A **natural key** is a primary key consisting of real-world observables
	\cite{WikipediaContributors2018a6}.
+ A natural key (or, **business key** or **domain key**) is a **unique key**
	in database design that uses the relational model, and is based on
	real-world attributes \cite{WikipediaContributors2018a7}.
+ Use natural keys in business-related columns
	\cite{WikipediaContributors2018a7}.
+ "A natural key is a **candidate key** that has a logical relationship
	to the attributes within that row" \cite{WikipediaContributors2018a7}.
+ The primary advantage of a natural key over a surrogate key is its
	existence \cite{WikipediaContributors2018a7};
	- hence, no new, artificial column has to be added to the schema to
		create the surrogate key \cite{WikipediaContributors2018a7}.
	- this has no significant meaning outside the database environment
		\cite{WikipediaContributors2018a7}.
	- When a natural key can be identified, selection of the natural key
		over the surrogate primary keys can simplify data processing
		\cite{WikipediaContributors2018a7}.
	- It ensures that there exists only a row per key, since this is
		based on a real-world observation \cite{WikipediaContributors2018a7}.
+ I noted some flimsy connection to the following references:
	- **Open-world assumption** (**OWA**) \cite{WikipediaContributors2018a8}
	- **Closed-world assumption** (**CWA**) \cite{WikipediaContributors2018a9}
	- **Single version of the truth** (**SVOT**)
		\cite{WikipediaContributors2018a10}
		* A data warehouse that has a single centralized database, or a
			distributed synchronized database, to store "all of an organization's data in a consistent and non-redundant form."
	- **Single source of truth** (**SSOT**) \cite{WikipediaContributors2018a11}
		* A method to "structure information models and associated data
			schema," so "that every data element is stored exactly once"
			\cite{WikipediaContributors2018a11}.
		* "Always source a particular piece of information from one place"
			\cite{WikipediaContributors2018a10}.
		* Use referencing to link to data elements in the SSOT databases,
			which are based on the relational schema or distant federated
			databases, so that "all other locations of the data" refer/point
			"to the primary `source of truth' location"
			\cite{WikipediaContributors2018a11};
			- this avoids the need to keep duplicates of a data element updated,
				by allowing value from the only/primary location to
				propagate throughout the computer network
				\cite{WikipediaContributors2018a11};
			- it also avoids the risks of "incorrectly linked duplicates",
				and denormalizing data elements (see
				database denormalization \cite{WikipediaContributors2018a12}).
			- Usage of pointers also covers copying and updating database
				tables, rows, and cells \cite{WikipediaContributors2018a11}


A **surrogate key** is an attribute that functions as a key
	\cite{WikipediaContributors2018a6,WikipediaContributors2018a13}.
+ Synonyms of "surrogate key" are \cite{WikipediaContributors2018a13}:
	- synthetic key
	- entity identifier
	- system-generated key
	- database sequence number
	- factless key
	- technical key
	- arbitrary unique identifier
+ In certain circumstances, during software development or a data
	science project, it can be inconvenient to use a natural key
	to identify a tuple in a relation, since it may require multiple
	columns or large text fields \cite{WikipediaContributors2018a6}.
	- Hence, use a surrogate key as a substitute (primary key) to avoid
		giving more priority/importance to the natural key or other
		candidate keys \cite{WikipediaContributors2018a6}.
	- Similarly, a surrogate key can be chosen instead of any of the
		multiple candidate keys that do not provide an advantage over
		the other candidate keys \cite{WikipediaContributors2018a6}.
+ Since primary keys are chosen to facilitate information processing
	during software development or a data science project, many cases
	of database application design use surrogate primary keys to
	further facilitate information processing
	\cite{WikipediaContributors2018a6}.
+ For databases based on the hybrid **object-relational model** (**ORM**),
	which is based on the object-oriented programming model and the
	relational model, they also use surrogate primary keys to further
	facilitate information processing \cite{WikipediaContributors2018a6}.
	- The restrictions on surrogate primary keys are
		\cite{WikipediaContributors2018a6}:
		* Primary keys are immutable (not changed nor reused)
			\cite{WikipediaContributors2018a6}
		* Primary keys should be deleted, together with associated
			record \cite{WikipediaContributors2018a6}
		* Primary keys should be an anonymous trigger, or numeric
			identifier \cite{WikipediaContributors2018a6}
		* These restrictions only apply for the object-relational model,
			such as the **active record pattern**
			\cite{WikipediaContributors2018a6}
		* Hence, for databases based on the relational model, or SQL
			standard, do due diligence when deciding which key should
			be an immutable primary key \cite{WikipediaContributors2018a6};
			some DBMSes do not allow usage of the **UPDATE** SQL statement
				to change values of the primary keys
				\cite{WikipediaContributors2018a6}.
+ A surrogate key "is a unique identifier for an entity in the
	modeled world ([data model]) or an object in the database ([storage model])"
	\cite{WikipediaContributors2018a13}.
	- It "is not derived from application data"
		\cite{WikipediaContributors2018a13}
		* In contrast, a natural key is derived from application data
			\cite{WikipediaContributors2018a13}.
	- A **storage model** represents important physical aspects of a
		data store's data structure \cite{WikipediaContributors2011};
		* on the other hand, a **data model** represents important
			logical aspects of a database's data structure
			\cite{WikipediaContributors2011}
+ The attributes/features/qualities/characteristics of a surrogate key are
	\cite{WikipediaContributors2018a13}:
	- a unique, system-wide value that is never reused
	- system generated value; it is generated by the database management
		system
	- immutable value that cannot be modified by users or applications
	- value without semantic significance
	- value is not accessible by users or applications
	- value is not comprised/combined/composed of values from different
		domains, and cannot be decomposed into constituents, and not
		a synthesis/derivation of application data in the database.
	- a surrogate key can be used as a primary key
+ The surrogate key can exist as a separate from other database/system generated
	values, such as universally unique identifier (UUID) and
	globally unique identifier (GUID) \cite{WikipediaContributors2018a13,WikipediaContributors2018a14}.
+ Surrogate keys are typically sequential numbers
	\cite{WikipediaContributors2018a13}.
+ By designing the surrogate key to be independent from all fields
	of the database, changes in the data values or design of the database
	would not affect the value of the surrogate key
	\cite{WikipediaContributors2018a13};
	such designs of the database facilitate software development using
		agile development processes and ensure that the surrogate keys
		remain unique \cite{WikipediaContributors2018a13}.
+ Advantages of surrogate keys \cite{WikipediaContributors2018a13}:
	- immutability of surrogate keys, unlike primary keys and natural keys
	- requirement changes, which may affect natural keys, would not affect
		surrogate keys;
		merging databases may affect natural keys, but not surrogate keys
	- performance (in terms of lookup time... access time???) of surrogate
		keys is better than natural/business keys
		- This is because the former only depends on finding records with
			one column (unique, immutable surrogate key), while the latter
			depends on finding records {CITE THIS!!!} with multiple columns.


In a temporal database, each row has a natural/business key and the
	surrogate key, so that the former has a mapping to an unique entity
	in modeled world and the latter has a mapping to a unique row in
	the database \cite{WikipediaContributors2018a13}.
+ Each row in the table/database represents the values of attributes for
	a time slice, and indicate the life span of the entity
	\cite{WikipediaContributors2018a13}.
+ Hence, for a natural/business key or unique entity in modeled world,
	it can have multiple entries in a temporal database (since a person
	or an organization can have multiple business entities)
	\cite{WikipediaContributors2018a13}.











"In relational database terms, a primary key does not differ in form
	or function from alternate keys" \cite{WikipediaContributors2018a6};
+ there can be different reasons for choosing a key as the primary
	key over other keys, such as \cite{WikipediaContributors2018a6}:
	- it is the "preferred" identifier for data in the table;
	- its usage as foreign key references from other tables;
	- it indicates certain technical rather than semantic feature
		of the table; and
	- special syntax features of certain computer languages and software
		that are used to identify primary keys.

Even though the **relational database model** (based on **relational
	calculus** and **relational algebra**) does not distinguish keys
	based on whether they are primary keys, the SQL computer language
	standard has a feature for primary keys to provide a convenience
	to the application engineer \cite{WikipediaContributors2018a6}.











###	Side Notes on Definitions

A **domain model** captures concepts of a **problem domain**, but it does not
	capture the relationships (and their structure) of data in that domain;
	a logical data model does capture such relationships and their structure
		\cite{WikipediaContributors2018y}.



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

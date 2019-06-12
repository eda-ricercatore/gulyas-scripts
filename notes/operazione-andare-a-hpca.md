#	Operation Go2HPCA

##	Questions

Questions:
+ \cite{Dahl2013}
	- How to convert QUBO into a quantum machine instruction (QMI)
		A QMI produces probabilistic results, rather than deterministic
			results that assembly instructions in von Neumann computing.
		Representations of qubits (and their weights) and couplers
			(and their strengths) as chimera graphs (bipartite graphs).
+ Get access to the API, or dynamic libraries, of dwave_sapi2.
+ Map coloring problems, and other NP-complete (or NP-hard) problems,
	such as QUBO, can be mapped into "a single quantum machine
	instruction (QMI) using the "direct embedding' programming model."
	Section 1, Page 3, of the map coloring white paper from D-Wave.
	By providing a transformation of the problem formulation of map
		coloring (or QUBO, or otherwise) into a chimera graph, we can
		synthesize the network of qubits and couplers on the D-Wave
		machine.






##	Flags for Work-in-Progress

Flags for work-in-progress:
+ \#\#\#\# IMPORTANT NOTES
+ \#\#\#\# TO BE COMPLETED
	- Or: @todo(\<message\>, \<version\>)
+ \#\#\#\# TO BE FIXED








##	To-Do List


***To-do list:***
+ [x] Figure what conferences to target next.
+ [x] List CFP deadlines in sequential order.
+ [x] **Reference machine learning libraries!!!**
+ [x] Libraries associated with NumFOCUS.
+ [x] Clear *Safari* tabs.
+ [ ] Clear *Chrome* tabs.
+ [x] Fix git "push" operation.
+ [x] Fix hg "push" operation.
+ [ ] Graph
	- [x] Synthesize functions/methods/behavior and attributes/fields/properties that have to exist for all graphs, all directed graphs, and all undirected graphs. COMPLETE THIS!!!!
	- [x] Fix functions for directed and undirected graphs.
	- [x] Extend the Exception class for graph_exception.
		* Note that the graph_exception class for the subpackages "utilities/custom_exceptions" and "utilities/specific_exceptions" are the same.
		* [ ] Use the term "exception" or "error"?
	- [x] References about graphs, the graph data structure:
		* [x] \cite{Goodrich2013}
		* [x] \cite{Goodrich2011}
		* [x] \cite{Cormen2013}
		* [x] \cite{Cormen2009}
		* [x] \cite{Goldman2008}
			+ Chapters (51), 52-57.
			+ Collection of Elements -> Algorthmically Positioned: Untagged: Elements are Comparable (need not be unique) -> FibonacciHeap (PriorityQueue Interface), Figures 2.6-2.7.
			* [x] \cite{Atallah2009}
			+ Chapters 1-5, 6???, 7-9, 10, 11, 17, 19, 24, 25, 28.
			+ See pp. 9-10 for information about Fibonacci heaps.
			+ Example using dynamic programming to solve the TSP problem,
				pp.1-17 - 1-18.
		* \cite{Atallah2009a} (for parallel graph algorithms)
	- [ ] directed graphs
		* Implement directed graphs that have:
			+ [ ] vertices with labels
			+ [x] edges with labels but no identities [Ignored]
			+ [ ] edges with labels and identities
		* Based on the definition of edges with labels and identities
			\cite{WikipediaContributors2018a39},
			if a set/list/heap pf edges are required,
				use a graph which edges have identities.
			Else, use a graph which edges have no identities.
		* [ ] directed graphs
		* [ ] directed acyclic graphs (DAGs)
		* [ ] directed multigraphs
		* [ ] directed acyclic multigraphs, where their edges have labels (DAMs)
	- [ ] undirected graphs
		* Implement undirected graphs that have:
			+ [ ] vertices with labels
			+ [ ] edges with labels but no identities
			+ [x] edges with labels and identities [Ignored]
			+ [ ] undirected multigraphs
		* Based on the definition of edges with labels and identities
			\cite{WikipediaContributors2018a39},
			if a set/list/heap pf edges are required,
				use a graph which edges have identities.
			Else, use a graph which edges have no identities.
	- [ ] mixed multigraphs
		* Where their edges can be directed or undirected
		* [x] Mixed multigraphs which edges have identities [Ignored]
		* [ ] Mixed multigraphs which edges have no identities
	- [ ] hypergraphs
		* \cite{Bretto2013}
		* \cite{Cong2003a}
		* \cite{Alpert1996}
		* \cite{Berge1989}
		* \cite{Johnson2013b}
		* These references are numbered [6,22,27,40,106] in my notes on data structures and algorithms.
		* Not so good references: \cite{Basu2007,Lovasz2012,Bunke2008,Crama2011,Lecoutre2009,Carrington2005,Scheinerman1997,Sarrafzadeh1996}
	- [ ] Use checkpointing to restart the simulation by continuing the simulation \cite{WikipediaContributors2019a,Koren2007,Wagner2011,Garg2002,Kshemkalyani2011,Koch2009,Bader2008}.
+ [ ] Database access
	- For experimental results.
+ [ ] Statistical comparison
+ [ ] Data visualization.
	- [ ] Bokeh
	- [ ] Matplotlib
+ [ ] Standard cell library
+ [ ] Logic simulator
+ [ ] Store test results in a database (in *CSV* format), and manage it with a *SQL*
+ [ ] Port logic simulator to GPGPU platform via CUDA.
	- [ ] Get references for CUDA-based programming (or software development).
	- [ ] Learn CUDA-based programming (or software development).
+ [ ] Build noise-based logic circuit for matrix and tensor operations, and to implement artificial neural networks.
+ [ ] Use circuits and scripts from TA job as toy examples to test my NBL solutions.
+ [ ] Write paper \#1 on the NBL cell library design and the NBL logic simulator.
+ [ ] Write paper \#2 on circuits and electronic system to implement matrix and tensor operations.
+ [ ] Update technologies listed in https://insights.stackoverflow.com/survey/2018/
	- SQL database
		* *MySQL*
		* *PostgreSQL*
		* *MariaDB*
	- *Python* interface to *SQL* database.
		* Aurora
		* SQLite
		* Kudu
			+ https://en.wikipedia.org/wiki/Apache_Kudu
			+ https://kudu.apache.org/
			+ *Is this a NoSQL database?*
			+ *Does this support "Big Data" analytics?*
	- Process this with a *NoSQL* database.
		* Cassandra
		* Hbase
		* Accumulo
		* Mongo/DynamoDB
			+ MongoDB
			+ AWS DynamoDB
		* Data-Structures:
			+ Redis
		* Riak
		* Redis/Riak/Dynamo
		* CouchBase
		* Apache
		* Nginx
		* Solr, Lucene, Elastic Search (ElasticSearch), Memcache/Memcached
		* DSE???
		* HDFS???
		* Apache Lucene, Memcache, RabbitMQ
		* ZooKeeper, and/or Consul
		* MariaDB???
		* Comprehensive knowledge of the internal workings of at least one of Postgres, Mongo, Redis
		* noSQL (e.g. Postgres), Python based ORM (e.g. SQL Alchemy) and database technologies (e.g. HDFS, Cassandra, Elastic Search, Druid, etc.)
		* knowledge of NoSQL databases (e.g. Cassandra, ELK), Storm, Nginx technologies.
		* cassandra/hbase/Elastic/Mongo/Couchbase/Redis
		* MongoDB (or any other NoSQL database), Redis (or any other key value store)
		* Working knowledge of SQL, Spark, or Hive preferred
		* SQL (Postgress) and NoSQL (Redis, DynamoDb) databases
		* Knowledge of Big data and NoSQL technologies such as Hadoop YARN, Spark, Hive, Cassandra, HBase, Storm, CASK, Kafka, Flume, is preferred.
		* Experience with NoSQL architectures and map-reduce concepts atop Hadoop, HDFS, and Hive
		* graph databases
			+ Neo4J
			+ AllgroGraph
			+ OrientDB
		* Document Store
			+ CouchDB
			+ MongoDB
			+ RethinkDB
		* Key/Value stores
			+ Redis
			+ KyotoTycoon
			+ Cassandra
			+ [LevelDB](https://github.com/google/leveldb)
				- Developed by Sanjay Ghemawat (sanjay@google.com) and Jeff Dean (jeff@google.com)
			+ [RocksDB](https://github.com/facebook/rocksdb)
			+ DynamoDB
		* Column Store / columnar databases
			+ ClickHouse
		* full text search engines
			+ Elastic Search (ElasticSearch)
		* See [DB-Engines Ranking of Wide Column Stores](https://db-engines.com/en/ranking/wide+column+store)
	- Process this with a *NewSQL* database.
	- Notes:
* https://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems
* https://en.wikipedia.org/wiki/Relational_database_management_system
* https://en.wikipedia.org/wiki/NoSQL
* https://en.wikipedia.org/wiki/NewSQL
* https://en.wikipedia.org/wiki/Apache_Ignite
* https://en.wikipedia.org/wiki/Shared-nothing_architecture
* https://en.wikipedia.org/wiki/Relation_algebra
* https://en.wikipedia.org/wiki/Database_transaction
* https://en.wikipedia.org/wiki/Transaction_log
* https://en.wikipedia.org/wiki/Database_trigger
* https://en.wikipedia.org/wiki/Database_index
* https://en.wikipedia.org/wiki/Stored_procedure
* https://en.wikipedia.org/wiki/Cursor_(databases)
* https://en.wikipedia.org/wiki/Partition_(database)
* https://en.wikipedia.org/wiki/Foreign_key
* https://en.wikipedia.org/wiki/Null_(SQL)
* https://en.wikipedia.org/wiki/Create,_read,_update_and_delete (CRUD)
* https://en.wikipedia.org/wiki/CAP_theorem
* https://en.wikipedia.org/wiki/Armstrong%27s_axioms
* https://en.wikipedia.org/wiki/ACID
* https://en.wikipedia.org/wiki/Concurrency_control
* https://en.wikipedia.org/wiki/Query_optimization
* https://en.wikipedia.org/wiki/Query_plan
* https://en.wikipedia.org/wiki/Query_optimization
* https://en.wikipedia.org/wiki/Replication_(computing)#DATABASE
* https://en.wikipedia.org/wiki/Database_administration_and_automation
* https://en.wikipedia.org/wiki/Database_storage_structures
* https://en.wikipedia.org/wiki/Distributed_database
* https://en.wikipedia.org/wiki/Referential_integrity
* https://en.wikipedia.org/wiki/Relational_algebra
* https://en.wikipedia.org/wiki/Transaction_processing
* https://en.wikipedia.org/wiki/Object-relational_database
* https://en.wikipedia.org/wiki/Outline_of_databases
* https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch
	- Time series databases
		* OpenTSDB
		* Graphite
		* Prometheus
		* Grafana
	- Resource:
		* [DB-Engines Ranking](https://db-engines.com/en/ranking)
	- Big data technologies
		* Hadoop
			+ Hadoop ecosystem (HDFS, MapReduce, Hive, Hbase)
			+ Hadoop integration with large scale distributed data platforms like Teradata, Teradata Aster, Vertica, Greenplum, Netezza, DB2, Oracle, etc
			+ Cloudera/MapR/Hortonworks
			+ MapReduce, HDFS, Tez, Hive, Spark
			+ Distributed systems experience, using tools such as Hadoop, EMR, Spark, ElasticSearch, MongoDB, AeroSpike, Kafka
		* Hive
			+ Proficiency in Hive internals (including HCatalog), SQOOP, Pig, Oozie and Flume/Kafka.
		* Pig
		* Spark
			+ MLlib or Mahout
		* Experience with Big Data and infrastructure technologies including: Kafka, AWS, Streamsets, Docker, Spark.
		* Real-time data pipelines and streaming applications
			+ Kafka
			+ NiFi
			+ Flink
			+ Beam
			+ Storm
			+ Spark-Streaming
		* Pig, Hive, Oozie and Impala
		* YARN, Tez
		* ZooKeeper
		* SQS
		* Mesos
		* Marathon
		* Ceph
		* Operational experience working with Memcache or Redis style caching cluster
		* Experience working with NoSQL solutions such as Cassandra, Redis is a big plus
		* big data pipelines (Hadoop, Spark, Kafka, Flume, Arrow, Avro, RabbitMQ, Flink, etc.)
		* familiarity with ELK stack (Elasticsearch, Logstash, Kibana)
			+ logs management (ELK stack)
		* data science technology stack (Spark, Hadoop, Docker, AWS etc.).
		* Hands-on experience with machine learning concepts: regression and classification, clustering, feature selection, feature engineering, curse of dimensionality, bias-variance tradeoff, neural networks, SVMs, etc.
		* Spark MLlib, Python (scikit-learn, pandas), and R
	- List of database systems:
		* PostgreSQL
		* MySQL
		* Orcale Database
		* Microsoft SQL Server
		* Azure
		* Amazon Redshift
		* SQLite
		* IBM DB2
		* H2
		* Sybase
		* Exasol
		* Apache Derby
		* MariaDB
		* HyperSQL
		* ClickHouse
		* cassandra
		* Reference: https://www.jetbrains.com/datagrip/
	- References from my *BibTeX* database about this:
		* \cite{Lutz2011}
		* \cite{Sileika2010}
		* \cite{Younker2008}
		* \cite{Sweigart2015}
		* \cite{Beazley2009}
+ Do statistical analysis via *Python*
	- [Statsmodels](https://en.wikipedia.org/wiki/Statsmodels)
+ Learn different data/information visualization tools (to plot graphs...)
 	- *Bokeh*
	- *Plot.ly* (i.e., Plotly and Plotly API)
	- [graph-tool](https://en.wikipedia.org/wiki/Graph-tool)
	- Graphviz
	- [Tulip (software)](https://en.wikipedia.org/wiki/Tulip_(software))
	- [Gephi](https://en.wikipedia.org/wiki/Gephi)
		* https://gephi.org/
	- [matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
	- [D3.js (uses JavaScript)](https://en.wikipedia.org/wiki/D3.js)
	- [Tableau](https://en.wikipedia.org/wiki/Tableau_Software)
	- Qlikview (from Qlik)
	- FusionCharts
	- Highcharts
	- Datawrapper
	- Sisense
	- [yEd](https://en.wikipedia.org/wiki/YEd)
	- [NetworkX](https://en.wikipedia.org/wiki/NetworkX)
	- TDWM, KXEN
	- Zeppelin
	- R-Shiny
	- Python Notebooks (Ipython/Jupyter Notebooks)
	- Sketch
	- Figma
	- Python Seaborn
	- Experience building reports and dashboards in a data visualization tool like Tableau, Birst, or Looker
	- JS D3??? Or, D3.js (see mention above)
	- Additional resources
		* https://en.wikipedia.org/wiki/List_of_information_graphics_software
		* https://en.wikipedia.org/wiki/Category:Python_scientific_libraries
		* https://en.wikipedia.org/wiki/Visual_analytics
		* https://en.wikipedia.org/wiki/Data_visualization
		* https://en.wikipedia.org/wiki/Information_visualization
		* https://en.wikipedia.org/wiki/Software_visualization
		* Exposure to tools data acquisition, transformation & integration tools like Talend, Informatica, etc. & BI tools like Tableau, Pentaho, etc.
+ Using Continuous Integration/Deployment (CI/CD) pipelines and DevOps
	- Concourse
	- Jenkins, TeamCity, TFS, CruiseControl
	- Jenkins, CircleCI, Concourse, Jira, GitHub, Artifactory, code analyzers and security scanners.
	- Bamboo
	- Jenkins
	- Travis
	- Jira/Confluence
	- Jira, VersionOne, TFS, Jenkins, Travis, CircleCI, Veracode, Fortify, Artifactory, Nexus, New Relic, Nagios
	- Zuul, Nodepool, Jenkins Job Builder
	- Jira
	- VSTS, AWS OpsWorks
	- Chef, Puppet, and Ansible
	- Nexus, SonarQube
	- Experience with a source code management/code review system (github, gerrit, etc).
	- Familiarity working with monitoring tools like Icinga, Sensu, Ganglia, Statsd, Graphite, or the TICK stack is a plus.
	- Ant, Maven, Git, SVN, Jenkins, Travis, Puppet, Ansible, Docker
	- DevOps: Docker, SonarQube, Ansible, Gradle, Maven.
	- administrating CI servers (preferable: Jenkins, GitLab CI)
	- creating Continuous Integration environments
	- configuration management tools (Ansible, Puppet, Chef... More than Git, Mercurial, SVN, and CVS)
	- Demonstrable experience with DevOps tools (e.g. Puppet, Cheff, Ansible or Vagrant).
	- Experience with containerization, AWS, PBX, SIP technologies is a plus
	- infrastructure monitoring
	- GitFlow
	- SaltStack
		* https://en.wikipedia.org/wiki/Salt_(software)
		* See [Infrastructure as code (IaC)](https://en.wikipedia.org/wiki/Infrastructure_as_Code)
		* See https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software
	- Bugzilla
	- Terraform, CloudFormation, Spinnaker, Concourse
		* Terraform Salt
	- Load balancing and reverse proxies
		* Nginx
		* Varnish
		* HAProxy
		* Apache
	- test driven development methodology
		* Junit, Mockito, Mocha, Chai
		* HVM testing
		* [Selenium](https://www.seleniumhq.org/)
			+ Selenium is a portable software-testing framework for web applications.
	- Build automation
		* [Gulp](https://gulpjs.com)
			+ https://gulpjs.com/docs/en/getting-started/quick-start
		* Maven
		* Ant
		* Gradle
		* Grunt, Gulp, Brunch, Closure Compiler etc
		* Gerrit, Jenkins, and Maven
		* Rake, Gradle, Webpack, and SBT
		* Anka
		* Dependency management and deployable artifact assembly
			+ Grunt
			+ WebPack
			+ NPM
			+ Yarn
			+ Bower
	- Cross-language development
		* Thrift
	- Experience with API tooling and standards
		* Swagger/OpenAPI, OAuth/JWT)
	- Task runners and bundling tools
		* NPM
		* yeoman
		* gulp
		* browserify
		* webpack
	- Monitoring/Alerting tools, and System management and monitoring technologies
		* Data Dog (or DataDog)
		* Nagios
		* Graphite
		* APM tools
		* New Relic
		* Icinga
		* AppDynamics
		* Prometheus
		* Experience using system monitoring tools (e.g. New Relic) and automated testing frameworks
		* Experience with monitoring frameworks such as Stackdriver.
	- ETL technologies
		* Flume
		* Avro
		* Experience with modern DevOps tooling for cloud provisioning (jcloud, fog, libcloud etc) and automation tooling like Docker, Chef, Puppet, CloudFormation or Salt.
	- front-end build pipeline tooling:
		* NPM
		* Bower
		* Grunt
		* Gulp
		* SASS
	- API design/development
		* RPC
		* REST
		* JSON
		* XML
		* SOAP
	- Proficiency with design software
		* Sketch
		* Framer
		* Invision
		* Adobe CC:XD
		* Or, other wireframing/prototyping design software
	- rapid prototyping tools (for UI/UX design):
		* InVision
	- serial data communication systems
		* CAN, FlexRay, MOST, and Ethernet
	- enterprise architecture
		* TEAF
		* FEAF
		* TOGAF
		* Zachman
		* Also, includes the following:
			+ [Project Portfolio Management (PPM)](https://en.wikipedia.org/wiki/Project_portfolio_management)
			+ https://en.wikipedia.org/wiki/Comparison_of_project_management_software
			+ JAXRS; JAXB; AMQP JMS; LDAP and SNMP.
	- Java/J2EE Experience
		* MySQL, Hibernate, JMS, Spring framework (Core, MVC, Integration)
		* JAXRS; JAXB; AMQP JMS; LDAP and SNMP.
		* Java developers:
			+ Java IDE
			+ Git client
			+ XML editor
			+ Mylyn
			+ Maven
			+ Gradle (integration)
		* Java EE developers:
			+ Enterprise Java and Web applications
			+ Java IDE
			+ JPA
			+ JSF
			+ Mylyn
			+ Maven
			+ Git
		* For JavaScript and Web developers
			+ JavaScript, HTML, CSS, XML languages support, Git client, Mylyn
		* For PHP developers
			+ PHP language support, Git client, Mylyn,
			+ editor with syntax highlighting for JavaScript, HTML, CSS, and XML
		* Eclipse committers
			+ Eclipse platform, package addition for PDE, Git, Marketplace Client, source code ...
		* Eclipse for Rich Client Platform/Applications (RCP) and Remote Application Platform (RCP + RAP)
			+ Eclipse plug-ins plus Maven and Gradle tooling and XML editor.
		* Eclipse for Scout Developers
			+ For Java/HTML5 framework, develop business applications to run on desktop, on tablets, and mobile devices.
	- data science skill sets:
		* skill set:
			+ Primary focus for the role is to transform development processes for existing applications software development into a Continuous Delivery-driven SDLC, influencing and educating development and QA teams to adjust working practices in alignment with modern day software development and delivery approaches (CI, CD, AWS). As a part of a DevOps team, the role is responsible for designing, implementing and maintaining automation processes needed to build and deploy software components in AWS cloud.
			+ Software delivery automation (CD, CI)
			+ Promotion and evangelization of DevOps best practices (CI, CD, automated testing, branching strategy, decoupling, etc…)
			+ Simplification and improvement of software delivery/release processes
			+ Support existing development processes
			+ Support cloud-based solutions by building and managing infrastructures in AWS
			+ Participate in services and software systems design
			+ Monitor and fix issues identified or reported
			+ Minor development for internal services and automation needs
			+ Plan, coordinate and implement changes to maintained software configurations and installations
			+ Interactions with development teams for task scheduling, clarification and implementation
			+ Participation in deployment processes (development and testing)
			+ Editing and maintenance of documentation for software architectures and automation processes
			+ Be part of the L2 production support team supporting applications and third party tools which will include legacy application environments
			+ BSc/MSc degree in the field of computer science is preferred, otherwise equivalent experience is expected
			+ A minimum of 5 years of work experience as a Systems Administrator/DevOps supporting development teams
			+ Excellent understanding of SDLC, patching, releases and software development at scale
			+ Good understanding of enterprise standards and enterprise building principles
			+ In-depth knowledge in Linux OS
			+ Theoretical and practical skills in Web-environments based on Java technologies, e.g. Tomcat, Jetty, Jboss
			+ Strong scripting skills in one or any combination of bash, python, perl, ruby
			+ Good understanding of the mechanisms of Web-environment architectures approaches
			+ Strong knowledge of cloud providers offering, AWS in particular
			+ Good knowledge of a configuration management tool like Ansible, Packer.
			+ Good knowledge of cloud infrastructure orchestration tools like CloudFormation or Terraform.
			+ Basic knowledge on software delivery orchestration tools like Spinnaker, GoCD, Jenkins Pipelines, Nolio, IBM UberCode.
			+ Strong practical knowledge of CI Tools, e.g. Jenkins
			+ Excellent knowledge of Continuous Integration and Delivery approaches
			+ Good understanding of enterprise search technologies, such as Elastic Search, Lucene, Solr is a plus
+ machine learning and data Visual_analytics
	- graphx
	- [mllib](https://spark.apache.org/mllib/)
	- hadoop
	- spark
	- tensorflow
	- Aster
	- Resources
		* Caffe, Torch, Theano, TensorFlow, CNTK
		* Caffe, Tensorflow, MxNet, Torch, PyTorch, Theano, Chainer, DyNet
		* Caffe2, TensorFlow, MPI, Gloo, NCCL2, Horovod
		* BigDL, Caffe, Caffe2, Chainer, Keras, Paddle.
		* Expertise in deep learning (CNN,RNN,DBN,DBM,LSTM),
		* pytorch, scikit-learn, tensorflow, pandas, jupyter, spacy, gensim, vowpal wabbit, crfsuite, scrapy, spark, AWS, docker, kafka
		* https://www.quora.com/What-are-the-best-machine-learning-libraries https://medium.com/activewizards-machine-learning-company/top-20-python-libraries-for-data-science-in-2018-2ae7d1db8049
		* Before Tensorflow, Caffe or PyTorch came to be, Theano was the most widely used library for deep learning.
		* Lasagne is a high-level deep learning library that runs on top of Theano.
		* Experience with cloud storage technologies (e.g. CloudSQL, Spanner, Bigtable, Aurora)
		* [MLJAR](https://mljar.com/)
		* https://github.com/josephmisiti/awesome-machine-learning
		* https://github.com/josephmisiti/awesome-machine-learning/blob/master/books.md
		* https://github.com/josephmisiti/awesome-machine-learning/blob/master/courses.md
		* https://github.com/josephmisiti/awesome-machine-learning/blob/master/blogs.md
		* https://www.kdnuggets.com/2018/04/top-16-open-source-deep-learning-libraries.html
		* mxnet, pytorch, tensorflow, Keras, sklearn, statsmodels
+ Log processing
	- Elastic
	- Logstash
	- Splunk
+ Cloud platforms
	- AWS/EC2
	- AWS (EC2, EMR, RDS, Redshift), Google Cloud, Microsoft Azure, Oracle Cloud (https://cloud.oracle.com/trial)
	- Experience with an Automation framework (Chef, Puppet Ansible, CloudFormation)
	- Celery, Redis, Docker, Kubernetes, Jenkins
	- Rackspace Open Cloud
	- Ceph
	- Consul
	- Container Orchestration
	- Container technologies
		* Docker
		* Rocket
		* Linkerd, Kubernetes, DC/OS, gRPC, Zipkin, Docker, and Prometheus.
		* Docker, Kubernetes, Helm, Jenkins, AWS, Prometheus, Grafana
		* Docker, LXC
		* VMware ESXi or Windows Development/Windows containers.
	- Virtualization
		* VMware
		* OpenStack
	- Data-driven:
		* Google Analytics, Google Optimize, HotJar, Metabase, Airflow, ELK
	- Others:
		* EC2, EMR, Kinesis and Redshift
		* Docker, Kubernetes, ceph
		* Experience with cloud storage technologies (e.g. CloudSQL, Spanner, Bigtable, Aurora)
		* cloud orchestration (Terraform, CloudFormation)
		* dynamic routing protocols
+ Cloud automation tools
	- Ansible
	- Chef
+ cryptographic hardware
	- TPM
	- HSM
+ Security vulnerability identification and remediation
	- OWASP
+ software-defined networking, SDN (i.e. OpenContrail)
+ **text editors and intergrated development environments (IDEs)**:
	- EmEditor
		* https://www.emeditor.com/#download
		* https://en.wikipedia.org/wiki/EmEditor
		* Can handle files up to 240 GB, but only runs on *Windows*.
	- Cloud-based text editors and IDEs
		* https://www.editpad.org/
		* https://www.mytextarea.com/
		* cloud9:http://c9.io/
		* Codenvy:https://codenvy.io/
		* Koding:http://koding.com/
		* http://www.ideone.com/
		* Codiva:https://www.codiva.io/
		* https://codepanel.io/?rc=crCNA%3D%3D+
		* [ShiftEdit](https://shiftedit.net/about)
		* Nitrous Inc., SourceLair,
		* [SloopEngine](https://sloopengine.io/)
		* [codeanywhere](https://codeanywhere.com/)
		* Eclipse Che
		* Repl.it
		* Tutorialspoint: Tutorialspoint.com
		* [Pythonanywhere.com, from PythonAnywhere LLP](https://www.pythonanywhere.com/)
		* Ideone
		* Hackerearth
		* Jdoodle
		* Ultimate++
	- For *LaTeX*:
		* TeXstudio
		* Texmaker
	- For C and C++:
		* With Mylyn integration
	- Eclipse DSL tools
		* Java and DSL developers: Java Xtrend IDE, DSL Framework (Xtext), Git client, XML editor, and Maven
	- Eclipse Modeling Tools
		* Has tools and runtimes for building model-based applications
		* For graphically design domain-specific models
	- Eclipse for Testers
		* Software development quality assurance process, such as Jubula and Mylyn
	- Eclipse for Parallel Application Developers
		* Tools for C, C++, Fortran, and UPC including MPI, OpenMP, OpenACC, a parallel debugger, and remotely building, running, and monitoring applications.
	- Eclipse IDE for Rust developers
		* Rust language support, Git client, command-line integration, Mylyn, and editors.
	- Data Science:
		* [Rodeo](https://rodeo.yhat.com/)
	- Failed attempts:
		- wisdom.ai. This has a limit of 5000 BibTeX entries.
		- CiteULike. This has a limit of 5000 BibTeX entries.
		- JabRef works, but it is hard to reuse keywords.
		- BibDesk crashes, if not hangs (is not responsive), for large BibTeX databases.
		- [RText](https://github.com/bobbylight/RText): Cannot build and install the software.
+ Other technology stacks:
	- Go, Docker, Kafka, Elasticsearch
	- Go, Ruby, Javascript, HTML, CSS, Ember.js, C/C++, MySQL, Libvirt, KVM, QEMU, OpenVSwitch, Chef, Ansible, Zookeeper, Kafka, Redis
	- Go, Consul, Kafka, SQL, Chef, Git, Jira, Sentry, Prometheus, Lightstep, Docker, Kubernetes
	- Kubernetes, Go, GRPC, MySQL, Prometheus, Kafka
	- Pytest/nose, Selenium, Jupyter, Jenkins, SQL.
	- AWS, Azure, Google cloud
	- Docker/Kubernetes, Apache Spark, Jupyter, and Hadoop
	- Docker, Kubernetes, Ansible, Terraform
	- Icinga2, ELK and Prometheus
	- Node.js, python, docker, Redis, postgress, ELK, prometheus
	- microservice architecture using Docker, Node.js, Python, Redis, Postgres and ELK stack in the backend with Angular & Electron in the frontend
	- Docker, cluster schedulers (Mesos/Kubernetes/Swarm)
	- ELK, Queuing and monitoring infra
	- security, AWS, Chef, Git, Jira, Docker, Jenkins, TDD, and Continuous Integration CI/CD.
	- Knowledge of BigQuery and GraphQL
	- Experience using system monitoring tools (e.g. New Relic) and automated testing frameworks
	- In-depth knowledge of relational databases (e.g. PostgreSQL, MySQL) and/or open source search engines (e.g. Elastic Search)
	- Experience with queuing platforms like ActiveMQ, Google Pub/Sub, Kafka
	- Gerkin, BDD.
	- Experience with distributed computing platforms (e.g. Spark)
	- Familiarity with Agile project management tools and practices such as Jira, Confluence, Trello.
	- Familiarity with modern data engineering ecosystem and relevant practices: Elastic Search, Graph databases, ETL/ELT, etc.
	- Familiarity with React/Redux frameworks is a plus.
	- Prototyping abilities with InVision / Axure / Flinto
	- Knowledgeable with industry standard authentication protocols such SAML SSO and OAuth2
	- Core Technical Skills that are REQUIRED: PHP 5, Javascript, JQuery, Node.js, MySQL (administration and database design/creation), Full-stack familiarity (HTML/CSS, Apache web server, Ubuntu Linux), Encoding and Decoding JSON to and from OOP, ORM, Consuming RESTful APIs, Experience with Eclipse IDE (desirable)
	- Experience with Statistical Process Control design including Six Sigma tools and processes.
	- Experience with Products Development Life Cycle (Systems, Software)
	- Experience in Software Quality and process (e.g., SPICE, CMMI)
	- Knowledge of Requirements Management tools (e.g., JAMA)
	- Experience with requirements derivation and tracking tools (DOORS, Jama, etc.)
	- Experience with design of experiment (DOE/DOX), critical analysis, and characterization.
	- Experience in a high-volume manufacturing environment.
	- Experience with optical design software such as Zemax, Code V or comparable
	- Ensure high level of data integrity with our ATS (Lever) and other HR systems
	- Experience in Java and Apex is an advantage
	- Experience with Zend Framework or Laravel (optional)
+ [x] Run automated regression testing, and/or regression verification, to put
		the experimental results of each build in the correct directory.
		And, commit and push that build to the cloud-based research repository.
+ Create scripts for performance measurement and analysis.
	- *Python*
	- *GNU Octave*
	- *Scala*/*Chisel*
	- *SPICE*???
	- [Nim](https://nim-lang.org/features.html)
	- ???
+ Develop *R* scripts for statistical analysis of experimental results.
+ Get references for QUBO and QUBO solvers.
	If there are no classical QUBO solvers, develop one using GLPK
		and meta-heuristics.
+ Run experiments on classical QUBO solvers.
	- Benchmark them.
+ Benchmark "Qbsolv" \cite{mwbooth2017} against classical QUBO solvers.
+ [Write the USRA research proposal for quantum computing time.](http://www.usra.edu/quantum/rfp/)
	- Get references for:
		* Pseudo-boolean optimization (PBO)
		* Weighted-Boolean Optimization (WBO)
		* Maximum satisfiability (Max-SAT), and maximum SMT (Max-SMT)
+ Get references for "adversarial machine learning."
+ Replicate experiments for adversarial machine learning.
	- Use others' software and libraries to reproduce their
		experimental results.
	- Implement my own machine learninhg software for adversarial
		machine learning.
	- Implement my adversarial machine learning software solution as
		hardware (VLSI system).
+ Implement my solution for adversarial machine learning using NBL.
































#	References

##	Quadratic Unconstrained Boolean Optimization (QUBO)


Journal and conference papers:
+ \cite{Boros2007}
+ \cite{Hanafi2013}
+ \cite{Rieffel2000}???


Books:
+ \cite{Anjos2012}
+ \cite{Wittek2014}
+ \cite{Crama2011}
+ \cite{Crama2010}
+ \cite{Rieffel2011}
+ \cite{Padberg1999}
+ \cite{Tandon2017}
+ \cite{Aaronson2013}
+ \cite{McGeoch2014}
+ \cite{Lanzagorta2008}
+ \cite{Miszczak2012}
+ \cite{Meglicki2008}
+ \cite{Resende2016}
+ \cite{Wang2016}
+ \cite{Ibaraki2005}
+ \cite{Koch2016}
+ \cite{Hoos2005}
+ \cite{Pardalos2007}
+ \cite{Adamatzky2017}
+ \cite{Florescu2016}
+ \cite{Vidick2016}
+ \cite{Kreher1999}


Not stored in my BibTeX database; append "https://dx.doi.org/" to DOI:
+ https://dx.doi.org/10.1002/net.21751
+ https://dx.doi.org/10.1109/IJCNN.2017.7966350


**Add more references!!!**

### QUBO + Pseudo-Boolean Optimization (PBO)

+ Anthony2017.pdf
+ Babbush2014.pdf
+ Gruber2015-copy.pdf
+ Gruber2015.pdf
+ HammerIvanescu1968.pdf


**Add more references!!!**


##	Pseudo-Boolean Optimization (PBO)

+ Andres2015.pdf
+ Lampert2017.pdf


**Add more references!!!**



##	Graph Coloring


##	Map Coloring






##	Image Recognition: Pattern Recognition + Machine Learning

###	Trustworthy Computing

###	Computer Security

Trustworthy computing

Design for Security









#	Operazione Andare a HPCA

+ Find the cross-correlation of RTW waves.
+ Find the covariance of RTW waves.
+ Determine the "time"-average of each RTW wave.
	- Report the mean. Determine if it is not zero.
+ Perform the hat-drawing experiment for time-shifted INBL

+ Keep learning *Scala*.
	- Implement tools for noise-based logic via object-oriented
		functional programming.
+ Learn *R*.
	- Apply *R*-based data analytics to my software development and
		hardware design process.
+ Learn [*Chisel* (Constructing Hardware in a Scala Embedded Language)](https://chisel.eecs.berkeley.edu).
+ Design cyber-physical systems using *Chisel* and *Scala*.
	- Determine if transaction-level modeling (TLM) can be done with
		*Chisel* and *Scala*.
+ Build benchmarks for running experiments in electronic design
	automation (EDA), and the design automation of cyber-physical
	systems (CPS-DA).
	- Processors based on [*RISC-V ISA*](https://riscv.org).
		* Single-cycle implementation \cite{Patterson2018}
		* Pipelined implementation \cite{Patterson2018}
		* Multi-cycle implementation
			\cite[\S5.5, pp. 318-340]{Patterson2005}
			\cite{Patterson2018}
		* Multi-/many- core implementations
			\cite{Patterson2018}
			\cite{Hennessy2003,Hennessy2007,Hennessy2012}
			\cite{Shen2005a}
	- System-on-Chip (SoC) designs
		* Digital signal processing
		* Image processing
		* Video processing
		* Computer Vision (highly advanced)
		* [Crypto-processors (highly advanced)](https://en.wikipedia.org/wiki/Secure_cryptoprocessor)
	- Processors for computer graphics
		* graphics processors (GPU)
	- Network processors
	- SoC designs for telecommunications
		* Transmitters
		* Receivers
		* Transceivers
		* Encoders
		* Decoders
+ Implement retargetable parallel compiler for the *RISC-V* ISA.
	- Compiler for the *RISC-V* ISA.
	- Retargetable compiler for the *RISC-V* ISA.
	- Retargetable parallel compiler for the *RISC-V* ISA.
+ Implement aforementioned processor and SoC designs using
	noise-based logic
+ Learn *Julia*.
+ Texinfo
	- Learn how to write comments in the *Texinfo* typesetting syntax
		for documentation generation.
	- E.g., see [example](https://searchcode.com/codesearch/view/20327447/).
+ Miscellaneous
	- \S17.5 Utility function
	- \S17.6 Special function
+ Generate RTW signals, using PRNG
	- Demonstrate that these signals have zero cross-correlation,
		since there are statistically independent.
		Do this for each pair of signals, H(t) and L(t)
	- Show the time-correlation for time-shifted signals.
+ Fix boilerplate code
	- Add utilities feature to convert real (or floating-point)
		numbers into strings.
		Test this feature.
+ Always practise "Continuous Integration"
+ Get references on:
	- Semiconductor device physics
	- Solid-state device physics
	- device engineering
	- device modeling
	- compact modeling
	- Big Data
	- data analytics
	- statistical process control
	- process control
	- Response Surface Methodology
	- financial engineering
	- computational finance
	- financial mathematics
	- mathematical finance
	- portfolio optimization
	- algorithmic portfolio optimization
	- meta-algorithms
	- parallel programming
	- concurrent programming
	- distributed computing
	- numerical computation
	- numerical methods
	- computer networks
	- distributed  networks
	- functional programming
	- software architecture
	- design patterns
	- software testing
	- revision control, version control, software configuration management
	- build automation
	- symbolic computation
	- symbolic-numeric computation
	- constraint programming
	- probabilisitic programming/computing
	- stochastic computing
	- approximate computing
	- neuromorphic processors
	- neuromorphic computing
	- cognitive computing
	- noise-based logic
	- microelectromechanical systems + nanoelectromechanical systems
+ Avoid technical debt
	- Minimize routine maintenance.
	- Refactor code and wetware.
	- Update programming skills to latest standards/versions.
+ Try to implement the following in *GNU Octave*:
	- Usage of private and hidden functions again
	- Examples of nested inheritance
	- Examples of multiple inheritance.
+ \S15 Plotting
+ \S14 Input/Output (I/O) operations
	(or I/O operazioni)
+ **Things to mull about**
	- python llvm
	- compiling for object-functional programming
		* https://www.reddit.com/r/ProgrammingLanguages/comments/8ggx2n/is_llvm_a_good_backend_for_functional_languages/
			+ I want to start on a small toy language which borrows a lot from Elm ( purely function, strong typing) but is compiled. I was wondering if I should use LLVM as the backend for it? I read that functional language compilers are based on CPS instead of SSA. AFAIk, LLVM doesnt have CPS support. Should I go with LLVM? Or are there other options which fit my use case? For me the ease of use and getting started are the most important bits. See https://www.reddit.com/r/ProgrammingLanguages/comments/8ggx2n/is_llvm_a_good_backend_for_functional_languages/.
			+ The Implementation of Functional Programming Languages by Simon Peyton-Jones (1987). This is about Miranda-like languages (Haskell is the modern language, though Haskell didn’t exist yet), and covers all of the interesting things that make compiling for these languages different. Several abstract machines are covered: lambda calculus, SK combinators, and the G machine. This book is available for free online. Once you’ve read this book, you can read about how things are done today.
				- http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.3729
				- https://www.microsoft.com/en-us/research/publication/the-implementation-of-functional-programming-languages/
				- Warren’s Abstract Machine: A Tutorial Reconstruction, by Hassan Aït-Kaci. This is about Prolog specifically, but logic languages have many of the same issues as functional languages.
				- http://wambook.sourceforge.net/
				- http://hassan-ait-kaci.net/
			+ Let’s go through some of the keynote differences between the 2 paradigms and how they are compiled:
				- recursion - it is compiled the same, HOWEVER the run-time code might act differently, as most FP languages implement tail recursion, which means state between calls won’t be held onto the stack, except for the last one. In most imperative programming languages, the calls keep adding up until they can eventually blow up - this too can happen in FP languages, as a function has to be “in tail position”
				- expressions (if, while, for, etc) - no difference (except maybe for the part when it will throw an error if an expression is not complete - ie if without the else part, else all is good)
				- immutability - no difference
				- higher order functions (map, filter, reduce) - this is where things are completely different. The compiler has to, first, create the lambda function, and then use that instead. However, as most programming languages nowadays also support hof, I wouldn’t say it’s a big deal. A heap is still necessary as, after all, FP languages still work upon objects, the difference being HOW they do so. Big differences exist only HOW you program, not how it is interpreted/compiled.
			+ Functional Programming: Application and Implementation by Peter Henderson (1980). This covers a Lisp-like language (Lispkit) based on the SECD machine.http://skelet.ludost.net/sec/
			+ There's really not a lot of difference in how most parts of functional and object-oriented languages are compiled, and a heap with garbage collection is central to both.
			+ The main difference is that compilers for functional languages focus on optimizing function calls while compilers for object-oriented languages focus on optimizing method calls. In particular, functional language compilers typically:
				- Do tail-call optimization.
				- Try to avoid building closures or thunks if this can be avoided (for example by specializing calls to map and fold, or in lazy languages by strictness analysis)
			+ Additionally, many functional language compilers also
				- Optimize pattern matching to avoid repeated tests.
				- Symbolically compose functions.
				- Exploit that functions are pure to enable other optimizations.
			+ In contrast, object-oriented language compilers typically:
				- Try to avoid virtual calls, for example by exploiting that a class or method is final (even when not declared as such).
				- Omit self pointers when they are not needed.
				- Analyze when null-pointer checks are not needed.
		* The latter is strictly speaking not specific to object-oriented languages, but most functional languages do not have null pointers, while most object-oriented languages implicitly allow any object variable to be a null pointer.
		* https://www.semanticscholar.org/paper/TIL%3A-A-Type-Directed-Optimizing-Compiler-for-ML-Tarditi-Morrisett/03e7b7bdb9377f521b84e97c6d9e051d1a6f42eb
	- Opportunities associated with programming languages.
		* The Eighth International Workshop on Static Analysis for Systems Biology
			+ equivalences and equivalence checking techniques,
			+ constraint-based and stoichiometric analysis,
			+ static analysis in verification of molecular devices design,
		* https://en.wikipedia.org/wiki/Java_memory_model
		* https://www.cs.cmu.edu/~jyang2/people.html
			+ http://www.cs.cmu.edu/Groups/pop/
			+ Our group mission is to take over the entire world with sound reasoning and provable guarantees. 🌈
			+ https://www.cs.cmu.edu/~jyang2/research.html
			+ Exploiting Structure to Analyze Rule-Based Biological Models
				- Understanding the mechanisms behind cellular signalling would help us understand and cure many diseases, but the complexity of cellular signalling precludes understanding. We are interested in developing language constructs and programming tools for modeling cellular signalling as programs. Our work on executable knowledge exploits a deep connection between programming language semantics and semantics to support a new way of modeling. We use Kappa, a rule-based graph-rewrite programming language that allows us to encode possible transformations over graphs representing the state of the cell. Kappa's precise operational semantics allow us to not only simulate the programs, but also perform static program analysis. We are currently working as part of the Big Mechanism project to mine models from the literature. Below are some project directions.
				- Formal methods techniques and tools for exploring a space of possible models.
				- Tools for analyzing causal relationships between rules.
				- Statistical analyses for answering questions about rules and rates.
				- Applications of rule-based modeling and causal analysis in traditional Computer Science domains.
			+ Policy-agnostic programming for security and privacy. As an alternative to approaches for detecting information leaks, my collaborators and I propose a new programming model that factors out the specification of security and privacy concerns from the rest of the program and enforces the properties by construction. In our work on Jeeves we designed a language semantics for policy-agnostic programming with informaton flow policies and developed dynamic and static enforcement techniques. We are currently interested in (1) extending the approach for statistical privacy and (2) techniques for retrofitting legacy code with the policy-agnostic model, for purposes of fixing bugs and interacting with new policies and code.
			+ Rule-based programming for biological modeling. Traditionally, researchers model intracellular signalling using systems of ordinary differential equations (ODEs), but there are two problems with ODE models. First, a precise model requires a different ODE for each interaction between agents, causing ODE models to scale poorly with respect to number of agent types. Second, ODE models have little structure that we can exploit for scale-mitigating analyses. As an alternative, rule-based languages allow the representation of models as programs describing rewrites over graphs, where nodes correspond to proteins and edges describe protein complexes. Not only are these programs more concise than the corresponding ODE systems, but their structure also supports various analyses that are otherwise not possible. Our current work focuses on analyzing causal relationships between rules, and combining causal information with language design and model-checking techniques to create biologically relevant model analyses.
			+ Factoring Privacy and Security Out of Programs
				-Information leaks often occur because conditional access checks are intertwined with other functionality. We want to make software more secure by reducing opportunities for programmers to inadvertently leak information. Our prior work on the Jeeves programming language introduced the idea of policy-agnostic programming: separating privacy and security policies from the rest of the code while relying on the compiler/compile to implement policy checks. Jeeves enforces policies at runtime. Follow-up work on Lifty uses a static program repair-based approach for inserting the necessary conditional checks at compile-time, where the programmer specifies policies as refinement types. We are interested in, among other things, the following extensions of this work:
				- Supporting policy-agnostic programming for legacy code.
				- Policy-agnostic programming for statistical privacy.
				- Extending these ideas to other domains, for instance resource usage.
				- Conducting realistic case studies, for instance on health record systems.
		* [How are algorithms, data structures, and architectures of compilers different between functional programming languages and object-oriented programming languages?](https://www.quora.com/anonymous/e4bb73303fdc413caa161b7a1e7d5460)
		* https://en.cppreference.com/w/cpp/language/history
			+ New language features: variable templates, polymorphic lambdas, lambda captures expressions, new/delete elision, relaxed restrictions on constexpr functions, binary literals, digit separators, return type deduction for functions, aggregate initialization for classes with brace-or-equal initializers.
			+ New library features: std::make_unique, std::shared_timed_mutex and std::shared_lock, std::integer_sequence, std::exchange, std::quoted, and many small improvements to existing library facilities, such as two-range overloads for some algorithms, type alias versions of type traits, user-defined string, duration, and complex number literals, etc.
				- Generic Lambdas - lambda expression can infer auto type parameters.
				- Relaxed constexpr functions - now can contain conditionals, loops etc.
				- Type inference for all functions, not only for lambdas.
				- Template variables similar to template functions and classes.
		* Not just lambdas!  Scala also has pattern matching, algebraic data types via case classes, type classes via implicits, tail-call optimisation, and immutability by default.  It also has far richer and more useable type inference.
	- quantum computing
		* [The only QC implementation that is not ultra-sensitive to EM (and often also thermal) noise are linear-optical quantum computers, simply because photons at low energies don’t interact with other photons (which electrical and magnetic fields are made of). They are sensitive to other things (such as mechanical vibrations).](https://www.quora.com/Are-quantum-computers-extra-susceptible-to-noise/answer/Vladislav-Zorov)
	- software engineering practices
		* [The Law of Demeter (LoD) or principle of least knowledge is a design guideline for developing software, particularly object-oriented programs. In its general form, the LoD is a specific case of loose coupling.](https://en.wikipedia.org/wiki/Law_of_Demeter)
		* https://en.wikipedia.org/wiki/Principle_of_least_astonishment
		* https://cacm.acm.org/magazines/2017/10/221326-a-large-scale-study-of-programming-languages-and-code-quality-in-github/fulltext
		* In a certain perspective all good things in programming come from laziness. The problem with Python is that it makes hard things easy to code and it’s a lie. Some programming languages are more honest: we have all this effects, lets express this in the type system. How do we compose them, maybe we find a good abstraction? Monads, perfect! Recursion, inductive types - initial algebras, Lambek lemma. Continuations - Yoneda lemma. But wait, coeffects, corecursion and so on.




















#	Names for Technologies and Research Papers


#	From Gen Z Lingo/Slang

+ bae
+ Boujee
+ come thru, pull up
+ Dank
+ fam
+ finesse
+ finna
+ finsta
+ flex
+ Gucci
+ hardo
+ highkey, high key
+ hip
+ hype
+ jams
+ jawn
+ lit
+ lowkey, low key
+ nunya
+ okurrr
+ oomf
+ OOF
+ opp
+ salty
+ self-drag
+ sick
+ sis
+ skrt skrt
+ skrr skrr
+ smol
+ snack/snacc
+ snaps
+ stan
+ steez
+ suh
+ swole
+ tea
+ wig
+ woke
+ Woot
+ YEET!, yeet
+ yikes


##	References

+ https://drive.google.com/file/d/1yrJmMHPkZzrxfWbUb4jALN0neE1tbkgH/view



#	Relevant *GNU Octave* Content

From the *GNU Octave* manual \cite{Eaton2016a}:
+ \S2.4 Command line editing
	- \S2.4.6 Customizing *readline()*
+ \S8.5 Boolean expressions
+ \S9.2 Evaluation in a different context
+ \S16 Matrix multiplication
+ \S17.7 Approximations: Rational approximations
+ \S17.8 Coordinate transformation
	- E.g., from polar coordinate system to cartesian coordinate system???
+ \S17.9 Mathematical constants
+ \S18 Linear algebra
+ \S27 Set operations
+ \S36 System utilities
+ \S38 Package installation, removal, usage, and creation
+ *Appendix B* Test and Demo functions
+ *Appendices C and D* Software development guidelines



#	Side Projects

+ Learn *R*.
+ Learn *Scala*.
+ Transfer objects between programs implemented in the following
	computer languages:
	- *GNU Octave*
	- *R*
	- *Scala*
	- *Python*
	- *C++*
+ Add experimental results and other information into databases,
	using database management systems (DBMS).
	- *SQL* databases; e.g., *MySQL*.
	- [*NoSQL* databases](https://en.wikipedia.org/wiki/NoSQL). Also,
		see [Comparison of structured storage software](https://en.wikipedia.org/wiki/Comparison_of_structured_storage_software).
	- [*NewSQL* databases](https://en.wikipedia.org/wiki/NewSQL)
	- Avoid using database administrator tools to manage such
		databases.
+ Design EDA benchmarks
	- processors
	- VLSI systems
	- AMS/RF ICs
	- mixed-signal SoC
	- In HDLs, such as Chisel and SystemC/SystemC-AMS

#	Scripts to Hack

+ Script to check if a list of names is unique
	- Flag similar names, and prompt use to verify their equivalence.
	- E.g., Ann Kripa George, Ann K. George, and Ann George are
		equivalent.
+ Script to change/remove file extensions.
	- Add (-a)
	- Delete (-d)
	- Modify = delete + add (-m)


#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).


@techreport{Dahl2013,
	Address = {Burnaby, British Columbia, Canada},
	Author = {E. D. Dahl},
	Date-Added = {2014-03-30 00:11:00 +0200},
	Date-Modified = {2014-03-30 00:11:00 +0200},
	Doi = {},
	Howpublished = {Available online at: \url{https://www.dwavesys.com/sites/default/files/Map%20Coloring%20WP2.pdf}; August 31, 2017 was the last accessed date},
	Institution = {{D-Wave Systems Inc.}},
	Keywords = {map coloring, quantum computation, quantum computing, NP-complete problems},
	Month = {November},
	Number = {},
	Title = {Programming with {D-Wave}: Map Coloring Problem},
	Url = {https://www.dwavesys.com/sites/default/files/Map%20Coloring%20WP2.pdf},
	Year = {2013}}


+ \cite{Chapellier2018}
	- Referred to information about checkboxes (or tickboxes).
	- Be wary of succumbing to a "culture of performativity" or tick-box culture




#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

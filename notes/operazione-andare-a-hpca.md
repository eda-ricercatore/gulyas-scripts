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



##	Sets of skills

+ skill set:
	- Understand data landscape i.e tooling, tech stack, source systems etc. and work closely with the data Engineering team to improve the data collection and quality.
	- Ability to define and spot macro and micro levels trends with statistical significance on a regular basis and understand key drivers driving those trends.
	- 8+ years of data analyst experience with 4+ years of proven industry experience in a large scale environment(PBs scale, globally distributed teams).
	- Strong experience in Python, R, SQL, Tableau, Google Analytics, Hive and BigQuery (or any other Big data/Cloud equivalent) etc.
+ skill set:
	- Build and Support scalable and reliable data solutions that can enable self-service reporting and advanced analytics at Cloudflare using modern data lake and EDW technologies (Hadoop, Spark, Cloud, NoSQL etc.) in a agile manner.
	- 3+ years of development experience in Big data space working with Petabytes of data and building large scale data solutions.
	- Solid understanding of Google Cloud Platform, Hadoop, Python, Spark, Hive, and Kafka.
	- Experience in all aspects of data systems(both Big data and traditional) including data schema design, ETL, aggregation strategy, and performance optimization.
	- Capable of working closely with business and product teams to ensure data solutions are aligned with business initiatives and are of high quality.
+ skill set:
	- Partner and align with business leaders, stakeholders, product managers and internal teams to understand the business and product challenges and goals and address them using predictive analytics in a globally distributed environment.
	- Understand data landscape i.e tooling, tech stack, source systems etc. and work closely with the data Engineering team to improve the data collection and quality.
	- Understand business/product strategy and high-level roadmap and align analysis efforts to enable them with data insights and help achieve their strategic goals.
	- Strong audience focused presentation and storytelling skills focused on key takeaways in a crisp and concise manner.
	- Define hypothesis driven models and best practices to derive and publish model scores/insights/learnings at scale within the company.
	- Ability to define and spot macro and micro levels trends with statistical significance on a regular basis and understand key drivers driving those trends.
	- 8+ years of data scientist experience with 4+ years of proven industry experience in a large scale environment(PBs scale, globally distributed teams).
	- Proven lead in driving multi-million dollar revenue generator models for the company and setting up data science related best practices at a company.
	- 2+ years experience with a fast-growing SaaS business based company is preferred.
	- Strong experience in Python, R, Spark, SQL, Tableau, Google Analytics, Hive and BigQuery (or any other Big data/Cloud equivalent) etc.
+ skill set:
	- Solid foundation in computer science, with strong competencies in algorithms, data structures, software design, web security, and building large, distributed systems
	- Excel at planning, working multi-functionally, leading execution across teams to meet commitments and deliver with predictability
	- Demonstrate a track record of leading teams, including hiring, onboarding, and professional development. You inspire your team to reach higher. You’re as good as explaining “why” as you are “how”
	- Experience implementing tools, process, internal instrumentation, methodologies and resolving blockages
	- Demonstrated ability to recruit and hire top talent
	- Comfortable managing teams/projects with tight deadlines and short release cycles
	- Experience working with and getting the best out of post-doctorate researchers
	- Being passionate about cryptography and/or web technology such as TLS
	- Familiarity working with DNS, database systems, Internet performance, and/or Internet security
+ skill set:
	- You will help build customer facing apps and our core platform to create, improve, and scale agricultural models. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us!
	- Graduate degree in a technical field and 5+ years experience as a Data Scientist working on commercial software products
	- Experience engineering production-level software systems evidenced by having built a parallel/distributed system, using software best practices, performance optimizations, or an automated pipeline to interpret other data science experiments
	- Experience applying the scientific method to complex, multivariate unstructured problems to produce rigorously-defendable conclusion in prose and graphics
	- Experience across and significant work in at least one of clustering and classification, multivariate regression, prediction, and forecasting; and dimensionality reduction and feature engineering
	- Experience or interest in Bayesian methods of crafting generative probabilistic models; engineering informative priors and solution via MCMC
	- Experience collecting, curating, structuring and retrieving large data sets in relational databases.
	- Additional experience with NoSQL preferred
	- Experience with either time-series or spatial statistics, especially Gaussian Processes
	- Experience creating complex data visualizations for multivariate data
	- Experience with AWS or other programmatic distributed computing environments
	- Experience with Bayesian non-parametrics (CRP, IBP, etc.)
	- Experience with advanced MCMC techniques such as DREAM, Hamiltonian-MC, variational approximations, etc.
	- Experience or keen interest in FP (Scala, Haskell, Clojure, Erlang, OCaML/SML, Elm, F\#)
+ skill set: Use Python, React/Redux, Spark, Presto, Airflow, Git, CircleCI, and more.
+ Experience with data analytics platforms, such as Semantic Pro, Semantic Cortex, IBM i2
+ Experience in working with large data sets and distributed computing tools (Hive, Redshift) is a plus
+ Experience using vector editors like Figma or Sketch and prototyping tools like Principle or Framer
+ You are an expert in AfterEffects, Cinema 4D, Sketch, Principle
+ You will be expected to have a good understanding of a broad range of traditional supervised and unsupervised techniques (e.g. logistic regression, SVMs, GBDTs, Random Forests, k-means and other clustering techniques, matrix factorization, LDA . . .) as well as be up to date with latest ML advances (e.g. Deep Neural Networks, or non-parametric Bayesian methods).
+ Conduct testing such as functional testing, user acceptance testing (UAT), automated acceptance testing (AAT), and specification by example.
+ skill set:
	- 3+ years of experience in machine learning, data mining, natural language processing, information retrieval, or statistical analysis
	- Experience working with large data sets using open source technologies such as Spark, Hadoop, and NoSQL
	- Experience developing and productizing real-world AI/ML applications such as prediction, personalization, recommendation, content understanding and NLP
	- Experience working with at least 3 of the following popular machine learning frameworks/libraries: sklearn, tensorflow, pytorch, caffe, keras, theano, cntk, mxnet, spark mllib
	- Experience developing and deploying deep learning NLP models is a plus
	- Experience working with a knowledge graph is a plus
+ tech stack:
	- Experience with Deep Learning frameworks, e.g., PyTorch, DeepLearning4J, TensorFlow
	- Experience in SPARK (using Python or Scala). Knowledge of AWS services will be appreciated.
+ tech stack:
	- 2+ years of analytical work experience (experience working with product organizations a plus)
	- Strong critical thinking and problem solving skills
	- Experience  communicating effectively with non-technical audiences
	- Strong ability to devise data-driven solutions to business problems
	- Strong competency with SQL
	- Experience with or exposure to a scripting language (Python preferred)
+ tech stack:
	- 5+ years of relevant analytical experience working with data or MS in a relevant technical field and 2+ years of analytical work experience (experience working with product organizations a plus)
	- Strong critical thinking and problem solving skills
	- Comfort and expertise communicating effectively with a wide-range of audiences (including product managers, engineers, business development managers, occasionally executives)
	- Strong ability to devise data-driven solutions to business problems
	- Ability to drive impact by thoughtfully tackling open-ended problems
	- Strong data intuition and deep understanding of and experience with statistical and/or ML modeling techniques
	- Strong competency with SQL
	- Fluency in a scripting language (Python preferred)
	- A plus: Experience with large scale data processing tools (Apache Spark) or implementing systems in production at scale
+ tech stack:
	- Netflix culture resonates with you.
	- You can communicate effectively with experts of all backgrounds.
	- You are an expert analyst and can pick up any tool (e.g. Tableau, D3) to get the job done.
	- You dream in SQL and Python (or other similar languages).
	- You are comfortable with Big Data technologies like Hadoop, Spark, Hive, Presto etc.
+ Expertise in SQL, programming (e.g. Python, Scala), ETL and data warehousing concepts at scale (TBs of data)
+ Expertise in broad technical skills spanning data access, data storage, data processing, and data visualization.  Skills include: SQL, logical / semantic data modeling, ETL and data warehousing concepts, programming languages (Python)
+ Expertise in statistical inference including experimentation and observational methods to causal inference
+ Strong coding experience. Experience with open-source ML packages (specifically sklearn, TensorFlow/Keras/PyTorch).
+ tech stack:
	- 5+ years of research experience with a track record of delivering quality results
	- Expertise in machine learning spanning supervised and unsupervised learning methods
	- Experience in successfully applying machine learning to real-world problems
	- Strong mathematical skills with knowledge of statistical methods
	- Strong software development experience in languages such as Scala, Java, Python, C++ or C#
	- Great interpersonal skills
	- PhD or MS in Computer Science, Statistics, or related field
	- Experience in Recommendation Systems, Personalization, Search, or Computational Advertising
	- Experience using Deep Learning, Bandits, Probabilistic Graphical Models, or Reinforcement Learning in real applications
	- Experience in optimization algorithms and numerical computation
	- Experience with Spark, TensorFlow, or Keras
	- Experience with cloud computing platforms and large web-scale distributed systems
	- Open source contributions
+ tech stack:
	- 5+ years of research experience with a track record of delivering quality results
	- Expertise in machine learning spanning supervised and unsupervised learning methods
	- Experience in contextual multi-armed bandit algorithms and/or reinforcement learning
	- Experience in successfully applying machine learning to real-world problems
	- Strong mathematical skills with knowledge of statistical methods
	- Strong software development experience in languages such as Scala, Java, Python, C++ or C#
	- Great interpersonal skills
	- PhD or MS in Computer Science, Statistics, or related field
	- Recommendation Systems, Personalization, Search, or Computational Advertising
	- Deep Learning or Causal Inference
	- Optimization algorithms and numerical computation
	- Spark, TensorFlow, or Keras
	- Cloud computing platforms and large web-scale distributed systems
+ tech stack:
	- Write C++ code to tackle scientific algorithmic problems such as: transforming 3D coordinates, Metropolis Monte Carlo simulation, Gradient Descent minimization, and others.
	- Implement highly optimized multi-threaded C++ or CUDA code that scales well on cloud infrastructure.
	- Work closely with other software engineers via code reviews and testing to foster high-quality software and systems.
	- Solid computer science fundamentals, with strong competencies in data structures, algorithms, and compilers.   
	- Experience profiling C/C++ code to find and fix performance bottlenecks.
	- Comfort with the Linux command-line environment.
	- Background in Biology, Chemistry or Physics.
	- Familiarity working with Docker and Kubernetes.
	- Knowledge of parallel computing paradigms and demonstrated proficiency in some of the following: openMP, CUDA, or openCL.
	- https://www.atomwise.com/jobs/senior-software-engineer-scientific-computing/
+ tech stack:
	- You should think about joining us if you care about making a difference in treating disease and saving human lives. But also, if you are up to tackling some of the hardest open challenges in deep learning today:
		+ Non-stationary, unbalanced, and noisy data: Our training data is seldom i.i.d.; new medicines are unlocked by pushing out into newly-discovered biology. Classes are extremely unbalanced, ratios of 1 positive to 70,000 negatives are typical. Help us reason about how to learn appropriately without dismissing nor overfitting to the data; identify when we can trust a label or have confidence in a prediction; and develop techniques to find and correct for systemic biases.
		+ Extreme scaling: Medicinal chemists can synthesize about a trillion trillion molecules today. Help us scale predictive algorithms to orders of magnitude beyond those contemplated in any other problem domain today.
		+ Multi-parameter optimization: Medicine has to be both safe and effective, so we have to concurrently optimize a number of criteria such as potency, selectivity, solubility, toxicity, synthesizability, etc. Help us efficiently explore the Pareto frontier and avoid mode collapse.
		+ Adversarial generation of synthetic data: Data augmentation has shown utility in improving the robustness of predictions. Help us find ways to best integrate molecular physics simulation and machine learning to impute new data.
		+ Explainability and visualization: Subtle patterns govern molecular recognition. Help us to understand how they lead to the discovery of fundamental chemistry by AI.
	- Ph.D. or M.Sc. in computer science, statistics, data science, or related field
	- 5+ years of extensive practical experience and proven track record of developing, implementing, debugging, and extending machine learning algorithm
	- Knowledge of modern neural network frameworks such as Tensorflow, Torch, or Theano
	- Strong analytical and statistical skills
	- Scientific rigor, healthy skepticism, and detail-orientation in running and analyzing experiments
	- Familiarity with processing large data sets in a Linux environment
	- Software engineering skills and coding experience in at least one high-level programming language (Python, R, Java, C/C++, etc.)
	- Biomedical knowledge or experience in processing chemical or biological data is preferred but not required
	- Experience with cloud computing environments (AWS/Azure/GCE)
	- https://www.atomwise.com/jobs/senior-machine-learning-research-scientist/
+ tech stack:
	- Interact with customers to understand their project requirements.
	- Generate and analyze predictive results, and deliver these to our clients.
	- Communicate our results and capabilities through scientific publications.
	- Analyze, curate, and automate the processing of our biochemical databases.
	- Help to develop our modeling software.
	- Ph.D. in chemistry, biology or a related field.
	- Extensive knowledge of medicinal chemistry.
	- Minimum 3 years of experience in lead optimization at a pharmaceutical company.
	- Experience in Computer-Aided Drug Design: structure/ligand-based drug design, molecular docking, virtual screening, QSAR, pharmacophore modeling, PK/PD data analysis and modeling.
	- Comfortable on the Linux command-line.
	- Undergraduate knowledge of statistics.
	- Good knowledge of Python, Perl, Bash, or related scripting languages.
	- Statistical modeling.
	- Experience with cloud computing environments (AWS/Azure/GCE).
	- https://www.atomwise.com/jobs/senior-computational-chemist/
+ tech stack:
	- M.Sc/Ph.D. in Computer Science, Statistics, Cheminformatics, Bioinformatics, Computational Biology or B.S. in Computer Science with 7+ years experience.
	- Strong computer science fundamentals
	- 5+ years of experience in database engineering, data processing pipelines, and HPC
	- Strong database design and software-engineering best practices
	- Strong knowledge of statistics, data analytics, and data visualization
	- Strong coding skills in at least one high-level programming language (Python, Java, C++, etc)
	- Good familiarity with Linux command-line environment
	- Experience in bioinformatics or cheminformatics, working with ingestion of third-party and internal data sources
	- Experience working with scalable algorithms utilizing large amounts of data
	- Experience with cloud computing environments (AWS/Azure/GCE)
	- Experience with non-relational databases
	- Familiarity with organic chemistry
	- https://www.atomwise.com/jobs/senior-data-engineer-cheminformatics-bioinformatics/
+ tech stack:
	- Hadoop ecosystem and its components.
	- Hadoop, Hive, HBase, and Pig
	- Working experience in HQL
	- Pig Latin Scripts and MapReduce jobs
	- Hands-on experience in backend programming, particularly Java, and Node.js
	- Analytical and problem-solving skills
+ Expertise in additional statistical methods (e.g., Bayesian approaches, dyadic analysis, causal inference approaches, factor analysis, SEM)
+ Use of Jira and A-Ha planning tools.
+ Build data tooling to enable data lake, data warehouse, and analytics workflows within the AWS cloud (S3, Redshift, DynamoDB, Spark, Kinesis, Kubernetes, etc.)
+ Experience with SAML, OAuth
+ Working with Jira and Confluence a plus.
+ Experience working with modern deep learning software architecture and frameworks including: Tensorflow, MxNet, Caffe, Caffe2, Torch, and/or PyTorch.
+ Experience with configuration management systems (Ansible and/or Puppet, Saltstack)
+ tech stack:
	- Remote hardware administration with IPMI
	- Configuration and management of
	- SGE/Univa, Slurm, LSF or other DRMS
	- Jenkins CI
	- Phabricator
	- FlexLM licensing
	- Puppet, Ansible, Nagios
	- LLVM, GCC
	- DVCS e.g. Git
	- AWS, Azure, Google Cloud
	- XML and XPath/XSLT
	- Web programming – HTML/DOM, JavaScript, SQL
	- A solid knowledge about how orchestration tools (Kubernetes, Swarm, OpenStack, etc) can be used to deploy, scale, and operate virtualized entities
	- Understand CPU virtualization and container technology from the inside out (hypervisors, Xen, LXC, Docker)
	- The role involves using a range of technologies, such as Python, CMake, BuildBot, Phabricator, AWS etc.
	- Good knowledge of management and security frameworks (SNMP/MIB agents, CLI, RESTful API, OpenBMC) is very useful
	- Knowledge of storage systems (File, Block) is a plus (Local/Network/Cloud Attached)
	- Knowledge of ILOM, BMC, and OCP (Open Compute) is a plus
	- Test automation experience (Some exposure to CTest is desirable)
+ Bonus: Prior experience with Zendesk, Jira or Asana, SQL, in Customer Service or Hospitality
+ Producing effective and interactive data visualizations (Tableau, Shiny, D3)
+ Experience with Databricks or Spark, EMR
+ Bonus points for experience building interactive data visualizations using libraries like D3, Highcharts, and Leaflet, and for experience working with big data systems like Hive, Hadoop, Scalding and Spark.
+ Experience with Scala, Scalding, Luigi,Hive, machine learning pipelines and model training is a plus
+ Automate DB (Oracle, Postgres, MongoDB, ...) configuration, deployment, backups, ...
+ Experience with at least one of: Oracle, Postgres, MongoDB, Solr
+ Chef/Puppet/Ansible/Terraform experience is nice to have
+ Experience with full-text search engines (Solr, Elasticsearch).
+ Familiarity with Docker (and Kubernetes/Mesos Marathon)
+ Familiarity with Angular framework
+ You will work with technologies like: AWS, Docker (Mesos/Kubernetes), HashiCorp tools (Terraform, Consul, Vault,...), Chef, Ansible, SQL and NoSQL databases, Nginx, ...
+ Elasticsearch, Hadoop, Big Data experience is a plus
+ workflow management tools like Airflow
+ search backends like ElasticSearch
+ Spark and/or other big data architectures (Hadoop, MapReduce) in high-volume environments
+ VM embeddings in other systems (e.g., DBMSs, Big Data frameworks, Microservices, etc.)
+ Virtual machines: Managed runtime systems (e.g., JVM, Dalvik VM, Android Runtime (ART), LLVM, .NET CLR, RPython, etc.)
+ We preferred students experienced in the use of ROS (Robot Operating System) and simulation engines such as Unity3D and Unreal Engine 4.
+ ***Knowledge of parallelism in shared (Intel TBB, OpenMP) and distributed (Intel MPI, Apache Spark, Dask) memory***
+ Speech (NLP: ASR, MT, NLP, NLU, TTS, DM, and ASP)
+ Knowledge of OpenCL/SYCL languages
+ ***Experience with large-scale, distributed data processing frameworks (e.g., Spark, Kafka, YARN, Tachyon, Mesos, etc.) is a plus***
+ Domain knowledge and project experience in below area will be a plus: x86 architecture; Linux kernel; Virtualization; Cloud SW stacks; Big data; Machine Learning, compiler and run time optimization, etc.
+ Knowledge of Linux and/or Windows programming and computer graphics including OpenCL\*, OpenGL\*, DirectX\*
+ ***Open-source projects that demonstrate relevant skills  and/or publications in relevant conferences and journals (e.g. NIPS, ICML, ICLR, CVPR, ICCV, ECCV, ICASSP)***
+ ***Experience working with analytics tools such as Google Analytics, Heap Analytics, Chartmogul, Baremetrics, Periscope, Tableau, Mode Analytics, Looker, or similar***
+ tech stack: Golang, AWS (DynamoDB, Lambda, EC2, Kinesis, SQS, S3), ReactJS, Snowflake, Terraform, Redis, SolrCloud, Kafka, Riak, Docker/Kubernetes, and Linux
+ tech stack:
	-  Solid knowledge in control theory, especially model predictive control
	- Experience in one or more of the following areas:
		* Robust control
		* Adaptive control
		* Nonlinear control
		* State estimation
		* Parameter estimation
		* Model identification
		* Optimization
	- Experience in one or more of the following areas:
		* Control theory
		* Motion planning
		* Optimization
		* Formal logic
		* Game AI development
	- Experience with sensors: cameras, lidars, ultrasonic, etc.
	- Computer vision experience, image processing experience
+ You know what the CAP theorem is and you feel confident that you can speak to what it does and does not cover in systems design.
+ Expert in prototyping traditional ML (GBMs, scikit, etc.) and AI frameworks (keras, tensorflow, mxnet, pytorch, etc.) for a variety of applications
+ tech stack:
	- Knowledge of dsx, IGC, and IA
	- Web service development with NodeJS (Backend server Javascript), front-end Javascript and Flask (Open source python library)
	- Both relational database and NoSQL database technologies
	- The main responsibility will be to enable different personas like Data Scientist, Data Curator, and Data Engineer to collaborate with each other on their Data Journey and work with various products like dsx, IGC, IA, and DFD.
+ tech stack:
	- PHP5, PHP7, HTML5, CSS3, JavaScript, Jquery, MySQL, NoSql
	- Should have in depth understanding in LAMP stack
	- Must have Good OOP (Object Oriented Programming) concepts
	- Knowledge in MVC Framework e.g (Zend Framework, Laravel)
	- Clear understanding of JSON, AJAX, XML, CURL, Web Service
	- Knowledge of the Linux command line tools optional
	- Good to have experience in Angular JS and Node JS, concept of UI/UX
	- Experience in handling large database, including designing & advanced querying in MySql
	- Good knowledge of version control tools like GIT, SVN
+ Versatile with languages and technologies. You pick the right technology for the job. You might have dabbled with iOS, Android, React Native or Flutter; you tinkered with TensorFlow, Caffe or Torch; you know when to use Mongo vs Redshift; and you have an opinion on web frameworks.
+ OpenStack:
	- Dashboard (Horizon)
	- Compute Service (Nova)
	- Networking (Neutron)
	- Object store (Swift)
	- Identity service (Keystone)
	- Metering & Data Collection Service (Ceilometer)
	- Orchestration (Heat)
	- Bare Metal Provisioning Service (Ironic)
	- Container Orchestration Engine Provisioning (Magnum)
	- Computable object storage (Storlets)
	- Deploys OpenStack using OpenStack itself (Tripleo)
	- Billing and chargebacks (Cloudkitty)
	- Optimization Service (Watcher)
	- Distributed SDN controller (Dragonflow)
	- OpenStack Networking integration for containers (Kuryr)
	- NFV Orchestration (Tacker)
	- Networking Automation for Multi-Region Deployments (Tricircle)
	- Command-line interface for all OpenStack services (Openstackclient)
	- Instances High Availability Service (Masakari)
	- Lightweight OCI containers (LOCI)
	- EC2 API proxy (EC2API)
	- Official Python SDK for OpenStack APIs (Openstacksdk)
	- Block Storage (Cinder)
	- Image service (Glance)
	- Big Data Processing Framework Provisioning (Sahara)
	- Application Catalog (Murano)
	- Containers Service (Zun)
	- Puppet modules to deploy OpenStack (Puppet-openstack)
	- Clustering service (Senlin)
	- Event, Metadata Indexing Service (Panko)
	- Root Cause Analysis service (Vitrage)
	- Load balancer (Octavia)
	- Accelerators resource management (Cyborg)
	- Deploys OpenStack in containers using Helm (Openstack-helm)
	- OpenStack Storage integration for containers (Fuxi)
	- Client library for interacting with OpenStack clouds (Shade)
	- Database as a Service (Trove)
	- Shared filesystems (Manila)
	- DNS service (Designate)
	- Key management (Barbican)
	- Governance (Congress)
	- Software Development Lifecycle Automation (Solum)
	- Deploys OpenStack in containers using Ansible (Kolla-ansible)
	- Monitoring (Monasca)
	- Workflow service (Mistral)
	- Functions Service (Qinling)
	- RPM package specs to deploy OpenStack (RPM-packaging)
	- Messaging Service (Zaqar)
	- Ansible playbooks to deploy OpenStack (Openstack-ansible)
	- Benchmark service (Rally)
	- Application Data Protection as a Service (Karbor)
	- Backup, Restore, and Disaster Recovery (Freezer)
	- Packaging-rpm (Packaging-rpm)
	- Indexing and Search (Searchlight)
	- Deploys OpenStack in containers using Charms and Juju (Openstack-charms)
	- Resource reservation service (Blazar)
	- Alarming Service (Aodh)
	- Ansible playbooks using ironic (Bifrost)
	- Chef cookbooks to deploy OpenStack (Chef-openstack)
	- EC2 API compatibility layer for OpenStack (Ec2-api)
	- Python Software Development Kit (Python SDK)
	- Ansible playbooks and roles for deployment (OpenStackAnsible)
+ Silicon bring-up
+ Silicon characterisation
+ Massively parallel computing systems
+ Laravel
+ SQL working experience (Redshift/PostgreSQL/MySQL)
+ Experience working with a CI system is preferred (ex. TeamCity, Concourse, Jenkins, etc.)
+ Functional test automation tool experience is preferred (ex. Junit, TestNG, Serenity, etc.)
+ Experience with profiling tools like PerfView (CPU, Memory, Garbage collection)
+ Expert knowledge of debugging and crash dump analysis in Windbg
+ Experience wrangling very large datasets by writing and maintaining data processing pipelines with Hadoop, Spark, BigQuery, Redshift, or similar
+ Google Data Studio
+ The successful candidate would be strong in SQL, AWS, Snowflake, Databricks, and Python.
+ Experience with streaming data frameworks like spark streaming, kafka streaming, Flink and similar tools a plus.
+ Experience with large scale messaging systems like Kafka or RabbitMQ or commercial systems.
+ Experience with working with and operating workflow or orchestration frameworks, including open source tools like Airflow and Luigi or commercial enterprise tools.
+ [Plus] Familiarity with interactive data visualization using tools like D3.js
+ Experience with MPP databases, such as Snowflake, Redshift, BigQuery, Vertica, etc.
+ A fluidity with tools commonly used for data analysis such as Python (numpy, pandas, and scikit learn), R, and Spark (MLlib).
+ Experience with at least one prototyping tool (eg. Axure, Framer, Principle)
+ Proficiency in developing pixel perfect mockups using Sketch and/or Adobe Design tools.
+ Analyze all aspects of the Snowflake Query Engine and drive initiatives to understand what bottlenecks may exist and to improve them.  
+ Build integration code with many cutting-edge technologies and processes, including Python 3, Go, Presto, AWS, ML, NLP.
+ Experience with cloud APIs (e.g., a public cloud such as AWS, Azure, GCP or an advanced private cloud such as Google, Facebook)
+ Prior experience with infrastructure automation frameworks (Ansible, Terraform, Chef or Puppet, etc.)
+ ***Experience with one of the ML platforms: Python / scikit-learn, Spark, vowpal wabbit, etc***
+ Virtualization and containerization (Xen, LXC, cgroups, Docker, Kubernetes)
+ tech stack:
	- Well-versed in one or more of the following languages and functional programming in general: Scala, Java, Python, JavaScript
	- Expert in SQL and comfortable designing, writing and maintaining complex SQL based ETL.
	- Experience with building large-scale batch and real-time data pipelines; ETL design, implementation, and maintenance.
	- Experience with schema design and data modeling, and the analytical skills to QA data and identify gaps and inconsistencies.
+ tech stack:
	- Write complex data flows using SQL, frameworks (e.g., Scalding, Spark), and scripting languages (e.g., Python, R)
	- Use data visualization tools (e.g., Tableau, Zeppelin) to share ongoing insights.
	- Skilled with Figma (or Sketch) and prototyping tools such as Framer, Principle
	- You have a deep and nuanced understanding of statistics, especially involving class imbalance problems.
	- Scalding
	- Full Stack Development
	- Presto or Hive
	- Spark
+ Knowledge of source control tools (Git, CodeCommit, SVN, and TFS), build/release tools (Jenkins, CodeBuild, CodeDeploy, CodePipeline), and infrastructure as code tools (Terraform, CloudFormation)
+ Experience in working with large data sets and distributed computing tools (Hive, Redshift)
+ skill set:
	- B.S. or M.S. in Economics, Statistics, or a similar field and 1+ year work experience in data science or analytics, or Ph.D. in a quantitative social/behavioral science (e.g. Economics, Sociology, Psychology, Statistics, or a similar field)
	- Coursework in experimental design, causal inference, and/or econometrics
	- Experience running and analyzing behavioral experiments
	- Statistical intuition and knowledge of various hypothesis testing and regression approaches, e.g. hierarchical modeling, difference-in-differences
	- Familiarity with Python or similar scripting language
	- Experience communicating technical statistical concepts clearly, for example, teaching or consulting
	- Demonstrated ability working effectively with cross-functional teams
	- Experience using git and pushing to a codebase
	- Experience with software engineering projects or coursework
+ skill set:
	- B.S., M.S., or Ph.D. in a quantitative field
	- 4+ years work experience in an analytical or quantitative role as a Data Scientist
	- 2+ years experience working on product analytics in a two-sided marketplace
	- Extensive experience generating insights using statistical techniques (e.g. regression, hypothesis testing)
	- Demonstrated ability to clearly explain data results to cross-functional teams
	- Experience using a procedural programming language (e.g. Python, R) to manipulate, clean, and analyze data
	- Ability to exercise judgment and combine quantitative skills with intuition and common sense
	- Experience evangelizing best practices and process improvements on your team
	- Experience working with large data sets and distributed computing tools (e.g. Redshift, Presto)
	- Experience pushing code and navigating a complex codebase
	- Active Quora user with curiosity about the product
	- Deep experience with MySQL, NoSQL datastores like HBase or similar
	- Strong grasp of Configuration Management (Chef, Puppet, Ansible, Salt Stack)
- skills to develop:
	- Deep understanding of at least one popular server side MVC Framework (e.g Django, Rails, AngularJS etc).
	- Knowledge of backend storage systems like MySQL, HBase, Memcached, Redis, Kafka etc.
	- Experience working with open source technologies like Kafka, Hadoop, Hive, Presto, and Spark
	- Take end to end ownership of Machine Learning systems - from data pipelines and training, to realtime prediction engines.
	- General understanding of Machine Learning at the level of a semester-long ML class (college or multiple MOOCs)
+ skill set:
	- Deep knowledge of web technologies, e.g. HTML, CSS. Experience with LESS or SASS is a plus.
	- Deep knowledge of JavaScript frameworks, e.g. jQuery. Experience with pure Javascript is a plus.
	- Some knowledge of server-side languages and web frameworks. Experience with Python is a plus.
	- Experience debugging across multiple browsers. Experience with UI testing tools like Selenium or phantomJS is a plus.
	- Experience optimizing the speed and performance of websites.
	- Experience maintaining large and growing code bases in a fast-moving environment.
	- Interest in staying current with new and evolving web technologies.
+ skill set:
	- 7+ years of industry/academic experience in Machine Learning or related field
	- You will be expected to have a good understanding of a broad range of traditional supervised and unsupervised techniques (e.g. logistic regression, SVMs, GBDTs, Random Forests, k-means and other clustering techniques, matrix factorization, LDA . . .) as well as be up to date with latest ML advances (e.g. Deep Neural Networks, or non-parametric Bayesian methods).
	- Previous experience building end to end scalable Machine Learning systems
	- Software engineering skills. Knowledge of Python and C++ is a plus.
	- Knowledge of existing open source frameworks such as scikit-learn, Torch, Caffe, or Theano is a plus
	- BS, MS, or PhD in Computer Science, Engineering, Statistics or a related technical field
	- Love of the Quora product
+ skill set:
	- BS, MS or PhD in Computer Science, Machine Learning, NLP or a related technical field
	- 5+ years of industry experience preferred
	- Good mathematical understanding of popular NLP and Machine Learning algorithms
	- Experience building production-ready NLP or information retrieval systems
	- Hands-on experience with NLP tools, libraries and corpora (e.g. NLTK, Stanford CoreNLP, Wikipedia corpus, etc)
	- Knowledge of Python or C++, or the ability to learn them quickly
	- Love of the Quora product
+ ***Experience building shallow or deep learning models (GBDT, CNN, RNN, LSTM), toolkits e.g. OpenCV, Matlab, RStudio, Weka, MLLib and frameworks PyTorch, TensorFlow, CNTK***
+ ***Expertise in multivariate analysis, graphical models, Bayesian hierarchical modelling, Markov chain Monte Carlo (MCMC), mixture models, stochastic processes, generalized linear models (GLMs), dimensionality reduction (PCA/CCA/MDS/tSNE) and other machine learning techniques***
+ Experience working with Atlassian products (JIRA, Confluence)
+ Knowledge of Internet protocols (e.g., TCP/IP, BGP, OSPF, TACACS, IPSEC, SNMP, SYSLOG)
+ Speech (NLP: ASR, MT, NLP, NLU, TTS, DM, and ASP)
+ Experience with SQL and Statistical/mathematical programming software packages (R, SPSS, CPLEX, LONDO or Xpress etc)
+ ***Programming skills sufficient to extract, transform, and clean large (multi-TB) data sets in a Unix/Linux environment.***
+ Experience with NLP libraries such as SpaCy, Stanford CoreNLP, OpenNLP, or NLTK
+ ***Experience with big data techniques (such as Hadoop, MapReduce, Hive, Pig, Spark)***
+ ***Familiar with one or more machine learning, statistical modeling tools such as R, Matlab, scikit learn and deep learning frameworks, such as tensorflow, keras, caffe, torch.***
+ skill set for data science:
	- ***Technical mastery in one or more of the following languages/tools to wrangle and understand data: Python (NumPy, SciPy, scikit-learn), Spotfire, Tableau.***
	- ***Experience with Spark (MapReduce, PIG, HIVE)***
	- 5+ years of experience with R or Python and some knowledge of SQL and experience with other software environments e.g. SAS, Matlab, Spotfire, Tableau, Qlikview, SPSS, KNIME and/or other data mining tools. Experience with other software components for data preparation and integration e.g. Data Virtualization and Big Data tools such as Hadoop and Spark and/or further programming or scripting environments e.g. .Net, Java, IronPython, Javascript, C++ is a plus.
	- 5+ years of experience with R or Python and some knowledge of SQL and experience with other software environments e.g. SAS, Matlab, Spotfire, Tableau, Qlikview, SPSS, KNIME and/or other data mining tools. Experience with other software components for data preparation and integration e.g. Data Virtualization and Big Data tools such as Hadoop and Spark and/or further programming or scripting environments e.g. .Net, Java, IronPython, Javascript, C++ is a plus.
+ stress testing (locust.io)
+ designing high availability systems
+ application security hardening
+ distributed tracing (OpenTracing/Zipkin)
+ collecting and analyzing performance metrics (InfluxDB, Prometheus, statsd, Grafana)
+ Docker orchestration systems and cluster managers (Kubernetes, Mesos/Marathon, ECS)
+ Experience in the technologies we use is helpful but not required. They are: Go for core infrastructure; ObjC, Java and C# for native UI development on iOS, OSX, Android and Windows; Node.js and IcedCoffeeScript for Web development; FUSE for client file systems; MySQL/InnoDB, DynamoDB, S3 and EC2 for hosting.
+ Load testing frameworks/tools like JMeter, Gatling, Locust
+ Java, Selenium, JUnit, Cucumber-JVM
+ API Testing experience
+ BDD (Cucumber, Gherkin)
+ Experience implementing search solutions with technologies such as SOLR, Elasticsearch, Lucene is preferred.
+ Python, Gherkin, Cucumber, Espresso, XUI Test
+ Experience with testing technologies (JUnit, Espresso, Mockito, Robolectric)
+ Unit Testing Tools  –  Google Test or CPPUnit ; Code quality tools
+ Familiarity with Linux, Maven, Git/Stash, Jira, Bamboo/Jenkins
+ Experience with distributed messages systems ( Apache Kafka)
+ Experience in CFD combustion or other reacting-flow simulations.
+ tech stack
	- Jira, Confluence, DevOps, Continuous Integration and Continuous Delivery, Microsoft Development Tools
	- Git, MS Build, Team Foundation Server, Jenkins, Unit Testing, Powershell, Perl, C#, .NET, Visual Studio, Python
+ tech stack:
	- Excellent skills in creating high-fidelity prototypes using Invision, Principle, Code or similar
	- Relevant experience in agile methodologies (Scrum, Agile, etc) and PM tools (e.g. Jira, Pivotal Tracker, Confluence etc.)
	- Experience with relational (e.g. MySQL, PostgreSQL) and NoSQL (e.g. MongoDB, ElasticSearch) databases
+ tech stack:
	- Expertise in Go preferred, but not required. If you’re new to Go, then proficiency in a mainstream language such as Java, Python, C++, Scala, etc.., and a willingness to learn Go required.
	- You've got experience writing, deploying and monitoring microservices.
	- Working knowledge of SQL and relational databases(we use Postgres)
	- You've used an RPC framework like gRPC or Thrift.
	- You have high level experience working in a containerized infrastructure deployed in the cloud(AWS, GCP, Azure)
+ tech stack:
	- Experience with NoSQL databases. MongoDB is a plus
	- Experience with real-time and streaming data processing
	- Experience with queuing platforms like Kafka
	- Knowledge of BigQuery
	- Familiarity with GCP/AWS cloud services
	- Familiarity with TensorFlow
	- Comfortable with CI/CD Pipelines
	- Experience with Git version control
+ tech stack:
	- Ability to configure and maintain webservers (e.g. apache & nginx), DNS servers, Firewalls, LDAP servers, Tomcat servers
	- Ability to back up the Data infrastructure
	- Ability to manage/configure  Git, Maven and Jenkins
	- Managing QA/production release and deployment
	- Ability to Install/Configure/Manage VM servers using OpenStack
	- Ability to install configure or manage Monitoring servers using Opensource softwares
	- Experience with Amazon Web Services:
	- autoscaling, & use of Netflix Asgard
	- ELB management,
	- EBS storage management
	- S3
	- RDS
	- Manage configuration using Puppet
	- Familiar with Cloud Computing in genera
+ tech stack:
	- ReactJS
	- GraphQL
	- Apollo Client & Server
	- Some Redux
	- Using ES6/7 features throughout the app so knowledge on those is a plus.
	- We use Cypress for testing
	- CircleCI for continuous integration.
	- Functional programming principles in React with Recompose
+ Celery
+ Elasticsearch and ELK pipeline
+ LibreOffice, Apache OpenOffice, and NeoOffice.
+ Tech stack is described as:
	- Front­end: JavaScript (ES5/ES6), AJAX, jQuery, React/Angular/Vue, Bootstrap, templating, markdown/markup, built tools, task runners, PWAs, etc...
	- Middle­tier: REST and RESTful interfaces, AJAX, RPC, WebSockets/Socket.io, Web Workers, Node.js/Express, etc…
	- Back­end: SQL/No­SQL databases, Message Queue Systems, Big Data systems, Node.js, MongoDB, Redis, etc...
+ data Science:
	- Knowledge of ElasticSearch/Solr/Lucene is a big plus.
	- Understanding in Java server platform and system tuning is a plus.
	- Knowledge with vector space models, text classification and categorization.
	- Implement high-quality code in an agile software development environment.
+ data science skill set:
	- Implement scalable algorithms and services using technologies such as Scala, Akka, elasticsearch, Kafka, Cassandra and Hadoop technologies such as Hive, Spark or MapReduce
	- Hands-on experience in analyzing large datasets (e.g. with SQL, Python, R, Hive, etc.)
	- Some knowledge and experience in working with technologies such as Kafka, Cassandra, Elasticsearch, Akka, Kubernetes, etc.
	- Experience in Scala or Java is a plus
	- You are fluent in English; German skills are a plus
+ AWS cloud services: EC2, EMR, RDS, Lambda, Redshift
+ NoSQL databases, such as HBase, Cassandra, MongoDB, or DynamoDB
+ messaging systems, such as AWS SQS, AWS Kinesis, Kafka, or RabbitMQ, ZeroMQ
+ big data tools and stream-processing systems: Hadoop, Spark, Storm, Spark-Streaming
+ **Expertise and experience in Revit, Dynamo and/or other Revit scripting languages**... Strong background in computational design and design analysis... Fluency in a technical programming language (python, javascript, C#) is highly desired.
+ Understanding of standard networking protocols and components such as: TCP/IP, HTTP, DNS, ICMP, the OSI Model, Subnetting, and Load Balancing
+ Knowledge of routing protocols such as BGP and OSPF
+ data pipeline and workflow management tools: Azkaban, Luigi, Airflow
+ Very well versed with ADT, ORU, ORM and document exchange messages specification
+ Develop public APIs on either APIGEE
+ DBT experience
+ Object oriented programming experience (e.g. using Java, J2EE, EJB, .NET, WebSphere, etc.).
+ data interchange formats like JSON and XML
+ Knowledge in machine learning framework - Tensorflow, Caffe, Torch or Theano
+ Django, Ruby on Rails, Flask
+ Must have experience with working on few technologies such as spring framework, SpringBoot, SpringMVC, JPA, MyBatis, Tomcat, Nginx
+ Experience with performance optimization of queries in Redshift & Postgres
+ Knowledge of authentication protocols such as basic and digest authentication, SAML, LDAP, and OAuth.
+ In-Memory caching technologies, such as memcached or Redis
+ Cutting edge C++ knowledge (C++17, C++20)
+ stream pipelines and all sorts of datastores (SQL, NoSQL, triplestores, wide column, graph)
+ Knowledge of data standards, file formats, and biomedical ontologies and vocabularies such as SNOMED-CT, UMLS, etc. DICOM
+ all types of datastores - NoSQL, wide column, Graph, triplestores
+ Spark, Kafka
+ Experience with stream pipelines and data store technologies (nosql, wide column and graph). We are Currently using Cassandra, Kafka, Amazon dynamoDB, Redis, Neo4j and Mysql.
+ NLP library: spaCy, NLTK, GATE, CoreNLP, gensim
+ Deep Learning applied to NLP, for example through distributed representations (e.g. Word2Vec, fastText, etc)
+ large databases (e.g. THIN)
+ Monitoring solutions experience (ELK, NewRelic)
+ Infrastructure-as-code and automation tools (e.g. Terraform, Ansible/Chef, Cloud Formation)
+ Configure and Monitor SIEMS and DLP systems
+ RxJava, Kotlin, Dagger
+ big data platform tools such as Hadoop, Hive, Druid, Kafka, Ambari, Spark
+ Experience with common security tools such as nmap, Burp Proxy, Brakeman, etc.
+ Experience with bug bounty programs and reporting issues to them (send examples, please!)
+ Familiarity with search domain (Information retrieval, NLP, Solr/ Lucene or related tech)
+ data management tools in on a big data plate form such as Atlas, Ranger , Knox
+ implementing BI solutions in a heavily regulated environment e.g. PII, GDPR, HIPPA & SOX
+ big data platform tools such as Hadoop, Hive Druid, Kafka, Ambari, Spark, Zeppelin
+ PowerBI, Tableau, Qlikview
+ Production experience with AWS tools including at least some of the following: EC2, S3, Kinesis, CloudFormation, Redshift
+ Experience with at least one data warehousing platform (Redshift, Athena, Hive, Snowflake, etc.)
+ Knowledge of a majority of the following: Elixir, Erlang, Ruby, JavaScript, PHP, Postgresql, MySQL, Apache Solr, Elasticsearch.
+ Knowledge of web frameworks (like Sinatra/Rails), testing frameworks (like Rspec/Minitest) and Javascript. Experience with Ruby, MySQL and Apache Solr is a plus.
+ Experience with Java, Boost, QML, Jira, JavaScript, React, or DDP
+ Demonstrated proficiency with Docker and container orchestration technologies (Kubernetes, ECS, etc.)
+ Expertise with AWS services such as EC2, IAM, S3, etc.
+ Expertise with several continuous integration technologies (Jenkins, Ansible, CloudFormation, Terraform, etc.)
+ Experience with load balancing technologies such as ELB, NGINX, etc.
+ Experience with network technologies like DNS, AWS security groups, VPCs, etc.
+ Extensive experience manipulating and analyzing complex data with SQL, Python and/or R. Knowledge of Google BigQuery and Java/Scala is a plus.
+ Tools: Slurm, Docker, Grafana.
+ skill set:
	- Bachelor’s degree in Computer Science, Math, Statistics, Economics, or other quantitative field; Masters or PhD strongly preferred
	- Significant experience in custom ETL design, implementation and maintenance, including serving machine learning models in production for multiple high-growth companies, preferably those with technical products
	- Track record of developing and evolving complex data environments and intelligence platforms for business users
	- Demonstrable ability to relate high-level business requirements to technical ETL and data infrastructure needs, including underlying data models and scripts
	- History of proactively identifying forward-looking data engineering strategies, utilizing cutting-edge technologies, and implementing at scale
	- Hands-on experience with schema design and dimensional data modeling
	- Understanding of statistical modeling, machine learning and data mining concepts
	- Demonstrable critical thinking and analytical skills, including the ability and confidence to make conclusions and recommendations from data
	- Experience interacting with key stakeholders in different fields, interpreting challenges and opportunities into actionable engineering strategies
	- Experience with Big Data/distributed frameworks such as Spark, Kubernetes, Hadoop, Hive, Presto,
	- Experience with job schedulers; Airflow, Luigi, Azkaban, etc.
	- Experience with continuous integration and automation tools and processes
	- Advanced SQL and relational database knowledge (MySQL, PostgreSQL) in addition to warehousing and dimension modeling
	- Scripting in Python required, experience with Scala/Go a plus
	- Programming against APIs required
	- Experience with Snowflake and/or Looker a plus
	- Effective communication and interpersonal skills
+ skill set:
	- Bachelor’s degree in Computer Science, Math, Statistics, Economics, or other quantitative field; Masters or PhD strongly preferred
	- Previous experience in data science or quantitative analytics role, preferably in a high-growth company
	- Comprehensive understanding of statistical modeling, machine learning and data mining concepts, and experience applying these methods within a business environment
	- Strong knowledge of Python. Familiarity with at least one statistical modeling / machine learning tool such as R or Matlab is a plus, as well as experience with languages such as Scala or Go
	- Expert knowledge of, and hands-on experience with, SQL
	- Demonstrable critical thinking and analytical skills, including the ability and confidence to make conclusions and recommendations from data
	- Experience interacting with key stakeholders in different fields, interpreting challenges and opportunities into actionable data-driven analysis and implementing science-driven data products
+ skill set:
	- Agile development approaches
		* Lean-startup and design-thinking inspired methods incorporating short product development, business-hypothesis-driven experimentation, iterative product releases, and validated learning
	- Programming languages and operating systems
		* Python
		* Javascript
		* Unix/Linux/MacOSX
		* RDF, JSON-LD, SPARQL
	- Tools
		* Git
		* Slack
		* JIRA
	- Web app development
		* Django
		* Django REST Framework (for API development)
		* Node
	- Backend
		* SOLR/Lucene or ElasticSearch
		* Amazon Web Services (AWS) or other cloud service providers
		* “Serverless” computing (e.g., AWS Lambda)
		* Application containerization (such as Docker or Kubernetes)
	- Javascript frameworks
		* Vue and/or Nuxt
		* Webpack
	- Mobile development
		* Using responsive design and development techniques, possibly including the use of Progressive Web Application (PWA) techniques and technologies
	- Other
		* Topic modeling (ideally using Mallet)
		* Video formats and metadata (for both archiving and streaming)
		* RDF, JSON-LD, Sparql and GraphQL for knowledge graph development and use
		* Content markup including:  HTML, XML, ePUB, PDF
		* Named Entity Recognition (NER)
		* Experience applying statistics, modeling, and machine learning
+ skill set:
	- SQL, javascript, and google appscript
	- Familiarity with HR systems and tools (e.g. Workday, Reflektive, Zugata, Culture Amp)
	- You are a skilled engineer. You've got a strong background working in our stack (Python, Django or React, ES6 or Node.js, etc.) -- even if you aren't a daily coder, you regularly exercise your coding muscles and try to be an asset on any technical context your team may need.
	- Help the team build tools for partners and developers that come to our platform to create Apps that live on Zapier. Imagine Postman meets OpenAPI on steroids.
+ tech stack:
	- Research publications at relevant conferences such as SIGGRAPH, ACM Trans on Graphics, CVPR, ICCV, ICCP, SPIE, JOSA a major plus.
	- Expertise in Deep Learning, Machine learning and familiarity with tools like Scipy, Boost, Caffe, TensorFlow, OpenCV, DLIB etc. and related areas.
+ Because compilers, interpreters, JIT, pre-processors, grammars, register allocation, term rewriting, LLVM and more are what brought us to computer science in the first place, Raincode Labs forms the largest independent compilation technology company in the world.
+ tech stack:
	- Publication record in top conferences (ICML, ICLR, NIPS, KDD, IJCAI, AAAI etc )
	- Good knowledge and handson experience in distributed technologies such as Hadoop, Hive, Spark Experience in Scala programming language.
	- Publications in relevant top venues (e.g., KDD, NIPS, ICML, AAAI, IJCAI, ICDM, ACL etc.)
	- You have publications in communities such as WWW, SIGIR, FAT*, NeurIPS, WSDM, SIGDIAL, RecSys, CHI, KDD, AAAI, ACL, ICML, or related.
	- You have hands-on experience implementing production machine learning systems at scale in Java, Scala, Python, or similar languages. Experience with XGBoost, TensorFlow is also a plus.
	- You preferably have experience with data pipeline tools like Apache Beam or even our open source API for it, Scio and cloud platforms like GCP or AWS.
	- Extensive experience manipulating and analysing complex data with SQL, Python and/or R. Knowledge of Google BigQuery and Java/Scala is a plus.
	- Familiarity with marketing tracking platforms (e.g. DoubleClick, Google Tag Manager, Google Analytics) preferred
	- Become an expert on leveraging existing state-of-the-art tooling into the Spotify eco-system (TensorFlow, TFX, Kubeflow Pipelines, Cloud Bigtable)
	- Contribute to new and existing Spotify open source machine learning and data processing products (scio, zoltar)
	- You preferably have experience with data processing and storage frameworks like Google Cloud Dataflow, Hadoop, Scalding, Spark, Storm, Cassandra, Kafka, etc.
	- Extensive publication record at peer-reviewed ML conferences (e.g. NIPS, ICML, AISTATS, UAI, COLT, ICLR, AAAI, etc) as well conferences with applied ML (e.g. KDD, WSDM, WWW, CIKM, RecSys, etc).
+ tech stack:
	- Security and privacy
	- Virtualization and container technologies (e.g., Xen and Docker)
	- Cloud services (e.g., AWS and Azure)
	- Distributed programming tools (e.g., Hadoop, Cassandra, and ZooKeeper)
	- In-home wireless network protocols (WiFi, Bluetooth, Zigbee, and Z-wave)
	- Systems for machine learning training and inference (Tensorflow, MXNet, Caffe etc)
	- Storage systems
+ Experience with open source platforms like Hadoop, Spark, Hive, Pig; and/or ML life-cycle/collaboration/automation platforms like AirFlow, FB Learner, MLFlow; and/or assistants like Alexa, a plus.
+ "Knowledge of Bayesian Global Optimization tools and technique"
+ Working with Big Data, ML, AI. Keras, TensorFlow, Python, Redshift, S3, Spark, Random Forests and Vowpal Wabbit
+ Experience implementing production-ready machine learning solutions is a plus
+ You’ll lead, analyze, implement, and socialize a robust A/B/multivariate testing program, collaborating closely with product, engineering, marketing, and content.
+ You’re familiar with all aspects of SEO: on-page, external, and technical, and you have used tools such as ahrefs, DeepCrawl, Screaming Frog, SEMRush, and Google Search Console to optimize for search.
+ Set of skills:
	- Experience with modern programming languages (Java, Scala, Go, TypeScript)
	- Database / Data Storage experience (SQL / MySQL, MongoDB, DynamoDB)
	- Interest in Infrastructure Tooling (Docker, Nomad, Consul, Vault, Prometheus)
+ RStudio packages: The tidyverse, R Markdown, and Shiny
+ A sample of the technologies you’ll be exposed to: Python, Javascript/Angular, Impala (Big data data database), AWS, Docker, Kubernetes, Git.
+ Experience with Python ORMs like SQLAlchemy and Python libraries like Pandas, Scikit-Learn, Numpy and Scipy
+ Should have experience in dealing with XML and JSON data formats.
+ Knowledge in Hadoop (HDFS, YARN), its programming models (MapReduce, Spark), and its services such as Hive, HBase etc.
+ Technical Fluency.  Languages and tools such as Python/Java/Scala, AWS (S3/EMR/Athena/Glue) and SQL. Experience with big data processing tools including Spark, Hadoop, Hive, Yarn, and Airflow. Experience working with either a MapReduce system of any size/scale.
+ Experience writing production datasets in SQL/Hive OR building internal/production data tools for ETL, experimentation, or exploration in a scripting language (Python, R, etc.)
+ Very strong experience in scaling and optimizing schemas, performance tuning SQL and ETL pipelines in the OLTP, OLAP and Data Warehouse environments
+ Passionate about various technologies including but not limited to SQL/No SQL/MPP databases etc.
+ Hands-on experience with Big Data technologies (e.g Hadoop, Hive, Spark)
+ Ansible: it’s not that bad, and helps us move quickly, but any configuration management tool is applicable.
+ Elasticsearch / Kibana: You can readily access information & love metrics
+ Familiarity with common web application testing tools for DAST, SAST, and IAST analysis such as Burp Suite, Checkmarx, Veracode
+ Completed graduate-level coursework in survey statistics—bonus points if you've completed coursework in adjacent fields/methods (e.g., econometrics, NLP, experimental design, political science, or quantitative social psychology)
+ Exposure to container technologies - container orchestrators (Kubernetes, Mesos, Docker Swarm Mode) is a plus
+ Experience with Cloud based services, Microservices a Cloud Computing class or similar experience
+ Technical Skills needed: vSphere, vSAN, NSX, vROps, Storage, Database, Middleware, and Scripting
+ Experience of Unity, C# and 3D application development.
+ Working knowledge of HMD (ie Oculus, HTC Vive, Hololens)
+ Experience with Hololens, HTC Vive, Oculus, Google Cardboard and other leading AR/VR platforms
+ Knowledge of NoSQL technologies (e.g. Cassandra, MongoDB, Redis, etc.) and/or search-based datastores and libraries (Lucene, Solr, etc.)
+ Experience within the domain of Advanced Analytics and Data Science is highly desirable, e.g. hands-on experience with solutions such as Spark, MapReduce, Python, Redshift, Hive, Pig and visualization tools.
+ Hadoop data platform is capable of supporting a growing list of downstream platforms like Tableau, Zeppelin etc.
+ Expertise with Hive, YARN, Spark, Presto, Kafka, SOLR, Oozie, Sentry, Encryption, Hbase, etc.
+ API development
+ You highly experienced with JavaScript/Node.js, SQL/NoSQL databases
+ We are fans of the Lean Startup methodology, we love Trello, Jira, Slack
+ We are cloud agnostic and run our infrastructure and systems on Azure, AWS, as well as dedicated servers.
+ Experience utilising Portfolio & Project Management (PPM) tools such as CA PPM (Clarity), ServiceNow, JIRA, Microsoft Project Server, etc.
+ project management tools (JIRA, Confluence),
+ big data platform tools such as Hadoop, Hive, Druid, Kafka, Ambari, Spark
+ web analytics platforms such as Google Analytics, Appsflyer or Mixpanel
+ NoSQL databases, such as MongoDB, Cassandra, HBase
+ Proficiency in using query languages such as SQL on a big data platform e.g. Hadoop, Hive
+ data visualisation tools, such as D3.js, GGplot, Tableau etc.
+ Excellent understanding of machine learning techniques and algorithms, such as k-NN, Naive Bayes, SVM, Decision Forests, etc.
+ Apache Kafka
+ vw / xgboost
+ Knowledges of Web test frameworks like Selenium, React.js, Headless Chromium is a plus
+ set of skills:
	- Statistical analysis and modeling
	- Database architectures
	- Hadoop-based technologies (e.g. MapReduce, Hive and Pig)
	- SQL-based technologies (e.g. PostgreSQL and MySQL)
	- NoSQL technologies (e.g. Cassandra and MongoDB)
	- Data modeling tools (e.g. ERWin, Enterprise Architect and Visio)
	- Python, C/C++ Java, Perl
	- MatLab, SAS, R
	- Data warehousing solutions
	- Predictive modeling, NLP and text analysis
	- Machine learning
	- Data mining
	- UNIX, Linux, Solaris and MS Windows
	- Python (3.5>=), packages: argparse, shapely, Munkres, numpy, cv2, logging, Pillow
* ES6
* Plotly.js
* OpenLayers
+ UI/UX:
	- Experience using design tools such as Photoshop, Illustrator, Sketch, InDesign, etc. for creating highly-detailed mockups
	- Some awareness of the technology which will serve your designs and implementations, such as apache/nginx, Flask/django, PostgreSQL/MySQL, git, websockets, etc.
	- Bootstrap, bulma, etc.
+ Areas of interest:
	- Distributed and parallel systems
	- Information retrieval
	- Large software systems
	- Web application development
	- Database management
	- Cloud computing
	- Cloud security
	- DevOps
+ technologies/frameworks:
	- ReactJS
	- Java/Scala
	- Spark
	- Ruby/JRuby
	- ElasticSearch
	- MySQL
	- Kubernetes
	- Amazon Web Services
	- MS Azure
	- Google Cloud Platform
+ Knowledge of NoSQL technologies (e.g. Cassandra, MongoDB, Redis, etc.) and/or search-based datastores and libraries (Lucene, Solr, etc.
+ Experience with Cloud based services, Microservices a Cloud Computing class or similar experience
+ Produce high quality and well-documented code in an automated CI/CD environment
+ Collaborate with engineering and product teams to design, develop, and publish software supporting a highly available, fault-tolerant SaaS platform
+ skill set:
	- Expertise in Golang and proficiency in other languages (Preferably C/C++,NodeJs, Python).
	- Commercial experience with REST, RPC and message exchange protocols.
	- Experience with frameworks such as: Gin, Gorilla, Dep, Ginkgo
	- Knowledge around message queuing and distributed tasking (SMS,ZeroQ, RabbitMQ etc)
	- Working knowledge in Kubernetes, Rancher or Docker swarm.
	- Ability to write clean and effective Godoc comments
+ Preferred Skills: Tensorflow, Slurm, Kubernetes
+ data science skills:
	- Excellent understanding of ML, NLP, and statistical methodologies
	- Excellent programming skills (Java/Python/R/Sas)
	- Ability to test ideas and adapt methods quickly end to end from data extraction to implementation and validation
	- Experience with search engines, classification algorithms, recommendation systems, and relevance evaluation methodologies a plus
	- Specific Big Data experience on cloud computing platforms with technologies such as Hadoop, Mahout, Pig, Hive and Spark a plus
	- 7+ years of experience with Data Science and Statistics, preferably in Life Sciences, and more specifically, in pharmaceuticals.
	- The ability to tell a story about data, in particular with visualization.
	- Solid understanding of statistics and the design and analysis of experiments. Solid skills in statistical language, SAS.
	- Provides automated and ad-hoc analysis of experiments.
	- Assesses and validates reliability of source data and business systems used to develop performance metrics.
	- Prepares recommendations and conclusions based on data summaries and communicates this information in a credible, convincing and timely manner.
	- Explores existing data for insights and recommends additional sources of data for improvements.
	- Guide the architecture of “big-data” business processes with an eye towards robustness, parsimony and reproducibility (at senior levels)
	- Define and develop software for the analysis and manipulation of large and very large data-sets
	- Narrate stories (sometimes to a non-technical audience) about our content and processes by data analysis and visualization
	- Collaborate with scientists, product groups and content groups to perform “big data” aggregations, fusion and manipulations of important data-sets
	- This is a thought leader.
	- Define, manipulate, aggregate and use both structured and unstructured "big data" in order to support descriptive and predictive analytics across the businesses.
	- Adept at all aspects of technical communications, including using presentations technologies (e.g. WebEx, PowerPoint) and software demonstrations.
	- Data Collections: Expertise in large data collection and processing including ETL, workflow and delivery of data
	- Business Intelligence (BI) tool like Qlik or Tableau
+ data science skill set:
	- Advanced knowledge of ElasticSearch/Solr/Lucene.
	- Advanced knowledge of backend paradigms
	- Knowledge with vector space models, text classification and categorization
	- Implement high quality code in an agile software development environment.
	- Able to respond and present work to peers, answer in-depth questions, accept constructive feedback, and modify product accordingly.
+ Testing and directly mitigating against common application security issues such as the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project).
+ Experience in a UGC (user generated content) environment
+ Design services for performant application of machine-learned models
+ Polyglot developer (e.g. Java, NodeJS, Python)
+ Experience with any one of segmentation, object detection, image classification, GANs, monocular depth estimation or a related field
+ Successful record of publication in top-tier international research venues (e.g. ICLR, AAAI, NeurIPS, CVPR, ECCV, ICCV, SIGGRAPH)
+ Very strong programming skill in C++14. You will be expected to know and use C++ templates, lambdas, and high-performance data structures.
+ Research and develop CNN/RNN neural network compression algorithms, focusing on quantization and pruning
+ embedded deep learning:
	- Analyze, test and improve neural network compression algorithms
	- Experience with at least one deep learning algorithm, such as CNN/LSTM/GRU
	- Experience with at least one deep learning framework, such as Tensorflow, Pytorch, Caffe, Kaldi
+ Demonstrated expertise with C++ with at least one of std::thread / OpenCL / CUDA
+ You know your way around SQL-like databases (e.g. PostGres, Impala, Hive) and even better if have experience with Spark and other big data platforms.
+ ***Strong publication record in top-tier research publications and conferences such as IJCV, CVPR, ICCV, ECCV, ICRA.***
+ https://www.openrobotics.org/interns
+ machine learning:
	- Develop backend services and infrastructure to expand our answer engine to support 10M+ documents and 100K+ QPS
	- Ship web applications and APIs using Python, Flask, MongoDB, MySQL, Lucene, Spark, React, Go, and/or TensorFlow
	- Optimize the performance of our indexing, processing, and query pipelines
	- Take product ideas from ideation to implementation
	- Implement state-of-the-art algorithms in Question Answering, Machine Reading Comprehension, Text Summarization, in a scalable, production-ready fashion using Tensorflow and Spark
	- Build systems to evaluate and tune performance of a real world deep learning system, from data collection to processing to model implementation to post-processing and visualization
	- modern Big Data stack (Spark or Hadoop, Kafka or RabbitMQ, ZooKeeper, Redis, Memcache, Lucene, MongoDB, MySQL)
	- Familiarity with containerization and dev-ops (Docker, Kubernetes, Docker Swarms, Jenkins, Phabricator, Continuous Integration, Continuous Delivery) is a plus
	- Familiarity with modern Deep Learning and Natural Language Processing / Natural Language Understanding (NLP, NLU), including Neural Networks, RNNs, seq2seq models, and real world machine learning in TensorFlow (incl. regularization, cross-validation, dropout) are a huge plus
	- Adaptable, humble, and interested in pushing the boundaries of what's possible
	- Work with world class talent (our team consists of former Facebook, Palantir, Dropbox, and LinkedIn Engineers; we have 2 ACM ICPC World Finalists)
+ data science:
	- Experience in modern Deep Learning and Natural Language Processing / Natural Language Understanding (NLP, NLU), including Neural Networks, RNNs, seq2seq+attention models, and real world machine learning in TensorFlow (incl. regularization, cross-validation, dropout)
	- Experience building production-ready NLP systems
	- Familiarity with non-standard machine intelligence models (Reinforcement Learning, Hierarchical Temporal Memory, Capsule Networks) is a plus
	- Familiarity with Distributed systems (Docker, Kubernetes, Kafka, Spark, Redis, AWS S3/EC2/RDS/KMS, MongoDB, or Lucene) is a plus
	- Adaptable, humble, and interested in pushing the boundaries of what's possible
	- Proficiency in Python, R, or Java
+ Installation, setup and calibration of MOCAP system, binocular cameras
+ Unigraphics or Pro-engineer fluency.
+ robotics engineering:
	- Background in multiple of the following: SLAM, mapping, localization, calibration, sensor fusion, tracking, scene understanding, robotic systems.
	- Experience in multiple of the following: non-linear optimization, 3D geometry, state estimation.
	- Experience with advanced algorithms, data structures and working with real sensor data.
	- Experience with Python and developing in the Linux and/or Mac OS environment.
	- Familiarity with real-time, multi-process and multi-threaded coding.
	- Strong C++ development skills.
	- Be an essential part of a team of engineers and scientists developing state-of-the-art estimation algorithms used for a variety of tasks, including calibration, localization and tracking.
+ Perform analysis of security incidents & threat actors for further enhancement of Detection Catalog and Hunt missions by leveraging the MITRE ATT&CK framework.
+ Experience with information security tools such as an enterprise SIEM solution (Splunk preferred), IDS/IPS, endpoint security, EDR and security monitoring solutions (NSM,DLP,Insider, etc).
+ Scikit-learn, Keras/Tensorflow, Spark MLlib, Spacy or other ML libraries
+ tech stack:
	- Docker (Kubernetes)
	- Spark (on Hadoop)
	- Kafka
	- Cassandra (or other NoSQL DBs)
	- AWS and some of its services
	- Azure and some of its services
+ Interesting projects with technologies like Scala, Java, Groovy, Akka, SpringBoot, Cassandra, MongoDB, Apache Kafka, JavaScript, TypeScript, React, Angular.
+ tech stack:
	- Python (numpy, pandas, sklearn, xgboost, TensorFlow)
	- MySQL, Hive
	- Java
	- Google Cloud Platform
	- Tableau, Looker
+ tech stack:
	- Python (numpy, pandas, scikit-learn, tensorflow, keras)
	- Google Cloud Platform
	- Machine Learning (e.g. regression, ensemble methods, deep learning, etc.)
	- Statistics (Bayesian methods, experimental design, causal inference)
	- Tableau, Looker
	- Snowflake (SQL)
+ skill set:
	- Familiarity with containerization technologies (docker, lxc, rkt, etc.).
	- Familiarity with container orchestration technologies (Kubernetes, Marathon, etc.).
	- Experience working with cloud computing services providers (AWS, Google cloud platform, Azure, etc.).
	- Experience with Elasticsearch /Apache Solr and Logstash
	- Experience working with Real-time messaging and NoSQL infrastructures: Redis, RabbitMQ, Celery, Kafka, etc.
	- Scalable data processing techniques: Kafka, Spark, ElasticSearch, Celery
	- Real-time messaging and NoSQL infrastructures: Redis, RabbitMQ
	- Have proven experience with ORMs (e.g. Django) and RDBMS (e.g. MySQL) including development of complex SQL queries.
+ skill set:
	- A fluidity with tools commonly used for data analysis such as Python (numpy, pandas, and scikit learn), R, and Spark (MLlib).
	- Experience with MPP databases, such as Snowflake, Redshift, BigQuery, Vertica, etc.
	- Familiarity with data visualization tools/frameworks as well as notebooks.
	- Experience with time-series forecasting.
	- Experience building and deploying production-grade models in a real-time setting.
	- Expert-level abilities building and deploying unsupervised, semi-supervised, and supervised models on large-scale data (in that order of importance).
	- A degree of comfort at the command line. That means a thorough understanding of basic file-system commands, as well as the ability to ssh into remote machines and troubleshoot without a GUI, grep through logs, and deploy scripts and applications.
+ skill set:
	- Exceptional SQL skills and experience working with granular web clickstream data and behavior tracking tools like SiteCatalyst
	- Fluency in data analysis, including defining KPIs, statistical and predictive modeling concepts, descriptive statistics, experimental design and multivariate A/B testing
+ skill set:
	- Hadoop, HDFS, Hive, HBase, MapReduce, and Mahout.
	- Large-scale graph algorithms, clustering, page-rank, and community detection.
	- Apache Spark, SparkSQL, MLlib, and Scala Actors.
	- Ensemble Methods, Deep Learning, and other trendy topics in the Machine Learning community.
+ skill set:
	- Extensive hands on experience with administering some of the following: HBase, Impala, Spark, EMR, Hive on Tez or Presto
	- Experience operating large scale Hadoop clusters running Cloudera distribution
	- Operational mindset with ability to do Problem, SLA and Incident Management
	- Experience installing and managing Kafka is good to have
	- Experience managing infrastructure in AWS using EMR
	- Experience with SQL and Python(Boto3 Library)
	- Experience with AWS products including EC2, S3, RDS, ElastiCache, ElasticSearch, Kinesis, Lambda, etc
	- Exposure to Big Data on AWS (DataPipeline, Batch, AWS Glue, S3, EMR/EC2)
	- Hands on expertise in AWS (S3, EMR, EC2, Hadoop, Hive, Spark, Kafka, Storm, Druid, Cassandra, Columnar Databases and Graph Databases like DSE Graph is huge plus.
+ skill set:
	- Efficient in SQL, Hive, SparkSQL, etc.
	- Serve as technical “go to” person for our core technologies – Hadoop, Spark, AWS, Vertica, Tableau, Cassandra, Graph Databases and others
	- Advanced SQL skills to perform data segmentation and aggregation from scratch; experience working with granular web clickstream data a plus!
	- Knowledge of programming languages and stats packages (e.g. python, R); comfortable running multiple regression analyses
+ Strong hands-on experience with at least one of the main stream deep learning frameworks such TensorFlow, PyTorch, BLVC Caffe, Theano
+ skill set:
	- Expert knowledge of either Python or R, strong experience with database management systems like SQL, preferably also Spark ML, Scala, Hive and Impala
	- Confidence and comfort working on projects and goals that are happening in a hypothesis driven environment (build – measure – learn mindset)
	- An excellent understanding of SQL.
	- Experience with big data technologies (Hive, Impala, Spark, etc.) would be a plus.
+ Automated testing: Karma, Protractor
+ skill set:
	- Proxmox, KVM virtualization, LXC and Docker containers
	- large scale object storage (Ceph, cloud-based object storages)
	- Puppet
	- PostgreSQL
	- Distributed architecture (RabbitMQ, Kafka)
	- Icinga/Prometheus/ELK monitoring
+ Knowledge of container (docker or others) and orchestration (K8S or others)
technology is a plus+ At least 2 years of experience using deep learning techniques (CNN, RNN, LSTM) on computer vision tasks (object detection and tracking, classification, action recognition)
+ skill set:
	- 2+ years of cloud experience using AWS (e.g., EC2, ECS, Batch, Lambda)
	- Familiarity with Continuous Integration tools (e.g., Jenkins, Travis)
+ Knowledge of distributed machine learning framework (distributedTensorFlow/MXNET) or cloud/edge federation is a plus
+ At least 2 years of experience using deep learning techniques (CNN, RNN, LSTM) on computer vision tasks (object detection and tracking, classification, action recognition)
+ skill set:
	- 2+ years of cloud experience using AWS (e.g., EC2, ECS, Batch, Lambda)
	- Familiarity with Continuous Integration tools (e.g., Jenkins, Travis)
+ skill set:
	- Technologies : AWS Batch,  Spark, Hive, EMR, Presto, Docker, Jenkins, Bitbucket
	- Databases: RDS MySQL, Redshift
	- Machine Learning: Distributed TensorFlow, Keras, PyTorch, Caffe2, scikit-learn, Apache MxNet, SageMaker
	- Developing DAOs (data access objects) and APIs
	- Extensive practical experience using a wide range of AWS technologies, including: S3, EC2s, Lambda, Step Functions, Glue, EMR, API Gateway
+ Experience with CoreAudio, Audio Unit, ASIO and VST APIs.
+ Familiarity with automated build systems such as Jenkins or buildbot.
+ Experience with distributed analytic processing technologies (Hive, Pig, Presto, Spark)
+ skill set:
	- Linux
	- Puppet
	- nginx
	- AWS
	- Datadog
	- Cloudformation
+ skill set:
	- API rest
	- Ruby on Rails
	- CDNs
	- Microservices
	- Python
	- MySQL
	- Bento4
	- FFmpeg
	- Docker
	- We are looking for students or graduates with strong knowledge of objected-oriented programming, SQL and NoSQL.
+ skill set:
	- Experience with advanced ML models and concepts: HMMs, CRFs, MRFs, deep learning, regularization etc.
	- Experience with distributed databases such as HBase, Redis, CouchBase etc.
	- Experience in search platform such as Solr, Elastic Search
+ Cross platform C++17, OpenCL, Qt/QML, git, Python 3, clang-tidy, clang-format, Jenkins, CMake, Catch2, Docker, Vagrant, KVM, C++/CLI.
+ Work with cutting edge technologies such as C++17 (anything that passes VS2017, latest Clang, GCC, clang-tidy, ...). C++/CLI, GPGPU, Python, Jenkins, docker, KVM, libclang, boost, Qt and CMake
+ skill set:
	- Java, mahout, Hadoop
	- Scala, Spark, SparkML
	- Spark with Python, numpy and pandas
+ skill set:
	- As part of the Advanced Product Development team, immediate responsibilities include:
		* Exploration and development of machine learning algorithms for spatiotemporal analysis, including multiclass classification, clustering, temporal segmentation, sequence labeling, and spatial segmentation.
		* Development of new technologies and digital products to improve surgeon and team performance on robotic surgery platforms.
		* Support clinical and academic collaborations in related fields.
	- Additional responsibilities include:
		* Contributing to multiple areas of research, including but not limited to the following:
		* Designing and applying machine learning algorithms to novel, surgical applications
		* Characterizing surgeon and team behavior and workflow to optimize new technologies
		* Fully integrating machine learning into core digital products and intelligent systems
		* Conducting user studies to evaluate digital product concepts
	- Establishing strong academic collaborations across research disciplines
	- Presenting research at international conferences and publishing research in top academic journals
	- Qualifications... Skill/Job Requirements:
		* Competency Requirements: (Competency is based on: education, training, skills and experience).
		* In order to adequately perform the responsibilities of this position the individual must have:
			+ Doctoral degree in Computer Science, Statistics, Applied Mathematics, or Neuroscience, or Master's degree with minimum (5) years industry experience developing machine learning applications
			+ Demonstrate excellent communication skills both written and verbal
			+ Interested in early research and development through to product roll-out
			+ Solid understanding of statistics, machine learning, and deep learning algorithms and techniques is required
			+ Experience with sequence modeling, image analysis, activity recognition, and/or temporal segmentation on real-world data is required
			+ Experience with Python is required
			+ Hands-on experience with deep learning frameworks such as Tensorflow, Theano, Caffe, and/or Torch is required
			+ Hands-on experience with CNNs, RNNs, and LSTMs is ideal
			+ Experience with R, SQL is ideal
			+ Experience with C/C++ is ideal
			+ Experience with clinical studies is a plus
			+ Ability to travel domestically and internationally (10%)
+ skill set:
	- Intuitive Surgical designs and manufactures state-of-the-art robot-assisted systems for use in minimally-invasive surgery. These systems are revolutionizing the way in which surgery is being done and offer a unique platform that is being used routinely at hospitals worldwide for exploring the potential of digital surgery. Joining Intuitive Surgical means joining a team dedicated to using technology to benefit patients by improving surgical efficacy and decreasing surgical invasiveness, with patient safety as our highest priority.
	- The Applied Research group within Intuitive Surgical has an immediate opening in Sunnyvale, CA for a research scientist with focus on Computer Vision, Deep Learning and Image Analytics, contributing to new technology development in the area of 3D scene understanding/reconstruction and spatial AI systems for next-generation robot-assisted surgery platforms. This role is an exciting opportunity to join a newly formed team and contribute to its growth and it will give you an opportunity to test your knowledge in a challenging problem solving environment.
	- Research, design and implement algorithms in deep learning for computer vision and image analytics
	- Contribute to research projects that develop a variety of algorithms and systems in computer vision, image and video analysis.
	- Advance the state-of-the-art in the field, including generating patents and publications
	- Develop prototypes of 3D recognition models that scale to large clinical datasets
	- Develop prototypes of dense 3D reconstruction systems based on multi-view image sensors
	- Contribute to building new clinical datasets and data pipelines
	- Participate in integration of new ML/CV algorithms into existing and future robotic platforms
	- Experiment with several users and clinical advisors to iterate prototype designs based on feedback and performance.
	- Develop new technologies and digital products to improve surgeon and team performance on robotic surgery platforms.
	- Support academic collaborations in related fields.
	- Contribute to multiple areas of research, including but not limited to the following:
		* Design and apply CV/ML algorithms to novel, surgical applications

		* Design/bring-up of novel sensing technologies

		* Characterize surgeon and team behavior and workflow to optimize new technologies
	- Establish strong academic collaborations across research disciplines
	- Doctoral degree in computer science, electrical and computer engineering, or Master's degree with minimum (5) years industry experience developing computer vision and machine learning applications
	- Strong understanding of machine learning: you should be familiar with the process (data collection, training, evaluation, and making iterative improvements) of building effective learning systems.
	- Strong hands-on experience with at least one of the main stream deep learning frameworks such TensorFlow, PyTorch, BLVC Caffe, Theano
	- Strong hands-on experience with Python (proficiency), C/C++ (proficiency), Shell Script, Matlab
	- Strong engineering practices, debugging/profiling skills, familiarity with multi- threaded programming.
	- Train machine learning and deep learning models on a computing cluster to perform visual recognition tasks, such as segmentation and detection
	- Hands-on experience with GPU accelerated algorithms and implementations
	- Hands-on experience with state-of-the-art models based on CNNs, RNNs, and LSTMs
	- Excellent communication skills both written and verbal
	- Interested in early phases of product exploration and iteration based on incomplete requirements.
	- Solid understanding of computer vision, machine learning, and deep learning algorithms and techniques is required
	- Experience with visualization tools is a plus
	- Self-starter and able to work in a collaborative and results-oriented environment
	- Ability to travel domestically and internationally (5-15%)
	- Able to view live and recorded surgical procedures
+ Experience with CUDA, VTK/ITK, and/or physics based simulation
+ skill set:
	- Experience developing virtual world environment for games, such as Lumberyard, Unity3d, Unreal, CryEngine and/or other world simulation environments
	- Experience with graphics APIs and frameworks such as OpenGL, DirectX, or Vulkan
	- Experience with physics engines (e.g. Bullet, Havok, PhysX)
	- Experience developing agent behaviors, physics, gameplay, tools, or GUIs
+ skill set:
	- Google Dialogflow
	- The Visual Fusion Engine, VFE
	- algolia - Search Made Powerful
	- Cruzr - Humanoid service robot
	- Descartes Labs
	- Blue River Technology - Smart Agricultural Machines
	- NLPBOTS - Intelligent Chat-bots
	- BrainShop - AI for developers
	- Flyr
	- Sisense
	- Mookkie
	- NanoNets
	- Workfusion - Rpa Express
	- MSG.AI
	- Keepers - Advanced Child Monitoring
	- Neura - User Awareness with AI
+ Distributed Deep Learning
+ Automate and integrate security into CI/CD pipelines, such as static code analysis and dynamic code analysis.
+ Enjoys working and deploying technologies such as Chef, AWS, Ruby, Rails, MySql, and Redis
+ Docker, Heroku, Kubernetes
+ Experience with monitoring (NewRelic, Prometheus, PagerDuty)
+ Authentication: CAS (Java)
+ skill set:
	- Experience in at least one of the following sequencing methodologies: cell-free DNA sequencing, methylation sequencing, single cell sequencing
	- Deep understanding of next generation sequencing methods, platform-specific bias and errors, and data interpretation
	- Hands-on experience with large-scale genomic data (e.g. whole genome sequencing, exome-seq, target enrichment, amplicon sequencing, RNA-seq, etc.)Hands-on experience with genome alignment, mapping, variant calling, and annotation tools
	- Familiarity with human and mammalian genomics, standard genomic databases (UCSC, Ensembl, NCBI), formats, and tools.
	- Proficiency in python, ruby, Perl, or another high-level scripting language (Python highly preferred)
	- Familiarity with UNIX-based operating systems and shell scripting
	- Excellent data analysis and visualization skills (Tableau, R, matplotlib, or similar)
	- Excellent understanding of molecular biology and cell biology
	- Experience with Seven Bridges, DNA Nexus or similar platform
+ Experience with applied ontology development (RDF(S)/OWL, SPARQL, the Semantic Web or Frame based KR systems).
+ Good understanding of high-throughput single cell assays such as single cell transcriptomics, single-cell epigenomics, FACS, and CyTOF.
+ Experience with relational (e.g. postgres, SQL) and/or distributed (e.g. MongoDB) databases
+ Experience with RNA-seq, ATAC-seq and/or ChIP-seq experiments and data at the single cell level.
+ skill set:
	- Developing scalable bioinformatics algorithms, pipelines and tools to solve complex, distributed computing challenges
	- Providing statistics, scientific computing and data analysis support to research, product development and manufacturing operations
	- BS in bioinformatics or related field with 6-8 years industry experience or MS/PhD in bioinformatics or related field with 4-6 years industry experience
	- Advanced proficiency in Python, R or Rust in a Linux environment
	- Broad experience with NGS data analysis, manipulation and presentation (in Python or R)
	- Excellent data analysis and visualization skills (in Python, R and using tools like Tableau)
	- Excellent understanding of molecular biology, with an emphasis on DNA chemistry preferred
	- Proven ability to synthesize and present conclusions from complex analyses in a clear and visually compelling way
	- Familiarity with common tools and file formats for genome-scale interval data manipulation and analysis (e.g. bedtools, bedops, etc.)
	- Formal software development experience, the software development lifecycle, unit and functional testing (via py.test) and version control via Git
	- Familiarity with database (PostgreSQL, NoSQL and Redshift) design, implementation and efficient query construction
	- Experience building and using Docker containers
	- Familiarity with cloud-based computing environments, especially Amazon Web Services
	- Experience using workflow management tools (e.g. Airflow, Galaxy, Luigi)
	- Familiarity with web application development including building REST-ful interfaces
	- Familiarity with DNA analysis software (MacVector, VectorNTI, SnapGene)
+ skill set:
	- M.S. or Ph.D. degree in Genetics, Biology, Bioinformatics, Biostatistics, Computational Biology, Computer Science, or related field
	- Knowledge and experience in the field of cancer or rare disease genomics.
	- Experience in at least one of the following sequencing methodologies: cell-free DNA sequencing, methylation sequencing, single cell sequencing
	- Deep understanding of next generation sequencing methods, platform-specific bias and errors, and data interpretation
	- Hands-on experience with large-scale genomic data (e.g. whole genome sequencing, exome-seq, target enrichment, amplicon sequencing, RNA-seq, etc.)
	- Hands-on experience with genome alignment, mapping, variant calling, and annotation tools
	- Familiarity with human and mammalian genomics, standard genomic databases (UCSC, Ensembl, NCBI), formats, and tools.
	- Proficiency in python, ruby, Perl, or another high-level scripting language (Python highly preferred)
	- Familiarity with UNIX-based operating systems and shell scripting
	- Excellent data analysis and visualization skills (Tableau, R, matplotlib, or similar)
	- Excellent understanding of molecular biology and cell biology
	- Strong interpersonal communication skills
	- Excellent publication track record
	- Additional desired qualities include:
		* Familiarity with version control (git, subversion)
		* Experience with target enrichment
		* Experience in clinical laboratory testing
		* Experience with Seven Bridges, DNA Nexus or similar platform
+ skill set:
	- Design and architect the backend for our computer aided genetic circuit pipeline, including the genetic compiler and simulation engine
	- Develop our cloud infrastructure, data warehouse, build and deploy system, and machine learning platform. You will drive discussion and decisions on microservices vs monoliths, managed services vs deployed, etc.
	- Work on tooling to help improve the efficiencies of our synthetic biologists including data analysis platforms and robotic automation
	- solid at communicating architectures internally through clear design documents
	- embracing ambiguity and driving for impact
	- excited to partner closely with and learn from our synthetic biology team
	- interested in helping define the company product, direction and culture
	- You are a highly skilled technical lead in software engineer with years of experience in industry. You are passionate about joining an early stage startup where autonomy, passion to learn and excitement to engineer biology take precedence over process and ego. If you have a background in genetics or cellular biology, great! If not, you have strong experience with ETL systems, data storage and access, cloud infrastructures, build and deploy systems with a passion to learn the science.
+ skill set:
	- Architect the overall automation software, hardware, wetware ecosystem including hardware configurations, experimental protocols, and software control and scheduling systems.
	- Mentor other automation engineers.
	- Design, create, and deploy software to schedule, control, and manage the automation system.
	- Design, configure, and assemble a state-of-the-art automation system for biological engineering.
	- Work with synthetic biologists to translate manual protocols into automated processes and validate them at high throughput.
	- Work with hardware engineers to develop custom automation hardware to physically perform synthetic biology's experimental procedures.
	- Work with software engineers to develop custom software tools to schedule, control, and manage the automation system.
	- Develop metrics to measure and track the success of the automation platform.
	- Partner with automation vendors to vet software platforms and work to integrate them into our larger pipeline though the development of new APIs and methods.
	- Partner with automation vendors to obtain new hardware, develop new prototype hardware elements, build interfaces, and integrate hardware into the automation platform.
	- Embrace ambiguity and drive for impact.
	- Contribute to the company’s product, direction, and culture.
	- B.S. or higher degree in Bioengineering, Computer Science or a related field. PhD preferred.
	- 5+ years direct experience in biotechnology industry. 2+ years directly with automation.
	- Strong coding skills in modern software development environments. GitHub (or similar) portfolio of work ideal.
	- Publication or patent record related to biotechnology.
	- Strong written and oral communication skills.
	- Ability to physically relocate to Cambridge, Massachusetts.
	- You are a highly skilled programmer with years of experience in industry or research. You want to work on software development projects with strong algorithmic and research foundations. You are highly skilled technical lead in laboratory automation with years of experience in industry or research. You are passionate about joining an early stage startup where autonomy, passion to learn, and excitement to engineer biology take precedence over process and ego. You ideally have some laboratory automation and biology wetlab experience. You are interested in learning more about how to integrate hardware, software, and wetware.
+ skill set:
	- Design, configure, and assemble a state-of-the-art automation system for biological engineering.
	- Work with synthetic biologists to translate manual protocols into automated processes and validate them at high throughput.
	- Work with software engineers to develop custom software tools to schedule, control, and manage the automation system.
	- Develop metrics to measure and track the success of the automation platform.
	- Partner with automation vendors to obtain new hardware, develop new prototype hardware elements, build interfaces, and integrate hardware into the automation platform.
	- Embrace ambiguity and drive for impact.
	- Contribute to the company’s product, direction, and culture.
	- You are a highly skilled technical lead in laboratory automation with years of experience in industry or research. You are passionate about joining an early stage startup where autonomy, passion to learn, and excitement to engineer biology take precedence over process and ego. You ideally have some software programming and biology wetlab experience. You are interested in learning more about how to integrate hardware, software, and wetware.
+ Working knowledge of industry leading configuration management tools and methods (Salt, Ansible, Chef, Puppet, etc)
+ Ideal candidate would have experience with metabolomic datasets and familiarity with analytical chemistry/assay methods, automation systems, and LIMs
+ Good understanding of protocols like AXI, ACE, ACP, CHI etc.
+ Experience with SQL and Statistical/mathematical programming software packages (R, SPSS, CPLEX, LONDO or Xpress etc)
+ skill set:
	- Knowledge or hands-on experience in Container technologies such as Docker is a plus.
	- Knowledge of Virtual machines, Hypervisors is a plus
+ At least one graphics API (OpenGL, Direct 3D, Vulkan)
+ Either in AI tools; or autonomous embedded area; or FPGA
+ Seeking motivated graduate interns in the intersection of computer vision, 3D graphics and machine learning with applications to interactive visual effects processing. In this position, you will collaborate with VFX artists and fellow researchers in NEXT team to invent algorithmic solutions to VFX challenges. This is a full-time position located in Hillsboro, Oregon.
+ Programming experience in Python and MATLAB. Experience with LabView, VPItransmissionMaker, Tensorflow is a plus.
+ You find the 10% work that gets us 90% of the value
+ skill set:
	- Experience with large scale messaging systems like Kafka or RabbitMQ or commercial systems.
	- Experience with working with and operating workflow or orchestration frameworks, including open source tools like Airflow and Luigi or commercial enterprise tools.
	- Experience with pipelines that are used by many downstream teams, including non-engineering functions.
	- Experience with streaming data frameworks like spark streaming, kafka streaming, Flink and similar tools a plus.
	- Experience working with Apache Spark and data warehousing products.
	- Direct experience with a log collection and aggregation system at scale.
	- Demonstrated execution at a growth stage technology company.
+ skill set:
	- Experience with distributed data processing systems like Spark and Hadoop
	- Familiarity with interactive data visualization using tools like D3.js
+ skill set:
	- Design new and extend existing components of MLflow, such as experiment tracking, project management, and model deployment
	- Implement proprietary integrations of MLflow into the core Databricks product
	- Has designed and developed APIs used in production systems.
	- Deployed production web services using container and orchestration technologies, such as Docker and Kubernetes to public or private clouds.
	- Developed services leveraging SQL backend stores.
	- Demonstrates customer obsession: has altered designs for frontend or APIs with the user experience in mind
	- Developed and debugged software running on Linux OS
	- Experience with Continuous Integration/Continuous Deployment frameworks.
	- [Preferred] Experience working on a SaaS platform or with Service Oriented Architectures
	- [Preferred] Experience with software security and systems that handle sensitive data
+ Experience with: Large scale distributed computing, Database internals, Big Data engines e.g. Spark, Hadoop
+ skill set:
	- Passion for process automation
	- Build system experience like Maven, Bazel, or Gradle
	- Continuous integration and testing experience like Jenkins
	- [Preferred] Kubernetes and Docker
	- [Preferred] Experience on working with services provided by AWS, Azure, or GCP
+ Strong familiarity with server-side web technologies (eg: Nodejs, Java, Python, Scala)
+ Experience with our web stack (React, Redux, TypeScript, protobuf, Apollo, GraphQL) and Spark
+ skill set:
	- Passionate about developer experience: you want tools to be fast, CLIs intuitive, giving your colleagues (and yourself) the best experience possible doing development at Databricks.
	- Passionate about automation: automated workflows, automated testing, automated deployments, automated monitoring, our job is to automate away any tedious work out of our own lives and that of our fellow engineers
	- Comfortable in a heterogeneous environment and able to quickly learn new technologies. The team deals with a variety of environments from Kubernetes services to Jenkins automation, Scala libraries to Python scripting, writing graph algorithms to debugging 3rd-party Javascript, Dev-Tools does it all.
	- Able to quickly learn their way around unfamiliar codebases: Dev-Tools routinely dives into unfamiliar third-party projects (in unfamiliar languages!), pushing them far beyond what they say they can do “on the box”
	- Experience with Continuous Integration/Continuous Deployment frameworks
	- Experience with monitoring frameworks for large systems
	- Experience with cloud APIs (e.g., a public cloud such as AWS, Azure, GCP or an advanced private cloud such as Google, Facebook)
+ skill set:
	- Develop and extend the Databricks platform. This implies, among others, writing clean, efficient code in Scala or Python and/or interacting with: cloud APIs (e.g., compute APIs, cloud formation, Terraform), with open source and third party APIs and software (e.g., Kubernetes) and with different Databricks services
	- Experience architecting, developing, deploying and operating large scale distributed systems at scale
	- Experience with cloud APIs (e.g., a public cloud such as AWS, Azure, GCP or an advanced private cloud such as Google, Facebook)
	- Experience working on a SaaS platform or with Service Oriented Architectures
	- Experience with Continuous Integration/Continuous Deployment frameworks
	- Experience with Docker and Kubernetes
+ skill set:
	- 2+ years experience with R or Python
	- 2+ years experience with predictive modeling
	- Familiarity with data visualization in R or Javascript
	- Understanding of relational data or SQL
	- French is not required and all European languages are appreciated
	- Experience with PySpark, SparkR or Scala
	- Experience developing WebApps
	- Experience building APIs
	- Experience with HDFS and NoSQL databases (MongoDB, Cassandra, etc)
	- Construct end-to-end data flows from raw data to predictions
	- Crunch, analyze and investigate any kind of data
	- Explore new machine learning algorithms
	- Build attractive visualizations
	- Communicate results to non-technical colleagues and clients
	- Provide data science expertise to sales, marketing, and R&D teams
+ skill set:
	- DSS is an on-premises application that connects together all big data technologies. We work with SQL databases, MongoDB, Cassandra, ElasticSearch, Hadoop, Spark, MLLib, scikit-learn, Shiny, … and many more. Basically, our technological stack is made of all technologies of the big data and machine learning landscape.
	- Our backend is mainly written in Java but also includes large chunks in Scala, Python and R. Our frontend is based on AngularJS and also makes vast usage of d3.js
	- One of the most unique characteristics of DSS is the breadth of its scope and the fact that it caters both to data analysts (with visual analytics) and data scientists (with deep integration in code and libraries, and a web-based IDE).
	- You are the ideal recruit if:
		* You are a full stack engineer. You know that low-level Java code and slick web applications in Javascript are two sides of the same coin and are eager to use both.
		* You know that ACID is not a chemistry term.
		* A first experience (either professional or personal) building a real product would be a big plus. Experience with some technologies of the Big Data and analytics stack (distributed databases, large-scale data processing, statistics, machine learning, JS visualizations, ...) is also desirable.
+ You are curious and pragmatic: you want to explore extensions to our product but are motivated by delivering production code for business use cases
+ skill set:
	- 2-4 years of experience in C/C++ development
	- Object oriented programming experience
	- Experience with applications design and implementation
	- Experience in multi-threaded programming
	- Proven track record of finding bottlenecks and delivering optimized, high-quality code
	- Knowledge in algorithms development and implementation
	- Fast learner, team player, reliable, motivated, hard worker
	- Experience in Android NDK development
	- Experience in image processing algorithms
	- Experience in runtime optimizations on embedded accelerators (e.g. Neon, DSP, GPU).
	- Experience in writing OpenCL kernels
	- Experience in Matlab
+ Open64 is a free, open-source, optimizing compiler for the Itanium and x86-64 microprocessor architectures.
+ Skill set:
	- Psyco, Nukita, Shed skin.
+ skill set:
	- Elastic Search, Lucene, SQL Server, Kibana, or similar experience
	- Prior experience aligning platform architecture with security, data
	- Demonstrated ability to document architectural standards and decisions
	- SaaS or high scale cloud experience
+ skill set:
	- Databases / Data warehousing
	- Writing complex SQL
	- Strong Microsoft Excel skills
	- Experience with Big Data platforms such as Hadoop
	- Experience with other reporting/visualization tools such as Tableau
	- Experience with monitoring and tracking tools such as  Splunk, NewRelic, Adobe/Google Analytics
+ skill set:
	- Experience with relational databases (MySQL, DB2 or Oracle) and NoSQL databases (Redis, Cassandra or DynamoDB)
	- Experience writing crisp, clean REST APIs
	- Experience with RSpec or equivalent integration test framework
	- Self-motivated individual who proactively identifies team bottlenecks and works with the team to resolve them
+ skill set:
	- Experience with data streaming technologies (Kinesis, Storm, Kafka, Spark Streaming) and real time analytics
	- Working experience and detailed knowledge in Java, JavaScript, or Python
	- Knowledge of ETL, Map Reduce and pipeline tools (Glue, EMR, Spark)
	- Experience with large or partitioned relational databases (Aurora, MySQL, DB2)
	- Experience with NoSQL databases (DynamoDB, Cassandra)
	- Agile development (Scrum) experience
	- Other preferred experience includes working with DevOps practices, SaaS, IaaS, code management (CodeCommit, git), deployment tools (CodeBuild, CodeDeploy, Jenkins, Shell scripting), and Continuous Delivery
	- Primary AWS development skills include S3, IAM, Lambda, RDS, Kinesis, APIGateway, Redshift, EMR, Glue, and CloudFormation
+ skill set:
	- Experience with Backbone, Marionette or equivalent framework
	- Experience with Protractor, RSpec or equivalent integration test framework
+ skill set:
	- Experience with system level monitoring tools such as Nagios or Zabbix and application performance monitoring tools such as NewRelic, AppDynamics or Dynatrace.
	- Understand configuration management tools such as Puppet, Chef or Ansible.
	- Strong understanding of the DevOps landscape from orchestration to instrumentation , from VCS to CI tools, and from APM to monitoring tools
+ skill set:
	- Working experience with AWS services (Aurora DB, Dynamo DB, Athena, EMR, Redshift, Data Catalog etc)
	- Experience with log analysis tools like Splunk
	- Experience with Issue trackers tools like Jira etc
+ You approach problems with a scrappy, creative, and entrepreneurial mindset.
+ You are comfortable with Big Data technologies like Hadoop, Spark, Hive, Presto etc.
+ Familiar with the operation of instrument -- VSG, VSA, Signal analyzer, channel emulator.
+ skill set:
	- LLVM compiler internals.
	- Polyhedral models.
	- Familiarity with HPC kernels and their optimization.
+ skill set:
	- Experience working with modern deep learning software architecture and frameworks including: Tensorflow, Pytorch, ONNX, MxNet, Caffe/Caffe2, and/or Torch;
	- Experience working with modern deep learning models including: Resnet, Mask-RCNN, RNN/LSMT, Bert, Transformer etc
+ Help the current effort of the AI research community, and contribute to cutting edge research in machine intelligence, starting from areas including Deep Learning, Generative Models, Reinforcement Learning, Evolutionary Computing, Sequence Modelling, Large-Scale Distributed Optimization and Low-Precision Numerical Formats.
+ Working on the IPU architecture compiler. Understanding code generation & optimization of C / C++ code to the instruction set of the machine. The architecture compiler and its ability to target the IPU for maximum performance and flexibility, is a fundamental component of the Poplar framework.
+ skill set:
	- Candidates should have a solid background with standard networking protocols (TCP, RPC, UDP, IPSec), low-latency protocols (RDMA, RMA) and Clustering.
	- Preferably, you should also have a background or interest in host device and network virtualisation (SR-IOV, Xen, Containers)
+ The role involves using a range of technologies, such as Python, CMake, BuildBot, Phabricator, AWS etc.
+ skill set:
	- Knowledge of storage systems (File, Block) is a plus (Local/Network/Cloud Attached)
	- Knowledge of ILOM, BMC, and OCP (Open Compute) is a plus
	- Good knowledge of common development tools such as yocto/git/gtest
+ Experience working with PCIe form-factor accelerators such as GPUs, DSPs or FPGAs
+ skill set:
	- SGE or other DRMS
	- XML and XPath/XSLT
+ skill set for DevOps:
	- Remote hardware administration with IPMI
	- Configuration and management of
		* SGE/Univa, Slurm, LSF or other DRMS
		* Jenkins CI
		* Phabricator
		* FlexLM licensing
	- Puppet, Ansible, Nagios
	- LLVM, GCC
	- DVCS e.g. Git
	- AWS, Azure, Google Cloud
	- XML and XPath/XSLT
	- Web programming – HTML/DOM, JavaScript, SQL
+ skill set:
	- Hardware-In-the-Loop (HIL) Systems
	- Development of test automation projects
	- Modeling of physical systems for HIL simulation
	- Specialized support of HIL systems and models
	- Development, testing, or familiarity of embedded control systems (mechatronics, automotive control systems)
	- HIL simulation systems
	- In-vehicle communication networks such as CAN, LIN, FlexRay
	- MIL/model-in-the-loop, SIL/software-in-the-loop, PIL/plant-in-the-loop, and HIL/hardware-in-the-loop
	- The implementation of software is done in project-specific technologies and thus extends over a wide area, including C/C++, C # (including WPF, WCF), Python, MATLAB ®, VHDL.
+ skill set for HPC Infrastructure Engineer:
	- Management of an on-premise computing cluster in a High Performance Computing (HPC) setting
	- Develop usage policies for deep learning training
	- Develop tools and infrastructure to scale deep learning
	- Maintain network infrastructure for local and cloud compute
	- Data management and backups
	- Familiarity with environments including LDAP, NFS, bare metal GPU servers, deployments and automation / conﬁguration management, modular user shell environments, networking
	- Hands on server hardware configuration experience
	- Experience with cluster management software
	- Comfortable with GPU servers
	- Strong knowledge of Linux systems and internals (Debian preferred) with a good understanding of networking and related protocols, OS customization, and package management (APT)
	- Hands on Infiniband experience
	- Have used or developed metrics/analytics tools for usage
	- Experience with Slurm or similar job systems
+ skill set for Deep Learning Research Scientist at DeepScale:
	- DeepScale was founded by the deep learning researchers from UC Berkeley who created SqueezeNet. DeepScale is developing perception systems that enable automated vehicles to interpret their environment in real-time using low-cost hardware.
	- A PhD in electrical engineering, computer engineering, or computer science.
	- A track record of advancing the state-of-the-art in an application of deep learning (ideally a computer vision or imaging application … but if you did speech-recognition or text-analysis, that's pretty good too)
	- Published papers that either (a) are in top peer-reviewed conferences such as CVPR, NIPS, ECCV, ICCV, or ICML … or … (b) a significant (>100) number of citations on one of your deep learning research publications
	- The ability to design, implement, train and test models in one or more of the leading deep learning frameworks like PyTorch or TensorFlow.
+ skill set:
	- Machine learning areas of special interests include: CNNs, RNNs, distributed GPU computing, detection, prediction, motion planning, mapping and localization
	- Work with lidar sensor firmware and low level signal processing
	- Perform Multi-Object Tracking & Multi-Sensor Fusion
	- Sensor calibration & Perception algorithms (all types and flavors)
+ skill set:
	- Familiar with the basics of lidars, radars, cameras, and ultrasonic systems.
	- Are familiar with Physics-based modeling and simulation of sensor systems (eg, link budget analysis, wave propagation, sensor noise sources, etc.).
	- At least 1 year of experience in radar, lidar, or camera modeling and/or evaluation.
	- Familiarity with test and calibration processes for autonomous vehicle sensors.
	- Familiarity with EVT, DVT, and PVT processes for sensor bring-up and validation as well as FMEA principles.
+ Working experience with large-scale data platform and pipelines such as Hadoop, Hive, Pig, MapReduce, Spark, Kafka, Flumes, etc.
+ Familiarity with GPU computing (CUDA, OpenCL) is preferred
+ Familiarity with modern planning approaches including randomized search methods and trajectory optimization
+ Solid work experiences with state-of-the-art mapping and localization algorithms
+ Experience with scheduling engines such as Airflow
+ Published papers (e.g. in Supercomputing, IPDPS, or PPOPP) and/or open-source code that demonstrate your skills in writing fast code.
















#	Bio Design Automation & Bio Manufacturing Automation Companies

bio manufacturing automation

+ [addgene](https://www.addgene.org/careers/)
+ [Amyris](https://amyris.com/careers/)
+ [Analytikjena](https://www.analytik-jena.com/company/careers/)
+ [Asimov, Inc.](https://www.asimov.io/)
+ BioFab:
	- http://www.uwbiofab.org/
	- http://erc-assoc.org/achievements/biofab-world%E2%80%99s-first-biological-design-build-facility-synthetic-biology
	- Not http://biofabproducts.com/about/
+ [Biolegio B.V.](https://www.biolegio.com/)
+ [BioSero](https://www.biosero.com/about-us/)
+ Boston University:
	- CIDAR Lab
	- Biological Design Center, BDC
+ BP
+ [De Novo DNA](http://www.denovodna.com/)
+ [DSM](https://www.dsm.com/corporate/home.html)
+ GE Healthcare
+ [genomatica](https://www.genomatica.com/careers/)
+ Genome Foundry
	- https://www.genomefoundry.org/aboutus
	- https://www.concordia.ca/research/genome-foundry.html
+ [Ginkgo Bioworks](https://www.ginkgobioworks.com/about/)
+ [Hamilton Robotics](https://www.hamiltoncompany.com/)
+ [HighRes biosolutions](https://highresbio.com/careers/)
+ [Integrated DNA Technologies](https://www.idtdna.com/pages)
+ [Labcyte](https://www.labcyte.com/)
+ Leselagen
+ [lifefoundry](http://www.life-foundry.com/careers.html)
+ Lincoln DNA Foundry
+ [Molecular Devices](https://www.moleculardevices.com/about-us#gref)
+ [New England BioLabs](https://www.neb.com/about-neb/careers)
+ [Novozymes](https://www.novozymes.com/en)
+ [opentrons](https://opentrons.com/jobs)
+ [OriCiro Genomics Inc.](https://www.oriciro.com/)
+ Ozen
+[Ranomics Incorporated](https://www.ranomics.com/careers)
+ [SGIDNA, a Synthetic Genomics, Inc. company](https://www.sgidna.com/careers/)
+ [Synbicite](http://www.synbicite.com/about-us/)
+ [Synbiobeta](https://synbiobeta.com/job-board/)
+ [Synlogic](https://www.synlogictx.com/our-people/join-us/)
+ [TeselaGen Biotechnology Inc.](https://teselagen.com/)
+ [ThermoFisher Scientific](http://jobs.thermofisher.com/)
+ [Zymergen](https://www.zymergen.com/careers/)
















##	Events to look for job opportunities in BDA

+ Annual Biomedical Research Conference for Minority Students, ABRCMS
+ Fungal Genetics Conference
+ Programming Biology Night (Seattle)
+ SACNAS -  The National Diversity in STEM Conference
+ Scientista Symposium
+ WomenHack Boston
+ WomenHack Seattle


##	Other Resources

+ [BioLEGO](http://www.cs.technion.ac.il/~edwardv/BioLego/html/BioLego.html)

















###	Skill Sets for Research Internships with Alibaba Group

+ Quantum Algorithm for Near-term Quantum Devices
	- A general-purpose fault-tolerant quantum computer will require millions of physical qubits and millions of quantum gate operations. With quantum computers of significant size now on the horizon, we should understand how to best exploit the initially limited abilities and how to develop and run useful quantum algorithms within the limited circuit depth of intermediate size quantum devices with limited error correction.
+ Research in Practical Applications of Quantum-Safe Communication
	- Quantum communication may refer to quantum cryptography, quantum teleportation, and quantum entanglement. Among those, quantum key distribution (QKD) is one of the most practical applications in recent years. Quantum cryptography takes the advantage of the laws of quantum physics to protect data,
	- Currently, the most significant problems in practical quantum cryptography systems include: high-speed quantum random number generation, long-distance fiber quantum key distribution with high key generation speed, co-fiber transmission of classical and quantum optical signals, as well as practical commercialization and stabilization.
	- Our project aims to study these critical issues in quantum cryptography system for practical applications. Due to the transmission loss and dark count, the bottleneck for its practical application lies in the trade-off between high speed key generation rate and long transmission distance. In order to solve these problems, one potential solution is to design more efficient telecommunication protocol to exceed the theoretical up bound of the generation rate. Meanwhile, the project will also focus on the study and practical solutions for quantum random number generation, post-quantum cryptography algorithm, the migration of classical and quantum networks, etc
+ Building an innovative and systematic AI benchmarks platform
	- Currently in Alibaba Group, deep learning and related applications have been employed in various business departments. Tmall, Alitrip, Taobao, Ant Financial and other departments are making extensive use of emerging deep learning technologies to continuously improve application and algorithms and enhance the consumer experience. On the one hand, Alibaba's engineering teams design, experiment and deploy different deep learning algorithms and applications every day. On the other hand, deep learning requires a lot of computational power, which also puts higher requirements on the computational power of the hardware and their adaptability to the application. How to balance the demand and supply relationship between these two and integrate the solution into a systematic platform product? How to automatically and systematically evaluate the computional power of an AI hardware? How to evaluate the advantages and disadvantages of a hardware for usage in an application and give customer recommendations through a systematic platform? These are the challenges we are currently dealing with and we need to solve. Recently we have launched the AI ​​Matrix product (through aimatrix.ai website), but it is still in the early stage of the product. In the future, we need more people who have the same understanding as us and are willing to involve in solving these problems. Let's contribute our own strength and make the AI ​​Matrix as an effective systematic platform and an impactful technical brand.
	- [AI Matrix](https://aimatrix.ai/en-us/)
	- https://github.com/alibaba/ai-matrix
+ Using HW/SW Mechanisms to Improve Performance of remote Heterogeneous Systems
	- Alibaba is an e-commerce and AI company. We generate enormous data and consume huge amount of computation and storage resources every day. It is critical for Alibaba to keep on improving data center design given the emerging of powerful accelerator computation clusters.
	- We would focus on:
		* 1. Analyze different AI workloads in distributed GPU clusters, study their computation and network requirement
		* 2. Based on current remote accelerator technique, improve its efficiency via hardware/software solutions
		* 3. Apply the technique to real workload
	- Requirement:
		* 1. PHD candidate, experienced with distributed heterogeneous systems
		* 2. It's a plus if candidate worked with deep learning algorithms
		* 3. it's a plus if candidate has top conference publications
+ Last mile of datacenter as a computer -- local protocol and semantics based ASIC/FPGA cloud
	- Developers and customers prefer to use heterogeneous compute resources with a set of local server access protocol and semantics. We need to find talents to do research and prototyping with a specific local API on an ASIC or FPGA chip.
+ Emerging Accelerator Architecture, Programming Model, and Optimizations
	- The emerging hardware accelerator architectures, such as process-in-memory (PIM) and neuromorphic computing,  have shown great potential to speed up AI/ML and data-heavy applications. This research aims to investigate these non-traditional architecture designs and their performance implications for domain-specific applications in Alibaba datacenters and ecosystem. It will study the emerging architecture’s programming model for usability and explore the software-hardware co-design strategies (e.g. reinforcement learning based architecture space exploration, architecture-aware compression and sparsity exploitation) and optimization trade-offs to maximize the performance.
+ Execution engine optimization based on GPUs and other modern hardware
	- Targeting Maxcompute SQL engine, we'd like to import modern hardware technology (such as GPU, FPGA etc) to model and improve the core operators of the distributed execution engine, optimize the system performance on specific scenes at last.
+ Performance/Power/Area (PPA) Modeling & Analysis
	- The ***Computing Technology Lab of Alibaba Damo Academy*** focuses on advanced research topics in computing, memory/storage, and interconnect technologies that can revolutionize today's computing systems with holistic innovations ranging from system architectures to VLSI designs, to enable new computing capabilities for improving energy efficiency and performance across multiple application domains, including both high-performance and embedded computing.
+ Research on Domain Specific Architecture
	- As the end of Dennard's scaling and Moore's Law running out of steam, the traditional architecture for general-purpose processors can no longer meet the requirements of high performance and low energy consumption for various emerging applications. To allow the computing to have higher performance/energy efficiency, Domain Specific Architecture (DSA) has become a popular solution. However, there are many challenges in the DSA design. For example, the definition of the scope of Domain, trade-off between specialization and general-purpose, instruction set design, compiler design and optimization, memory wall, ultra-low-power design, micro-structure design and optimization, etc. This internship Project is a thorough and detailed study of the DSA to address these challenges.
	- The Computing Technology Lab focuses on advanced research topics in computing, memory/storage, and interconnect technologies that can revolutionize today's computing systems with holistic innovations ranging from system architectures to VLSI designs, to enable new computing capabilities for improving energy efficiency and performance across multiple application domains, including both high-performance and embedded computing.
+ Research on Cloud Server Architecture
	- Perform profiling/modeling and evaluation of workloads for our cloud server, design and optimize server architecture including but not limited to: CPU, cache/memory, storage and accelerators.
+ Research on algorithms/architectures of the next-generation AliNPU for training
	- AliNPU targeting for neural network training is a key component of Alibaba’s AI Chip strategy. To design an architecture surpassing the best of the AI training chips, such as GPU and TPU, we must look into all aspects from algorithms to HW architecture, for the potential computational efficiency improvements.
	- The works may focus on one or a few of the following directions：
		* 1. Algorithm innovations that may improve the system efficiency, and the experiments.
		* 2. The analysis of the theoretic bounds and/or the proof with regards to the algorithm innovations.
		* 3. Experimental HW architecture designs, simulations and their PPA analysis.
+ Hyper-scale cloud datacenter's compute resource pool and management platform prototype
	- Compute pools will be widely deployed in hyper-scale cloud datacenter. Alibaba Infrastructure AI Ops Platform (TIANJI) team is now actively seeking talents to work on research in this area.
+ Research on optimization of AI accelerator
	- Nowadays high performance computing has become one of the hot topics of AI research. The research aims on optimizing power dissipation and energy efficiency of AI accelerators targeting various of AI applications, providing high quality computation support for AI applications.
	- The research topics include:
		* 1. Research on computation pattern of various AI applications to look for bottleneck
		* 2. Research on AI accelerator architectures, implementations to improve performance and energy efficiency
		* 3. Codesign AI accelerator (SW/HW) and application to maximize the performance of accelerator)
+ Accelerating Machine Learning Applications on Heterogeneous Computing Architectures
	- This research aims to optimize ML applications on heterogeneous accelerators such as GPUs, FPGAs, and/or ASICs. S/he will conduct analysis and exploration on various performance bottlenecks in the full software/hardware stack, including ML algorithm improvement, model level transformation (e.g. compression, sparsity, data parallelization), and domain-specific architecture innovations, in order to dramatically boost the ML application's performance.










###	Other Information From Job Descriptions

Funny lines in job descriptions:
+ ["Frequently caught reading and engaging too much in AI/ML banter"](https://jobs.lever.co/sigopt/b172f247-6185-43e3-bc18-4a79f243122a), last viewed May 7, 2019. Jobs with SigOpt







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

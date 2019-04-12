#	Operation Go2ICCAD

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
	- skill set:
		* Understand data landscape i.e tooling, tech stack, source systems etc. and work closely with the data Engineering team to improve the data collection and quality.
		* Ability to define and spot macro and micro levels trends with statistical significance on a regular basis and understand key drivers driving those trends.
		* 8+ years of data analyst experience with 4+ years of proven industry experience in a large scale environment(PBs scale, globally distributed teams).
		* Strong experience in Python, R, SQL, Tableau, Google Analytics, Hive and BigQuery (or any other Big data/Cloud equivalent) etc.
	- skill set:
		* Build and Support scalable and reliable data solutions that can enable self-service reporting and advanced analytics at Cloudflare using modern data lake and EDW technologies (Hadoop, Spark, Cloud, NoSQL etc.) in a agile manner.
		* 3+ years of development experience in Big data space working with Petabytes of data and building large scale data solutions.
		* Solid understanding of Google Cloud Platform, Hadoop, Python, Spark, Hive, and Kafka.
		* Experience in all aspects of data systems(both Big data and traditional) including data schema design, ETL, aggregation strategy, and performance optimization.
		* Capable of working closely with business and product teams to ensure data solutions are aligned with business initiatives and are of high quality.
	- skill set:
		* Partner and align with business leaders, stakeholders, product managers and internal teams to understand the business and product challenges and goals and address them using predictive analytics in a globally distributed environment.
		* Understand data landscape i.e tooling, tech stack, source systems etc. and work closely with the data Engineering team to improve the data collection and quality.
		* Understand business/product strategy and high-level roadmap and align analysis efforts to enable them with data insights and help achieve their strategic goals.
		* Strong audience focused presentation and storytelling skills focused on key takeaways in a crisp and concise manner.
		* Define hypothesis driven models and best practices to derive and publish model scores/insights/learnings at scale within the company.
		* Ability to define and spot macro and micro levels trends with statistical significance on a regular basis and understand key drivers driving those trends.
		* 8+ years of data scientist experience with 4+ years of proven industry experience in a large scale environment(PBs scale, globally distributed teams).
		* Proven lead in driving multi-million dollar revenue generator models for the company and setting up data science related best practices at a company.
		* 2+ years experience with a fast-growing SaaS business based company is preferred.
		* Strong experience in Python, R, Spark, SQL, Tableau, Google Analytics, Hive and BigQuery (or any other Big data/Cloud equivalent) etc.
	- skill set:
		* Solid foundation in computer science, with strong competencies in algorithms, data structures, software design, web security, and building large, distributed systems
		* Excel at planning, working multi-functionally, leading execution across teams to meet commitments and deliver with predictability
		* Demonstrate a track record of leading teams, including hiring, onboarding, and professional development. You inspire your team to reach higher. You’re as good as explaining “why” as you are “how”
		* Experience implementing tools, process, internal instrumentation, methodologies and resolving blockages
		* Demonstrated ability to recruit and hire top talent
		* Comfortable managing teams/projects with tight deadlines and short release cycles
		* Experience working with and getting the best out of post-doctorate researchers
		* Being passionate about cryptography and/or web technology such as TLS
		* Familiarity working with DNS, database systems, Internet performance, and/or Internet security
	- skill set:
		* You will help build customer facing apps and our core platform to create, improve, and scale agricultural models. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us!
		* Graduate degree in a technical field and 5+ years experience as a Data Scientist working on commercial software products
		* Experience engineering production-level software systems evidenced by having built a parallel/distributed system, using software best practices, performance optimizations, or an automated pipeline to interpret other data science experiments
		* Experience applying the scientific method to complex, multivariate unstructured problems to produce rigorously-defendable conclusion in prose and graphics
		* Experience across and significant work in at least one of clustering and classification, multivariate regression, prediction, and forecasting; and dimensionality reduction and feature engineering
		* Experience or interest in Bayesian methods of crafting generative probabilistic models; engineering informative priors and solution via MCMC
		* Experience collecting, curating, structuring and retrieving large data sets in relational databases.
		* Additional experience with NoSQL preferred
		* Experience with either time-series or spatial statistics, especially Gaussian Processes
		* Experience creating complex data visualizations for multivariate data
		* Experience with AWS or other programmatic distributed computing environments
		* Experience with Bayesian non-parametrics (CRP, IBP, etc.)
		* Experience with advanced MCMC techniques such as DREAM, Hamiltonian-MC, variational approximations, etc.
		* Experience or keen interest in FP (Scala, Haskell, Clojure, Erlang, OCaML/SML, Elm, F\#)
	- tech stack:
		* Experience with Deep Learning frameworks, e.g., PyTorch, DeepLearning4J, TensorFlow
		* Experience in SPARK (using Python or Scala). Knowledge of AWS services will be appreciated.
	- Knowledge of source control tools (Git, CodeCommit, SVN, and TFS), build/release tools (Jenkins, CodeBuild, CodeDeploy, CodePipeline), and infrastructure as code tools (Terraform, CloudFormation)
	- Strong grasp of Configuration Management (Chef, Puppet, Ansible, Salt Stack)
	- stress testing (locust.io)
	- designing high availability systems
	- application security hardening
	- distributed tracing (OpenTracing/Zipkin)
	- collecting and analyzing performance metrics (InfluxDB, Prometheus, statsd, Grafana)
	- Docker orchestration systems and cluster managers (Kubernetes, Mesos/Marathon, ECS)
	- Experience in the technologies we use is helpful but not required. They are: Go for core infrastructure; ObjC, Java and C# for native UI development on iOS, OSX, Android and Windows; Node.js and IcedCoffeeScript for Web development; FUSE for client file systems; MySQL/InnoDB, DynamoDB, S3 and EC2 for hosting.
	- Load testing frameworks/tools like JMeter, Gatling, Locust
	- Java, Selenium, JUnit, Cucumber-JVM
	- API Testing experience
	- BDD (Cucumber, Gherkin)
	- Experience implementing search solutions with technologies such as SOLR, Elasticsearch, Lucene is preferred.
	- Python, Gherkin, Cucumber, Espresso, XUI Test
	- Experience with testing technologies (JUnit, Espresso, Mockito, Robolectric)
	- Unit Testing Tools  –  Google Test or CPPUnit ; Code quality tools
 	- Familiarity with Linux, Maven, Git/Stash, Jira, Bamboo/Jenkins
	- Experience with distributed messages systems ( Apache Kafka)
	- Experience in CFD combustion or other reacting-flow simulations.
	- tech stack
		* Jira, Confluence, DevOps, Continuous Integration and Continuous Delivery, Microsoft Development Tools
		* Git, MS Build, Team Foundation Server, Jenkins, Unit Testing, Powershell, Perl, C#, .NET, Visual Studio, Python
	- tech stack:
		* Excellent skills in creating high-fidelity prototypes using Invision, Principle, Code or similar
		* Relevant experience in agile methodologies (Scrum, Agile, etc) and PM tools (e.g. Jira, Pivotal Tracker, Confluence etc.)
		* Experience with relational (e.g. MySQL, PostgreSQL) and NoSQL (e.g. MongoDB, ElasticSearch) databases
	- tech stack:
		* Expertise in Go preferred, but not required. If you’re new to Go, then proficiency in a mainstream language such as Java, Python, C++, Scala, etc.., and a willingness to learn Go required.
		* You've got experience writing, deploying and monitoring microservices.
		* Working knowledge of SQL and relational databases(we use Postgres)
		* You've used an RPC framework like gRPC or Thrift.
		* You have high level experience working in a containerized infrastructure deployed in the cloud(AWS, GCP, Azure)
	- tech stack:
		* Experience with NoSQL databases. MongoDB is a plus
		* Experience with real-time and streaming data processing
		* Experience with queuing platforms like Kafka
		* Knowledge of BigQuery
		* Familiarity with GCP/AWS cloud services
		* Familiarity with TensorFlow
		* Comfortable with CI/CD Pipelines
		* Experience with Git version control
	- tech stack:
		* Ability to configure and maintain webservers (e.g. apache & nginx), DNS servers, Firewalls, LDAP servers, Tomcat servers
		* Ability to back up the Data infrastructure
		* Ability to manage/configure  Git, Maven and Jenkins
		* Managing QA/production release and deployment
		* Ability to Install/Configure/Manage VM servers using OpenStack
		* Ability to install configure or manage Monitoring servers using Opensource softwares
		* Experience with Amazon Web Services:
		* autoscaling, & use of Netflix Asgard
		* ELB management,
		* EBS storage management
		* S3
		* RDS
		* Manage configuration using Puppet
		* Familiar with Cloud Computing in genera
	- tech stack:
		* ReactJS
		* GraphQL
		* Apollo Client & Server
		* Some Redux
		* Using ES6/7 features throughout the app so knowledge on those is a plus.
		* We use Cypress for testing
		* CircleCI for continuous integration.
		* Functional programming principles in React with Recompose
	- Celery
	- Elasticsearch and ELK pipeline
	- LibreOffice, Apache OpenOffice, and NeoOffice.
	- Tech stack is described as:
		* Front­end: JavaScript (ES5/ES6), AJAX, jQuery, React/Angular/Vue, Bootstrap, templating, markdown/markup, built tools, task runners, PWAs, etc...
		* Middle­tier: REST and RESTful interfaces, AJAX, RPC, WebSockets/Socket.io, Web Workers, Node.js/Express, etc…
		* Back­end: SQL/No­SQL databases, Message Queue Systems, Big Data systems, Node.js, MongoDB, Redis, etc…
	- Sets of skills
		* AWS cloud services: EC2, EMR, RDS, Lambda, Redshift
		* NoSQL databases, such as HBase, Cassandra, MongoDB, or DynamoDB
		* messaging systems, such as AWS SQS, AWS Kinesis, Kafka, or RabbitMQ, ZeroMQ
		* big data tools and stream-processing systems: Hadoop, Spark, Storm, Spark-Streaming
		* **Expertise and experience in Revit, Dynamo and/or other Revit scripting languages**... Strong background in computational design and design analysis... Fluency in a technical programming language (python, javascript, C#) is highly desired.
		* Understanding of standard networking protocols and components such as: TCP/IP, HTTP, DNS, ICMP, the OSI Model, Subnetting, and Load Balancing
		* Knowledge of routing protocols such as BGP and OSPF
		* data pipeline and workflow management tools: Azkaban, Luigi, Airflow
		* Very well versed with ADT, ORU, ORM and document exchange messages specification
		* Develop public APIs on either APIGEE
		* DBT experience
		* Object oriented programming experience (e.g. using Java, J2EE, EJB, .NET, WebSphere, etc.).
		* data interchange formats like JSON and XML
		* Knowledge in machine learning framework - Tensorflow, Caffe, Torch or Theano
		* Django, Ruby on Rails, Flask
		* Must have experience with working on few technologies such as spring framework, SpringBoot, SpringMVC, JPA, MyBatis, Tomcat, Nginx
		* Experience with performance optimization of queries in Redshift & Postgres
		* Knowledge of authentication protocols such as basic and digest authentication, SAML, LDAP, and OAuth.
		* In-Memory caching technologies, such as memcached or Redis
		* Cutting edge C++ knowledge (C++17, C++20)
		* stream pipelines and all sorts of datastores (SQL, NoSQL, triplestores, wide column, graph)
		* Knowledge of data standards, file formats, and biomedical ontologies and vocabularies such as SNOMED-CT, UMLS, etc. DICOM
		* all types of datastores - NoSQL, wide column, Graph, triplestores
		* Spark, Kafka
		* Experience with stream pipelines and data store technologies (nosql, wide column and graph). We are Currently using Cassandra, Kafka, Amazon dynamoDB, Redis, Neo4j and Mysql.
		* NLP library: spaCy, NLTK, GATE, CoreNLP, gensim
		* Deep Learning applied to NLP, for example through distributed representations (e.g. Word2Vec, fastText, etc)
		* large databases (e.g. THIN)
		* Monitoring solutions experience (ELK, NewRelic)
		* Infrastructure-as-code and automation tools (e.g. Terraform, Ansible/Chef, Cloud Formation)
		* Configure and Monitor SIEMS and DLP systems
		* RxJava, Kotlin, Dagger
		* big data platform tools such as Hadoop, Hive, Druid, Kafka, Ambari, Spark
		* Experience with common security tools such as nmap, Burp Proxy, Brakeman, etc.
		* Experience with bug bounty programs and reporting issues to them (send examples, please!)
		* Familiarity with search domain (Information retrieval, NLP, Solr/ Lucene or related tech)
		* data management tools in on a big data plate form such as Atlas, Ranger , Knox
		* implementing BI solutions in a heavily regulated environment e.g. PII, GDPR, HIPPA & SOX
		* big data platform tools such as Hadoop, Hive Druid, Kafka, Ambari, Spark, Zeppelin
		* PowerBI, Tableau, Qlikview
		* Production experience with AWS tools including at least some of the following: EC2, S3, Kinesis, CloudFormation, Redshift
		* Experience with at least one data warehousing platform (Redshift, Athena, Hive, Snowflake, etc.)
		* Knowledge of a majority of the following: Elixir, Erlang, Ruby, JavaScript, PHP, Postgresql, MySQL, Apache Solr, Elasticsearch.
		* Knowledge of web frameworks (like Sinatra/Rails), testing frameworks (like Rspec/Minitest) and Javascript. Experience with Ruby, MySQL and Apache Solr is a plus.
		* Experience with Java, Boost, QML, Jira, JavaScript, React, or DDP
		* Demonstrated proficiency with Docker and container orchestration technologies (Kubernetes, ECS, etc.)
		* Expertise with AWS services such as EC2, IAM, S3, etc.
		* Expertise with several continuous integration technologies (Jenkins, Ansible, CloudFormation, Terraform, etc.)
		* Experience with load balancing technologies such as ELB, NGINX, etc.
		* Experience with network technologies like DNS, AWS security groups, VPCs, etc.
		* Extensive experience manipulating and analyzing complex data with SQL, Python and/or R. Knowledge of Google BigQuery and Java/Scala is a plus.
		* Tools: Slurm, Docker, Grafana.
		* skill set:
			+ Agile development approaches
				- Lean-startup and design-thinking inspired methods incorporating short product development, business-hypothesis-driven experimentation, iterative product releases, and validated learning
			+ Programming languages and operating systems
				- Python
				- Javascript
				- Unix/Linux/MacOSX
				- RDF, JSON-LD, SPARQL
			+ Tools
				- Git
				- Slack
				- JIRA
			+ Web app development
				- Django
				- Django REST Framework (for API development)
				- Node
			+ Backend
				- SOLR/Lucene or ElasticSearch
				- Amazon Web Services (AWS) or other cloud service providers
				- “Serverless” computing (e.g., AWS Lambda)
				- Application containerization (such as Docker or Kubernetes)
			+ Javascript frameworks
				-  Vue and/or Nuxt
				- Webpack
			+ Mobile development
				- Using responsive design and development techniques, possibly including the use of Progressive Web Application (PWA) techniques and technologies
			+ Other
				- Topic modeling (ideally using Mallet)
				- Video formats and metadata (for both archiving and streaming)
				- RDF, JSON-LD, Sparql and GraphQL for knowledge graph development and use
				- Content markup including:  HTML, XML, ePUB, PDF
				- Named Entity Recognition (NER)
				- Experience applying statistics, modeling, and machine learning
		* skill set:
			+ SQL, javascript, and google appscript
			+ Familiarity with HR systems and tools (e.g. Workday, Reflektive, Zugata, Culture Amp)
			+ You are a skilled engineer. You've got a strong background working in our stack (Python, Django or React, ES6 or Node.js, etc.) -- even if you aren't a daily coder, you regularly exercise your coding muscles and try to be an asset on any technical context your team may need.
			+ Help the team build tools for partners and developers that come to our platform to create Apps that live on Zapier. Imagine Postman meets OpenAPI on steroids.
		* tech stack:
			+ Research publications at relevant conferences such as SIGGRAPH, ACM Trans on Graphics, CVPR, ICCV, ICCP, SPIE, JOSA a major plus.
			+ Expertise in Deep Learning, Machine learning and familiarity with tools like Scipy, Boost, Caffe, TensorFlow, OpenCV, DLIB etc. and related areas.
		* tech stack:
			+ Publication record in top conferences (ICML, ICLR, NIPS, KDD, IJCAI, AAAI etc )
			+ Good knowledge and handson experience in distributed technologies such as Hadoop, Hive, Spark Experience in Scala programming language.
			+ Publications in relevant top venues (e.g., KDD, NIPS, ICML, AAAI, IJCAI, ICDM, ACL etc.)
		* tech stack:
			+ Security and privacy
		    + Virtualization and container technologies (e.g., Xen and Docker)
			+ Cloud services (e.g., AWS and Azure)
			+ Distributed programming tools (e.g., Hadoop, Cassandra, and ZooKeeper)
			+ In-home wireless network protocols (WiFi, Bluetooth, Zigbee, and Z-wave)
			+ Systems for machine learning training and inference (Tensorflow, MXNet, Caffe etc)
			+ Storage systems
		* Experience with open source platforms like Hadoop, Spark, Hive, Pig; and/or ML life-cycle/collaboration/automation platforms like AirFlow, FB Learner, MLFlow; and/or assistants like Alexa, a plus.
		* You’ll lead, analyze, implement, and socialize a robust A/B/multivariate testing program, collaborating closely with product, engineering, marketing, and content.
		* You’re familiar with all aspects of SEO: on-page, external, and technical, and you have used tools such as ahrefs, DeepCrawl, Screaming Frog, SEMRush, and Google Search Console to optimize for search.
		* Set of skills:
			+ Experience with modern programming languages (Java, Scala, Go, TypeScript)
			+ Database / Data Storage experience (SQL / MySQL, MongoDB, DynamoDB)
			+ Interest in Infrastructure Tooling (Docker, Nomad, Consul, Vault, Prometheus)
		* RStudio packages: The tidyverse, R Markdown, and Shiny
		* A sample of the technologies you’ll be exposed to: Python, Javascript/Angular, Impala (Big data data database), AWS, Docker, Kubernetes, Git.
		* Experience with Python ORMs like SQLAlchemy and Python libraries like Pandas, Scikit-Learn, Numpy and Scipy
		* Should have experience in dealing with XML and JSON data formats.
		* Knowledge in Hadoop (HDFS, YARN), its programming models (MapReduce, Spark), and its services such as Hive, HBase etc.
		* Technical Fluency.  Languages and tools such as Python/Java/Scala, AWS (S3/EMR/Athena/Glue) and SQL. Experience with big data processing tools including Spark, Hadoop, Hive, Yarn, and Airflow. Experience working with either a MapReduce system of any size/scale.
		* Experience writing production datasets in SQL/Hive OR building internal/production data tools for ETL, experimentation, or exploration in a scripting language (Python, R, etc.)
		* Very strong experience in scaling and optimizing schemas, performance tuning SQL and ETL pipelines in the OLTP, OLAP and Data Warehouse environments
		* Passionate about various technologies including but not limited to SQL/No SQL/MPP databases etc.
		* Hands-on experience with Big Data technologies (e.g Hadoop, Hive, Spark)
		* Ansible: it’s not that bad, and helps us move quickly, but any configuration management tool is applicable.
		* Elasticsearch / Kibana: You can readily access information & love metrics
		* Familiarity with common web application testing tools for DAST, SAST, and IAST analysis such as Burp Suite, Checkmarx, Veracode
		* Completed graduate-level coursework in survey statistics—bonus points if you've completed coursework in adjacent fields/methods (e.g., econometrics, NLP, experimental design, political science, or quantitative social psychology)
		* Exposure to container technologies - container orchestrators (Kubernetes, Mesos, Docker Swarm Mode) is a plus
		* Experience with Cloud based services, Microservices a Cloud Computing class or similar experience
		* Technical Skills needed: vSphere, vSAN, NSX, vROps, Storage, Database, Middleware, and Scripting
		* Experience of Unity, C# and 3D application development.
		* Working knowledge of HMD (ie Oculus, HTC Vive, Hololens)
		* Experience with Hololens, HTC Vive, Oculus, Google Cardboard and other leading AR/VR platforms
		* Knowledge of NoSQL technologies (e.g. Cassandra, MongoDB, Redis, etc.) and/or search-based datastores and libraries (Lucene, Solr, etc.)
		* Experience within the domain of Advanced Analytics and Data Science is highly desirable, e.g. hands-on experience with solutions such as Spark, MapReduce, Python, Redshift, Hive, Pig and visualization tools.
		* Hadoop data platform is capable of supporting a growing list of downstream platforms like Tableau, Zeppelin etc.
		* Expertise with Hive, YARN, Spark, Presto, Kafka, SOLR, Oozie, Sentry, Encryption, Hbase, etc.
		* API development
		* You highly experienced with JavaScript/Node.js, SQL/NoSQL databases
		* We are fans of the Lean Startup methodology, we love Trello, Jira, Slack
		* We are cloud agnostic and run our infrastructure and systems on Azure, AWS, as well as dedicated servers.
		* Experience utilising Portfolio & Project Management (PPM) tools such as CA PPM (Clarity), ServiceNow, JIRA, Microsoft Project Server, etc.
		* project management tools (JIRA, Confluence),
		* big data platform tools such as Hadoop, Hive, Druid, Kafka, Ambari, Spark
		* web analytics platforms such as Google Analytics, Appsflyer or Mixpanel
		* NoSQL databases, such as MongoDB, Cassandra, HBase
		* Proficiency in using query languages such as SQL on a big data platform e.g. Hadoop, Hive
		* data visualisation tools, such as D3.js, GGplot, Tableau etc.
		* Excellent understanding of machine learning techniques and algorithms, such as k-NN, Naive Bayes, SVM, Decision Forests, etc.
		* Apache Kafka
		* vw / xgboost
		* Knowledges of Web test frameworks like Selenium, React.js, Headless Chromium is a plus
		* a set of skills:
			+ Statistical analysis and modeling
			+ Database architectures
			+ Hadoop-based technologies (e.g. MapReduce, Hive and Pig)
			+ SQL-based technologies (e.g. PostgreSQL and MySQL)
			+ NoSQL technologies (e.g. Cassandra and MongoDB)
			+ Data modeling tools (e.g. ERWin, Enterprise Architect and Visio)
			+ Python, C/C++ Java, Perl
			+ MatLab, SAS, R
			+ Data warehousing solutions
			+ Predictive modeling, NLP and text analysis
			+ Machine learning
			+ Data mining
			+ UNIX, Linux, Solaris and MS Windows
			+ Python (3.5>=), packages: argparse, shapely, Munkres, numpy, cv2, logging, Pillow
		* ES6
		* Plotly.js
		* OpenLayers
	- UI/UX:
		* Experience using design tools such as Photoshop, Illustrator, Sketch, InDesign, etc. for creating highly-detailed mockups
		* Some awareness of the technology which will serve your designs and implementations, such as apache/nginx, Flask/django, PostgreSQL/MySQL, git, websockets, etc.
		* Bootstrap, bulma, etc.
+ Finish assignments 1 and 2 for the data science course.
+ Run automated regression testing, and/or regression verification, to put
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









#	Operazione Andare a ICCAD

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

#	Operation Go2DAC

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




To-do list:
+ Store test results in a database (in *CSV* format), and manage it with a *SQL*
	database (e.g., *MySQL*).
	- *Python* interface to *SQL* database.
	- Process this with a *NoSQL* database.
	- Process this with a *NewSQL* database.
	- References from my *BibTeX* database about this:
		* \cite{Lutz2010}
		* \cite{Lutz2011}
		* \cite{Sileika2010}
		* \cite{Younker2008}
		* \cite{Sweigart2015}
+ Finish assignments 1 and 2 for the data science course.
+ Run automated regression testing, and/or regression verification, to put
		the experimental results of each build in the correct directory.
		And, commit and push that build to the cloud-based research repository.
+ Create scripts for performance measurement and analysis.
	- *Python*
	- *GNU Octave*
	- *Scala*/*Chisel*
	- *SPICE*???
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




### QUBO + Pseudo-Boolean Optimization (PBO)

+ Anthony2017.pdf
+ Babbush2014.pdf
+ Gruber2015-copy.pdf
+ Gruber2015.pdf
+ HammerIvanescu1968.pdf

##	Pseudo-Boolean Optimization (PBO)

+ Andres2015.pdf
+ Lampert2017.pdf






##	Graph Coloring


##	Map Coloring






##	Image Recognition: Pattern Recognition + Machine Learning

###	Trustworthy Computing

###	Computer Security

Trustworthy computing

Design for Security









#	Operazione Andare a DATE

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







#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

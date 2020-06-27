# Getting People to Use, Read, Modify, and Cite Your Released Source Code

ZHIYANG ONG·SUNDAY, JUNE 7, 2020·

## Document Your Source Code for Your Software and/or Hardware

When you document your source code for your software, hardware/circuit, computer/embedded system, and/or cyber-physical system, it makes it easier for people to use your solution, read and modify your source code, and cite your work.

This involves comments in your source code, and accompanying documentation. Accompanying technical documentation and user documentation from your project life cycle (or IEEE software life cycle) refer to the following (from https://en.wikipedia.org/wiki/Software_documentation):
+ SRS – Software requirements specification IEEE 830. Or system/hardware requirements specification.
+ SDD – Software design description IEEE 1016. Or, architecture design documentation.
+ SPM – Software project management IEEE 1058. Or system/hardware project management.
+ SCM – Software configuration management IEEE 828. Or configuration management or version/revision control for system/hardware projects.
+ SQA – Software quality assurance IEEE 730. Or, system/hardware quality assurance.
+ V&V – Software verification and validation IEEE 1012. Or, system/hardware verification and validation.
+ STD – Software test documentation IEEE 829. Or, system/hardware testing.
+ SUD – Software user documentation IEEE 1063. Or, system/hardware user documentation.
+ user guides
+ tutorials
+ reference guides

### Commenting Your Source Code

Use comments to describe each class/structure, constructor, and function/method of your software (or computer program).

You can also do likewise for each subcircuit, circuit, and module of your hardware design.

When you import packages, modules, semiconductor manufacturing technology libraries, cell libraries (for logic synthesis and physical design), describe this.

When you make assumptions in designing your circuits, systems, algorithms, software architecture, platform, or framework, document these in your comments and accompanying documentation.

Hence, be consistent in commenting your functions/methods, classes/modules, and subcircuits/circuits. 

For computer programs, I use Javadoc style commenting, which is supported by Doxygen (automatically generates HTML files, LaTeX documents, and “man pages” to describe your software, hardware, or system) and similar documentation generation tools.  Pydoc has a similar commenting style.


### Combining Source Code with Additional Documentation

Markdown documents can include tables and figures, so you may want to include them to describe your solution, from algorithm design (from flow charts to step-by-step animation of algorithms, just like our data structures textbook, and software architecture).  Jupyter notebooks can allow you to combine source code, the results of executing code fragments, with text in Markdown format (including tables, figures, and LaTeX-typeset mathematical equations).


### Reference All Documents/Publications

Reference documents/publications properly...

I put the information for these in a BibTeX document, and use the "\cite{}" command to cite them.

See https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/guidelines/guidelines.pdf.

Don't just put down URLs, such as https://en.wikipedia.org/wiki/Software_requirements_specification.

Include the author(s), publisher, address of publisher, date of publication, last date in which you accessed a URL, title of the URL/publication, ...

Design and document your coding style, which I did in: https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/guidelines/guidelines.pdf.

Encourage your collaborators to use the same coding style as you, so that it is easier for people to read your source code.

Describe the mathematical formulae/formulas/expressions that you are implementing in LaTeX notation, so that people can understand what you are doing.

For complex (or non-trivial) mathematical expressions that you took from publications, cite them.

If you do not reference them, you are violating rules and regulations regarding academic integrity (applicable for students, faculty, and researchers) and research integrity (for researchers, research students, and research/tenured faculty at research universities). Likewise, obey intellectual property laws by using appropriate licenses for your work/solutions, and paying for licenses that enable you to use the work of other people/organizations.

## Refactor Your Code

Releasing your code in classes/modules (or subcircuits and circuits) and Python/Java packages (or equivalent) make it easy for people to import your source code and use it, even with Google Colab, similar cloud-based Python programming/execution (like Anaconda Cloud), or equivalent.

When you use modularity, abstraction, and encapsulation, it makes it easier to refactor your solutions, and enable people to integrate (parts of) your work/solutions into their work/solutions.


## Verify, Test, and Validate Your Solutions

Verify/Test each constructor (if you use classes or object-oriented design), each function (or method, if you use classes), subcircuit and circuit (for SPICE-like circuit descriptions), and modules (for hardware descriptions like Verilog).

Validate if these aforementioned components meet user requirements and needs, not just software/hardware/system specifications. This is because software/hardware/system specifications may not be specified to meet user requirements and needs.

Use formal verification, and semi-formal verification, techniques to provide additional confidence to users that your work/solutions work.

When you verify, test, and validate your work/solutions, and provide test suites and/or testbenches for your solutions/work give people confidence that your solutions work with high quality. Also, try to provide an estimate of the test/verification coverage for your work, so that people know if your verification/testing effort has been adequate.

## Benchmark Your Work

If your problem is not an open problem, data sets and/or benchmarks should be available for your task/problem. Hence, the implementation of existing solutions for your task/problem exists. You can clone existing solutions from GitHub or elsewhere, and execute/test/simulate them on the same data sets or benchmarks to compare their metrics (e.g., performance, accuracy, memory usage, and power consumption) with the metrics of your work/solution.

Hence, benchmarking does not have to involve a lot more work.

If solutions from other people’s work are not available, implementing them (as described in publications) help you learn more about their work, and their strengths and weaknesses. Doing so is typical for course projects in graduate-level courses for Masters and Ph.D. students in electrical/computer engineering and computer science (EE, ECE, CS, or EECS).

For software solutions, some common metrics to benchmark/compare your solution/work with other solutions/work are: performance (i.e., execution time), accuracy (if applicable), memory usage (i.e., computational space complexity), and power consumption (especially for for embedded systems).

Hence, you should perform design space exploration of your solutions, and plot the experimental results of your solutions and those of other solutions on the axes of concern (i.e., the aforementioned metrics)...

E.g., in 2-D space, performance (or execution time) versus accuracy. Or, plot worst-case/nominal delay (or delay on the critical path or set of equivalent critical paths) versus area usage of the integrated circuit’s layout (i.e., VLSI/IC layout). Or, plot worst-case/nominal delay versus number of cells/gates used for logic circuits. For embedded software, worst-case execution time (WCET) is a good metric; use program analysis tools to obtain this number.

E.g., in 3-D space, performance (or execution time) versus accuracy (if applicable) versus memory usage (i.e., computational space complexity). Or, you can look at delay, area (or number of cells/gates), and power consumption.

For an alternate 3-D space, you can also look power consumption for embedded systems/software in addition to performance and memory usage.

The resulting plots of your plot trade-off decisions would reveal trade-off decisions you as the software, hardware, or system designer have to make to select a solution on the Pareto frontier.




## Conclusion

In general, good (software) documentation makes the source code for your software, hardware, and/or system and documentation/text readable, and makes it more likely for people to read, use, modify, and cite your work.  Likewise, testing/verifying your code shows people how to use your code (i.e., how to apply your work/solution), and gives them confidence that your solutions work.


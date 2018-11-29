#	This Makefile is written by Zhiyang Ong for build automation of his BDAthlon code.

#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.







# Makefile for Standard Cell Library Chracterization.
# @author Zhiyang Ong

# =============================================================

# Definition of macro flags...
# IMPORTANT NOTE:



# IMPORTANT:: Paths to be modified!!!
# Benchmark directory, relative from the repository.
BENCHMARKS=	./benchmarks/


# Version of g++ used is GCC version 4.5.2
GPLUSPLUS=		g++
COMPILE=			-c
LINK=					-o
RMHG=					hg remove
EXECUTABLE=		./test-boilerplate-code				# ./sizer.exe
OBJFILES=			*.o
SOURCE=				*.cpp
HEADER=				*.h
RUBY=					*.rb
JAVA=					*.java
MATLAB=				*.m
TILDE=				*~
PREVDIR=			../
PARALLEL=			-lpthread
HOME=					../
SLASH=				/
# Macros that are useful to help me debug
COMPILATIONSTEPS=	-v
WARNINGS=			-Wall
EFFCPP=				-Weffc++
HARDERRORS=		-Werror
PEDANTIC=			-pedantic
PEDANTICERRORS=		-pedantic-errors
EXTRAWARNINGS=		-Wextra
COMPATIBILITY=		-Wc++-compat
DEBUGGINGINFO=		-g -dA
DEBUGDUMP=		-dD
COREDUMP=			-dH
MEMORYUSAGE=	-dm
MEMORYTIME=		-fdump-tree-all
CPPTIME=			-time
SIMPLEOPT=		-O1
MOREOPT=			-O2
EVENMOREOPT=	-O3
MAXPERFORMANCE=		-fast
SIZEOPT=			-Os
INCLUDE=			-I
DYNDIRINC=		-L
DYNINCLUDE=		-l
#	Used when testing and debugging.
COVERAGE=			-coverage
#	Normal output message/text file
NORMALTXT=		normal_output.txt
#	Error output message/text file
ERRORTXT=			error_output.txt
#	Used when testing and debugging.
COVERAGE=			-coverage
CPP11=				-std=c++11
CPP14=				-std=c++14
CPP17=				-std=c++17






# Basic software architecture description at the module level.
# Paths for different modules/packages of the software.
#
# Note that the paths of the modules are relative.
# The modules are located in the "src" directory.
# This is because I am building and testing the software in a
#	separate directory, so that I can isolate the object files
#	and the executable from the source code.
# Such isolation would make it easier to clean up the directory where
#	the software resides, so that it is easier to maintain.
#
# Module that defines the key components of a (hyper)graphs.
GRAPHPATH=		../src/graph/
DIRGRAPHPATH=	../src/graph/directed/
UNDIRGRAPHPATH=	../src/graph/undirected/
#
# Module containing the input benchmarks that are used to test my software.
BENCHMARKS=		../benchmarks/
# Benchmarks provided for lamiera-per-caldaie
STACK1=			stack1
STACK2=			stack2
# Name of output file
OPRESULTS=		output-results
#
# Module containing the parser for the input benchmarks.
PARSERPATH=		../src/parsers/
#
# Module containing the elements of the data structures
#	that I would implement.
ELEMPATH=		../src/elements/
#
# Module that contains the source of the main function.
MAINPATH=		../src/main/
#
# Module containing test cases/suites for the software.
# It does not contain Exception classes, which are placed
#	in the utilities module.
TESTPATH=		../src/test/
# Submodules of the Test module
TPGRAPH=		graph_t/
TPDIRGRAPH=		directed/
TPUNDIRGRAPH=	undirected/
TPMAIN=			main_t/
TPUTILITIES=	utilities_t/
TPPARSERS=		parsers_t/
#
# Module that provides classes to support the development and
#	debugging of the software, including Exception classes.
UTILITYPATH=	../src/utilities/
#
# Module containing scripts used for file processing/management
#	and statistical analysis
SCRIPTS=		../scripts/
#
# Module containing the binaries, object files, and build automation
#	tools.
BINARIES=		../binaries/
#
# Module containing the documention of the software.
NOTESPATH=		../notes/
DOCSPATH=		../docs/
# Module containing "test" code from the "sandbox".
SANDBOXPATH=	../src/sandbox/
TEMPLATEPATH=	classes/simple_template.cpp





#	Location of the experimental results.













# UNIX commands/utilities that are used
TIME=			time -p
DATE=			date






# =============================================================

# Definition of Target Rules
# Use a FOR loop to sweep through the list of benchmarks when
#	the parse is ready, and do regression testing when the router
#	is done.

########################################################################
# BUILD THE SOFTWARE	--	FIX THIS!!!
########################################################################
# Build and test the latest software build
all:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	@echo === Compiling C++ source code in the...
	@echo === Graph Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(GRAPHPATH)$(SOURCE)
	@echo === Synthesis Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(SYNTHESISPATH)$(SOURCE)
	@echo === Macromodeling Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(MACROMODELINGPATH)$(SOURCE)
	@echo === Parser Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(PARSERPATH)$(SOURCE)
	@echo === Main Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(MAINPATH)$(SOURCE)
	@echo === Test Directory
	$(GPLUSPLUS)	$(COMPILE)	$(TESTPATH)$(SOURCE)
	@echo === Utilities Directory
#	$(GPLUSPLUS)	$(COMPILE)	$(UTILITYPATH)$(SOURCE)
	@echo === Link the C++ object files...
	$(GPLUSPLUS)	$(LINK)		$(EXECUTABLE)	$(OBJFILES)
	@echo === Executing the software...
	$(TIME) $(EXECUTABLE) $(ISPD_CONTEST_ROOT) $(SIMPLE)
	@echo
	@echo
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo







########################################################################
# TEST THE SOFTWARE: UNIT, MODULE, INTEGRATION, AND REGRESSION TESTING
########################################################################
# Build and test the latest software build.
test:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	$(TBBSETUP)
	@echo === Compiling C++ source code in the...
	@echo === Utilities Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(UTILITYPATH)$(SOURCE)
	@echo === Graph Directory
#	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(DIRGRAPHPATH)$(SOURCE)
	@echo === Parsers Directory
	@echo === Sandbox Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(SANDBOXPATH)$(TEMPLATEPATH)
	@echo === Test/Utilities Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(TESTPATH)$(TPUTILITIES)$(SOURCE)
	@echo === Test/Graph Directory
#	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(TESTPATH)$(TPGRAPH)$(SOURCE)
#	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(TESTPATH)$(TPGRAPH)$(TPDIRGRAPH)$(SOURCE)
	@echo === Test/Parsers Directory
	@echo === Test Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(TESTPATH)$(SOURCE)
	@echo === Link the C++ object files...
	$(GPLUSPLUS)	$(CPP11)	$(LINK)		$(EXECUTABLE)	$(OBJFILES)
	@echo === Executing the software...
	$(TIME) $(EXECUTABLE) $(BENCHMARKS)$(STACK1)	$(OPRESULTS)
	@echo
	@echo
	@echo
	@echo
	@echo "The code is rather buggy; use is at own risk."
	@echo "-- Donald Chai"
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo
	@echo
	@echo
	@echo
	more $(NORMALTXT)
	more $(ERRORTXT)



#####################################################################
#	Target for testing templates.
#####################################################################
# Build and run C++ program to experiment with templates.
template:
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	@echo + + + + + + + + + + + + + + + + + + + + + + + + + + +
	$(DATE)
	@echo === Compiling C++ source code...
	@echo === Elements Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(ELEMPATH)$(SOURCE)
	@echo === Test Directory
	$(GPLUSPLUS)	$(CPP11)	$(COMPILE)	$(TESTPATH)temp/test_templates.cpp
	@echo === Link the C++ object files...
	$(GPLUSPLUS)	$(CPP11)	$(LINK)		$(EXECUTABLE)	$(OBJFILES)
	@echo === Executing the software...
	$(TIME) $(EXECUTABLE)
	@echo
	@echo
	@echo
	@echo
	@echo "The code is rather buggy; use is at own risk."
	@echo "-- Donald Chai"
	@echo
	@echo "Beware of bugs in the above code."
	@echo "I have only proved it correct, not tried it."
	@echo "-- Donald E. Knuth"
	@echo
	@echo
	@echo


########################################################################
#	Resolving linking problems during compilation.
#	g++ -v -o ./test-boilerplate-code *.o
#	g++ -o ./test-boilerplate-code *.o -v












########################################################################
# CLEAN THE TEMPORARY FILES
########################################################################
# Remove all executables, object files, and the output file(s)
clean:
	@echo ===Removing all temporary files...
	$(SCRIPTS)clean_temp_files.rb
	@echo "	=Removed all temporary files."












########################################################################
# RUN THE PROGRAM
########################################################################
# Run/Execute the program
run:
#	@echo -->Executing the SoFTwaRe...
	$(EXECUTABLE) $(BENCHMARKS)$(STACK1)	$(OPRESULTS)




########################################################################
# COUNT THE NUMBER OF LINES OF SOURCE CODE
########################################################################
# Count the number of lines in my source files
# cat *.h *.cpp *.rb *.java *.m | wc -l
numlines:
	@echo == Count the number of lines in my source files
	$(SCRIPTS)numlines.rb









########################################################################
# HELP ME!!!
########################################################################
# The options for make targets are:
help:
	@echo The options are:
	@echo all:_______Compile all source files and link their
	@echo ___________object code, and run the program.
	@echo clean:_____Remove all executables, object files,
	@echo ___________other temporary files, and output files.
	@echo run:_______Execute the program.
	@echo numlines:__Count the number of lines in the source
	@echo ___________code, including header files, and the scripts.
	@echo test:______Test the program.















########################################################################
# INITIALIZE DOCUMENTATION GENERATION
########################################################################
# Initialize Documentation Generation
doxygeninit:
	doxygen -g doxygen.config


########################################################################
# GENERATE DOCUMENTATION
########################################################################
# Generate Documentation
doxygen:
	doxygen doxygen.config
















#	$(GPLUSPLUS)	$(PARALLEL)	$(LINK)		$(EXECUTABLE)	$(OBJFILES)

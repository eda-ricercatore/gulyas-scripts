/**
 * lamiera-per-caldaie: A library of common data structures and
 *	algorithms, including common data structures and algorithms for
 *	electronic design automation (such as AND-Inverter Graphs and
 *	binary decision diagrams).
 *
 * The MIT License (MIT)
 *
 * Copyright	(C)	<2014>	<Zhiyang Ong>
 *
 * Permission is hereby granted, free of charge, to any person
 *	obtaining a copy of this software and associated documentation
 *	files (the "Software"), to deal in the Software without
 *	restriction, including without limitation the rights to use, copy,
 *	modify, merge, publish, distribute, sublicense, and/or sell copies
 *	of the Software, and to permit persons to whom the Software is
 *	furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 *	included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 *	MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 *	NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 *	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 *	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 *	DEALINGS IN THE SOFTWARE.
 * 
 * 
 *
 * @author Zhiyang Ong
 *
 * Test suite for lamiera-per-caldaie.
 *
 * Main function for test suite:
 * This test suite will set up the instance variables necessary to test
 * different functions of lamiera-per-caldaie.
 * Subsequently, it will test the various modules, and classes and
 * their functions of Tiramisu.
 * Next, it will clear up the virtual memory used by the instance variables.
 *
 * For each class, the testing sequence would be:
 * # constructors
 * # accessor functions
 * # mutator functions
 * # destructor
 *
 * The current testing sequence of classes is:
 * # utilities
 *		@ violated_assertion
 *		@ violated_postcondition
 *		@ violated_precondition
 *		@ printer
 * ...
 * # node
 *
 *
 * #### IMPORTANT NOTES:
 * To be completed...
 */

// Import Header files from the C++ STL
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <cstring>
#include <math.h>
#include <climits>
#include <cfloat>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

// Import Header files from the other modules of Tiramisu.
// Utilities module
#include "../utilities/printer.h"
#include "utilities_t/printer_ut.h"
//#include "../utilities/file_io.h"
//#include "utilities_t/file_io_ut.h"
#include "../utilities/violated_assertion.h"
#include "utilities_t/violated_assertion_ut.h"
#include "../utilities/violated_precondition.h"
#include "utilities_t/violated_precondition_ut.h"
#include "../utilities/violated_postcondition.h"
#include "utilities_t/violated_postcondition_ut.h"


using namespace std;

// =======================================================================

// FIX THESE!!!
// Shortcuts to use data structures and iterators from the STL
// Shortcut to represent list of blk_pins
//typedef list<blk_pin *> blk_pin_list;
// Shortcut to represent a pointer to list of blk_pins
//typedef list<blk_pin *>::iterator blk_pin_l_p;

// =======================================================================

// Start of main function...
int main(int argc, char *argv[]) {
	// cout << "===============================================================" << endl;
	// cout << "		- START OF TEST SUITE -"<<endl;
	// cout << "===============================================================" << endl;
	// cout << "Run the automated regression test suite..."<<endl;
	// cout <<endl;

	
	
	
	
	/*
	 * If the first two input arguments for this program is null,
	 * request for the user to rerun the program and exit.
	 */
	if((argv[1] == NULL) || (argv[2] == NULL)) {
		// cout << "To run this program, lamiera-per-caldaie (test-boilerplate-code)," << endl;
		// cout << "do the following:" << endl;
		// cout << "./test-boilerplate-code [benchmark] [output-filename]" << endl;
		// cout << endl;
		// cout << "E.g., ./test-boilerplate-code stack stack-op.txt" << endl;
		return 0;
	}

	// cout << "Benchmark is located at:" << endl;
	// cout << argv[1] << endl;
	// cout << "Output filename to store test results is:" << endl;
	// cout << argv[2] << endl;
	
/*
	// Check if the benchmark is valid.
	if(!file_io::is_bmk_loc_valid(argv[1])) {
		cerr<<argv[1]<<" is NOT a valid benchmark."<< endl;
		throw new violated_assertion("Invalid benchmark!!!");
	}else{
		// Set the benchmark.
		file_io::set_bmk_loc(argv[1]);
	}


	
	// Check if the benchmark is valid.
	if(!file_io::is_bmk_valid(argv[2])) {
		cerr<<argv[2]<<" is NOT a valid output filename."<< endl;
		throw new violated_assertion("Output filename is invalid!!!");
	}else{
		// Set the benchmark.
		file_io::set_name_of_bmk(argv[2]);
	}
*/	

	// =======================================================================
	// =======================================================================
	// =======================================================================
	
	

// seg fault - accessing something that isn't there
// bus error - accessing some thing (data element) that has been freed


	
	// Start testing my code here!
	
	// Testing the utilities package
	// cout << "--------------------------------------------------------" << endl;
	// cout << "		TESTING the Utilities package" << endl << endl << endl;
	// Test the class violated_assertion
	violated_assertion_ut::test_violated_assertion();
	// Test the class violated_precondition
	violated_precondition_ut::test_violated_precondition();
	// Test the class violated_postcondition
	violated_postcondition_ut::test_violated_postcondition();
	// Test the class printer
	printer_ut::test_printer();
	// Test the class file_io
//	file_io_ut::test_file_io();

	
	
	
	// Testing the graph package
	// cout << "--------------------------------------------------------" << endl;
	// cout << "		TESTING the Graph package" << endl << endl;
	// Test the class node



	
	//file_io::open_io_streams();
	
	// Tally up the software testing score.
	// cout << "--------------------------------------------------------" << endl;
	// cout << "		Summary of Automated Regression Testing";
	// cout << endl << endl;
	// cout << "Number of test cases: "<<printer::get_num_test_cases()<<endl;
	// cout << "Number of passed test cases: ";
	// cout << printer::get_num_passed_test_cases()<<endl;
	double results = (double) printer::get_num_passed_test_cases() / printer::get_num_test_cases();
	results = results * 100;
	// cout << "	Success Rate: " << results << "%" << endl << endl;
	

	// cout << "===============================================================" << endl;
	// cout << "		- END OF TEST SUITE -"<<endl;
	// cout << "===============================================================" << endl;
	
	// End of main function...
	return 0;
}

/**
 * Test/Utilities_t package:
 * Submodule of Test package to test classes in the Utilities package.
 *
 * printer_ut class:
 * Class that tests the printer class.
 * The constructors and functions of the printer class shall be tested.
 * 
 *
 *
 * Copyright	(C)	<2010-2011>	<Zhiyang Ong>
 * @author Zhiyang Ong
 * @version 1.0.0
 * @since January 1, 2011
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

// Import Header files from the other modules of Tiramisu.
#include "printer_ut.h"

// Import appropriate header files from the C++ STL
#include <iostream>
#include <string>
using namespace std;

// Default constructor of the unit test for the class printer
printer_ut::printer_ut() {
	cerr << "==tu	Don't instantiate the tester for printer";
	cerr << endl;
	string err_msg = "==tu	Don't use printer's default constructor";
	throw new violated_assertion(err_msg);
}



// Function to test the constructor and functions of printer
void printer_ut::test_printer() {
	cout << "==tu	Testing: printer..." << endl;
	
	//	Test the default and standard constructors of printer.
	test_printer_constructor();
	
	// Function to test the debugging mode
	test_debugging_mode();
	
	// Function to test the output print functions
	test_print_fn();
	
	cout << endl;
}




/**
 * Function to test the default constructor of the class printer.
 * @param - None
 * @return - Nothing
 */
void printer_ut::test_printer_constructor() {
	// Check if printer should not be instantiated.
	try {
		printer::num_test_cases_eval();
		cout << "==tu	>>	Testing: default constructor." << endl;
		printer *my_printer = new printer();
	}
	catch (violated_assertion *va_ex) {
		cout << "==tu	==>	default constructor works." << endl;
		printer::num_passed_test_cases_eval();
	}
}




/**
 * Function to test the debugging mode.
 * @param - None.
 * @return - Nothing.
 */
void printer_ut::test_debugging_mode() {
	// Check if the default debugging mode is FALSE.
	cout << "==tu	>>	Is the default debugging mode FALSE?";
	printer::num_test_cases_eval();
	if(!printer::is_debugging_mode()) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "		NO!!!" << endl;
	}
	// Set the debugging mode to TRUE.
	printer::set_debugging_mode(true);
	// Check if the debugging mode is now set to TRUE.
	cout << "==tu	>>	Is program in debugging mode?";
	printer::num_test_cases_eval();
	if(printer::is_debugging_mode()) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "			NO!!!" << endl;
	}
}




/**
 * Function to test the output print functions.
 * @param - None.
 * @return - Nothing.
 */
void printer_ut::test_print_fn() {
	printer::set_debugging_mode(false);
	cout << "==tu	>>	Print message outside debugging mode fail?";
	printer::num_test_cases_eval();
	printer::debug_std_op("Message shall not be printed.");
	printer::debug_std_err("Error Message shall not be printed.");
	cout << "	Yes." << endl;
	printer::num_passed_test_cases_eval();
	printer::set_debugging_mode(true);
	printer::debug_std_op("==tu		Message shall be printed.");
	printer::debug_std_err("==tu		Error Message shall be printed.");
	cout << "==tu	>>	Print a message in debugging mode?";
	printer::num_test_cases_eval();
	cout << "		Yes." << endl;
	printer::num_passed_test_cases_eval();
}

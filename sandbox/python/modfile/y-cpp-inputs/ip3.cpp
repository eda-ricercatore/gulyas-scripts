/**
 * Test/Utilities_t package:
 * Submodule of Test package to test classes in the Utilities package.
 *
 * File_io_ut class:
 * Class that tests the File_IO class.
 * The constructors and functions of the File_IO class shall be tested.
 * 
 * IMPORTANT NOTE:
 * As of Jan 7, 2012 at 1706 hrs, the function [dump_output()] would
 *	not be tested in this test suite since it has yet to be implemented.
 * This function shall be tested upon the completion of the software
 *	at a later date.
 * 
 *
 *
 * Copyright	(C)	<2010-2011>	<Zhiyang Ong>
 * @author Zhiyang Ong
 * @version 1.0.0
 * @since January 1, 2011
 *
 * This program is free software: you can redistribute it and/or modify
 *	it under the terms of the GNU General Public License as published by
 *	the Free Software Foundation, either version 3 of the License, or
 *	(at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 *	but WITHOUT ANY WARRANTY; without even the implied warranty of
 *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *	GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 *	along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

// Import Header files from the other modules of Tiramisu.
#include "file_io_ut.h"

// Import appropriate header files from the C++ STL
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

// --------------------------------------------------------------

// Default constructor of the unit test for the class file_io
file_io_ut::file_io_ut() {
	cerr << "==tu	Don't instantiate the tester for file_io";
	cerr << endl;
	string err_msg = "==tu	Don't use file_io_ut's default constructor";
	throw new violated_assertion(err_msg);
}

// --------------------------------------------------------------

// Function to test the constructor and functions of file_io
void file_io_ut::test_file_io() {
	cout << endl;
	cout << "==tu	Testing: file_io..." << endl;
	
	//	Test the default and standard constructors of file_io.
	test_file_io_constructor();
	
	
	/**
	 * Test the accessor functions for getting the filenames of
	 * the standard and error output log files.
	 */
	test_get_log_filenames();
	
	
	/**
	 * Test the mutator function for assigning the filenames of
	 * the standard and error output log files.
	 */	
	test_set_log_filenames();
	
	
	// Test functions concerning the logging mode.
	test_logging_mode();
	
	// Test functions for printing messages to output files.
	test_file_op_print_fn();
	
	// Test functions for other file I/O operations.
	test_file_IO_fn();
		
	// Test miscellaneous functions.
	test_misc_fn();
	
	cout << endl << endl;
}




/**
 * Function to test the default constructor of the class file_io.
 * @param - None
 * @return - Nothing
 */
void file_io_ut::test_file_io_constructor() {
	// Check if file_io should not be instantiated.
	try{
		printer::num_test_cases_eval();
		cout << "==tu	>>	Testing: default constructor." << endl;
		file_io *my_file_io = new file_io();
	}catch(violated_assertion *va_ex) {
		cout << "==tu	==>	default constructor works." << endl;
		printer::num_passed_test_cases_eval();
	}
}



/**
 * Function to test the accessor functions for getting the
 * filenames of the standard and error output log files.
 * @param - None
 * @return - Nothing
 */
void file_io_ut::test_get_log_filenames() {
	// Determine if the default values for the filenames are empty
	cout << "==tu	>>	standard_logfile has a non-empty default value?";
	printer::num_test_cases_eval();
	if(!file_io::get_std_log_filename().empty()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
	}

	cout << "==tu	>>	error_logfile has a non-empty default value?";
	printer::num_test_cases_eval();
	if(!file_io::get_std_log_filename().empty()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
	}
}



/**
 * Function to test the mutator function for assigning the
 * filenames of the standard and error output log files.
 * @param - None
 * @return - Nothing
 */
void file_io_ut::test_set_log_filenames() {
	// New filenames of the output log files
	string op_o = "output.txt";
	string op_e = "error.txt";
	// Assign values to the filenames of the output log files
	file_io::set_log_filenames(op_o, op_e);
	
	// Check the updated value of standard_logfile
	cout << "==tu	>>	Is assignment of standard_logfile correct?";
	printer::num_test_cases_eval();
	if(0 == op_o.compare(file_io::get_std_log_filename())) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
		/**
		 * The compare() function for strings in the C++ STL returns
		 * ZERO if the strings are equivalent.
		 */
	}else{
		cout << "	NO!!!" << endl;
		cout << "==tu	==>	Value of get_std_log_filename()::";
		cout << file_io::get_std_log_filename() << endl;
	}
	
	// Check the updated value of error_logfile
	cout << "==tu	>>	Is assignment of error_logfile correct?";
	printer::num_test_cases_eval();
	if(0 == op_e.compare(file_io::get_err_log_filename())) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "		NO!!!" << endl;
		cout << "==tu	==>	Value of get_err_log_filename()::";
		cout << file_io::get_err_log_filename() << endl;
	}
}




/**
 * Function to test the logging mode.
 * @param - None.
 * @return - Nothing.
 */
void file_io_ut::test_logging_mode() {
	// Check if the default logging mode is FALSE.
	cout << "==tu	>>	Is the default logging mode FALSE?";
	printer::num_test_cases_eval();
	if(!file_io::is_logging_mode()) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "		NO!!!" << endl;
	}
	// Set the logging mode to TRUE.
	file_io::set_logging_mode(true);
	// Check if the logging mode is now set to FALSE.
	cout << "==tu	>>	Is program in logging mode?";
	printer::num_test_cases_eval();
	if(file_io::is_logging_mode()) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "			NO!!!" << endl;
	}
}



/**
 * Function to test the file output print functions.
 * @param - None.
 * @return - Nothing.
 */
void file_io_ut::test_file_op_print_fn() {
	// Set up file I/O operations.
	file_io::set_up_file_io();
	// Disable logging mode.
	file_io::set_logging_mode(false);
	
	cout << "==tu	>>	Is the Verilog file stream closed?";
	printer::num_test_cases_eval();
	if(!file_io::fstream_is_open("v")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	// Open the file I/O streams.
	file_io::open_io_streams();
	
	cout << "==tu	>>	Print message outside logging mode fail?";
	printer::num_test_cases_eval();
	file_io::fileIO_std_op("Message shall not be printed.");
	file_io::fileIO_std_err("Error Message shall not be printed.");
	cout << "	Yes." << endl;
	printer::num_passed_test_cases_eval();
	// Enable logging mode.
	file_io::set_logging_mode(true);
	cout << "==tu	>>	Print a message in logging mode?";
	printer::num_test_cases_eval();
	file_io::fileIO_std_op("==tu		Message shall be printed.");
	file_io::fileIO_std_err("==tu		Error Message shall be printed.");
	cout << "		Yes." << endl;
	printer::num_passed_test_cases_eval();
file_io::fileIO_std_op("==tu		Print another message.");
	// Close the file I/O streams.
//	file_io::close_io_streams();
	/**
	 * MAJOR BUG FOUND!!!
	 * In the debugging mode, messages printed to the logging files
	 *	are not recorded when the file streams are closed.
	 * Why???
	 */
}



/**
 * Function to test the functions for reading from input file streams
 *	and writing to output file streams.
 * It also tests if these file streams can be opened and closed.
 * @param - None.
 * @return - Nothing.
 */
void file_io_ut::test_file_IO_fn() {
	string temp="";
	
//cout << "==tu	>>	>>	>>	>>	>>	>>	>>"<<endl;
	cout << "==tu	>>	Is list of input filenames initally empty?";
	printer::num_test_cases_eval();
	if(0 == file_io::get_input_filenames().size()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}

	cout << "==tu	>>	Is list of output filenames initally empty?";
	printer::num_test_cases_eval();
	if(0 == file_io::get_output_filenames().size()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	cout << "==tu	>>	Is list of I/O filenames initally empty?";
	printer::num_test_cases_eval();
	if(0 == file_io::get_ip_op_filenames().size()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	// Set up file I/O.
	file_io::set_up_file_io();
	file_io::set_delimiters(". \t");
	file_io::set_io_filenames(file_io::generate_ip_filenames(),file_io::generate_op_filenames(),file_io::generate_io_filenames());
	// Open the file I/O streams.
	file_io::open_io_streams();
	
	
	// Read from the Verilog file.
	file_io::read_fr_an_input_file_stream("spef",temp);
//cout<<"SPEF::"<<temp<<"="<<endl;
	cout << "==tu	>>	Does the line of text being read contain data?";
	printer::num_test_cases_eval();
	if(!temp.empty()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
	}
	// Keep reading from the SPEF file till its EOF.
	cout << "==tu	>>	Have we reached the end of the SPEF file?";
	printer::num_test_cases_eval();
	while (!file_io::ip_fstream_at_eof("spef")) {
		file_io::read_fr_an_input_file_stream("spef",temp);
	}
	cout << "	Yes." << endl;
	printer::num_passed_test_cases_eval();
	
	
	cout << "==tu	>>	Is the Verilog file stream open?";
	printer::num_test_cases_eval();
	if(file_io::fstream_is_open("v")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "		NO!!!" << endl;
	}
	
	cout << "==tu	>>	Verilog: Do init and cur get ptr pos differ?";
	printer::num_test_cases_eval();
	int init_get_ptr_pos = file_io::find_get_pointer_position("v");
	file_io::read_fr_an_input_file_stream("v",temp);
	file_io::read_fr_an_input_file_stream("v",temp);
	file_io::read_fr_an_input_file_stream("v",temp);
	file_io::read_fr_an_input_file_stream("v",temp);
	file_io::read_fr_an_input_file_stream("v",temp);
	int cur_get_ptr_pos = file_io::find_get_pointer_position("v");
	if(init_get_ptr_pos != cur_get_ptr_pos) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
	}
	
	/**
	 * Reset the get pointer position of the input file stream to
	 *	the beginning.
	 */
	file_io::restart_ip_file_proc("v");
	cout << "==tu	>>	Reset Verilog ifstream:Token #1@ln 1=module?";
	printer::num_test_cases_eval();
	file_io::read_fr_an_input_file_stream("v",temp);
	if(0 == file_io::str_tokenizer(temp).front().compare("module")) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
		cout<<"	TEMP!!!"<<temp<<"==="<<endl;
	}
	// Reset the position of the get pointer again.
	file_io::restart_ip_file_proc("v");
	

	// Write to the 'sizes' file.
	temp="Hello World";
	// Find the initial location of o/p file stream's put pointer.
	long init_ofs_p = file_io::get_put_pointer_position("sizes");
	file_io::write_to_an_output_file_stream("sizes",temp);
	// Find the final location of o/p file stream's put pointer.
	long final_ofs_p = file_io::get_put_pointer_position("sizes");
	cout << "==tu	>>	Do put pointers differ due to write operation?";
	printer::num_test_cases_eval();
	if(final_ofs_p != init_ofs_p) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else{
		cout << "	NO!!!" << endl;
	}
	
//cout << "==tu	~~		~~		~~		~~"<<endl;

file_io::fileIO_std_op("==tu		Print yet another message.");
	// Close the file I/O streams.
//	file_io::close_io_streams();
}


/**
 * Function to test the miscellaneous functions for file_io.
 * This includes functions concerning determining and
 *	validating file extensions, string tokenization, and
 *	standard/error file output.
 * It also tests functions concerning the name and location
 *	of benchmarks.
 * In addition, it tests the initialization [set_up_file_io()]
 *	function of file_io.
 * @param - None.
 * @return - Nothing.
 */
void file_io_ut::test_misc_fn() {
	// Temporary string.
	string temp;
	
	cout << "==tu	>>	Is the file extension of 'qwerty.sdc' sdc?";
	printer::num_test_cases_eval();
	if(0 == file_io::get_file_extn("qwerty.sdc").compare("sdc")) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	
	try{
		printer::num_test_cases_eval();
		// Are random file extensions rejected (e.g., 'qwerty.uio')?
		if(0 == file_io::get_file_extn("qwerty.uio").compare("uio")) {
			cout << "	Yes. What? violated_assertion not thrown???" << endl;
		}else {
			cout << "	NO!!!" << endl;
		}
	}catch(violated_assertion *va) {
		cout << "==tu	>>	Reject rndm file extns (e.g., 'qwerty.uio')?";
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}
	
	
	try{
		printer::num_test_cases_eval();
		cout << "==tu	>>	Is #tokens for int.sizes file correct?";
		if(0 == file_io::get_file_extn("qwerty.int.sizes").compare("int.sizes")) {
			cout << "		Yes." << endl;
			printer::num_passed_test_cases_eval();
		}else {
			cout << "	NO!!!" << endl;
		}
	}catch(violated_assertion *va) {
		cerr << "==tu	>>	Error in processing 'int.sizes' files.";
		cerr << endl;
	}
	
	
	
	try{
		printer::num_test_cases_eval();
		// Does error in processing empty filenames exist?
		if(0 == file_io::get_file_extn("").compare("int.sizes")) {
			cout << "==tu	>>	Does empty string has no file extension?";
			cout << "		Yes. What??? No exception thrown???" << endl;
		}else {
			cout << "	NO!!!" << endl;
		}
	}catch(violated_precondition *vpr) {
		cout << "==tu	>>	Does error in processing empty filenames exist?";
		cerr << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}
	
	
	try{
		printer::num_test_cases_eval();
		// Does error in processing filename without file extension exist?
		if(0 == file_io::get_file_extn("myfilename").compare("int.sizes")) {
			cout << "==tu	>>	No error in processing filename w/o file extn?";
			cout << "		Yes. What??? No exception thrown???" << endl;
		}else {
			cout << "	NO!!!" << endl;
		}
	}catch(violated_assertion *vpr) {
		cout << "==tu	>>	Err in processing fname w/o file extn?";
		cout << "		Yes.";
		cout << endl;
		printer::num_passed_test_cases_eval();
	}catch(violated_postcondition *vpr) {
		cerr << "==tu	>>	Error in processing filename w/o file extn?";
		cerr << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}
	
	
	
	cout << "==tu	>>	Is the location './' a valid dir?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_loc_valid("./")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	cout << "==tu	>>	Are '../../qwerty' and 'zxcvbnm' invalid dirs?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_loc_valid("/data/2012/projects/gs-n-va/qwerty/")
		|| (file_io::is_bmk_loc_valid("zxcvbnm")) ) {
		cout << "	NO!!!" << endl;
	}else {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}
	
	cout << "==tu	>>	Is this valid location a valid dir?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_loc_valid("/data/2012/projects/gs-n-va/unwanted/try_concepts_here")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	
	cout << "==tu	>>	Is the benchmark 'simple' valid?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_valid("simple")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	cout << "==tu	>>	Is the benchmark 'qwerty' invalid?";
	printer::num_test_cases_eval();
	if(!file_io::is_bmk_valid("qwerty")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	cout << "==tu	>>	Is this directory an invalid benchmark?";
	printer::num_test_cases_eval();
	if(!file_io::is_bmk_valid("/data/2012/projects/gs-n-va/unwanted/try_concepts_here")) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	
	cout << "==tu	>>	Is this benchmark path invalid?";
	printer::num_test_cases_eval();
	if(!file_io::is_bmk_valid("/data/2012/projects/gs-n-va/tiramisu/benchmarks/leon3mp")) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "			NO!!!" << endl;
	}
	
	
	cout << "==tu	>>	Is the current benchmark location valid?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_loc_valid(file_io::get_bmk_loc())) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	cout << "==tu	>>	Is the current benchmark valid?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_valid(file_io::get_name_of_bmk())) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "			NO!!!" << endl;
	}
	
	// Modify the location of benchmarks.
	temp = "/data/2012/projects/gs-n-va/benchmarks/ispd2012";
	file_io::set_bmk_loc(temp);
	cout << "==tu	>>	Is the new benchmark location valid?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_loc_valid(file_io::get_bmk_loc())) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	cout << "==tu	>>	Is the new benchmark location correct?";
	printer::num_test_cases_eval();
	if(0 == temp.compare(file_io::get_bmk_loc())) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	// Modify the name of the benchmark.
	temp = "usb_phy";
	file_io::set_name_of_bmk(temp);
	cout << "==tu	>>	Is the new benchmark valid?";
	printer::num_test_cases_eval();
	if(file_io::is_bmk_valid(file_io::get_name_of_bmk())) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "			NO!!!" << endl;
	}
	cout << "==tu	>>	Is the new benchmark correct?";
	printer::num_test_cases_eval();
	if(0 == temp.compare(file_io::get_name_of_bmk())) {
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "			NO!!!" << endl;
	}
	
	
	
	// Modify the location of benchmarks to an invalid directory.
	try{
		printer::num_test_cases_eval();
		file_io::set_bmk_loc("/data/2012/projects/gs-n-va/qwerty/ispd2012");
		cout << "==tu	>>	BMK_LOC ERROR. DO NOT print this!";
		cout << endl;
	}catch(violated_precondition *vp) {
		cout << "==tu	>>	Is updated benchmark location invalid?";
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}

	
	// Modify the name of the benchmark to an invalid benchmark.
	try{
		printer::num_test_cases_eval();
		file_io::set_name_of_bmk("random_benchmark");
		cout << "==tu	>>	BMK_ERROR. DO NOT print this!" << endl;
	}catch(violated_precondition *vp) {
		cout << "==tu	>>	Is updated benchmark invalid?";
		cout << "			Yes." << endl;
		printer::num_passed_test_cases_eval();
	}
	
	temp = "first1secondmthird$fourth&fifth";
	file_io::set_delimiters("1m$&");
	str_vec tokens = file_io::str_tokenizer(temp);
//cout<<"delimiters are::"<<file_io::get_delimiters()<<"="<<endl;
	cout << "==tu	>>	Is this string correctly delimited?";
	printer::num_test_cases_eval();
	if((0 == tokens[0].compare("first"))
		&& (0 == tokens[1].compare("second"))
		&& (0 == tokens[2].compare("third"))
		&& (0 == tokens[3].compare("fourth")) 
		&& (0 == tokens[4].compare("fifth")) ) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	
	cout << "==tu	>>	Is the set of delimiting characters NOT empty?";
	printer::num_test_cases_eval();
	if(0 != file_io::get_delimiters().size()) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	temp = file_io::get_delimiters();
	// Modify the set of delimiting characters.
	file_io::set_delimiters("asdfghjk");
	cout << "==tu	>>	For delimiters: modified != original?";
	printer::num_test_cases_eval();
	if(0 != temp.compare(file_io::get_delimiters())) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	cout << "==tu	>>	Is 's' a delimiter?";
	printer::num_test_cases_eval();
	if(file_io::is_delimiter('s')) {
		cout << "				Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "				NO!!!" << endl;
	}
	cout << "==tu	>>	Is '.' not a delimiter?";
	printer::num_test_cases_eval();
	if(!file_io::is_delimiter('.')) {
		cout << "				Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "				NO!!!" << endl;
	}
	
	
	// Set up file I/O
	file_io::set_up_file_io();
	cout << "==tu	>>	Is 'random' an invalid input file extension?";
	printer::num_test_cases_eval();
	if((!file_io::chk_ip_file_extn("random")) && (!file_io::chk_file_extn("random"))) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	cout << "==tu	>>	Is 'spef' a valid input file extension?";
	printer::num_test_cases_eval();
	if((file_io::chk_ip_file_extn("spef")) && (file_io::chk_file_extn("spef"))) {
		cout << "		Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "		NO!!!" << endl;
	}
	
	
	// Generate some I/O filenames.
//cout<<"Before - i/o fnames ::"<<file_io::get_ip_op_filenames().size()<<"="<<endl;
	file_io::set_delimiters(". \t");
	file_io::set_io_filenames(file_io::generate_ip_filenames(),file_io::generate_op_filenames(),file_io::generate_io_filenames());
//cout<<"After - i/o fnames ::"<<file_io::get_ip_op_filenames().size()<<"="<<endl;
	cout << "==tu	>>	Is 'int.sizes' a valid input file extension?";
	printer::num_test_cases_eval();
	if((file_io::chk_ip_file_extn("int.sizes")) && (file_io::chk_file_extn("int.sizes"))) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	
	cout << "==tu	>>	Is 'random' an invalid output file extension?";
	printer::num_test_cases_eval();
	if((!file_io::chk_op_file_extn("random")) && (!file_io::chk_file_extn("random"))) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	cout << "==tu	>>	Is 'sizes' a valid output file extension?";
	printer::num_test_cases_eval();
	if((file_io::chk_op_file_extn("sizes")) && (file_io::chk_file_extn("sizes"))) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	cout << "==tu	>>	Is 'timing' a valid output file extension?";
	printer::num_test_cases_eval();
	if((file_io::chk_op_file_extn("timing")) && (file_io::chk_file_extn("timing"))) {
		cout << "	Yes." << endl;
		printer::num_passed_test_cases_eval();
	}else {
		cout << "	NO!!!" << endl;
	}
	// Test the check_file_extension functions.
}

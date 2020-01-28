#!/usr/local/bin/python3

import warnings

# ============================================================
##	Method to determine the factorial of "number_to_compute"
#		by recursion.
#	@param given_number - Number to determine the factorial of.
#	@return the factorial of given_number (if it is a non-negative
#		integer);
#		else, return 'None'.
#	O(n) method, where n is the number of test cases used.
def get_factorial_recursion(given_number):
	if isinstance(given_number, int):
		if (0 == (given_number) or (1 == given_number)):
			return 1
		elif (0 > given_number):
			warnings.warn("The factorial of a negative number cannot be determined.")
			return None
		else:
			return given_number * calculate_factorial.get_factorial_recursion(given_number - 1)
	elif isinstance(given_number, float):
		warnings.warn("The factorial of a floating-point number cannot be determined.")
		return None
	else:
		warnings.warn("The factorial of a non-integer cannot be determined.")
		return None


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	print("Calculate the factorial of a given number.")
	warnings.filterwarnings("error")
	prompt = "= Test: get_factorial_iteration('This is a string!')	{}."
	try:
		if None == get_factorial_recursion('This is a string!'):
			print(prompt .format("OK"))
		else:
			print(prompt .format("FAIL!!!"))
	except DeprecationWarning: 
		print(prompt .format("OK"))

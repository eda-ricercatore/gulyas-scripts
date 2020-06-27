#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to try out Solutions 1-4
		from [Sceenivasan, 2017].

	Reference for Solutions 1, 2, 3, and 4 [Sceenivasan, 2017]:
	Sreeram Sceenivasan, "How to implement a switch-case statement
		in Python: No in-built switch statement here," from JAXenter.com,
		Software {\rm \&}\ Support Media {GmbH}, Frankfurt, Germany,
		October 24, 2017.
		Available online from JAXenter.com at: https://jaxenter.com/implement-switch-case-statement-python-138315.html; June 26, 2020 was the last accessed date
		
	See https://gist.github.com/eda-ricercatore/8cbb931f330af2b5e96edaa8b89ed0c4
		for the public GitHub Gist of this.
"""


#	--------------------------------------------------------
# Solution 1.
def switch_demo(argument):
	switcher = {
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December"
	}
	#print(switcher.get(argument, "Invalid month"))
	return switcher.get(argument, "Invalid month")	


#	--------------------------------------------------------
# Solution 2.
def one():
	return "January"
 
def two():
	return "February"
 
def three():
	return "March"
 
def four():
	return "April"
 
def five():
	return "May"
 
def six():
	return "June"
 
def seven():
	return "July"
 
def eight():
	return "August"
 
def nine():
	return "September"
 
def ten():
	return "October"
 
def eleven():
	return "November"
 
def twelve():
	return "December"

# For solution 4, create a case for the 93th month.
def new_month():
	return "new-month-created"
"""
	Redundant function.
	For solution 4, create a catch-all case for invalid input.
def invalid_input():
	return "Invalid month"
"""




"""
	Create a dictionary with function names as values, rather
		than basic data types such as strings and integers/floats,
		since the values of a Python dictionary can be of any
		data type.
	Likewise, we can also use lambdas as values for a dictionary.
	
	This enables users to use the dictionary "to execute ...
		blocks of code within each function".
"""
def numbers_to_months(argument):
	switcher = {
		1: one,
		2: two,
		3: three,
		4: four,
		5: five,
		6: six,
		7: seven,
		8: eight,
		9: nine,
		10: ten,
		11: eleven,
		12: twelve
	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "Invalid month")
	# Execute the function
	#print(func())
	return func()


#	--------------------------------------------------------
# Solution 3.
class Switcher(object):
	def numbers_to_months(self, argument):
		#Dispatch method
		method_name = 'month_' + str(argument)
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Invalid month")
		# Call the method as we return it
		return method()
	def month_1(self):
		return "January"
	def month_2(self):
		return "February"
	def month_3(self):
		return "March"
	def month_4(self):
		return "April"
	def month_5(self):
		return "May"
	def month_6(self):
		return "June"
	def month_7(self):
		return "July"
	def month_8(self):
		return "August"
	def month_9(self):
		return "September"
	def month_10(self):
		return "October"
	def month_11(self):
		return "November"
	def month_12(self):
		return "December"



#	--------------------------------------------------------
# Solution 4.

switcher = {
	1: one,
	2: two,
	3: three,
	4: four,
	5: five,
	6: six,
	7: seven,
	8: eight,
	9: nine,
	10: ten,
	11: eleven,
	12: twelve
}

"""
	Published Solution 4 in [Sceenivasan, 2017] fails to work
		for the default case, or the catch-all case for cases
		not covered in the dictionary named "switcher".
	
	Used a lambda function to provide the catch-all case for
		cases not covered in the dictionary named "switcher".
"""
def numbers_to_strings(argument):
	# Get the function from switcher dictionary
	#func = switcher.get(argument, "nothing")
	func = switcher.get(argument, lambda: "Invalid month")
	# Execute the function
	return func()




#	--------------------------------------------------------
# Solution from [patel, 2017]

def f(x):
	return {
		1 : "output for case 1",
		2 : "output for case 2",
		3 : "output for case 3"
	}.get(x, "default case")   




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("===	Trying solutions from [Sceenivasan, 2017].")
	#print("Get month for 9:",switch_demo(9),"=")
	print("Trying Solution 1.")
	print("=	Testing: switch_demo().")
	for x in range(1, 12+1):
		print("Get month for:",x,"named:",switch_demo(x),"=")
	print("Get month for 56798:",switch_demo(56798),"=")
	print("Get month for -443:",switch_demo(-443),"=")
	print("Trying Solution 2.")
	print("=	Testing: numbers_to_months().")
	for x in range(1, 12+1):
		print("Get month for:",x,"named:",numbers_to_months(x),"=")
	print("Get month for 56798:",numbers_to_months(56798),"=")
	print("Get month for -443:",numbers_to_months(-443),"=")
	print("Trying Solution 3.")
	print("=	Testing: Switcher class solution with lambda function.")
	a=Switcher()
	for x in range(1, 12+1):
		print("Get month for:",x,"named:",a.numbers_to_months(x),"=")
	print("Get month for 56798:",a.numbers_to_months(56798),"=")
	print("Get month for -443:",a.numbers_to_months(-443),"=")
	print("Trying Solution 4.")
	print("=	Testing: numbers_to_strings() method with modification to dictionary.")
	for x in range(1, 12+1):
		print("Get month for:",x,"named:",numbers_to_strings(x),"=")
	print("	- Modify the case for the 8th month to the 3rd month, March.")
	switcher[8] = three
	print("Get month for 8:",numbers_to_strings(8),"=")
	print("	- Create a case for the 93th month.")
	switcher[93] = new_month
	print("Get month for 93:",numbers_to_strings(93),"=")
	print("Get month for 56798:",numbers_to_strings(56798),"=")
	print("Get month for -443:",numbers_to_strings(-443),"=")
	"""
		Additional resources that I looked at:
		+ Prashant Kumar, Answer to "What is the Python equivalent for a case/switch statement? [duplicate]," Stack Exchange Inc., New York, NY, December 3, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/11479840/1531728; June 27, 2020 was the last accessed date.
			- This is used as Solution 1 in [Sceenivasan, 2017].
		+ Raymond Hettinger, Answer to "Why doesn't Python have switch-case?," Stack Exchange Inc., New York, NY, October 12, 2017. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/46701087/1531728; June 27, 2020 was the last accessed date.
			- "We considered it at one point, but without having a way to declare named constants, there is no way to generate an efficient jump table. So all we would be left with is syntactic sugar for something we could already do with if-elif-elif-else chains.
			- "See PEP 275 and PEP 3103 for a full discussion."
				* https://www.python.org/dev/peps/pep-0275/
				* https://www.python.org/dev/peps/pep-3103/
			- "Roughly the rationale is that the various proposals failed to live up to people's expections about what switch-case would do, and they failed to improve on existing solutions (like dictionary-based dispatch, if-elif-chains, getattr-based dispatch, or old-fashioned polymorphism dispatch to objects with differing implementations for the same method)."
		+ wim glenn, Answer to "Why doesn't Python have switch-case?," Stack Exchange Inc., New York, NY, October 12, 2017. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/46701135/1531728; June 27, 2020 was the last accessed date.
			- https://docs.python.org/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
		+ vedant patel and Vincenzo Carrese, Answer to "Why doesn't Python have switch-case?," Stack Exchange Inc., New York, NY, December 20, 2017. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/47902285/1531728; June 27, 2020 was the last accessed date.
			- [patel, 2017]
	"""
	print("Trying Solution from [patel, 2017].")
	print("=	Testing: dictionary method, alternate specification/declaration.")
	"""
		range(1, 3+2) results in 1, 2, 3, 4, since range(x,y)
			results in x, x+1, ..., y-2, y-1.
	"""
	for x in range(1, 3+2):
	#for x in range(1, 8):
		print("Trying index:",x,"with output:",f(x),"=")

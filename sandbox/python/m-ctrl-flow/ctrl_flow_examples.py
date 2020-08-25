#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to try out different things with
		control statements that shape the control flow.
"""



###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	"""
		Reference:
		+ 
	"""
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
			- References the following:
				* Shrutarshi Basu, "Switch-case statement in Python",
					Powerful Python series, The ByteBaker, Cambridge, MA,
					November 3, 2008.
					Available online from The ByteBaker: Powerful Python at: 
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

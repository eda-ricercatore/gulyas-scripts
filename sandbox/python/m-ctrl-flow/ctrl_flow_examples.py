#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to try out different things with
		control statements that shape the control flow.
"""

class empty_class():
	pass

def empty_function():
	pass



###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	"""
		Finding out what the "pass" statememt does.

		Does the "pass" statememt actually do nothing?
			Yes. It does nothing, and allows the interpreter and
				execution environment to move on to the next
				statement (if there is any).

		The body of a class or function/method definition can consist only
			only of the "pass" statememt, which results in an
			empty class or method [rlms2013].

		References:
		+ [rlms2013]
			- rlms, Answer to "How do I get a python program to do nothing?", Stack Exchange Inc., New York, NY, October 28, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19632742/1531728 and https://stackoverflow.com/questions/19632728/how-do-i-get-a-python-program-to-do-nothing/19632742#19632742; August 26, 2020 was the last accessed date.
		+ [Lix2013]
			- Lix, Answer to "How do I get a python program to do nothing?", Stack Exchange Inc., New York, NY, October 28, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19632790/1531728 and https://stackoverflow.com/questions/19632728/how-do-i-get-a-python-program-to-do-nothing/19632790#19632790; August 26, 2020 was the last accessed date.
		+ [Aggarwal2019]
			- nikhilaggarwal3 (Nikhil Aggarwal???), "Python Continue Statement," GeekstoGeeks, Noida, Uttar Pradesh, India, November 22, 2019. Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-continue-statement/; August 27, 2020 was the last accessed date
		+ [DrakeJr2016a, \S7.9 for the break statement, \S7.10 for the continue statement, and \S7.4 for the pass statement]

	"""
	print("Before the 1st if-else statement.")
	if(5 == 20/4):
		print("Entered the 1st if statement.")
		pass
		# The following statement is printed anyway.
		print("After the pass statement in the 1st if statement.")
	else:
		print("Entered the 1st else statement.")
	print("After the 1st if-else statement.")
	print("=	Another attempt.")
	print("Before the 2nd if-else statement.")
	if(5 == (38-33)):
		pass
		# The following statement is printed anyway.
		print("After the pass statement in the 2nd if statement.")
	else:
		print("Entered the 2nd else statement.")
	print("=	Yet another attempt.")
	print("Before the 3rd if-else statement.")
	if(6 == (39-33)):
		pass
		# The following statement is printed anyway.
	else:
		print("Entered the 3rd else statement.")
	print("After the 3rd if-else statement.")
	a = empty_class()
	print("a is:",a,"=")
	empty_function()
	print("= Called and executed empty function.")
	"""
		The continue statement cannot be used with only an "if statement".

		It has to be used with a loop, because of its definition in the
			Python Language Reference.
	
	print("Before the 4th if-else statement.")
	if(10 == (93-83)):
		continue
		# The following statement is printed anyway.
		print("After the continue statement in the 4th if statement.")
	else:
		print("Entered the 4th else statement.")
	print("=	4th attempt.")
	"""
	print("Before a 'for loop' with an embedded 'if-else statement'.")
	for x in range(1,10):
		if(0 == (x%2)):
			continue
			# The following statement is not printed.
			print("After the continue statement in the 'for loop' with an embedded 'if-else statement'.")
		else:
			print("x is:",x,"=")
	print("=	End of 'for loop' with an embedded 'if-else statement'.")
	"""
		The following solution gets stuck in an infinite loop.
	"""
	print("Before a 'while loop' with an embedded 'if-else statement'.")
	x = 15
	while 4 < x:
		x = x - 1
		if(0 == (x%2)):
			continue
			# The following statement is not printed.
			print("After the continue statement in the 'while loop' with an embedded 'if-else statement'.")
		else:
			print("x is:",x,"=")
		"""
			Putting the increment statement here causes it to
				become an infinite loop.
		"""
		#x = x - 1
	print("=	End of 'while loop' with an embedded 'if-else statement'.")
	print("Before a 'for loop' with embedded 'if-else' and break statements.")
	for x in range(1,10):
		if(0 == (x%6)):
			break
			# The following statement is not printed.
			print("After the break statement in the 'for loop' with embedded 'if-else' and break statements.")
		else:
			print("x is:",x,"=")
	print("=	End of 'for loop' with embedded 'if-else' and break statements.")
	print("Before a 'while loop' with another embedded 'if-else statement'.")
	x = 17
	while 4 < x:
		if(0 == (x%6)):
			break
			# The following statement is not printed.
			print("After the continue statement in the 'while loop' with another embedded 'if-else statement'.")
		else:
			print("x is:",x,"=")
		x = x - 1
	print("=	End of 'while loop' with another embedded 'if-else statement'.")
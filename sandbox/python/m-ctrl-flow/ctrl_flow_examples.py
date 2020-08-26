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
		Finding out what the "pass" statememt does.

		Does the "pass" statememt actually do nothing?
			Yes. It does nothing, and allows the interpreter and
				execution environment to move on to the next
				statement (if there is any).

		#### TODO
		+ Cite references that explain the "pass" statememt.
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
	print("=	Another attempt")
	print("Before the 2nd if-else statement.")
	if(5 == (38-33)):
		pass
		# The following statement is printed anyway.
		print("After the pass statement in the 2nd if statement.")
	else:
		print("Entered the 2nd else statement.")
	print("=	Yet another attempt")
	print("Before the 3rd if-else statement.")
	if(6 == (39-33)):
		pass
		# The following statement is printed anyway.
	else:
		print("Entered the 3rd else statement.")
	print("After the 3rd if-else statement.")
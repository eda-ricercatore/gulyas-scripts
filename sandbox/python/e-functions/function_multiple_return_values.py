#!/Users/zhiyang/anaconda3/bin/python3

"""
This Python script is written by Zhiyang Ong to try out ideas
	with Python functions that return multiple values.
	
	Solutions that I experimented with to return multiple values:
	+ as a tuple \cite{Agrawal20XY}
	+ 
	
	
	
	Alternatives:
	+ as an object \cite{Agrawal20XY}
	+ as a dictionary \cite{Agrawal20XY}
	
	
	
	References:
	+ \cite{Agrawal20XY}
"""

# Return multiple values using a tuple.
def return_multiple_values():
	x = 30
	y = 58
	z = 91
	return x, y, z

# Return multiple values using a tuple.
def return_multiple_values_2():
	x = 30
	y = 58
	z = 91
	return (x, y, z)

# Return multiple values using a list.
def return_multiple_values_3():
	x = 30
	y = 58
	z = 91
	return [x, y, z]

# Return multiple values using a set.
def return_multiple_values_4():
	x = 30
	y = 58
	z = 91
	return {x, y, z}

# Return multiple values using a dictionary.
def return_multiple_values_5():
	return {"xxx":30, "yyy":58, "zzz":91}



a, b, c = return_multiple_values()
print("a is:",a,".")
print("b is:",b,".")
print("c is:",c,".")
abc = return_multiple_values()
print("abc is:",abc,".")
print("	Is the type of 'abc' a tuple?:",type(abc) is tuple,"=")
try:
	ab, bc = return_multiple_values()
	print("ab is:",ab,".")
	print("bc is:",bc,".")
except ValueError:
	print("=	For functions that return more than 3 values,")
	print("	their output can't be assigned to a subset of those values.")
	print("=	In Python, multiple (& separate) return values automatically get grouped as a tuple.")
	print("=	Tuples cannot be broken up separately with reassigning them to other variables")



a1, b1, c1 = return_multiple_values_2()
print("a1 is:",a1,".")
print("b1 is:",b1,".")
print("c1 is:",c1,".")
abc1 = return_multiple_values_2()
print("abc1 is:",abc1,".")
try:
	ab1, bc1 = return_multiple_values_2()
	print("ab1 is:",ab1,".")
	print("bc1 is:",bc1,".")
except ValueError:
	print(">	For functions that return more than 3 values,")
	print("	their output can't be assigned to a subset of those values.")
	print(">	In Python, multiple (& separate) return values automatically get grouped as a tuple.")
	print(">	Tuples cannot be broken up separately with reassigning them to other variables")





a_list = return_multiple_values_3()
print("a_list[0] is:",a_list[0],".")
print("a_list[1] is:",a_list[1],".")
print("a_list[2] is:",a_list[2],".")

a_set = return_multiple_values_4()
print("my set is:",a_set,"=")

a_dict = return_multiple_values_5()
print("my dictionary is:",a_dict,"=")
adic = a_dict["xxx"]
bdic = a_dict["yyy"]
cdic = a_dict["zzz"]
print("adic is:",adic,".")
print("bdic is:",bdic,".")
print("cdic is:",cdic,".")
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

def return_multiple_values():
	x = 30
	y = 58
	z = 91
	return x, y, z


def return_multiple_values_2():
	x = 30
	y = 58
	z = 91
	return (x, y, z)

def return_multiple_values_3():
	x = 30
	y = 58
	z = 91
	return [x, y, z]


a, b, c = return_multiple_values()
print("a is:",a,".")
print("b is:",b,".")
print("c is:",c,".")


a1, b1, c1 = return_multiple_values_2()
print("a1 is:",a1,".")
print("b1 is:",b1,".")
print("c1 is:",c1,".")


a_list = return_multiple_values_3()
print("a_list[0] is:",a_list[0],".")
print("a_list[1] is:",a_list[1],".")
print("a_list[2] is:",a_list[2],".")
#!/usr/local/bin/python3




# Use the math.ceil() and math.floor() functions
import math


print("============================================")

print("= Experiments with the 'round()', 'ceil()', and 'floor()' methods/functions.")
print("")

a = 32.1923
b = math.ceil(a)
print("math.ceil(32.1923) is:",b,".")
c = math.floor(a)
print("math.floor(32.1923) is:",c,".")
"""
	Use the round() function to round off numbers, instead of the
		following functions.
	+ math.ceil()
	+ math.floor()
"""
d = round(a)
print("d is:",d,".")
d = round(54.9744)
print("d - 54.9744) -is:",d,".")
d = round(546789.57928)
print("d  - 54.9744) -i is:",d,".")
d = round(152.5)
print("d is:",d,".")
d = round(5392.67089043,3)
print("d is:",d,".")


"""
	References:
	+ https://stackoverflow.com/questions/20296125/python-decimal-and-import-how-to-use-round-up-without-import
	+ https://stackoverflow.com/questions/37825909/round-python-decimal-to-nearest-0-05
"""

"""
import decimal
d = decimal.Decimal(612.65439708969).quantize(decimal.Decimal(612.65439708969),rounding=decimal.ROUND_UP)
print("d is:",d,".")
"""




print("------------------------------------ floating-point")

print("= Round off to nearest incremental step size between the start-point and the end-point.")

print("")

increments_for_0_25 = [0, 0.25/2, 0.25, 0.25+0.25/2, 0.5, 0.5+0.25/2, 0.75, 0.75+0.25/2, 1.0]
print("increments_for_0_25 is:",increments_for_0_25,"=")
start_point = 0
end_point = 10
increments = 0.25
increments_for_x = [(i+1)*increments/2 for i in range(0,10)]
print("(i+1)*increments/2 for range(0,10) is:",increments_for_x,"=")
increments_for_x = [(i)*increments/2 for i in range(start_point,end_point)]
print("(i)*increments/2 for range(start_point,end_point) is:",increments_for_x,"=")
"""
	TO-DO!!! TO BE COMPLETED!!!
	Implement this as a function and test it.

	This solution is acceptable, since I can customize this in a
		function call using variables.
"""
increments_for_x = [(i)*increments/2 for i in range(start_point,end_point-1)]
print("(i)*increments/2 for range(start_point,end_point-1) is:",increments_for_x,"=")

"""
	Round each floating-point number in the list to the nearest
		increment.

	Reference:
	+ Scott Hunter, Answer to "Python round to nearest .0125",
		Stack Exchange Inc., New York, NY, February 6, 2018.
		Available online from Stack Exchange Inc.: Stack Overflow:
			Questions at: https://stackoverflow.com/a/48638894/1531728
			and https://stackoverflow.com/questions/48638805/python-round-to-nearest-0125/48638894#48638894;
			March 4, 2020 was the last accessed date.
"""
a_number = 234.8343
increments = 0.25
print("round(a_number/increments)*increments for 234.8343 is:",round(a_number/increments)*increments,"=")
half_increments = increments/2

#dt = 0.2
#xdt = 12.5
#t_max = 14
"""
t_max = 14.0
def xdt(n):
	return dt*float(n)
"""
"""
	The following statement does not work.
	tlist  = list(map(xdt, range(int(t_max/dt)+1)))

	Error message:
		TypeError: 'int' object is not callable
"""
#tlist  = map(xdt, range(int(t_max/dt)+1))

#tlist  = map(dt*float(i), i in range(int(t_max/dt)+1))
dt = 0.2
t_max = 14
number_of_increments = round(t_max/dt)
print("round(t_max/dt) is:",round(t_max/dt),"=")
#end_point = int(t_max/dt)
#end_point = Integer(t_max/dt)		# If I want to use SymPy's Integer() method.
#end_point = int(number_of_increments)
tlist = [dt*float(i) for i in range(int(round(t_max/dt))+1)]
#tlist = [dt*float(i) for i in range(number_of_increments+1)]
#tlist_list = list(tlist)
print("tlist is:",tlist,"=")
a = [dt*int(i/dt) for i in tlist]
print("dt*round(i/dt) for i in tlist is:",a,"=")
#!/usr/local/bin/python3
###!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s



print("============================================")

print("= Experiments to determine the arithmetic mean, or average, of the absolute value of numbers in a list.")

# Python code to illustrate  
# abs() built-in function 
  
# floating point number 
float = -54.26
print('Absolute value of float -54.26 is:', abs(float),"=") 
  
# An integer 
int = -94
print('Absolute value of integer -94 is:', abs(int),"=") 
  
# A complex number 
complex = (3 - 4j) 
print('Absolute value, or magnitude, of complex number (3 - 4j) is:', abs(complex),"=") 



"""
	Methods to find the average number of numbers in a list.
	
	https://www.geeksforgeeks.org/find-average-list-python/
"""


my_list = [2, -3, 5, -9, -6, 8]
print("my_list is:",my_list,"=")
abs_my_list = []
for elem in my_list:
	abs_my_list.append(abs(elem))
print("abs_my_list:",abs_my_list,"=")

abs_my_list_2 = []
for index, elem in enumerate(my_list):
	#print("index:",index,"=")
	abs_my_list_2.insert(index,abs(elem))
print("abs_my_list_2:",abs_my_list_2,"=")

abs_my_list_3 = np.absolute(my_list)
print("abs_my_list_3:",abs_my_list_3,"=")
"""
	Convert the NumPy array into a (Python) list.
	This makes the NumPy.absolute() solution acceptable.

	Reference:
	+ user3654478, Answer to "How to use a decimal range() step value?,"
		Stack Exchange Inc., New York, NY, February 12, 2016.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions
			at: https://stackoverflow.com/a/35362489/1531728 and
			https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value/35362489#35362489;
			March 4, 2020 was the last accessed date.
"""
abs_my_list_4 = np.absolute(my_list).tolist()
print("abs_my_list_4:",abs_my_list_4,"=")


#sum_of_absolute_numbers = sum(abs(my_list))
sum_of_absolute_numbers = sum(abs_my_list)
print("sum_of_absolute_numbers:",sum_of_absolute_numbers,"=")
#average_of_absolute_numbers = sum(abs(my_list))/len(my_list)
average_of_absolute_numbers = sum(abs_my_list)/len(abs_my_list)
print("average_of_absolute_numbers:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = np.mean(abs_my_list)
print("average_of_absolute_numbers, via NumPy:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = s.mean(abs_my_list)
print("average_of_absolute_numbers, via statistics module/package:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = sum(abs_my_list_3)/len(abs_my_list_3)
print("average_of_absolute_numbers, for abs_my_list_3 - NumPy array:",average_of_absolute_numbers,"=")
print("	The following solution produces a rounded-off/down solution.")
average_of_absolute_numbers = s.mean(abs_my_list_3)
print("average_of_absolute_numbers, via NumPy and absolute():",average_of_absolute_numbers,"=")

print("============================================")

print("= Experiments with the 'None' object, and boolean comparisons using the 'is' operator and the '==' operator.")
print("")

x = None
if x:
	print("if 'x'.")
else:
	print("not 'if x'.")

if x is not None:
	print("if 'x' is not None.")
else:
	print("else 'x' isn't 'not None'; or, 'x' is None.")

if x is None:
	print("if 'x' is None.")
else:
	print("else, 'x' is not None.")


"""
	In this case, they are the same. None is a singleton object (there only ever exists one None).
	is checks to see if the object is the same object, while == just checks if they are equivalent.
	
	Reference:
		https://stackoverflow.com/a/3257951/1531728
"""
p = [1]
q = [1]
if p is q:
	print("p is q; [1] is [1]; something is wrong!!! They point to different objects.")
else:
	print("False because they are not the same actual object.")
if p == q:
	print("p == q; [1] == [1]")
	print("True because they are equivalent.")
else:
	print("p != q; [1] != [1]; something is wrong!!! They are supposed to be equivalent in value/content.")
# But since there is only one None, they will always be the same, and is will return True.
p = None
q = None
if p is q:
	print("True because they are both pointing to the same 'None'.")
else:
	print("Something is wrong, since 'p' and 'q' are supposed to point to the same/only 'None' object.")














print("--------------------------------------------")



try:
	print("Dividing a number, 23, by 0", 23/0,"=")
except ZeroDivisionError:
	print("Cannot dividing 23 by 0.")




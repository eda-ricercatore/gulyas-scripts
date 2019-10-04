#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s



# Python code to illustrate  
# abs() built-in function 
  
# floating point number 
float = -54.26
print('Absolute value of float is:', abs(float)) 
  
# An integer 
int = -94
print('Absolute value of integer is:', abs(int)) 
  
# A complex number 
complex = (3 - 4j) 
print('Absolute value or Magnitude of complex is:', abs(complex)) 



"""
	Methods to find the average number of numbers in a list.
	
	https://www.geeksforgeeks.org/find-average-list-python/
"""


my_list = [2, -3, 5, -9, -6, 7]
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



#sum_of_absolute_numbers = sum(abs(my_list))
sum_of_absolute_numbers = sum(abs_my_list)
print("sum_of_absolute_numbers:",sum_of_absolute_numbers,"=")
#average_of_absolute_numbers = sum(abs(my_list))/len(my_list)
average_of_absolute_numbers = sum(abs_my_list)/len(abs_my_list)
print("average_of_absolute_numbers:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = np.mean(abs_my_list)
print("average_of_absolute_numbers, via NumPy:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = s.mean(abs_my_list)
print("average_of_absolute_numbers, via NumPy:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = sum(abs_my_list_3)/len(abs_my_list_3)
print("average_of_absolute_numbers, for abs_my_list_3:",average_of_absolute_numbers,"=")
print("	This solution produces a rounded-off/down solution.")
average_of_absolute_numbers = s.mean(abs_my_list_3)
print("average_of_absolute_numbers, via NumPy and absolute():",average_of_absolute_numbers,"=")


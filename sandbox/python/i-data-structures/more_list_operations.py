#!/usr/local/bin/python3



"""
	This is written by Zhiyang Ong to demonstrate how to scale
		a list by a scalar factor (or, scaling factor, or scale
		factor).
	
	References:
	+ See references cited in text.
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.
"""


string_of_names = "Min Chen and Sergio Gonzalez and Athanasios Vasilakos and Huasong Cao and Victor C. M. Leung"


"""
	The following method works.
	
	References:
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.
"""
#list_of_names = string_of_names.split(' and ')
list_of_names = string_of_names.split(" and ")
print("list_of_names is:",list_of_names,"=")
print("string_of_names.split(' and ') is:",string_of_names.split(" and "),"=")


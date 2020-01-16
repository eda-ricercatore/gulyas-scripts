#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to enumerate
		multiple lists (of the same length) concurrently.
	
	References:
	+ \cite{Chaudhary2019}
		- indicates how to enumerate two lists concurrently.
		- can be extended to enumerate more lists concurrently.
		- this answer also addresses how to enumerate lists of
			different lengths concurrently.
"""

import itertools



# 3 lists of even length
data1 = range(11,20)
data2 = range(111,120)
data3 = range(211,220)
data4 = range(311,330)




# Enumerate 
for index, (value1, value2) in enumerate(zip(data1, data2)):
	print(index, "value1 is:", value1, ".")
	print(index, "value2 is:", value2, ".")
	print(index, value1 + value2)


for index, (value1, value2, value3) in enumerate(zip(data1, data2, data3)):
	print(index, "value1 is:", value1, ".")
	print(index, "value2 is:", value2, ".")
	print(index, "value3 is:", value3, ".")
	print(index, value1 + value2 + value3)

for index, (value1, value2, value3) in enumerate(zip(data1, data2, data3)):
	print("value1 is:", value1, ".")
	print("value2 is:", value2, ".")
	print("value3 is:", value3, ".")
	print(value1 + value2 + value3)



print("	Enumerating lists of different lengths, for the longest list.")
for i in itertools.zip_longest(data1, data2, data3, data4):
	print(i)



print("	Enumerating lists of different lengths, for the shorter/shortest list.")
for i in itertools.zip_longest(data1, data2, data3, data4):
	print(i)

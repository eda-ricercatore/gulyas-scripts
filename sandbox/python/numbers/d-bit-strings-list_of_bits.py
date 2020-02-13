#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np

a = [int(i) for i in np.binary_repr(0b0111, 4)]
print("0b0111 is:",a,".")
a = [int(i) for i in np.binary_repr(0b000000111, 9)]
print("0b000000111 is:",a,".")
a = [int(i) for i in np.binary_repr(0b11010011, 4)]
print("0b11010011 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0100001, 7)]
print("0b0100001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0001, 4)]
print("0b0001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b0000, 4)]
print("0b0000 is:",a,".")
a = [int(i) for i in np.binary_repr(0b1001, 4)]
print("0b1001 is:",a,".")
a = [int(i) for i in np.binary_repr(0b10000000000, 11)]
print("0b10000000000 is:",a,".")

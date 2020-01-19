#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to experiment with scientific
"""


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s



nanosecond_threshold = 0.000000001
microsecond_threshold = 0.000001
millisecond_threshold = 0.001

ns_threshold = 1.00000000e-09
us_threshold = 1.00000000e-06
ms_threshold = 1.00000000e-03

if ns_threshold == nanosecond_threshold:
	print("1.00000000e-09 == 0.000000001")
if us_threshold == microsecond_threshold:
	print("1.00000000e-06 == 0.000001")
if ms_threshold == millisecond_threshold:
	print("1.00000000e-03 == 0.001")



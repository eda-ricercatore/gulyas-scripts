#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to experiment with scientific
		notations.
	
	References:
	+ http://extraconversion.com/time/nanoseconds/nanoseconds-to-seconds.html
		- ExtraConversion staff, "Nanoseconds to Seconds Conversion Calculator",
			from {Extra Conversion: Time Conversion: Nanosecond}, ExtraConversion.com, no address, 2020.
			Available from {Extra Conversion: Time Conversion: Nanosecond} at: http://extraconversion.com/time/nanoseconds/nanoseconds-to-seconds.html;
				last accessed on January 19, 2020.
	+ Joe Sexton, "Nanoseconds to Seconds Conversion", from {Inch Calculator, Find Your Calculator: Unit Conversion Calculators: Time Conversion Calculators: Nanoseconds Conversion},
		Calc Hub, LLC, 2020.
		Available from {Inch Calculator, Find Your Calculator: Unit Conversion Calculators: Time Conversion Calculators: Nanoseconds Conversion} at:
			https://www.inchcalculator.com/convert/nanosecond-to-second/;
			last accessed on January 19, 2020.
"""



import numpy as np
import numpy.testing as npt
# From https://docs.python.org/3/library/statistics.html
import statistics as s


a = 7189325435.3435345634
b = 7189325435.34353456447665
c = 7189325435.798765543
d = 7189325535.3435345634
e = 7199325435.3435345634
f = 7209325435.3435345634


try:
	if not npt.assert_approx_equal(a,b):
		print("'a' and 'b' are approximately equal.")
	else:
		print("'a' and 'b' are NOT approximately equal!!!")
except AssertionError as e:
	print("'a' and 'b' are NOT approximately equal!!! Oops.")
try:
	if not npt.assert_approx_equal(a,c):
		print("'a' and 'c' are approximately equal.")
	else:
		print("'a' and 'c' are NOT approximately equal!!!")
except AssertionError as e:
	print("'a' and 'c' are NOT approximately equal!!! Oops.")
try:
	if not npt.assert_approx_equal(a,d):
		print("'a' and 'd' are approximately equal.")
	else:
		print("'a' and 'd' are NOT approximately equal!!!")
except AssertionError as e:
	print("'a' and 'd' are NOT approximately equal!!! Oops.")

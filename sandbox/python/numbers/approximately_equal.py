#!/Users/zhiyang/anaconda3/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3 -m unittest
###!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to experiment with scientific
		notations.
	
	
	
	Notes:
	+ From https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm,
	
	
	
	Complete referencing the publications cited in this document!!!
	
	
	
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
"""
	To use the npt.assert_approx_equal() function.
		Or, np.testing.assert_almost_equal() function.
		Or, numpy.testing.assert_almost_equal() function.
"""
import numpy.testing as npt
# From https://docs.python.org/3/library/statistics.html
import math					# To use the math.isclose() function.
#import statistics as s		# To use the
"""
	To use the unittest.assertAlmostEqual() and
		unittest.assertNotAlmostEqual() functions.
"""
import unittest



a = 7189325435.3435345634
b = 7189325435.34353456447665
c = 7189325435.798765543
d = 7189325535.3435345634
e = 7199325435.3435345634
f = 7209325435.3435345634


print("==============================================")
print("Use assert_approx_equal() from numpy.testing.")

try:
	if not npt.assert_approx_equal(a,b):
		print("'a' and 'b' are approximately equal.")
	else:
		print("'a' and 'b' are NOT approximately equal!!!")
except AssertionError as ef:
	print("'a' and 'b' are NOT approximately equal!!! Oops.")




try:
	if not npt.assert_approx_equal(a,c):
		print("'a' and 'c' are approximately equal.")
	else:
		print("'a' and 'c' are NOT approximately equal!!!")
except AssertionError as ef:
	print("'a' and 'c' are NOT approximately equal!!! Oops.")




try:
	if not npt.assert_approx_equal(a,d):
		print("'a' and 'd' are approximately equal.")
	else:
		print("'a' and 'd' are NOT approximately equal!!!")
except AssertionError as ef:
	print("'a' and 'd' are NOT approximately equal!!! Oops.")




try:
	if not npt.assert_approx_equal(a,e):
		print("'a' and 'e' are approximately equal.")
	else:
		print("'a' and 'e' are NOT approximately equal!!!")
except AssertionError as ef:
	print("'a' and 'e' are NOT approximately equal!!! Oops.")



try:
	if not npt.assert_approx_equal(a,f):
		print("'a' and 'f' are approximately equal.")
	else:
		print("'a' and 'f' are NOT approximately equal!!!")
except AssertionError as ef:
	print("'a' and 'f' are NOT approximately equal!!! Oops.")













print("==============================================")
print("Use isclose() from math (Python Standard Library).")

"""
	References:
	+ https://docs.python.org/3/library/math.html#math.isclose
		- \cite[From math — Mathematical functions, for Python version 3.8.1]{DrakeJr2016b}
		- Can set relative and absolute tolerance.
	+ https://www.python.org/dev/peps/pep-0485/
		- PEP 485 -- A Function for testing approximate equality
			* \cite{Barker2015}
	+ Salim Fadhley and {Fermi paradox}, ``Function to determine if two numbers are nearly equal when rounded to n significant decimal digits,'' Stack Exchange Inc., New York, NY, August 5, 2016. Available online from {Stack Exchange Inc.: Stack Overflow: Questions} at: https://stackoverflow.com/questions/558216/function-to-determine-if-two-numbers-are-nearly-equal-when-rounded-to-n-signific; February 27, 2019 was the last accessed date.
"""

if math.isclose(a,b):
	print("'a' and 'b' are approximately equal.")
else:
	print("'a' and 'b' are NOT approximately equal!!!")



if math.isclose(a,c):
	print("'a' and 'c' are approximately equal.")
else:
	print("'a' and 'c' are NOT approximately equal!!!")



if math.isclose(a,d):
	print("'a' and 'd' are approximately equal.")
else:
	print("'a' and 'd' are NOT approximately equal!!!")



if math.isclose(a,e):
	print("'a' and 'e' are approximately equal.")
else:
	print("'a' and 'e' are NOT approximately equal!!!")



if math.isclose(a,f):
	print("'a' and 'f' are approximately equal.")
else:
	print("'a' and 'f' are NOT approximately equal!!!")






"""
	References:
	+ \cite[From Development Tools: unittest — Unit testing framework]{DrakeJr2016b}
	+ \cite{TutorialsPointContributors2020}
		- https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm
	+ \cite{Pajankar2017b}
	+ https://www.ics.uci.edu/~pattis/ICS-33/lectures/unittest.txt
	+ https://www.eandbsoftware.org/unit-tests-in-python-python-tutorial-learn-python-programming/
	+ serv-inc, Answer to ``Function to determine if two numbers are nearly equal when rounded to n significant decimal digits,'' from {Stack Exchange Inc.: Stack Overflow: Questions}, August 22, 2018.
		Available at: https://stackoverflow.com/a/51963714/1531728;
			last accessed January 20, 2020. 
	
"""

"""
print("==============================================")
print("Use assertAlmostEqual() from unittest (Python Standard Library).")

	IMPORTANT NOTE:
		This does not work for me...
		Try to attempt this in the future.

		Make sure to use the following Linux/UNIX shebang:
			#!/Users/zhiyang/anaconda3/bin/python3 -m unittest
"""
#if unittest.assertAlmostEqual(a,b,places=9,msg="'a' and 'b' should be equal."):
#if unittest.assertAlmostEqual(a,b,msg="'a' and 'b' should be equal."):
#if unittest.assertAlmostEqual(a,b):
"""
if unittest.TestCase.assertAlmostEqual(self,a,b):
	print("'a' and 'b' are approximately equal; places=9.")
else:
	print("'a' and 'b' are NOT approximately equal!!! places=9.")
if unittest.assertAlmostEqual(a,b,msg="'a' and 'b' should be equal.",delta=0.001):
	print("'a' and 'b' are approximately equal; delta=0.001.")
else:
	print("'a' and 'b' are NOT approximately equal!!! delta=0.001.")
"""
#unittest.assertNotAlmostEqual()



"""
	Other dodgy/sketchy approaches not considered.
	+ SingleNegationElimination, Answer to ``Function to determine if two numbers are nearly equal when rounded to n significant decimal digits,'' Stack Exchange Inc., New York, NY, May 7, 2009. Available online from {Stack Exchange Inc.: Stack Overflow: Questions} at: https://stackoverflow.com/a/564086/1531728; January 20, 2020 was the last accessed date.
		- Returns the comparison (math.log10(average/difference) > 3)

	There is a interesting solution to this by B. Dawson (with C++ code) at "Comparing Floating Point Numbers". His approach relies on strict IEEE representation of two numbers and the enforced lexicographical ordering when said numbers are represented as unsigned integers.
	+ https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/
		- B. Dawson (with C++ code) at "Comparing Floating Point Numbers"
"""



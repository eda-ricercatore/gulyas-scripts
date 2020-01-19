#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to experiment with scientific
		notations.
	
	References:
	+ http://extraconversion.com/time/nanoseconds/nanoseconds-to-seconds.html
		- ExtraConversion staff, "Nanoseconds to Seconds Conversion Calculator",
			from {\it Extra Conversion: Time Conversion: Nanosecond}, ExtraConversion.com, no address, 2020.
			Available from {\it Extra Conversion: Time Conversion: Nanosecond} at: http://extraconversion.com/time/nanoseconds/nanoseconds-to-seconds.html;
				last accessed on January 19, 2020.
	+ Joe Sexton, "Nanoseconds to Seconds Conversion", from {\it Inch Calculator, Find Your Calculator: Unit Conversion Calculators: Time Conversion Calculators: Nanoseconds Conversion},
		Calc Hub, LLC, 2020.
		Available from {\it Inch Calculator, Find Your Calculator: Unit Conversion Calculators: Time Conversion Calculators: Nanoseconds Conversion} at:
			\url{https://www.inchcalculator.com/convert/nanosecond-to-second/};
			last accessed on January 19, 2020.
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


"""
	Use "%e" to get the scientific notation format.
	
	Reference:
	+ \cite{Mattiuzzo2019}
"""
# Get scientific notation of number in 2 decimal places.
x = 12345678901234567890.534
print("{0:.2E}".format(x))
# 1.23E+19
# Get scientific notation of number in 3 decimal places.
print("{0:.3E}".format(x))
# 1.235E+19



"""
	\cite[\S Routines: Input and output, String formatting]{TheSciPyCommunity2019c}
"""

#!/Users/zhiyang/anaconda3/bin/python3

import time
#from datetime import date
#from datetime import datetime
#from datetime import date, datetime, tzinfo, timezone
from datetime import date, datetime, timezone
#import datetime

#utctimestamp = datetime.utcfromtimestamp()
utctimestamp = date.fromtimestamp(time.time())
print("1) current time, date.fromtimestamp(time.time(), is:",utctimestamp,"=")
#utctimestamp = datetime.utcfromtimestamp(time.time())
#print("current time is:",utctimestamp,"=")
utctimestamp = time.time()
print("2) current time, time.time(), is:",utctimestamp,"=")
#utctimestamp = datetime.utcnow()
#utctimestamp = datetime.now()
"""
utctimestamp = datetime.utcnow().timestamp()
print("3) current time is:",utctimestamp,"=")
utctimestamp = datetime.utcnow()
print("4) current time is:",utctimestamp,"=")
"""

current_milli_time = lambda: int(round(time.time() * 1000))
current_timestamp = current_milli_time()
print("5) current time, int(round(time.time() * 1000)), is:",current_timestamp,"=")


"""
	Conclusion:
		Use time.time() to measure time in seconds.
"""
utctimestamp = time.time()
print("current time, time.time(), is:",utctimestamp,"=")
current_date = date.fromtimestamp(utctimestamp)
print("current date, date.fromtimestamp(time.time()), is:",current_date,"=")
current_date_time = datetime.fromtimestamp(utctimestamp)
print("current date, datetime.fromtimestamp(time.time()), is:",current_date_time,"=")
current_date_time = datetime.utcfromtimestamp(utctimestamp)
print("current date, datetime.utcfromtimestamp(time.time()), is:",current_date_time,"=")
#current_date_time = datetime(tzinfo=timezone.utc).timestamp()
#current_date_time = time.time()
current_date_time = datetime.now()
current_date_time = current_date_time.replace(tzinfo=timezone.utc)
print("current date, datetime.now().replace(tzinfo=timezone.utc), is:",current_date_time,"=")



"""
	Remarks/Comments:
	
	"Unix time (also known as Epoch time,[1][2][3] POSIX time,[4] seconds since the Epoch,[5] or UNIX Epoch time[6]) is a system for describing a point in time."
		References:
			Wikipedia contributors, ``Unix time,'' in {\it Wikipedia, The Free Encyclopedia: Calendaring standards}, Wikimedia Foundation, San Francisco, CA, September 15, 2019. Available online from {\it Wikipedia, The Free Encyclopedia: Calendaring standards} at: \url{https://en.wikipedia.org/wiki/Unix_time}; last accessed on September 16, 2019.
			\cite{DrakeJr2016b}
				https://docs.python.org/3/library/time.html#time.time
"""

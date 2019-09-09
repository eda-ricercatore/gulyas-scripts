#!/Users/zhiyang/anaconda3/bin/python3

import time
#from datetime import date
#from datetime import datetime
from datetime import date, datetime
#import datetime

#utctimestamp = datetime.utcfromtimestamp()
utctimestamp = date.fromtimestamp(time.time())
print("1) current time is:",utctimestamp,"=")
#utctimestamp = datetime.utcfromtimestamp(time.time())
#print("current time is:",utctimestamp,"=")
utctimestamp = time.time()
print("2) current time is:",utctimestamp,"=")
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
print("5) current time is:",current_timestamp,"=")


"""
	Conclusion:
		Use time.time() to measure time in seconds.
"""
utctimestamp = time.time()
print("current time is:",utctimestamp,"=")
current_date = date.fromtimestamp(utctimestamp)
print("current date is:",current_date,"=")
current_date_time = datetime.fromtimestamp(utctimestamp)
print("current date is:",current_date_time,"=")

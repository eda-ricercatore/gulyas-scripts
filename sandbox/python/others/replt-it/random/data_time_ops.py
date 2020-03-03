import statistics as s
import datetime
import operator


#if __name__ == "__main__":
class dt_ops:
	@staticmethod
	def test_date_time_methods():
		a = [1, 2, 3, 4, 5]
		print("a's arithmetic mean is:",s.mean(a),".")
		b = str(datetime.timedelta(seconds=45))
		print("b is:",b,".")
		b = str(datetime.timedelta(seconds=32*60+17))
		print("b is:",b,".")
		b = str(datetime.timedelta(seconds=15*60*60+32*60+17))
		print("b is:",b,".")
		b = str(datetime.timedelta(seconds=73*24*60*60+15*60*60+32*60+17))
		print("b is:",b,".")
		print("=========================================================")
		a = False
		print("'a' is:",a,"=")
		b = False
		print("'b' is:",b,"=")
		c = operator.xor(a, b)
		print("xor(a, b) is:",c,"=")
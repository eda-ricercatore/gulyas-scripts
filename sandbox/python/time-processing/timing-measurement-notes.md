#	Notes about Timing Measurements


+ [get_factorial.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/get_factorial.py)
	- Functions to calculate factorials using:
		* iteration
		* recursion
+ [experimental data](compare_different_methods_to_measure_elapsed_periods.csv)
	- Experimental data stored in a [comma-separated values file](https://en.wikipedia.org/wiki/Comma-separated_values) that should be plot with [Matplotlib](https://matplotlib.org/).
+ performance/timing measurements
	- [performance_measurement.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/performance_measurement.py)
	- [performance_measurement_1.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/performance_measurement_1.py)
		* Measure current time with: ***timeit.timeit()***
	- [performance_measurement_2.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/performance_measurement_2.py)
		* Measure current time with: ***time.perf_counter()***
	- [performance_measurement_3.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/performance_measurement_3.py)
		* Measure current time with: ***time.process_time_ns()***
	- [test_time_operations.py](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/sandbox/python/time-processing/test_time_operations.py)
		* Sandbox to test different ways of measuring the current time.



##	To-Do List

Merge code into my BDA code base. Port it to Google Colab projects.

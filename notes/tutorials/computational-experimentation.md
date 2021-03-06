#	Notes for Computational Experimentation

##	Accuracy and Precision

+ \cite{Carter2005c}:
	- "Accuracy refers to the closeness of a measured value to a standard or known value."
	- "Precision refers to the closeness of two or more measurements to each other."
	- "Precision is independent of accuracy."
+ \cite{Pierce2019}:
	- "Accuracy is how close a measured value is to the actual (true) value."
	- "Precision is how close the measured values are to each other."
	- "aCcurate is Correct (a bullseye)".
	- "pRecise is Repeating (hitting the same spot, but maybe not the correct spot)".
	- "When we measure something several times and all values are close, they may all be wrong if there is a `Bias'."
	- "Bias is a systematic (built-in) error which makes all measurements wrong by a certain amount."
	- "In each case all measurements are wrong by the same amount. That is bias."
	- "Degree of Accuracy is how precise a measurement is, often shown as the number of decimal places or significant digits."
	- "Accuracy depends on the instrument we are measuring with."
	- "As a general rule," "the degree of accuracy is half a unit each side of the unit of measure."
	- "We should show final values that match the accuracy of our least accurate value used."
	- From "Errors in Measurement: Absolute, Relative and Percentage Error" Web page referred to by \cite{Pierce2019}, \url{https://www.mathsisfun.com/measure/error-measurement.html}:
		* "The Absolute Error is the difference between the actual and measured value." ... Or, the "the size (the absolute value) of the difference."
		* "But ... when measuring we don't know the actual value! So we use the maximum possible error."
		* "The Relative Error is the Absolute Error divided by the actual measurement."
		* "Relative Error =  Absolute Error/Measured Value"
		* "The Percentage Error is the Relative Error shown as a percentage"
			+ "(|Approximate Value − Exact Value|/|Exact Value|) * 100%"
+ \cite{WikipediaContributors2019c}:
	- "Precision is a description of random errors, a measure of statistical variability."
	- Definition \#1: Accuracy "is a description of systematic errors, a measure of statistical bias; low accuracy causes a difference between a result and a `true' value. ISO calls this trueness."
	- Definition \#2: "ISO defines accuracy as describing a combination of both types of observational error above (random and systematic), so high accuracy requires both high precision and high trueness."
	- "Given a set of data points from repeated measurements of the same quantity, the set can be said to be precise if the values are close to each other, while the set can be said to be accurate if their average is close to the true value of the quantity being measured".
	- "The two concepts are independent of each other, so a particular set of data can be said to be either accurate, or precise, or both, or neither."
	- "In the fields of science and engineering, the accuracy of a measurement system is the degree of closeness of measurements of a quantity to that quantity's true value.[1] The precision of a measurement system, related to reproducibility and repeatability, is the degree to which repeated measurements under unchanged conditions show the same results."
+ \cite{ManagementStudyGuideStaff2019}:
	- "A measurement system is said to be accurate, if the average of its observed values is close to the actual value. In other words, values must be observed and their mean be calculated. This mean should then be compared to a standard value. The closer the mean is to the standard value, the more accurate the system is."
	- "Accuracy, therefore pertains to the mean of the observed data."
	- "A measurement system is said to be precise, if the observed values are in close proximity to each other. In other words, the observed values must lie within a small distance from each other. Precision, therefore is a function of the standard deviation of the data that has been observed. The less the standard deviation, the more precise the measurement system is."
	- "The characteristics of a precise system are repeatability and reproducibility."
	- "Repeatability is the ability of a system to produce measurements that are in close proximity to each other when the same person measures it using the same equipment. The factor being varied here is time. A repeatable system ensures that measurements taken over time are consistent."
	- "Reproducibility is the ability of the system to produce consistent measurements when different operators are using different equipment to measure it. A strong system must be capable of giving consistent measurements regardless of who is operating it and with what."
	- "There are 4 possible states that a measurement system can have":
		* Both accurate and precise
		* Accurate but not precise
		* Precise but not accurate
		* Neither accurate nor precise
	- "When accuracy and precision are present in the system together, it gives measurements that are close to the standard value and to each other. This is the desired state of affairs that every measurement system eventually works toward."
+ \cite{MinitabBlogEditor2012}:
	- "Accuracy refers to how close measurements are to the `true' value, while precision refers to how close measurements are to each other."
	- "Accuracy describes the difference between the measurement and the part’s actual value, while precision describes the variation you see when you measure the same part repeatedly with the same device."
	- "Repeatability: The variation observed when the same operator measures the same part repeatedly with the same device."
	- "Reproducibility: The variation observed when different operators measure the same part using the same device."
















![Accuracy and Precision](https://upload.wikimedia.org/wikipedia/commons/3/38/Accuracy_and_precision.svg)
Figure on accuracy and precision.


![High precision and low accuracy](https://upload.wikimedia.org/wikipedia/commons/3/3a/High_precision_Low_accuracy.svg)
Figure on high precision and low accuracy.



![High accuracy and low precision](https://upload.wikimedia.org/wikipedia/commons/1/10/High_accuracy_Low_precision.svg)
Figure on high accuracy and low precision.






















##	wall-clock-time, user-cpu-time, system-cpu-time

Information about wall clock time, wall-clock-time, user cpu time, user-cpu-time, system cpu time, and system-cpu-time:
+ \cite{Humphreys2011}:
	- "wall-clock time [is] really the number of seconds the process has spent on the CPU".
	- "user-cpu time [is] the amount of time spent executing user-code".
	- "kernel-cpu time the amount of time spent in the kernel due to the need of privileged operations (like IO to disk)"
	- Answer by Jonathan Leffler, September 7, 2011.
		* "Wall-clock time is the time that a clock on the wall (or a stopwatch in hand) would measure as having elapsed between the start of the process and 'now'."
		* "The wall-clock time is not the number of seconds that the process has spent on the CPU; it is the elapsed time, including time spent waiting for its turn on the CPU (while other processes get to run)."
		* "The user-cpu time and system-cpu time are pretty much as you said - the amount of time spent in user code and the amount of time spent in kernel code."
		* Comment (December 16, 2014) to his answer in response to somebody's question comment (December 16, 2014) to his answer.
			+ For "a single core machine" (Jonathan Leffler), "wall-clock time will always be greater than the cpu time" (Pacerier)
			+ "Multi-core machines and multi-threaded programs can use more than 1 CPU second per elapsed second" (Jonathan Leffler).
			+ "You cannot derive elapsed time from CPU time for a number of reasons. First, a process can be idle, not consuming any CPU time, for arbitrary periods (for example, a daemon process waiting for a client to connect to it over the network), so it may do nothing for days at a time of elapsed time. Second, if it is running, it may have multiple threads, and if it has, say, 4 threads and there are 4 or more cores on the system, it might rack up 4 CPU seconds of expended effort per second of elapsed time. These show that there's no simple (or even complex) formula that you could use" (Jonathan Leffler, December 6, 2017).
			+ "Are you aware that the Unix kernel runs separately from user programs. When your program makes a system call (for example, read() or getpid()), the kernel executes code on behalf of your program. The kernel also handles pre-emptive multi-tasking so that other programs get their turn to run, and does some general housekeeping work to keep the system running smoothly. This code is executed in 'kernel code' (also in 'kernel mode'). This is distinct from the code you wrote, and the user libraries (including the system C library) that you run" (Jonathan Leffler, October 13, 2018).
	- Answer by Fred Foo, September 7, 2011.
		* "Wall clock time: time elapsed according to the computer's internal clock, which should match time in the outside world. This has nothing to do with CPU usage; it's given for reference."
		* "User CPU time and system time: exactly what you think. System calls, which include I/O calls such as read, write, etc. are executed by jumping into kernel code and executing that."
		* "If wall clock time < CPU time, then you're executing a program in parallel. If wall clock time > CPU time, you're waiting for disk, network or other devices."
+ \cite{WikipediaContributors2019f}:
	- "Conversely, programs running in parallel on more than one processing unit can spend CPU time many times beyond their elapsed time. Since in concurrent computing the definition of elapsed time is non-trivial, the conceptualization of the elapsed time as measured on a separate, independent wall clock is convenient."
+ \cite[\S21 Date and Time]{GNUCLibraryContributors2019}:
	- "Elapsed Time: Data types to represent elapsed times."
	- "Processor And CPU Time: Time a program has spent executing."
	- "Calendar Time: Manipulation of `real' dates and times."
	- \cite[\S21.1 Time Basics]{GNUCLibraryContributors2019}:
		* "A calendar time is a point in the time continuum, for example November 4, 1990, at 18:02.5 UTC. Sometimes this is called `absolute time'."
		* "An interval is a contiguous part of the time continuum between two calendar times, for example the hour between 9:00 and 10:00 on July 4, 1980."
		* "An elapsed time is the length of an interval, for example, 35 minutes. People sometimes sloppily use the word `interval' to refer to the elapsed time of some interval."
		* "An amount of time is a sum of elapsed times, which need not be of any specific intervals."
		* "A period is the elapsed time of an interval between two events, especially when they are part of a sequence of regularly repeating events."
		* "CPU time is like calendar time, except that it is based on the subset of the time continuum when a particular process is actively using a CPU. CPU time is, therefore, relative to a process."
		* "Processor time is an amount of time that a CPU is in use. In fact, it's a basic system resource, since there's a limit to how much can exist in any given interval (that limit is the elapsed time of the interval times the number of CPUs in the processor). People often call this CPU time, but we reserve the latter term in this manual for the definition above."
	- \cite[\S21.3 Processor And CPU Time]{GNUCLibraryContributors2019}:
		* "If you're trying to optimize your program or measure its efficiency, it's very useful to know how much processor time it uses. For that, calendar time and elapsed times are useless because a process may spend time waiting for I/O or for other processes to use the CPU."
		* "CPU time (see Time Basics) is represented by the data type clock_t, which is a number of clock ticks. It gives the total amount of time a process has actively used a CPU since some arbitrary event. On GNU systems, that event is the creation of the process. While arbitrary in general, the event is always the same event for any particular process, so you can always measure how much time on the CPU a particular computation takes by examining the process' CPU time before and after the computation."
	- \cite[\S21.3.1 CPU Time Inquiry]{GNUCLibraryContributors2019}:
		* "In typical usage, you call the clock function at the beginning and end of the interval you want to time, subtract the values, and then divide by CLOCKS_PER_SEC (the number of clock ticks per second) to get processor time."
		* ***"Do not use a single CPU time as an amount of time; it doesn't work that way. Either do a subtraction as shown above or query processor time directly. See Processor Time."***
		* ***"Different computers and operating systems vary wildly in how they keep track of CPU time. It's common for the internal processor clock to have a resolution somewhere between a hundredth and millionth of a second."***
+ \cite{XilinxStaff2013}:
	- CPU time is the time for which the CPU was busy executing the task. It does not take into account the time spent in waiting for I/O (disk IO or network I/O). Since I/O operations, such as reading files from disk, are performed by the OS, these operations may involve a noticeable amount of time in waiting for I/O subsystems to complete their operations. This waiting time will be included in the elapsed time, but not CPU time. Hence CPU time is usually less than the elapsed time.
	- ***But in certain cases, the CPU time may be more than the elapsed time! When multiple threads are used on a multi-processor system or a multi-core system, more than one CPU may be used to complete a task. In this case, the CPU time may be more than the elapsed time.***
+ \cite{jiml82008}:
	- "In a multiprocessor environment, CPU time can exceed wallclock time because you have multiple processors and if your process spends enough time running on more than one processor simultaneously, you'll have that effect. After all, why else would you go multiprocessor, but to have more CPU cycles available per unit of wallclock time?"
+ \cite{Ersenie2010}:
	- "System time - This is the time that the CPU was used for executing system calls. It is literally the time the kernel is using the CPU for its operations. You can think of I/O operations, context switches, inter process communication, memory management, interrupt requests, etc."
	- "User Time - This is the time the CPU spent running your code. It is called user time because the CPU is used by an operation in a program that a user has started."
	- "It is the ratio between user time and system time that gives you the hints on possible performance bottlenecks."
	- "Case 1 - High user time and low system time. This is the sign that the problem lies within your application. In JAVA, this means the problem is inside your JVM. It could be the efficiency of your code, it could be memory leaks leading to garbage collection. This is already a good starting point on your path downwards to finding the source of the problem, since you know you are not delayed/restricted by some system limitations"
	- "Case 2 - Low user time and high system time. High system time usually means that somewhere, somehow a queue is [being] built. Take for example logging. Suppose your application wants to access a log method that is synchronized. Let's go further, and say you have a bunch of users doing something in your application, and the log level is high enough for this method to become a bottleneck. Synchronized basically means that when one thread is executing a synchronized method for an object, all other threads invoking synchronized methods for the same object will suspend execution until the first thread is done with the object. This will eat a lot of the CPU time, that you would actually want spending time in your application, in user time."
	- "Like Kirk was saying in his Java Performance Tuning Workshop, the system time should not grow bigger than 10 %. Any value bigger than that is an alarm that somebody is eating your valuable resources."
	- "Now, you are well prepared and ready to drill down on that problem. You just made sure that the consumer is in your application, and hear all those words like 'sampling', 'tracing', 'profiling', 'backtracing' etc. etc. Where to go, how to start? Once you make sure that your problem is in the code, and the consumer is indeed your application and not some other stuff in JVM (like poor configuration of Garbage Collection leading to excessive Garbage Collections), you need to see where is the CPU being spent. There are two indicators, often misleading if not prepared: Wall Time and CPU Own Time."
	- Wall Time " `In the context of a task being performed on a computer, wall clock time or wall time is a measure of how much real time that elapses from start to end, including time that passes due to programmed (artificial) delays or waiting for resources to become available. In other words, it is the difference between the time at which a task finishes and the time at which the task started.' (Wikipedia)"
	- "CPU Own Time - This is the time actually spent by CPU executing method code, and this is the one you are most interested in. This is where you have to dig: for invocation count vs cpu own time. A low invocations count with a large cpu own time usually means your code is [inefficient]."
+ \cite{Gantan2013}:
	- "CPU or execution time, which measures how much time a CPU spent on executing a program"
	- "wall-clock time, which measures the total time to execute a program in a computer. The wall-clock time is also called elapsed or running time. Compared to the CPU time, the wall-clock time is often longer because the CPU executing the measured program may also be executing other program's instructions at the same time."
	- "system time, which is measured by the system clock. System time represents a computer system's notion of the passing of time. One should remember that the system clock could be modified by the operating system, thus modifying the system time."
	- "Python's time module provides various time-related functions. Since most of the time functions call platform-specific C library functions with the same name, the semantics of these functions are platform-dependent."
	- "time.time vs time.clock. Two useful functions for time measurement are time.time and time.clock. time.time returns the time in seconds since the epoch, i.e., the point where the time starts." "While time.time behaves the same on Unix and on Windows, time.clock has different meanings. On Unix, time.clock returns the current processor time expressed in seconds, i.e., the CPU time it takes to execute the current thread so far. While on Windows, it returns the wall-clock time expressed in seconds elapsed since the first call to this function, based on the Win32 function QueryPerformanceCounter. Another difference between time.time and time.clock is that time.time could return a lower-value than a previous call if the system clock has been set back between the two calls while time.clock always return non-decreasing values."
	- "Which timer is timeit using? According to timeit's source code, it uses the best timer available"
	- "On Windows, the best timer is time.clock"
	- ***"On most other platforms the best timer is time.time"***
	- "Another important mechanism of timeit is that it disables the garbage collector during execution"
	- ***"If garbage collection should be enabled to measure the program's performance more accurately, i.e., when the program allocates and de-allocates lots of objects, then you should enable it during the setup."***
	- timeit.timeit("[v for v in range(10000)]", setup="gc.enable()", number=10000)
	- "Except for very special cases, you should always use the module timeit to benchmark a program. In addition, it is valuable to remember that measuring the performance of a program is always context-dependent since no program is executing in a system with boundless computing resources and an average time measured from a number of loops is always better than one time measured in one execution."







###	Python: Performance Measurement for Timing

+ \cite{Ardit2017}:
	- "The way to measure the script execution time is by using the time built-in Python module."
+ \cite{DrakeJr2016b}:
	- "timeit — Measure execution time of small code snippets"
	- Use timeit as an option ("-m timeit") from the command line, or import the module from the Python Interface for timeit and use it as a function call.
	- https://docs.python.org/3/library/timeit.html
+ [The Python Profilers](https://docs.python.org/3/library/profile.html)
+ [use perf_counter() or process_time()](https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python/7370824)
+ ["timeit.default_timer() is used instead of time.time() or time.clock() because it will choose the timing function that has the higher resolution for any platform."](https://stackoverflow.com/questions/15707056/get-time-of-execution-of-a-block-of-code-in-python-2-7)
+ [Python time module](https://realpython.com/python-time-module/)
	- Understand core concepts at the heart of working with dates and times, such as epochs, time zones, and daylight savings time
	- Represent time in code using floats, tuples, and struct_time
	- Convert between different time representations
	- Suspend thread execution
	- Measure code performance using perf_counter()
	- Avoid the following:
		* from time import time, ctime
		* t = time()
		* ctime(t)
+ https://realpython.com/python-time-module/
+ https://linuxhint.com/python-timeit-module/
+ http://caffe.berkeleyvision.org/tutorial/interfaces.html
	- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html
+ ***https://www.ploggingdev.com/2016/12/performance-measurement-in-python-3/***
	- mprof run mem.py
	- mprof plot
	- kernprof -l -v line.py (requires: pip install line_profiler)
+ https://en.wikipedia.org/wiki/List_of_performance_analysis_tools
+ https://github.com/Neurochrom/iprof
+ ***https://opensource.com/article/18/4/metrics-monitoring-and-python***
+ https://codereview.stackexchange.com/questions/48416/measuring-execution-times
+ start = time.time()
+ timer()
+ datetime.now()
+ advanced profiling with cProfile











From https://stackoverflow.com/questions/25958562/python-time-measure-for-every-function

	python -m profile -s time file.py
	python -m cProfile -s time file.py





From https://stackoverflow.com/questions/766335/python-speed-testing-time-difference-milliseconds:

	from datetime import datetime
	tstart = datetime.now()
	# code to speed test
	tend = datetime.now()
	print tend - tstart



From https://stackoverflow.com/questions/1938048/high-precision-clock-in-python

	import time
	time.time_ns()				#1530228533161016309
	time.time_ns() / (10 ** 9)	# convert to floating-point seconds
								#1530228544.0792289




From https://blog.sicara.com/profile-surgical-time-tracking-python-db1e0a5c06b6

	python -m cProfile load_and_normalize.py

	import cProfile
	cProfile.run('run()')

	pyflame -t python your_code.py | flamegraph > profile.svg	# install pyflame and flamegraph on your computer






From https://docs.opencv.org/trunk/dc/d71/tutorial_py_optimization.html

	e1 = cv.getTickCount()
	# your code execution
	e2 = cv.getTickCount()
	time = (e2 - e1)/ cv.getTickFrequency()



















###	Python: Performance Measurement for Memory Usage


+ ***https://www.ploggingdev.com/2016/12/performance-measurement-in-python-3/***
	- mprof run mem.py
	- mprof plot
	- kernprof -l -v line.py (requires: pip install line_profiler)
+ https://pythonfiles.wordpress.com/2017/05/18/hunting-python-performance-part-2/
+ [mprof](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python)
	- https://pypi.org/project/memory-profiler/
+ [http://pypi.python.org/pypi/Pympler/](https://stackoverflow.com/questions/5022725/how-do-i-measure-the-memory-usage-of-an-object-in-python)
	- import pympler
	- print pympler.asizeof.asizeof(your_object)
+ https://stackoverflow.com/questions/644419/measuring-execution-time-and-memory-used
+ https://stackoverflow.com/questions/552744/how-do-i-profile-memory-usage-in-python
+ https://stackoverflow.com/questions/42845088/python-measure-amount-of-memory-used-in-script
+ https://stackoverflow.com/questions/1331471/in-memory-size-of-a-python-structure
+ https://stackoverflow.com/questions/9850995/tracking-maximum-memory-usage-by-a-python-function
+ https://stackoverflow.com/questions/110259/which-python-memory-profiler-is-recommended
+ https://stackoverflow.com/questions/552744/how-do-i-profile-memory-usage-in-python
+ https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
+ https://stackoverflow.com/questions/53872699/python-and-compression-algorithm-performance
+ http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage
+ https://graph-tool.skewed.de/
+ [Massif: a heap profiler](http://valgrind.org/docs/manual/ms-manual.html)





























#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).

**If these citations/references are not found in this list of references,
	information about them can be found in my *BibTeX* database.**




























#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

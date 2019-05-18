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

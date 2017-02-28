#	This is written by Zhiyang Ong as for build automation in the
#		context of running GNU Octave scripts for testing different
#		concepts in GNU Octave.
#
#       The MIT License (MIT)
#
#       Copyright (c) <2016> <Zhiyang Ong>
#
#       Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#       The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#       Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
#
#       =============================================================
#



#       =============================================================
#       Make targets for build automation.




#       =============================================================
#       Regression Testing.
torture:
	@echo "========================================================="
	@echo "=>	Call function without input arguments nor return variable."
	./a_caller.m
	@echo "========================================================="
	@echo "=>	Call function with input arguments, without return variable."
	./b_caller.m
	@echo "========================================================="
	@echo "=>	Call another function: input arguments, no return variable."
	./c_caller.m
	@echo "========================================================="
	@echo "=>	Call function: input arguments, return variables."
	./d_caller.m
	./d_main_function.m
	@echo "========================================================="
	@echo "=>	Test: Resetting PRNG."
	./e-prng-reset.m
	./e-prng-vector-reset.m
	@echo "========================================================="
	@echo "=>	Test raising errors and error management."
	./f-raising-errors.m
	@echo "=>	Test try-catch block implementation."
	./f-try-catch-block.m
	@echo "=>	Test unwind-protect implementation."
	./f-unwind-protect.m
	@echo "=>	Test error catching."
	./g-catching-errors.m
	@echo "=>	Test debugging mode entry/exit."
	./g-debugging-mode-enter-exit-warning.m
	@echo "=>	Test debugging mode entry/exit (#2)."
	./g-debugging-mode-enter-exit.m
	@echo "=>	Test error recovery: try-catch block."
	./g-error-recovery.m
	@echo "=>	Test raising warnings as errors."
	./g-raising_warnings.m
	@echo "========================================================="
	@echo "=>	Test software profiling."
	./g-profiling.m
	@echo "========================================================="
	@echo "=>	Test basic operations."
	./h-basic-operations.m
	@echo "========================================================="
	@echo "=>	Test structure operations."
	#./h-structures.m
	@echo "========================================================="
	@echo "=>	Test class operations."
	#./i-class.m
	@echo "========================================================="
	@echo "=>	Test string operations."
	./i-strings.m











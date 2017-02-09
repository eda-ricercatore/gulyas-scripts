#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of using
%		the unwind_protect statement in GNU Octave.
%
%
%	The MIT License (MIT)
%
%	Copyright (c) <2016> Zhiyang Ong
%
%	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
%
%	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
%
%	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
%
%	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%	Preamble.
%addpath("/Users/zhiyang/Documents/ricerca/gulyas-scripts/dummy")

disp("============================================================")
disp("	Begin:	Testing Error Management and Exception Handling")


format('long')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%	Matrices with matching dimensions for multiplications.
%	a = [1 2 3]*[4; 5; 6]
%	Matrices with non-matching dimensions for multiplications.
%		Generates an error.
%	a = [1 2 3]*[4; 5; 6; 7; 8; 9]


%	Divide a number by zero.
%		Generates a warning, not an error.
%	a = 57/0


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("------------------------------------------------------------")
disp("	Exception Handling via *unwind_protect*")

disp("	= Divide a number by zero.")
unwind_protect
	a = 57/0
	disp("	= Warning is generated for divide by zero.")
unwind_protect_cleanup
	disp("	= Handle the warning.")
	disp("	= Continue execution of the script.")
	a = 123456
end_unwind_protect
disp("	= Divide a number by zero generates a warning, not an error.")

disp("	= Warnings cannot be handled by *unwind_protect*.")

unwind_protect
	a = 23/45
unwind_protect_cleanup
	disp("	= No Error and No Warning.")
	a = 987654321
end_unwind_protect
disp("	= Cleanup of *unwind_protect* is executed regardless")
disp("		of whether errors/warnings are generated.")

try
	unwind_protect
		a = [1 2 3]*[4; 5; 6; 7; 8; 9]
	unwind_protect_cleanup
		disp("	= Error Caught and Handled.")
		a = 192837465
		disp("	= Terminate Program.")
		disp("	= Program must terminate after executing cleanup.")
		%	Program dies as expected: Error found and caught.
	end_unwind_protect
catch
	disp("	= Proceed with regression testing...")
end_try_catch

%{
	a = [4; 5; 6; 7; 8; 9] * [1 2 3]
	disp("	= Error not caught/handled.")
	disp("	= Program terminated prematurely.")
%}


disp("	= Warnings cannot be handled with *unwind_protect*.")
disp("	= Only errors are handled with *unwind_protect*.")











%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing Error Management and Exception Handling")


#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of using
%		try-and-catch block in GNU Octave.
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
disp("	Error Handling via *try-catch-block*")


disp("	= Multiply two 'unmatched' matrices.")
try
	a = [1 2 3]*[4; 5; 6; 7; 8; 9]
catch
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	a = [1 2 3]*[4; 5; 6]
end_try_catch

disp("	= Divide a number by zero.")
try
	a = 37 / 0
catch
	disp("	= Warning: Divide a number by zero.")
	disp("	= Warning is caught.")
	a = 1234567
end_try_catch

disp("	= Warnings cannot be caught. Only errors are caught.")

disp("	= Perform an operation without error or warning.")
try
	a = 37 / 17
catch
	disp("	= Catch block should not be executed.")
end_try_catch

disp("	= Normal execution. Catch block is not executed.")

disp("------------------------------------------------------------")

disp("	= Repeat: Multiply two 'unmatched' matrices.")
try
	a = [19; 28; 37; 46; 5; 90; 82]*[21; 87]
catch div_by_zero_error_usc
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	a = [9; 1; 8; 2; 7]*[6 4 5 3 21]
	disp("***************************************************")
	disp("=	Print information resulting from the error.")
	div_by_zero_error_usc
end_try_catch










%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing Error Management and Exception Handling")

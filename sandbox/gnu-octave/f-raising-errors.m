#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of managing
%		errors (and exceptions) in GNU Octave.
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
disp("	Begin:	Testing Error Raising")


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
disp("	Raise an Error and Catch It.")



try
	error("=	Raised a silly error.")
catch Unmatched_Matrices_Error
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	a = [1 2 3]*[4; 5; 6]
	Unmatched_Matrices_Error
end_try_catch

disp("------------------------------------------------------------")
disp("	= Raise an Error with Null String.")
error("")
disp("	= Null String Error is ignored.")
disp("------------------------------------------------------------")


%err_id = "Ciao Mondo!";

%	Failed to raise error with ID number.
err_id = 194;
try
	error(err_id, "=	Raised another error.")
catch Unmatched_Matrices_Error_err_id
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	Unmatched_Matrices_Error_err_id
	#if error_id = Unmatched_Matrices_Error_err_id
	
	a = [1 2; 4 3]*[4 9; 5 6]
end_try_catch





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing Testing Error Raising")


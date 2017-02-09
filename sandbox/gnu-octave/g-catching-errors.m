#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of managing
%		errors in GNU Octave.
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


err_val =  beep_on_error()
new_err_val = 57;

try
	error("=	Raised a foolish error.")
catch Unmatched_Matrices_Error
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	a = [1 2 3]*[4; 5; 6]
	Unmatched_Matrices_Error
	old_err_val =  beep_on_error(new_err_val)
	new_err_val = new_err_val + 15;
	not_so_old_err_val =  beep_on_error(new_err_val)
end_try_catch

disp("------------------------------------------------------------")

try
	error("=	Raise another foolish error.")
catch Unmatched_Matrices_Error2
	disp("	= Error: Unmatched Matrices")
	disp("	= Error is caught.")
	a = [1 2; 9 3]*[4 8; 5 6]
	Unmatched_Matrices_Error2
	old_err_val2 =  beep_on_error(new_err_val)
	new_err_val2 = new_err_val + 35;
	not_so_old_err_val2 =  beep_on_error(new_err_val2)
end_try_catch

disp("------------------------------------------------------------")
disp("	= Error value returns from beep_on_error()")
disp("	= 	can't be incremented.")
disp("------------------------------------------------------------")

try
	try
		error("=	Raise yet another foolish error.")
	catch Unmatched_Matrices_Error3
		disp("	= Error: Unmatched Matrices")
		disp("	= Error is caught.")
		a = [1 2 8; 2 9 3; 7 3 54]*[49 89 32; 25 6 20; -12 -21 -43]
		Unmatched_Matrices_Error3
		beep()
		Unmatched_Matrices_Error2
		rethrow(Unmatched_Matrices_Error)
	end_try_catch
catch Unmatched_Matrices_Error4
	disp("	= Finished raising & catching old errors.")
end_try_catch

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Raise an Error and Catch It.")


#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of using
%		variables in GNU Octave.
%
%
%
%	References:
%
%	Citations/References that use the *LaTeX/BibTeX* notation are
%		taken from my *BibTeX* database (set of *BibTeX* entries).
%
%
%
%	The MIT License (MIT)
%
%	Copyright (c) <2017> Zhiyang Ong
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
disp("	Begin:	Testing usage of variables.\n\n")
format('long')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%	Declare and use a function in the same script. 

global x = 1

printf("=	The value of 'x' is (1): %d.\n",x)

function foo()
	global x
	printf("=	The value of 'x' is (3): %d.\n",x)
	x = 92837465
	printf("=	The value of 'x' is (4): %d.\n",x)
endfunction

%	Call the function 'foo'
printf("=	The value of 'x' is (2): %d.\n",x)
foo()
printf("=	The value of 'x' is (5): %d.\n",x)
global x = 82834
printf("=	The value of 'x' is (6): %d.\n",x)
x = 2933476
printf("=	The value of 'x' is (7): %d.\n",x)


function bar()
	global x = 653124
	printf("=	The value of 'x' is (9): %d.\n",x)
	x = 8213246
	printf("=	The value of 'x' is (10): %d.\n",x)
endfunction

printf("=	The value of 'x' is (8): %d.\n",x)
bar()
printf("=	The value of 'x' is (11): %d.\n",x)

function foobar()
	x = 312
	printf("=	The value of 'x' is (13): %d.\n",x)
endfunction
printf("=	The value of 'x' is (12): %d.\n",x)
foobar()
printf("=	The value of 'x' is (14): %d.\n",x)
disp("")
disp("")

function status_update()
	persistent freq = 20;
	printf("=	status_update() is called %d times.\n",++freq)
endfunction

function change_persistent_value_fail()
	persistent call = 70;
	persistent call = 50;
	printf("=	change_persistent_value_fail() is called %d times.\n",++call)
endfunction

function change_persistent_value_pass()
	persistent pp = 30;
	pp = pp + 50;
	printf("=	change_persistent_value_fail() is called %d times.\n",pp)
endfunction



for i=1:7
	status_update()
	change_persistent_value_fail()
	change_persistent_value_pass()
endfor

disp("------------------------------------------------------------")

if(exist("pp","var"))
	disp("	'pp' exists as a variable.")
else
	disp("	'pp' does not exist as a variable.")
endif



if(exist("x","var"))
	disp("	'x' exists as a variable.")
else
	disp("	'x' does not exist as a variable.")
endif

disp("1-----------------------------------------------------------")
type x
disp("2-----------------------------------------------------------")

%type qq
%	Undefined variables will cause an error to be thrown at run time.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing usage of variables.")

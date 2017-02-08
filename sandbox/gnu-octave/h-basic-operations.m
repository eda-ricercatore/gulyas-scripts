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
disp("	Begin:	Testing basic operations.")
disp("=	Testing all data types, except data containers")
disp("		(i.e., struc and cell array).")
format('long')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("=	Pre- matrix transpose operation.")
a = [1 2 3; 4 5 6; 7 8 9; 10 11 12; 13 14 15]
b = a'
disp("=	Matrix transpose operation: Finished.")

c = 17:3:29
printf("The range of i is: %d.\n",c)
d = [c]
e = "Ciao Mondo!"

disp("=	Get the type of 'a', 'b', 'c', 'd', and 'e'.")
type_of_a = typeinfo(a)
type_of_b = typeinfo(b)
type_of_c = typeinfo(c)
type_of_d = typeinfo(d)
type_of_e = typeinfo(e)


printf("=	The value of sizemax is:	%d.\n",sizemax)
printf("=	The value of intmax is:		%d.\n",intmax)
if(sizemax < intmax)
	printf("=	sizemax %d < intmax %d is expected.\n",sizemax,intmax)
endif
printf("=	The value of realmax is:	%f.\n",realmax)
printf("=	The value of realmin is:	%f.\n",realmin)
printf("=	The value of realmax is:	%e.\n",realmax)
printf("=	The value of realmin is:	%e.\n",realmin)
printf("=	The value of eps is:		%g.\n",eps)
printf("=	Value of eps(294345.32423):	%g.\n",eps(294345.32423))
printf("=	eps(1,2,3,'single'):		%g.\n",eps(1,2,3,"single"))
printf("=	eps('single'):			%g.\n",eps("single"))
printf("=	eps('double'):			%g.\n",eps("double"))
%{
	"eps" indicates the precision of the machine, specifically the
	relative spacing between any pair of adjacent numbers in the
	floating point system of the machine. 
	"eps" is system dependent.
	"eps(x) returns the distance between 'x' and the next largest value."
	\cite{Abbott2016,Eaton2016}.
%}
print("=	Explicitly represent a matrix." matlab, %g,)
print("=	Compare matrices to NA (not available), using isna(g)", %g,)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing basic operations.")


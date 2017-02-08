#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of string
%		manipulation in GNU Octave.
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
disp("	Begin:	Test String Operations.")


format('long')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("=	Create a character vector.")
a1 = "Ciao!"
if(ischar(a1))
	disp(">	a1 is a character array/matrix.")
else
	disp(">	a1 IS NOT a character array/matrix.")
endif

if(isvector(a1))
	disp(">	a1 is a character vector.")
else
	disp(">	a1 IS NOT a character vector.")
endif

disp("------------------------------------------------------------")

disp("=	Create a character matrix.")
a2 = ["Mondo."]
if(ischar(a2))
	disp(">	a2 is a character array/matrix.")
else
	disp(">	a2 IS NOT a character array/matrix.")
endif

if(isvector(a2))
	disp(">	a2 IS A character vector???")
else
	disp(">	a2 is not a character vector.")
endif

disp("------------------------------------------------------------")

disp("=	Create another character matrix.")
a3 = ["Amo la mamma", ""]
if(ischar(a3))
	disp(">	a3 is a character array/matrix.")
else
	disp(">	a3 IS NOT a character array/matrix.")
endif

if(isvector(a3))
	disp(">	a3 IS A character vector???")
else
	disp(">	a3 is not a character vector.")
endif

disp("------------------------------------------------------------")

disp("=	Create yet another character matrix.")
a4 = [""; ""; "Amo la mamma"; ""; ""; ""; ""; ""; ""]
if(ischar(a4))
	disp(">	a4 is a character array/matrix.")
else
	disp(">	a4 IS NOT a character array/matrix.")
endif

if(isvector(a4))
	disp(">	a4 IS A character vector???")
else
	disp(">	a4 is not a character vector.")
endif

disp("=	Create character matrix #5.")
a5 = ["Amo la mamma"; "@"]
if(ischar(a5))
	disp(">	a5 is a character array/matrix.")
else
	disp(">	a5 IS NOT a character array/matrix.")
endif

if(isvector(a5))
	disp(">	a5 IS A character vector???")
else
	disp(">	a5 is not a character vector.")
endif

disp("=	When creating a character matrix (i.e., array of strings),")
disp("		it is an array of character vectors.")
disp("	However, a matrix of null strings, except for 1 element,")
disp("		would cast that non-null string into a character vector.")

disp("------------------------------------------------------------")
collection = [ "String #1"; "String #2" ]
ischar (collection)
ischar (collection) && isvector (collection)
ischar ("my string") && isvector ("my string")


disp("------------------------------------------------------------")
c_string = 'Ciao, '
d_string = "buona giornata!!!"
printf("=	Concatenate the strings %s and %s.\n", "c_string", "d_string")
e_string = [c_string d_string]

disp("------------------------------------------------------------")

disp("= Test the use of index(s,t, direction).")

c = index("Since coping with the above-mentioned tasks on an industrial scale depends critically on effective decision procedures, SMT is a vibrant and prospering research subject for many researchers around the world, both in academia and in industry. Intel, AMD, ARM and IBM are some of the companies that routinely apply decision procedures in circuit verification with ever-growing capacity requirements. Microsoft is developing an SMT solver and applies it routinely in over a dozen code analysis tools. Every user of Microsoft Windows and Microsoft Office therefore indirectly enjoys the benefits of this technology owing to the increased reliability and resilience to hacker attacks of these software packages. There are hundreds of smaller, less famous companies that use SMT solvers for various software engineering tasks, and for solving various planning and optimization problems.","SMT","first")
d = index("Since coping with the above-mentioned tasks on an industrial scale depends critically on effective decision procedures, SMT is a vibrant and prospering research subject for many researchers around the world, both in academia and in industry. Intel, AMD, ARM and IBM are some of the companies that routinely apply decision procedures in circuit verification with ever-growing capacity requirements. Microsoft is developing an SMT solver and applies it routinely in over a dozen code analysis tools. Every user of Microsoft Windows and Microsoft Office therefore indirectly enjoys the benefits of this technology owing to the increased reliability and resilience to hacker attacks of these software packages. There are hundreds of smaller, less famous companies that use SMT solvers for various software engineering tasks, and for solving various planning and optimization problems.","SMT","last")
% --------------------------------------------------------------------
disp("=	Calling the function index(s,t,direction) with an")
disp("	  invalid direction (i.e., not 'first' nor 'last')")
disp("	  will result in a thrown error.")
%{
	Calling the function index(s,t,direction) with an invalid
		direction (i.e., not "first" nor "last") will result in a
		thrown error.
%}
try
	e = index("Since coping with the above-mentioned tasks on an industrial scale depends critically on effective decision procedures, SMT is a vibrant and prospering research subject for many researchers around the world, both in academia and in industry. Intel, AMD, ARM and IBM are some of the companies that routinely apply decision procedures in circuit verification with ever-growing capacity requirements. Microsoft is developing an SMT solver and applies it routinely in over a dozen code analysis tools. Every user of Microsoft Windows and Microsoft Office therefore indirectly enjoys the benefits of this technology owing to the increased reliability and resilience to hacker attacks of these software packages. There are hundreds of smaller, less famous companies that use SMT solvers for various software engineering tasks, and for solving various planning and optimization problems.","and",324)
catch InvalidDirectionError
	disp("=	Invalid direction error has been caught.")
end_try_catch







%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Test String Operations.")


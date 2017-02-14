#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of carrying
%		out basic operations in GNU Octave.
%
%
%
%	References:
%		[Eaton1996] John W. Eaton, "Built-in Variables", in manual
%			for Octave version 1.1.1, January 1995. Available from
%			{\it GNU documentation tree, Department of Mathematics,
%			College of Science, University of Utah} at:
%			\url{https://www.math.utah.edu/docs/info/octave_8.html};
%			last accessed on February 9, 2017.
%
%	Citations/References that use the *LaTeX/BibTeX* notation are
%		taken from my *BibTeX* database (set of *BibTeX* entries).
%
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
printf("The range of c is: %d.\n",c)
d = [c]
e = "Ciao Mondo!"

disp("=	Get the type of 'a', 'b', 'c', 'd', and 'e'.")
type_of_a = typeinfo(a)
type_of_b = typeinfo(b)
type_of_c = typeinfo(c)
type_of_d = typeinfo(d)
type_of_e = typeinfo(e)

f1 = 123.456789
%g1 = 918273645
g1 = 918273
h = 6574839201.1837465
if(isa(f1,"float"))
	printf("=	The value of f1 is:		%f.\n",f1)
else
	disp(">	Type of f1 is wrong!!!")
endif

if(isa(g1,"integer"))
	printf("=	The value of g1 is:		%d.\n",g1)
elseif(isa(g1,"float"))
	printf("=	value of float g1 is:		%f.\n",g1)
else
	disp(">	Type of g1 is wrong!!!")
endif

if(isa(h,"numeric"))
	printf("=	The value of h is:		%g.\n",h)
else
	disp(">	Type of h is wrong!!!")
endif


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

disp("=	Perform arithmetic on complex numbers.")
a = complex(5,4)
b = complex(3,7)
c = a + b

disp("=	Cast 32-bit value into 8-bit value.")
try
	n315 = cast(315,"uint8") 
	disp(">	Numbers > 255 are cast into 255 (max 8-bit value).")
catch CastingOverflow
	disp(">	Casting 32-bit value into 8-bit value is forbidden.")
end_try_catch
disp("=	Cast 32-bit value into 64-bit value.")
n130 = cast(130,"uint64")
disp("=	Cast double value into 8-bit value.")
n34 = cast(34.565739829,"uint8")
n34 = cast(34.365739829,"uint8")
disp(">	Casting floating-point numbers into integers")
disp(">		would round them [off] to nearest integer.")

disp("=	Access data in the address indicated by '34.565739829'")  
n34 = typecast(34.565739829,"uint8")


disp("=	Missing data representation, using NA() -- 'Not Available'.")
k0 = NA()
k1 = NA(5)
k2 = NA(2,3,4)
%print("=		for a matrix:", matlab, %g,)
%print("=		Compare matrices to NA (not available), using isna(g)", %g,)

if(NA == NA)
	disp("(NA == NA) is TRUE.")
elseif(isna(k0))
	disp("<	Value of 'k0' is NA.")
	disp("<	(NA == NA) is FALSE.")
endif

disp("=	Determine which element of 'k3' is 'NA'.")
k3 = [2 3 4 5 NA() 7 8]
k4 = isna(k3)

disp("=	List predefined constants of GNU Octave.")
m1 = I
m1 = i
m1 = J
m1 = j
m1 = Inf
m1 = inf
m1 = NaN
m1 = nan
m1 = eps
m1 = pi
m1 = realmax
m1 = realmin
disp("=	Other predefined constants of GNU Octave are:")
printf("	-%s\n	-%s\n	-%s\n","stdin","stdout","stderr")
printf("	-%s\n	-%s\n	-%s\n","SEEK_SET","SEEK_CUR","SEEK_END")

disp("=	Environment variables [Eaton1996]:")
disp("	- EDITOR: Text editor for GNU Octave.")
printf("= The current editor is: %s.\n",EDITOR)
disp("	- IMAGEPATH: Location of image files.")
disp("	- INFO_FILE: Location of GNU Octave info file.")
disp("	- LOADPATH: List of directories to search for function files.")
disp("	- OCTAVE_VERSION: Version of GNU Octave.")
disp("	- PS1: Primary prompt string.")
disp("	- PS2: Secondary prompt string.")

disp("------------------------------------------------------------")
disp("=	Fun with null matrices.")
n1 = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16; 17 18 19 20; 21 22 23 24]
if(isnull(n1))
	disp("	Oops! 'n1' IS null.")
else
	disp("	= 'n1' is not null.")
endif
if(isempty(n1))
	disp("	Oops! 'n1' IS empty.")
else
	disp("	= 'n1' is not empty.")
endif

n2 = []
if(isnull(n2))
	disp("	= 'n2' is null.")
else
	disp("	Oops! 'n2' IS NOT null.")
endif
if(isempty(n2))
	disp("	= 'n2' is empty.")
else
	disp("	Oops! 'n2' IS NOT empty.")
endif


try
	n3(n1) = []
	if(isnull(n3))
		disp("	= 'n3' is null.")
	else
		disp("	Oops! 'n3' IS NOT null.")
	endif
catch ArrayIndexOutOfBoundsError
	disp("	= Don't assign n3(n1) to [], if n1 is not empty")	
end_try_catch

n4 = []
try
	n5(n1) = n4
catch MismatchedDimensionsError
	disp("	= Mismatched dimensions error.")
	disp("	= n1 & n4 should have the same size")
end_try_catch
n6(n2) = n4
n7 = n1*6
n8(n7) = n1
n9 = ""
if(isnull(n9))
	disp("	'n9' is an empty string.")
else
	disp("	Oops, 'n9' IS NOT an empty string.")
endif
if(isempty(n9))
	disp("	'n9' is empty.")
else
	disp("	Oops, 'n9' IS NOT empty.")
endif

n10 = ''
if(isempty(n10))
	disp("	'n10' is empty.")
else
	disp("	Oops, 'n10' IS NOT empty.")
endif
n11 = zeros(5)
disp("=	Null matrices can be instantiated with: zeros(n).")

disp("=	Use isempty(a) to show a null value or empty string as null.")

disp("------------------------------------------------------------")
disp("	isnull(x) \cite{OctaveForgeContributors2017a}:")
disp("	= Return true if x is a special null matrix, string, or single quoted string.")
disp("	isempty(a) \cite{OctaveForgeContributors2017a}:")
disp("	= Return true if a is an empty matrix (any one of its dimensions is zero).")
disp("	isindex (ind) \cite{OctaveForgeContributors2017a}:")
disp("	= Return true if ind is a valid index.")
disp("	= Valid indices are either positive integers (although ")
disp("	  possibly of real data type), or logical arrays.")
disp("------------------------------------------------------------")


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	\cite[\S7.3 Status of Variables]{Abbott2016,Eaton2016}
disp("=	Show a 'list currently defined variables'")
disp("=		(matching the given patterns.)'")
who
disp("=	Show a detailed 'list currently defined variables'")
whos
disp("=	Determine if a 'name' is used for an existing")
disp("		'variable, function, file, directory, or class'.")
n12 = exist("n1")
n13 = exist("n100")

disp("=	Remove a subset of, or all, names from the symbol table.")
clear
disp("=	Show a detailed 'list currently defined variables'")
whos


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	\cite[\S7.3 Status of Variables]{Abbott2016,Eaton2016}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	\cite[\S16.1 Finding Elements and Checking Conditions]{Abbott2016,Eaton2016}




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing basic operations.")


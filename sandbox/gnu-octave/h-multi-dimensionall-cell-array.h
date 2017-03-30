#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of cell
%		arrays in GNU Octave.
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
disp("	Begin:	Testing multi-dimensional cell arrays.\n\n")
format('long')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("=	Create a cell array, with fields of different sizes.")
a = {{1 2 3 4 5}, {6 7}, 8, {9 10 11 12}}
disp("=	Create another cell array, with fields of different sizes.")
b = {{8.1, 8.2, 8.3}, {4.2, 4.3, 4.5, 4.6, 4.7, 4.8}, {9.2, 9.3}}
c = {{9.9, 9.8}, {7.1, 8.1, 9.1, 10.1, 11.1, 12.1}, {4.1, 4.2, 4.3, 4.4}}
d = {{33.1, 33.2}, {98.3, 97.3, 96.3, 95.3, 94.3, 93.3, 92.3, 91.2}}
e = {a,b,c,d}

disp("=	This demonstrates that the elements of multi-dimensional ")
disp("	matrices are processed from the right-most dimension to the ")
disp("	left-most dimension.")
disp("=	Embedded elements are displayed first, before visiting.")
disp("	next cell/field/array.")








%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing multi-dimensional cell arrays.")

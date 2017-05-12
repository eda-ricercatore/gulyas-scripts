#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of using
%		expressions in GNU Octave.
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
disp("	Begin:	Testing usage of expressions.\n\n")
format('long')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


a_matrix = [8 2 3 18; 5 27 4 8; 7 31 6 97]

disp("The matrix 'a_matrix' has a size of: 3*4.")

a_matrix(3,2)

%a_matrix(4,3)
%error: ./i-expressions.m: A(I,J): row index out of bounds; value 4 out of bound 3

a_matrix(7)

a = 13
a(ones(1,4))


%mask = [false true true false true]
mask_f = false
tval = [true false false true true]
fval = [true true false true false]
result_mf = merge(mask_f, tval, fval)
mask_t = true
result_mt = merge(mask_t, tval, fval)
disp("------------------------------------------------------------")
result_iet = ifelse(mask_t, tval, fval)
result_ief = ifelse(mask_f, tval, fval)
disp("------------------------------------------------------------")
a = b = c = d = e = 12345
b
c
d
e
disp("------------------------------------------------------------")

%	Experimenting with placeholders.
%[u, s, v] = svd([7 3 9; 5 8 2; 4 1 1])
[rz, ry, rx] = lib_precondition(3427.234, 89435, 437)
disp("+	+	+	+	+	+	+	+")
[rz1, ry1, rx1, rw1] = lib_precondition(56237,4345,32,123, 12,102417)
%printf("=	The value of nargout is:\d.," nargout(@histc))
disp("+	+	+	+	+	+	+	+")
[~, ry2, rx2, rw2] = lib_precondition(267,12,3,102, 8.1,329.4)
disp("+	+	+	+	+	+	+	+")
[rz3, ~, rx3, rw3] = lib_precondition(843,4.3,0.2349)


disp("------------------------------------------------------------")


z = 30
z += 45*3






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Testing usage of expressions.")

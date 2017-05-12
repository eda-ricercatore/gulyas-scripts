%	This is written by Zhiyang Ong to record programming idoms for
%		preconditions of functions in GNU Octave.
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

%	Function with three input arguments, return three variables.
function [ret_a,ret_b,ret_c,ret_d] = lib_precondition(number_a, number_b, number_c)
	ret_a = number_c
	ret_b = number_b
	ret_c = number_a
	ret_d = 1000

	printf("Input arguments: d_callee(%d%%,%f,%e).\n", number_a, number_b, number_c)
	printf("Return values: (%d%%,%f,%e).\n", ret_a,ret_b,ret_c)
	printf("=	The value of nargout is:%d.\n", nargout(@histc))
%{
	The following statement cannot work, since variables cannot
		include the pound symbol.
%}
%	printf("=	The value of min_#_inputs is:%d.\n", min_#_inputs)

	min_numof_inputs = 1
	max_numof_inputs = 3

	%	Programming idoms for preconditions.
	if((nargin < min_numof_inputs) || (nargin > max_numof_inputs))
		disp("=	Call this function with the help option.")
	endif

endfunction













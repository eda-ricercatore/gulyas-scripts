%	This is written by Zhiyang Ong to generate random-telegraph waves
%		(RTW).
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

%	Add paths to GNU Octave, so that it can load scripts to execute.
%addpath("/Users/zhiyang/Documents/ricerca/gulyas-scripts/time-shifting/")

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%	Function to generate random-telegraph waves (RTW).
%	@param	num_cycles		Number of cycles for the RTW.
%	@param	period_length	Number of bits per period/cycle of the RTW.
%	@return	rtw_signal		A RTW signal.	
%	References:
%		[Eaton2016]
function [rtw_signal,k] = generate_rtw(num_cycles, period_length)
%	disp("	Generate RTW signal.")
	%	Index of RTW signal
	k = 1;
	%	Generate RTW signal for num_cycles periods/cycles.  
	for i = 1:num_cycles
		HL_value = generate_HL_values
		for j = 1:period_length
			rtw_signal(k) = HL_value
			k = k+1
		endfor
	endfor
	%{
		Decrement extra time segment from total number of time
			segments.
	%}
	k = k -1
	% Postcondition.
	if (numel(rtw_signal) != k)
		error("=	Error with number of data points of RTW signal.")
	endif
endfunction









%	Eaton2016


%	References:
%
%	[Eaton2016]
%		John W. Eaton, "GNU Octave," Free Software Foundation, Boston, MA, 2016. Available online from {\it {GNU Operating System}: GNU Software} at: \url{https://www.gnu.org/software/octave/doc/v4.0.3/}; October 10, 2016 was the last accessed date.
%			In Functions and Scripts: Function Files: Manipulating the Load Path"















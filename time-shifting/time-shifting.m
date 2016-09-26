#!/opt/local/bin/octave

%	This is written by Zhiyang Ong


%	\stackrel{\otimes}{\underline{\overline{A}}}




%   Length of array
array_length = 64
%   Boolean arrays of random values: 
x1 = randi([0 1],1,array_length)
x2 = randi([0 1],1,array_length)

%   Cross-correlation of x1 and x2
[R, lag] = xcorr (x1, x2)






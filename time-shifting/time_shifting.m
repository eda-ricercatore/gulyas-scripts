#!/opt/local/bin/octave
%	This is written by Zhiyang Ong


%	\stackrel{\otimes}{\underline{\overline{A}}}


%	Load various GNU Octave packages
%pkg load /Applications/apps/math/octave/signal-1.3.2/src
%pkg load /Applications/apps/math/octave/signal-1.3.2/inst
%cd /Applications/apps/math/octave/pkg
pkg load struct 
pkg load control
pkg load signal




%   Length of array
%array_length = 64
array_length = 8
%   Boolean arrays of random values: 
x1 = randi([0 1],1,array_length)
x2 = randi([0 1],1,array_length)

%   Cross-correlation of x1 and x2
[R, lag] = xcorr (x1, x2)

%avg_for 100 xcorr

%   Time-shifted x1
x3a = [9 1 2 3 4 5 6 7 8]
%horzcat = [0 0 0 x3a[1:1:5]]










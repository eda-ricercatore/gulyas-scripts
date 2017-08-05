#!/opt/local/bin/octave

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

%	Load various GNU Octave packages
%	pkg load struct 
%	pkg load control
	pkg load signal


%	Add paths to GNU Octave, so that it can load scripts to execute.
%addpath("/Users/zhiyang/Documents/ricerca/gulyas-scripts/time-shifting/")

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%	Global "constants"/variables

%	Setting up high and low logic values.
global high_value = 1;
global low_value = -1;

pdflatex = "pdflatex "
delta_y = 0.1

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



cur_value = ciao_mondo
printf("	Current value is:%u.\n",cur_value)

%aval = generate_HL_values

% Get RTW rtw1, and number of plotting points (time segments).
%[rtw1,t] = generate_rtw(12,8)
[rtw1,t] = generate_rtw(30,10)
% Generate an array for the time segments.
t_range = 1:1:t;
%t_range = [1:1:t];

fig1 = figure();
fig1_name = "fig1.tex"
plot(t_range,rtw1,"r");
ylim([low_value-delta_y,high_value+delta_y])
xlabel("Time t");
ylabel("$RTW_1$");
title("Plot of $RTW_1$.");
%set(fig1,"visible","off");		% Problem with offscreen display.
print(fig1, fig1_name,"-dpdflatexstandalone")
set(fig1,"visible","on");
fig1_typeset = [pdflatex fig1_name]
system(fig1_typeset);
%open(fig1_name);
%saveas(fig1,"pdf-plot-rtw1.ps","ps")

%	===============================================================

% Get RTW rtw2, and number of plotting points (time segments).
[rtw2,t2] = generate_rtw(30,10)
% Generate an array for the time segments.
t_range2 = 1:1:t2;

fig2 = figure();
fig2_name = "fig2.tex"
%plot(t_range2,rtw2,"r", "marker",".");
plot(t_range2,rtw2,"r");

ylim([low_value-delta_y,high_value+delta_y])
xlabel("Time t");
ylabel("$RTW_2$");
title("Plot of $RTW_2$.");
%set(fig2,"visible","off");		% Problem with offscreen display.
print(fig2, fig2_name,"-dpdflatexstandalone")
set(fig2,"visible","on");
fig2_typeset = [pdflatex fig2_name]
system(fig2_typeset);
%open(fig2_name);
%saveas(fig2,"pdf-plot-rtw1.ps","ps")

%	===============================================================

% Determine the covariance between RTW_1 and RTW_2

%{
	"xcov" function is undefined, without the package "signal".
	Need to load the package "signal".
	See preamble.
%}
[Rcov,lag_cov] = xcov(rtw1,rtw2)
cov_rtw1_rtw2 = cov(rtw1,rtw2)

[Rcorr,lag_corr] = xcorr(rtw1,rtw2)
corr_rtw1_rtw2 = corr(rtw1,rtw2)













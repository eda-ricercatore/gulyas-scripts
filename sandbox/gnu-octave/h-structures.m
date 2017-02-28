#!/opt/local/bin/octave

%	This is written by Zhiyang Ong to test my knowledge of managing
%		and using structures in GNU Octave.
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
disp("	Begin:	Structure Testing")

format('long')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("------------------------------------------------------------")
disp("	Test structures without using functions.")

disp("=	Create structure for logic signals.")
logic_signal.shape = "RTW"
logic_signal.value = 0
logic_signal.value1 = false
logic_signal.value2 = true
disp("=	Copy the structure logic_signal to structure digital_signal.")
digital_signal = logic_signal

disp("=	Create a structure that references another structure.")
computer_system.name = "microarchitecture"
computer_system.arch = "pipelined"
computer_system.signal = digital_signal
disp("=	Create a nested structure of 4 levels.")
computer_system.functional_unit.circuit.outputs.pins = 0
computer_system.embedded.compiler.cpp.cpp11.year = 2011
computer_system.embedded.compiler.cpp.cpp14.year = 2014
computer_system.embedded.compiler.cpp.cpp17.year = 2017
computer_system.embedded.compiler.scala.v17 = 2017
computer_system.embedded.compiler.scala.v14 = 2014
computer_system.embedded.compiler.scala.v11 = 2011
computer_system.embedded.compiler.systemc.v10 = 2010
computer_system.embedded.compiler.systemc.v05 = 2005

old_level = struct_levels_to_print(4)
computer_system
old_level = struct_levels_to_print(5)
computer_system

disp("------------------------------------------------------------")
disp("	Test structures by using functions.")
[clk_signal, bio_signal] = h-callee(digital_signal, logic_signal)


disp("------------------------------------------------------------")
disp("	Enumerate all elements of a structure using a for statement.")
disp("=		Print name of element (of the structure).")
disp("=		Print value of element (of the structure).")
for [value, key] = clk_signal
	key
	value
endfor


disp("------------------------------------------------------------")
disp("	Test array of structures.")

circuit_signals = { digital_signal, logic_signal, clk_signal }

nbl(1).signal = "Square wave."
nbl(1).num_clk_cycles = 512
nbl(2).signal = "Random telegraph wave (RTW)."
nbl(2).num_clk_cycles = 1024
nbl(3).signal = "Sine wave."
nbl(3).num_clk_cycles = 1024
nbl(4).signal = "Cosine wave."
nbl(4).num_clk_cycles = 1024
nbl(5).signal = "Decaying sinusoidal wave."
nbl(5).num_clk_cycles = 1024

x(1,1).a = "string 1,1"
x(1,2).a = "string 1,2"
x(1,3).a = "string 1,3"
x(1,4).a = "string 1,4"
x(1,5).a = "string 1,5"
x(2,1).a = "string 2,1"
x(2,2).a = "string 2,2"
x(2,3).a = "string 2,3"
x(2,4).a = "string 2,4"
x(2,5).a = "string 2,5"
x(1,1).b = 1
x(1,2).b = 2
x(1,3).b = 3
x(1,4).b = 4
x(1,5).b = 5
x(2,1).b = 6
x(2,2).b = 7
x(2,3).b = 8
x(2,4).b = 9
x(2,5).b = 10

disp("=	Print content of 'nbl'.")
nbl
disp("=	Print content of 'x'.")
x
disp("=	Print content of 'x.a'.")
disp("=		Enumerate dimension i,")
disp("=		then dimension (i+1),")
disp("=		then dimension (i+2), ...")
x.a
disp("=	Print content of 'x(2,3)'.")
x(2,3)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp("=	Print content of non-existent 'x(4,9)'.")
try
	x(4,9)
catch ArrayIndexOutOfBoundsError
	disp(">>	ArrayIndexOutOfBoundsError occurred.")
end_try_catch

try
	z
catch UndefinedVariableError
	disp(">>	Undefined variables cannot be accessed.")
end_try_catch

try
	x.c
catch NoSuchMemberError
	disp(">>	Undefined members of array elements can't be accessed.") 
end_try_catch


disp("=	Delete x(2,3).a.")
x(2,3).a = {}
disp("=	Delete x(2,4).a.")
x(2,4).a = []
disp("=	Print content of 'x.a' again.")
x.a

disp("------------------------------------------------------------")
disp("=	Test structure creation.")
disp("=	Test structure creation: Via dynamic naming.")

signal_type = "RTW"
signals.signal_type = 573
signals.(signal_type) =43 


disp("------------------------------------------------------------")
disp("=	Test structure creation: Enumerate equal-length arrays/lists.")

%names = [Alpar; Bollobas; Czako; Daranyi; Eotvos; Fabinyi]
signal_types = ["sinusoidal"; "RTW"; "square"; "triangle"; "exponential"; "logarithmic"] 
signal_values = [23.34; 345.4; 945.45; 13; 943.2; 23.001] 

for i=1:rows (signal_types)
	ensemble.(signal_types(i,:)) = signal_values(i)
endfor


types_of_experiments = ["hat drawing " "encryption " "secure communication " "verification " "approximate computing "; "dependable computing " "autonomic computing " "probabilistic model checking " "statistical static timing analysis " "theorem proving"] 
a = [1 2 3 4 5; 6 9 10 22 33]
b = [82 91 324 29 49; 92 192 18234 19 82]
















%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Structure Testing")


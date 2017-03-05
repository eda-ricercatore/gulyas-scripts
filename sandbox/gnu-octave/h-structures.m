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
%	\cite[\S6.1.1, pp. 99-100]{Eaton2016a}

disp("=	Create structure for logic signals.")
logic_signal.shape = "RTW"
logic_signal.value = 0
logic_signal.value1 = false
logic_signal.value2 = true
disp("=	Copy the structure logic_signal to structure digital_signal.")
digital_signal = logic_signal

%	\cite[\S6.1.1, pp. 100-101]{Eaton2016a}
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



%	\cite[\S6.1.2, pp. 104]{Eaton2016a}
disp("=	Get the size of a nested structure.")
sz = size(computer_system)
sz1 = size(computer_system.embedded)

%	\cite[\S6.1.1, pp. 101]{Eaton2016a}
old_level = struct_levels_to_print(4)
computer_system
old_level = struct_levels_to_print(5)
computer_system
old_level = struct_levels_to_print(6)
disp("------------------------------------------------------------")
disp("=	Delete computer_system.embedded.compiler.scala.v14.")
%	\cite[\S6.1.2, pp. 104]{Eaton2016a}.
computer_system.embedded.compiler.scala.v14 = []


disp("------------------------------------------------------------")
disp("	Test structures by using functions.")
%	\cite[\S6.1.1, pp. 101]{Eaton2016a}
[clk_signal, bio_signal] = h_callee(digital_signal, logic_signal)


disp("------------------------------------------------------------")
disp("	Enumerate all elements of a structure using a for statement.")
disp("=		Print name of element (of the structure).")
disp("=		Print value of element (of the structure).")
%	\cite[\S6.1.1, pp. 102; \S10.5.1, pp.165-166]{Eaton2016a}
for [value, key] = clk_signal
	key
	value
endfor

%	\cite[\S6.1.4]{Eaton2016}
disp("	Enumerate all the fields of a structure.")
names = fieldnames(clk_signal)
disp("	Reorder the fields of clk_signal in a specific order.")
reordered_clk_signal = orderfields(clk_signal,{"value2","shape","value1","value"})
disp("	Reorder the fields in a lexicographical order.")
lexicographical_clk_signal = orderfields(reordered_clk_signal)



disp("------------------------------------------------------------")
disp("	Test array of structures.")
%	\cite[\S6.1.2, pp. 103]{Eaton2016a}

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

%	\cite[\S6.1.2, pp. 104]{Eaton2016a}.
disp("=	Delete x(2,3).a.")
x(2,3).a = {}
disp("=	Delete x(2,4).a.")
x(2,4).a = []
disp("=	Print content of 'x.a' again.")
x.a

disp("------------------------------------------------------------")
disp("=	Test structure creation.")
disp("=	Test structure creation: Via dynamic naming.")

%	\cite[\S6.1.3, pp. 104-105]{Eaton2016a}.
signal_type = "RTW"
signals.signal_type = 573
signals.(signal_type) =43 


disp("------------------------------------------------------------")
disp("=	Test structure creation: Enumerate equal-length arrays/lists.")
%	\cite[\S6.1.3, pp. 104-105]{Eaton2016a}.

%names = [Alpar; Bollobas; Czako; Daranyi; Eotvos; Fabinyi]
signal_types = ["sinusoidal"; "RTW"; "square"; "triangle"; "exponential"; "logarithmic"] 
signal_values = [23.34; 345.4; 945.45; 13; 943.2; 23.001] 

for i=1:rows (signal_types)
	ensemble.(signal_types(i,:)) = signal_values(i)
endfor




disp("------------------------------------------------------------")
disp("=	Test structure creation: Cell array as an individual field.")
%	\cite[\S6.1.3, pp. 106]{Eaton2016a}.


%types_of_experiments = {"hat drawing ", "encryption ", "secure communication "} 
%low_values = [1, 2, 3, 4, 5, 6, 9, 10, 22, 33]
%high_values = [82 91 324 29 49 92 192 18234 19 82]

%	indiv_field_struc = struct("types_of_experiments", {"hat drawing ", "encryption ", "secure communication "},
%		"low_values", [1, 2, 3, 4, 5, 6, 9, 10, 22, 33], 
%		"high_values", [82 91 324 29 49 92 192 18234 19 82])


indiv_field_struc = struct("types_of_experiments", {"hat drawing ", "encryption ", "secure communication "},
	"low_values", {4, 2, 7}, 
	"high_values", {192 18234 82},
	"last_field_name","last_field_value")
disp("=	Print the contents of 'indiv_field_struc'.")
indiv_field_struc.types_of_experiments
indiv_field_struc.low_values
indiv_field_struc.high_values
indiv_field_struc.last_field_name



disp("------------------------------------------------------------")
disp("=	Test if something is a structure.")
if (isstruct(indiv_field_struc))
	disp("	indiv_field_struc is a struct.")
else
	disp("	indiv_field_struc IS NOT A struct.")
endif
floating_point_number = 17234.43423423
if (isstruct(floating_point_number))
	disp("	floating_point_number IS A struct.")
else
	disp("	floating_point_number is not a struct.")
endif










%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp("============================================================")
disp("	End:	Structure Testing")


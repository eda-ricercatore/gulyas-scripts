#	Notes About *GNU Octave*

##	Build Automation for *GNU Octave*

For *Makefile*-based build automation for executing/running 
	*GNU Octave* scripts, I have to do the following:
+ ./[*filename*]
	- Requires adding the UNIX shebang for *GNU Octave*
	- Requires using *chmod* (UNIX command) to change the file
		permission, so that the script(s) can be executed via the
		Terminal as a UNIX command/process.

And avoid doing the following:
+ octave [*filename*]

Experimentally/Empirically demonstrated in the execution of the
	*Make* target *torture*. See: [link to sandbox/gnu-octave](../sandbox/gnu-octave).


##	Functions

Each *GNU Octave* script can only contain one function.

If more than one function is defined in a script, all the functions
	(except the first function) cannot be recognized by other
	*GNU Octave* scripts. 

Experimentally/Empirically demonstrated in the execution of the
	*Make* target *torture*. See: [link to sandbox/gnu-octave](../sandbox/gnu-octave).


##	Miscellaneous

###	Formatted Output

Conversion specifications \cite[\S14.2.4 Formatted Output]{Abbott2016}:
+ '%d': scalar argument, decimal notation
+ '%s': string argument
+ '%o': integer argument, octal radix
+ '%u': integer argument, decimal radix
+ '%x': integer argument, hexadecimal radix
+ '%c': character value 
+ '%f': fixed-point notation
+ '%e': exponential notation
+ '%g': fixed-point or exponential notation

For these aforementioned specific conversion specifications \cite[\S14.2.4 Formatted Output]{Abbott2016}:
+ Specific modifiers can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.
+ Specific flags can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.
+ These aforementioned flags and modifiers can be inserted between the percentage ("%") symbol and the character specifying/indicating the conversion type.  



#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


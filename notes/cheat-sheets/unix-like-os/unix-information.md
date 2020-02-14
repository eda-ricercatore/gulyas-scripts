#	Notes About *UNIX*-like Operating Systems



##	Data compression and File Archiving

###	"*.tar.xz" Files

To compress/archive "*.tar.xz" files, try:
- xz -z
- xz --compress
- xz -l
	+ Display information about the compressed files.
- xz --list
	+ Display information about the compressed files.
- xz -z -F auto
- xz -z -F xz
- xz -z -F lzma
- xz -z -F alone
- xz -z -F raw
- tar cvf --options *[xz:compression-level]* *[filename]* *[files or set(s) of file types]*




To uncompress/unarchive "*.tar.xz" files, try:
- xz --decompress
- unxz *[filename.tar.xz]* *[filename.tar]*
- unxz *[filename.tar.xz]*
- xz -dc *[filename.tar.xz]* *[filename.tar]*
- tar xvf *[filename]*





##	Making Files Executable

`chmod 744 *[filename]*` makes the file *[filename]* executable, via
	invoking its filename.
	That is, it enables the file *[filename]* to be executed as a
	computer program.


##	Notes on Using the GNU Build System / Autotools

Dr. Anders Franz{\'{e}}n (or Anders Franzen) suggested that I use "autoreconf --install" to generate the "./configure" executable if it is not available in my working directory (for a software project that uses the GNU Build System / Autotools).

Steps that I would use to build a software project that uses the GNU Build System (or Autotools):
+ autoreconf --install
+ ./configure
	-  I can use flags/options to configure different parameters to indicate where to install/place the software build.
+ make all




##	List of UNIX commands to find their man pages of

Check if I can access the man pages for the following UNIX commands in the "Terminal" application:
+ man clang
+ man java
+ man gfortran
+ man make
+ man rmdir
+ man chmod
+ man gcc
+ man g++
+ man chmod
+ man rmdir
+ man rm
+ man pwd
+ man ls
+ man wc









##	macOS

###	macOS Catalina

https://mkyong.com/mac/wget-on-mac-os-x/
mkyong
2020
wget on Mac OS X
By mkyong | January 4, 2017 | Viewed : 84,628 | +630 pv/w
mac
No address
On Mac OS X, the equivalent of Linux’s wget is curl -O
P.S Uppercase alphabet O, not number zero.
curl -O http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.9/bin/apache-tomcat-8.5.9.tar.gz






#	References


Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).


These references about *UNIX* are:
+ \cite{Adelstein2007}
+ \cite{AppleIncStaff2002}
+ \cite{Apple2011}
+ \cite{Bach1986}
+ \cite{Benvenuti2006}
+ \cite{Blum2008}
+ \cite{Bovet2006}
+ \cite{Chan1996}
+ \cite{Creary2003}
+ \cite{Dougherty1997}
+ \cite{Esteve2009}
+ \cite{Goyvaerts2009}
+ \cite{Hall2015}
+ \cite{Heard20XY}
+ \cite{Kernighan1984}
+ \cite{Kerrisk2010}
+ \cite{Love2005}
+ \cite{Matthew2008}
+ \cite{Mitchell2001}
+ \cite{Muster2003}
+ \cite{Negus2012}
+ \cite{Newham2005}
+ \cite{Ong2004a}
+ \cite{Parlante2001}
+ \cite{Petersen2008}
+ \cite{Powers2003}
+ \cite{Raymond2004}
+ \cite{Raymond2004a}
+ \cite{Riesbeck2009a}
+ \cite{Robbins2003}
+ \cite{Rochkind2004}
+ \cite{Rosen2007a}
+ \cite{Stallings2005}
+ \cite{StanfordUniversityStaff2006}
+ \cite{Stevens2013}
+ \cite{Storimer2012}
+ \cite{vanVugt2009}
+ \cite{VibrantPublishers2010a}
+ \cite{VibrantPublishers2011b}
+ \cite{VibrantPublishers2011c}
+ \cite{VibrantPublishers2011h}







#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

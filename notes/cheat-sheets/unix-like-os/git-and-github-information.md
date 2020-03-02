#	Information about *Git* and *GitHub*

A very simple, [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)-based tutorial for using *Git* and *GitHub* via a [Web browser](https://en.wikipedia.org/wiki/Web_browser) is available as one of my written [tutorials](https://github.com/eda-ricercatore/gulyas-scripts/tree/master/notes/tutorials) at: [Git and GitHub Tutorial](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/git-tutorial.md).

This note contains information in addition to that note for more advanced users of *Git* and *GitHub*.

##	Addressing ("Unresolved") Problems with *Git* and *GitHub*

Some ("unresolved") problems with *Git* and *GitHub* are listed as follows. If they are resolved temporarily or permanently, at least one solution would be described.


### error: invalid object \[A short integer\] \[A (very) long alphanumeric string\] for '.gitignore'

Attempted solutions that failed to resolve the problem:
+ https://medium.com/@panjeh/git-error-invalid-object-error-building-trees-44b582769457
+ https://git-annex.branchable.com/bugs/__34__error__58___invalid_object__34____44___after_add__59___cannot_commit/
+ https://stackoverflow.com/questions/14448326/git-commit-stopped-working-error-building-trees
+ https://www.freecodecamp.org/forum/t/question-on-moving-computers/115910/9


Attempted solutions that resolves, or works around, the problem:
+ re-clone the *Git* repository:
	- move *Git* repository to a temporary directory
	- get the *Git* clone URL/Internet address \[to run the *Git* command with\]
	- use the *Git* command to clone the repository again
		* Note that since modifications/update, deletions, and additions to the *Git* repository are not necessarily reflected/updated via my *GitHub* repository (hosted in *GitHub*'s data centers)
	- move the contents of my "working directory" in the aforementioned temporary directory to the newly cloned *Git* repository, so that this newly cloned *Git* repository would become the "working directory" for my *Git* repository






##	Tips

###	Customized *Git* Commit Messages with Build Automation

Enter the following text into a Makefile for build automation for your project, using *Git* as the revision/version control tool, or software configuration management tool.


	# From the "Terminal" application, try:
	#	make git m="your message"
	git:
		git add -A
		git commit -m "$m"
		git push -u origin master


The command `git push` can be used instead of `git push -u origin master`, so that the command is used more succinctly.



	# From the "Terminal" application, try:
	#	make git m="your message"
	git:
		git add -A
		git commit -m "$m"
		git push




This allows me to avoid entering three commands into the command line (or use the arrow keys to recall the previous/recent commands to reuse them), and allow me to just enter/use on command. 










Since the process/workflow for committing modifications/updates, insertions, and deletions using [*Mercurial*](https://www.mercurial-scm.org/) as a revision/version control tool, or software configuration management tool, is very similar, this code fragment would be modified to the following:



	# From the "Terminal" application, try:
	#	make git m="your message"
	hg:
		hg addremove
		hg commit -m "$m"
		hg push






#	Author Information

The MIT License (MIT)

Copyright (c) <2016> <Zhiyang Ong>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.


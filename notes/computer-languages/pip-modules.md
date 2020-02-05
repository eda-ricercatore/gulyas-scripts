#	List of *PIP*-based *Python* modules


##	For Boilerplate Code

List of *PIP*-based *Python* modules to add to, or install in, my Google Colab
	environment (for boilerplate code):
+ pip install numpy
+ pip install matplotlib





##	For Stochastic Computing



List of *PIP*-based *Python* modules to add to, or install in, my Google Colab
environment (for stochastic computing):
+ pip install pycorrelate












#	Problems with Common *Python* Libraries



##	Using Common *Python* Libraries on *Google Colab*

###	Via the *PIP* Platform

Use *PIP* commands to install common *Python* libraries in my *Google Colab*
	environment.





####	For Consistency, Use These Common *Python* Libraries in My Projects


For consistency, try to use these common *Python* libraries in my
	*Python*-based projects.
+ Endeavor (i.e., try to) use the same *Python* libraries, with the same versions,
	 in my *Python*-based projects.
	- Else, this may cause discrepancies to occur between my command-line
		-based *Python* software and my *Python*-based *Jupyter* notebook
		on *Google Colab*.
		* This can make tricky more complicated, since I have to mentally
			juggle the differences between the two libraries/versions.
+ With the *Anaconda* platform, it may contain *conda*-based installations of
	common *Python* libraries.
	- Hence, this may prevent users/people from using *PIP* to install such
		common *Python* libraries.
		* However, [there are ways to force an installation to occur](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/computer-languages/pip-modules.md#force-installation-of-modules-via-pip). 






#####	Force installation of modules via PIP

Command to force installation of modules via PIP [KGo2017].

	pip install --upgrade --force-reinstall <package>


From [Butnaru2017]:

	pip3 install numpy





References:
+ [orome2013] orome, "Can I force pip to reinstall the current version?", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, October 23, 2013.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/19548957/can-i-force-pip-to-reinstall-the-current-version;
		February 5, 2020 was the last accessed date.
	- [KGo2017] KGo and Arturo MP, Answer to "Can I force pip to reinstall the current version?", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, August 14, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
			https://stackoverflow.com/a/19549035/1531728 and 	https://stackoverflow.com/questions/19548957/can-i-force-pip-to-reinstall-the-current-version/19549035#19549035
			February 5, 2020 was the last accessed date.
+ [Butnaru2017] Andrei Madalin Butnaru and Daniel Patru, Answer to "Import Error: No module named numpy", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, December 14, 2017.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
		https://stackoverflow.com/a/35476722/1531728 and https://stackoverflow.com/questions/7818811/import-error-no-module-named-numpy/35476722#35476722
		February 5, 2020 was the last accessed date.






###	Via *Anaconda* Platform

Since *Google Colab* may not support the *Anaconda* platform for data science
	and scientific computing, use the *PIP* package manager to install *Python*
	packages.
+ To use the *Anaconda* platform on *Google Colab*, try:
	- https://anaconda.org/conda-forge/google-auth (may not be relevant)
	- https://rjai.me/posts/google-colab-conda/ (works for Python 2.7, not
		Python 3.X)
	- Resources that mentioned *Google Colab*:
		* \cite{McKay2019}
		* \cite{Au2019}
		* \cite{Li2018}
		* \cite{FacebookEngineers2020}


##	Module in *Python* Library Not Found

If the following error occur during execution of my *Python* scripts/programs,

	ModuleNotFoundError: No module named 'numpy'

it indicates that it cannot recognize the path for the *Python* library that the
	specified *Python* module (in this case, "*numpy*") belongs to.

Hence, I should uninstall the current version of that *Python* library, and reinstall
	it.
+ [If the *Python* library cannot be installed via *PIP* or *conda*, use these
	specified options with *PIP* to force installation of this *Python* library
	to occur](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/computer-languages/pip-modules.md#force-installation-of-modules-via-pip).
	- If the *conda*-installed version of the *Python* library is older than the
		available version via *PIP*, doing this will uninstall the
		*conda*-installed version and install the currently available version
		via *PIP*.
+ Doing this via *PIP* may not work, since the associated version of *Python*
	that is used belongs to *Python* 2.7.x (or later) rather than *Python* 3.8.x
	(or later).
	- Hence, [use *pip3* instead, as shown above](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/computer-languages/pip-modules.md#force-installation-of-modules-via-pip).

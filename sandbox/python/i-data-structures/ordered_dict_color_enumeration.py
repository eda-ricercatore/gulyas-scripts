#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to enumerate
		multiple lists (of the same length) concurrently.
	
	References:
	+ \cite{Chaudhary2019}
		- indicates how to enumerate two lists concurrently.
		- can be extended to enumerate more lists concurrently.
		- this answer also addresses how to enumerate lists of
			different lengths concurrently.
"""

import matplotlib.colors as mcolors


print("	mcolors.TABLEAU_COLORS:",mcolors.TABLEAU_COLORS,".")
print("	mcolors.TABLEAU_COLORS[tab:gray]",mcolors.TABLEAU_COLORS['tab:gray'],".")

for current_color in mcolors.TABLEAU_COLORS:
	print("current_color:",current_color,".")




from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'mango': 2}
od=OrderedDict(d.items())
print(od)
OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('mango', 2)])
od=OrderedDict(sorted(d.items()))
print(od)
t=od.popitem()
print(t)
od=OrderedDict(d.items())
t=od.popitem()
print(t)
print(od)

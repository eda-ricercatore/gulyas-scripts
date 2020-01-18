#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to enumerate
		multiple lists (of the same length) concurrently.
	
	List of Wikipedia pages about given names
	+ https://en.wikipedia.org/wiki/Category:Italian_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Italian_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Italian_feminine_given_names                                                                                                                                                           ./in	
	+ https://en.wikipedia.org/wiki/Category:Germanic_given_names
	+ https://en.wikipedia.org/wiki/Category:German_given_names
	+ https://en.wikipedia.org/wiki/Category:German_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:German_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Dutch_given_names
	+ https://en.wikipedia.org/wiki/Category:Spanish_given_names
	+ https://en.wiktionary.org/wiki/Category:Italian_male_given_names
	+ https://en.wikipedia.org/wiki/Category:Spanish_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Iranian_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Iranian_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Persian_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Persian_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Pakistani_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Pakistani_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Arabic_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Arabic_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Romanian_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Romanian_feminine_given_names
	+ https://en.wikipedia.org/wiki/Category:Yoruba_given_names
	+ https://en.wikipedia.org/wiki/Category:Sinhalese_masculine_given_names
	+ https://en.wikipedia.org/wiki/Category:Given_names_by_culture
	
	
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
print("===================================")
print("	Add dictionary to ordered dictionary, and check ordering.")
od=OrderedDict(d.items())
for obj in od:
	print("Current object is:",obj,".")
print("===================================")
print("	Add sorted dictionary to ordered dictionary, and check ordering.")
od=OrderedDict(sorted(d.items()))
for obj in od:
	print("Current object is:",obj,".")
t=od.popitem()
print(t)
print(od)
t=od.popitem()
print(t)
print(od)
print("	Popped 2 elements.")
d = {'Maruja':85, 'Paloma':73, 'Dolores':57, 'Magdalena':83, 'Elena':91, 'Carolina':43, 'Bonita':62, 'Xiomara':39}
od = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print("sort by value:",od,".")
od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print("sort by key:",od,".")
od = OrderedDict(sorted(d.items()))
print("sort by key:",od,".")
od = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print("sort by length of key:",od,".")

#!/Users/zhiyang/anaconda3/bin/python3
"""
=============================
Grouped bar chart with labels
=============================

This example shows a how to create a grouped bar chart and how to annotate
bars with labels.


@modified by Zhiyang Ong, January 15, 2020.
+ Added code to make the comparison between three gender groups:
	- Men (default group)
	- Women (another default group)
	- Others (new group)
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
# @modified by Zhiyang Ong, January 15, 2020.
other_means = [18, 31, 40, 27, 20]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

plt.gca()
"""
	@modified by Zhiyang Ong, January 15, 2020.
	Center point of each bar per group, G_i, for number of populations:
	+ 2: x - width/2, x + width/2
	+ 3: x - width, x, x + width
	+ 4: x - width
"""
fig, ax = plt.subplots()
"""
	rects1 = ax.bar(x - width/2, men_means, width, label='Men')
	rects2 = ax.bar(x + width/2, women_means, width, label='Women')
	
	From https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html,
		default width is 0.8.
"""
rects1 = ax.bar(x - width, men_means, width=0.3, label='Men')
rects2 = ax.bar(x, women_means, width=0.3, label='Women')
# @modified by Zhiyang Ong, January 15, 2020.
rects3 = ax.bar(x + width, other_means, width=0.3, label='Others')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_xlabel('Groups and genders')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend()
# @modified by Zhiyang Ong, January 15, 2020.
#ax.legend(handletextpad=5)
#	No effect. Does not work.


def autolabel(rects):
	"""Attach a text label above each bar in *rects*, displaying its height."""
	for rect in rects:
		height = rect.get_height()
		ax.annotate('{}'.format(height),
			#xy=(rect.get_x() + rect.get_width() / 2, height),
			# @modified by Zhiyang Ong, January 15, 2020.
			xy=(rect.get_x() + rect.get_width() / 3, height),
			xytext=(0, 3),  # 3 points vertical offset
			textcoords="offset points",
			ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()


"""
	@modified by Zhiyang Ong, January 15, 2020.
	Save plot in PDF format.
	This save to PDF command has to appear before the .show()
		command;
		else, the PDF fuile would be empty.
	https://github.com/futurestudio/matplotlib-tutorials/tree/master/export_samples
	
	Reference:
		Norman Peitek, "Matplotlib — Save Plots as File", from
			{\it Future Studio: Future Studio Tutorials},
			{Fellner, P{\"{o}}hls, Peitek GbR}, Magdeburg,
			Saxony-Anhalt, Germany, August 5, 2019.
			Available at: https://futurestud.io/tutorials/matplotlib-save-plots-as-file;
				last accessed on January 15, 2019.
"""
plt.savefig(__file__+".pdf")
plt.show()




#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods and classes is shown
# in this example:

matplotlib.axes.Axes.bar
matplotlib.pyplot.bar
matplotlib.axes.Axes.annotate
matplotlib.pyplot.annotate









"""
	Reference(s):
	+ \cite{MatplotlibDevelopmentTeam2020a}
		- data visualization gallery (with examples, or sample code)

"""

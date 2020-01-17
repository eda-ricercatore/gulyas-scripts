#!/Users/zhiyang/anaconda3/bin/python3
"""
====================
EventCollection Demo
====================

Plot two curves, then use EventCollections to mark the locations of the x
and y data points on the respective axes for each curve
"""

import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np


# Generate random numbers for the synthetic dataset.
# Fixing random state for reproducibility
np.random.seed(19680801)
#numpy.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])

# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# create the events marking the x data points
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# set the limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title('line plot with data points')

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
# display the plot
plt.show()

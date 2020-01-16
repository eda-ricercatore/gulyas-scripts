#!/Users/zhiyang/anaconda3/bin/python3

import numpy as np
import matplotlib.pyplot as plt

N = 150
data = np.linspace(0, N, N)

plt.plot(data)

plt.xticks(range(N)) # add loads of ticks
plt.grid()

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*N+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

plt.savefig(__file__+".png")
plt.show()

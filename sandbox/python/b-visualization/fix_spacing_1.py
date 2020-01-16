#!/Users/zhiyang/anaconda3/bin/python3

import pylab

N = 100
data = pylab.np.linspace(0, N, N)

pylab.plot(data)

pylab.xticks(range(N)) # add loads of ticks
pylab.grid()
pylab.tight_layout()
pylab.show()

pylab.close()

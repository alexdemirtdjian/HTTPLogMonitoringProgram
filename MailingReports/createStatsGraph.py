__author__ = 'alexandre'

# This class will create a stat graph that will be sent by mail
# to appropriate person

import numpy as np
import matplotlib.pyplot as plt
from operator import add

# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution

err_y = mu + sigma * np.random.randn(25)
ok_aux = mu + sigma * np.random.randn(25)
ok_y = map(add, err_y, ok_aux)

ind = np.arange(25)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

ok = plt.bar(ind, ok_y, width, color='y', label="OK")
error = plt.bar(ind, err_y, width, color='r', label="Errors")


plt.xlabel('Time of the day')
plt.ylabel('Number of requests')
plt.title(r'Histogram of daily requests')

# the average number of requests on a daily basis
plt.axhline(y=100, xmin=0, xmax=1, hold=None)

# we add the legend for the colors

plt.legend()

plt.show()

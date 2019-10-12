import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

n_bins = 60

x = np.random.uniform(1,0,10)
y = 1

plt.hist(x, bins=n_bins,edgecolor='black', linewidth=1.2)


plt.show()
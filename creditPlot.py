import matplotlib.pyplot as plt
import numpy as np
x = [
    545,
    595,
    640,
    675,
    705,
    750
]

y = [
    18.982,
    17.967,
    12.218,
    8.612,
    6.680,
    5.150
]

colors = (0,0,0)
area = np.pi*3

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Credit Score')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
"""
============
Scatter plot
============

This example showcases a simple scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)  # 如果使用相同的seed( )值，则每次生成的随即数都相同；


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
print(x)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
# print(area)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions and methods is shown in this example:
import matplotlib

matplotlib.axes.Axes.scatter
matplotlib.pyplot.scatter

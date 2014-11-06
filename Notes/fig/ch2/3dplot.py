from matplotlib import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import math

fig = plt.figure(figsize=[8,2])

ax = fig.add_subplot(111, projection='3d')


U = V = np.arange(0, 2*pi + 2*pi/700, 2*pi/700)

U, V = np.meshgrid(U, V)

#Parametrize the curve
X = 2*U*np.cos(V)
Y = 2*U*np.sin(V)
Z = U**2

ax.set_xticklabels("","")
ax.set_yticklabels("","")
ax.set_zticklabels("","")
ax.set_zlim([5,35])
ax.set_ylim([-1.5*pi*2,1.5*pi*2])
ax.set_xlim([-1.5*pi*2,1.5*pi*2])
ax.elev = -20
ax.azim = 5
plt.axis('off')

ax.plot_surface(X, Y, Z,  rstride=20, cstride=40, cmap=cm.Blues, linewidth=0.25, alpha=0.8)

fig.savefig('paraboloid_vortex.eps',bbox_inches='tight')
fig.savefig('paraboloid_vortex.png',bbox_inches='tight')
fig.savefig('paraboloid_vortex.pdf',bbox_inches='tight')


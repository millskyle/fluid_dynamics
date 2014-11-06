from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from math import * #import math
from mpltools.style import use as uuu
from mpmath import besseljzero
uuu('ggplot')

a=100.0
nu=1.0
nmax=100
resolution=100.0
U=1.0
v=1.0

position=1
y_max = 10
y2_max= 10 / sqrt(10)
#y_max=10.0 /sqrt(10)
def u(y,t):
   eta = y/sqrt(v*t)
   return float(U*(1.0-1/sqrt(pi)*float(quad(lambda x: exp(-x**2/4.0),0,eta)[0])))
fig = plt.figure(num=None, figsize=(10,4.4), dpi=300)

ax = fig.add_subplot(1,2,1)
ax1 = fig.add_subplot(1,2,2)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height])
box1 = ax1.get_position()
ax1.set_position([box1.x0, box1.y0, box1.width, box1.height])


ax.axis([0,y_max,0,1.05])
ax1.axis([0,y2_max,0,1.05])

ax.set_yticks([1,0.8,0.6,0.4,0.2,0])
ax.set_yticklabels(["$U$","","","","","0"])
ax.set_xticks([i*y_max/5 for i in range(6)])
ax.set_xticklabels(["0","","","","","$10$"])
ax1.set_yticks([1,0.8,0.6,0.4,0.2,0])
ax1.set_yticklabels(["$U$","","","","","0"])
ax1.set_xticks([i*y2_max/5 for i in range(6)])
ax1.set_xticklabels(["0","","","","","$10/\\sqrt{\\nu t}$"])

fig.text(0.5,0.01, 'Distance from plate, $y$', ha='center', va='center')
fig.text(0.04,0.5, 'Flow speed, $u(y)$', ha='center', va='center', rotation='vertical')


mesh = [i/resolution for i in xrange(int(y_max*resolution))]
mesh2 = [i/resolution for i in xrange(int(y2_max*resolution))]

ax.plot([x for x in mesh],[u(i,1) for i in mesh], label="$t=1$", linewidth=2.0)
ax.plot([x for x in mesh],[u(i,10) for i in mesh], label="$t=10$", linewidth=2.0)

#main.set_ylabel('Flow speed, $u(y)$')
#main.set_xlabel("Distance from boundary, $y$")



ax1.plot([x for x in mesh2],[u(i,1) for i in mesh2], label="$t=1$", linewidth=2.0)
ax1.plot([x for x in mesh2],[u(i,10) for i in mesh2], label="$t=10$", linewidth=2.0)

ax1.legend(loc='center left', bbox_to_anchor=(box.x1+0.4, 0.8))

fig.savefig("A6_Q2_a_plot.eps")
fig.savefig("A6_Q2_a_plot.png")





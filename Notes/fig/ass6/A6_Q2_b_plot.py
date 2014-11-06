from scipy.integrate import quad
import numpy as np
import pylab
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
gg=6.0


y2_max = 10.0
y_max = 20.0

position=1
#y_max=10.0 /sqrt(10)
def u(r,t):
   return (gg / (2*pi*r)) * (1- exp(-r**2 / (4*v*t)))

def w(r,t):
   if (r==0 or t==0):
      return 0
   return (gg/(4*pi*v*t))*exp(-r**2 / (4*v*t))

axes = pylab.axes()

fig = plt.figure(num=None, figsize=(10,4.4), dpi=300)
fig2 = plt.figure(num=None, figsize=(10,4.4),dpi=300)
ax = fig.add_subplot(1,1,1)
ax1 = fig2.add_subplot(1,1,1)
box = ax.get_position()
#ax.set_position([box.x0-0.013, box.y0, box.width, box.height])
box1 = ax1.get_position()
#ax1.set_position([box1.x0+0.025, box1.y0, box1.width, box1.height])


ax.axis([0,20,0,0.35])
ax1.axis([0,5,0,0.6])

#xxx = "G"
ax.set_yticks([gg*(1-exp(-1.0/(1.0*v)))/(4*pi)] + [(0.25 - 0.05*i) for i in xrange(5)] + [0])
ax.set_yticklabels(["$\\frac{\\Gamma_0}{2\\pi}\\left(1-e^{-\\frac{1}{4\\nu}}\\right)$"]+[""]*5 + ["0"])
ax.set_xticks([i*5 for i in range(5)])

ax1.set_yticks([gg/(4*pi*v), 3*gg/(16*pi*v)    ,gg/(8*pi*v), gg/(16*pi*v),0])
ax1.set_yticklabels(["$\\frac{\\Gamma_0}{4\\pi\\nu}$","","","","","0"])
#ax1.set_xticks([i*y2_max/5 for i in range(6)])
#ax1.set_xticklabels(["0","","","","","$10/\\sqrt{\\nu t}$"])

#fig.text(0.5,0.01, 'Distance from plate, $y$', ha='center', va='center')
#fig.text(0.04,0.5, 'Flow speed, $u(y)$', ha='center', va='center', rotation='vertical')


mesh = [i/resolution for i in xrange(int(y_max*resolution))]
mesh2 = [i/resolution for i in xrange(int(y2_max*resolution))]

#ax.plot([x for x in mesh],[u(i+0.1,0.01) for i in mesh], label="$t=0.01$", linewidth=2.0)
ax.plot([x for x in mesh],[u(i+0.1,1.0) for i in mesh], label="$t=1$", linewidth=2.0)
ax.plot([x for x in mesh],[u(i+0.1,2.0) for i in mesh], label="$t=2$", linewidth=2.0)
ax.plot([x for x in mesh],[u(i+0.1,10.0) for i in mesh], label="$t=10$", linewidth=2.0)
ax.plot([x for x in mesh],[u(i+0.1,100.0) for i in mesh], label="$t=100$", linewidth=2.0)


ax1.plot([x for x in mesh2],[w(i+0.0001,1) for i in mesh2], label="$t=1$", linewidth=2.0)
ax1.plot([x for x in mesh2],[w(i+0.01,2) for i in mesh2], label="$t=2$", linewidth=2.0)
ax1.plot([x for x in mesh2],[w(i+0.01,10) for i in mesh2], label="$t=10$", linewidth=2.0)
ax1.plot([x for x in mesh2],[w(i+0.01,100) for i in mesh2], label="$t=100$", linewidth=2.0)


ax.set_ylabel("Angular fluid speed, $u_\\theta$")
ax.set_xlabel("Distance from line vortex, $r$")

ax1.set_ylabel("Vorticity, $\\omega_z$")
ax1.set_xlabel("Distance from line vortex, $r$")



pylab.axes().axes.yaxis.LABELPAD=-1000

#ax1.legend(loc='center left', bbox_to_anchor=(box.x1+0.10, 0.8))
#ax.legend(loc='center left', bbox_to_anchor=(box.x1+0.10, 0.8))
ax.legend()
ax1.legend()

fig.savefig("A6_Q2_bi_plot.eps")
fig.savefig("A6_Q2_bi_plot.png")

fig2.savefig("A6_Q2_bii_plot.eps")
fig2.savefig("A6_Q2_bii_plot.png")




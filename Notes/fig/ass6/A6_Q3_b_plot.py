from sympy.abc import x,n
from sympy.utilities.lambdify import lambdify
from scipy.special import j1,j0,jn_zeros
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
from mpltools.style import use as uuu
from mpmath import besseljzero
uuu('ggplot')

a=10.0
nu=1.0
nmax=100
Omega = 1.0
l = [float(besseljzero(1,n+1)) for n in range(nmax + 1)]

def u(r,t):
   summ=0
   for n in xrange(nmax):
      summ+=j1(r/a * l[n]) / (l[n] * j0(l[n]))  *  math.exp((- l[n]**2 * t * nu / a**2))
   return - 2 * Omega * summ

fig = plt.figure(num=None, figsize=(7.5,5), dpi=300)
ax = fig.add_subplot(1,1,1)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height])

ax.axis([0,a*100,0,Omega])

ax.set_yticks([0,Omega / 4, Omega / 2, 3*Omega / 4, Omega])
ax.set_yticklabels(["0.0","","$\\Omega/2$","$3\\Omega/4$","$\\Omega$"])
ax.set_xticks([0,100,200,300,400,500,600,700,800,900,1000])
ax.set_xticklabels(["0","","","","","$a/2$","","","","","$a$"])

ax.plot([Omega * x/(100*a) for x in xrange(int(a)*100+1)], label="$t=0$", color='#AFAFAF', linewidth=2.0)
ax.plot([u(i/100.0,1) for i in xrange(int(a)*100+1)], label="$t=1$", linewidth=2.0)
ax.plot([u(i/100.0,3) for i in xrange(int(a)*100+1)], label="$t=3$", linewidth=2.0)
ax.plot([u(i/100.0,5) for i in xrange(int(a)*100+1)], label="$t=5$", linewidth=2.0)
ax.plot([u(i/100.0,10) for i in xrange(int(a)*100+1)], label="$t=10$", linewidth=2.0)
ax.plot([u(i/100.0,20) for i in xrange(int(a)*100+1)], label="$t=20$", linewidth=2.0)
plt.xlabel('Distance from centre of cylinder, $r$')
plt.ylabel("Flow speed, $u_{\\theta}$",rotation="vertical")
ax.legend(loc='center left', bbox_to_anchor=(0.03, 0.77))

fig.savefig("A6_Q3_b_plot.eps")
fig.savefig("A6_Q3_b_plot.png")


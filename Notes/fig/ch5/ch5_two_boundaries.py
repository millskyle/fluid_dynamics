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
nu=10.0
nmax=50
U = 10.0
h = 1.0


def u(y,t):
   summ=0
   print "y=",y
   for n in xrange(1,nmax):
      summ+= (1./n)*exp(-n**2*pi**2*nu*t / h**2) * sin( n*pi*y/h)
   return U * (1 - y/h - (2./pi)*summ )


fig = plt.figure(num=None, figsize=(7.5,5), dpi=300)
ax = fig.add_subplot(1,1,1)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height])

ax.axis([-0.005*U,U,0,h])

ax.set_yticks([0,h / 4., h / 2., 3*h/4., h])
ax.set_yticklabels(["0","","$h/2$","","$h$"])
ax.set_xticks([0*U,0.2*U,0.4*U,0.6*U,0.8*U,1.0*U])
ax.set_xticklabels(["0","","","","","$U$"])

s = 100
rrange = np.linspace(0,h,100)

ax.plot( [u(i,h**2 / (pi**2 * nu*100)) for i in rrange], [i for i in rrange],label="$t=h^2 / 100\\pi\\nu$", linewidth=2.0)
ax.plot( [u(i,h**2 / (pi**2 * nu*10)) for i in rrange], [i for i in rrange],label="$t=h^2 / 10\\pi\\nu$", linewidth=2.0)
ax.plot( [u(i,h**2 / (pi**2 * nu*1.)) for i in rrange], [i for i in rrange],label="$t=h^2 / \\pi\\nu$", linewidth=2.0)
ax.plot( [u(i,1000.0) for i in rrange], [i for i in rrange],label="$t\\to\\infty$", linewidth=2.0)
plt.ylabel('$y$ position',rotation='vertical')
plt.xlabel("Flow speed, $u(y,t)$")
ax.legend(loc='center left', bbox_to_anchor=(0.68, 0.77))

fig.savefig("ch5_two_boundaries.eps")
fig.savefig("ch5_two_boundaries.png")


from sympy.abc import x,n
from sympy.utilities.lambdify import lambdify
from scipy.special import j1,j0,jn_zeros
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
from mpltools.style import use as uuu
from matplotlib.patches import Ellipse

uuu('ggplot')

k=2.4
h=1.0
D=1.0
w=1.0
a=0.01

def x(x0,y0,t):
   return 2*exp(1-2*h*k)*cosh(k*(h+y0))*sin(k*x0 - w*t) - x0
#   return -exp(k*y1)*sin(k*x1 - w*t) - x1

def y(x0,y0,t):
   return 2*exp(1-2*h*k)*sinh(k*(h+y0))*cos(k*x0 - w*t) - y0

#   return exp(k*y1)*cos(k*x1 - w*t) - y1




ts = [i/100.0 for i in xrange(1000)]
timespace = [-i for i in reversed(ts)] + [i for i in ts]
timespace = [i for i in ts]


print timespace


fig = plt.figure(num=None, figsize=(8,8), dpi=300)
ax = fig.add_subplot(1,1,1)

box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

def relabel_axis():
   ax.axis([-0.6,0.6,-1.1,0.1])
   ax.set_yticks([0,-2*h/10,-4*h/10,-6*h/10,-8*h/10,-h ])
   ax.set_yticklabels(["$y=0$","","","","","$y=-h$"])
   ax.set_xticks([-0.6,-0.4,-0.2,0,0.2,0.4,0.6])
   ax.set_xticklabels(["","","","$x=x_0$","",""])

relabel_axis()


#xlist = [x(0,-1.5,t) for t in timespace]
#ylist = [y(0,-1.5,t) for t in timespace]



points = [
[0,-0.2],
[0,-0.47],
[0,-0.675],
[0,-0.8],
[0,-0.9],
[0,-0.97],

#[0.4,-0.95],
#[-0.4,-0.95]

]


for pt in points :
   ax.plot( [x(pt[0],pt[1],t) for t in timespace], [-y(pt[0],pt[1],t) for t in timespace],  label="$t=20$", linewidth=2.0, color='#348abd')

ax.axhline(y=0.01, lw=10,color='k')
ax.axhline(y=-1.01, lw=10,color='k')

#plt.title("Flow speed decay of infinite cylinder")

#plt.xlabel('$x$')
#plt.ylabel("$y$")
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig.savefig("A8_Q1_plot.eps")
fig.savefig("A8_Q1_plot.png")


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

a=1.0
#plt.xkcd()
def u(y):
   return -(a**2 - y**2)

fig = plt.figure(num=None, figsize=(8,5), dpi=300)
ax = fig.add_subplot(1,1,1)

box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

def relabel_axis():
   ax.axis([-1.5,1.5,-20,110])
   ax.set_yticks([100,80,60,40,20,0,-20])
   ax.set_yticklabels(["0","","","","","$-Pa^2/4\\rho\\mu$",""])
   ax.set_xticks([-1,-0.5,0,0.5,1])
   ax.set_xticklabels(["$a$","",0,"","$a$"])

relabel_axis()

mesh = [-1000+i for i in range(1000)] + [i for i in range(1000)]

ax.plot( [x/1000.0 for x in mesh], [u(i)/10000.0 for i in mesh],  label="$t=20$", linewidth=2.0)
#plt.title("Flow speed decay of infinite cylinder")

plt.xlabel('Radial position,   $r$')
plt.ylabel("Flow speed,  $u_z(r)$")
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.axvline(x=a+0.02,linewidth=10.0,color='k')
ax.axvline(x=-a-0.02,linewidth=10.0,color='k')

ac="#AFAFAF"
plt.arrow(-0.33,100,0,-80,fc=ac,ec=ac,linewidth=1.5, head_width=0.065, head_length=3.0)
plt.arrow(-0.66,100,0,-45,fc=ac,ec=ac,linewidth=1.5, head_width=0.065, head_length=3.0)
plt.arrow(0.33,100,0,-80,fc=ac,ec=ac,linewidth=1.5, head_width=0.065, head_length=3.0)
plt.arrow(0.66,100,0,-45,fc=ac,ec=ac,linewidth=1.5, head_width=0.065, head_length=3.0)
plt.arrow(0,100,0,-95,fc=ac,ec=ac,linewidth=1.5, head_width=0.065, head_length=3.0)

#Pressure Gradient arrow
plt.arrow(-0.80,10,0,-12,fc='k',ec='k',linewidth=0.8,head_width=0.03,head_length=3.2)
plt.annotate("$\\large{\\nabla} p$",(-0.83,12))

#ellipse = Ellipse(xy=(0,120),width=2.0, height=30,edgecolor='k',lw=10,fc='None')
#ax.add_patch(ellipse)

fig.savefig("A6_Q1_b_plot.eps")
fig.savefig("A6_Q1_b_plot.png")


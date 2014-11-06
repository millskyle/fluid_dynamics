from sympy.abc import x,n
from sympy.utilities.lambdify import lambdify
from scipy.special import j1,j0,jn_zeros
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
from mpltools.style import use as uuu

uuu('ggplot')

h=1.0
#plt.xkcd()
def u(y):
   return (h**2 - y**2)

fig = plt.figure(num=None, figsize=(7.5,5), dpi=300)
ax = fig.add_subplot(1,1,1)

box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

def relabel_axis():
   ax.axis([-120,10,-1.5,1.5])
   ax.set_yticks([-1,-0.5,0,0.5,1.0])
   ax.set_yticklabels(["$-h$","","$0$","","$h$"])
   ax.set_xticks([0,-20,-40,-60,-80,-100,-120])
   ax.set_xticklabels(["$Ph^2 / 2\\rho\\mu$","","","","","0","","","","0",""])

relabel_axis()



mesh = [-1000+i for i in range(1000)] + [i for i in range(1000)]

ax.plot( [u(i)/10000.0 for i in mesh],[x/1000.0 for x in mesh],  label="$t=20$", linewidth=2.0)
#plt.title("Flow speed decay of infinite cylinder")

plt.ylabel('Position,  $y$')
plt.xlabel("Flow speed,  $u(y)$")
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.axhline(y=h+0.03,linewidth=10.0,color='k')
ax.axhline(y=-h-0.03,linewidth=10.0,color='k')

ac="#AFAFAF"
plt.arrow(-100,-0.33,80,0,fc=ac,ec=ac,linewidth=1.5, head_width=0.075, head_length=2.0)
plt.arrow(-100,-0.66,45,0,fc=ac,ec=ac,linewidth=1.5, head_width=0.075, head_length=2.0)
plt.arrow(-100,0.33 ,80,0,fc=ac,ec=ac,linewidth=1.5, head_width=0.075, head_length=2.0)
plt.arrow(-100,0.66,45,0,fc=ac,ec=ac,linewidth=1.5, head_width=0.075, head_length=2.0)
plt.arrow(-100,0,95,0,fc=ac,ec=ac,linewidth=1.5, head_width=0.075, head_length=2.0)

#Pressure Gradient arrow
plt.arrow(-13,0.70,11,0,fc='k',ec='k',linewidth=0.8,head_width=0.07,head_length=2.7)
plt.annotate("$\\large{\\nabla} p$", (-18,0.67))


fig.savefig("A6_Q1_a_plot.eps")
fig.savefig("A6_Q1_a_plot.png")


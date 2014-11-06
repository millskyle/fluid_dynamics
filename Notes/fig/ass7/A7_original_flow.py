import matplotlib.pyplot as plt
import math
#from mpltools.style import use as uuu

#uuu('ggplot')

h=1.0
#plt.xkcd()
def u(y,c=0):
   if y==0:
      return 500
   else:
      return c/y

fig = plt.figure(num=None, figsize=(7.5,5), dpi=300)
ax = fig.add_subplot(1,1,1)

#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

def relabel_axis():
   ax.axis([900,1100,-0.01,400])
#   ax.set_yticks([-1,-0.5,0,0.5,1.0])
#   ax.set_yticklabels(["","","","","$h$"])#
#   ax.set_xticks([0,-20,-40,-60,-80,-100,-120])
#   ax.set_xticklabels([""])

relabel_axis()



mesh = [-1000+i for i in range(1000)] + [i for i in range(1000)]

for j in range(200):
   j=(j-100)*1.5
   ax.plot( [u(i/1000.0,j) for i in mesh], linewidth=2.0, color='k')


ax.axvline(x=0,linewidth='50')

#plt.title("Flow speed decay of infinite cylinder")

plt.ylabel('y')
plt.xlabel("x")
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ac="#AFAFAF"

#Pressure Gradient arrow
#plt.arrow(-13,0.70,11,0,fc='k',ec='k',linewidth=0.8,head_width=0.07,head_length=2.7)
#plt.annotate("$\\large{\\nabla} p", (-18,0.67))


fig.savefig("A7_original_flow.eps")
fig.savefig("A6_original_flow.png")


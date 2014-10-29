#!/usr/bin/python
import sympy, math
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import sympy.mpmath as mpmath
#======================
#--- Configuration ---#
#======================
show_streamfunction = False #   #Display the function that's going to be plotted in a "popup"
output_file_name = "Temp"   #Name the file
xlim=(-2,2)                      #Bounds on the display x-axis
ylim=(0,2)                      #Bounds on the display y-axis
is_complex_potential = True      #True if the functions given are w. False if they're Psi
arrow_size=1

density_factor = 4.5             #More or less streamlines
thickness_factor =0.8            #Streamline thickness
constant_thickness = True        #False if thickness based on velocity (sometimes causes error).

def mapping(z):
   return z

#List of implicit functions to plot
function_list = [
"1.0/2.0*a*z**2",
]

#======================
#---   Constants   ---#
#======================
#Define any constants which are used in the equations above
pi = math.pi
U = 2.0
d = 0.7
aa = -pi/4
a = 1.0
A = 1.0
l = 1.0
n=3
c = 1.01
S=1.0
gg = 3.0

def zz(t):
   return 1.0 + 1.0*sympy.I

#Map commonly used functions to the sympy equivalent
def exp(x):
   return sympy.exp(x)
def log(z):
   return sympy.log(z)
def ln(z):
   return sympy.log(z)
def sin(x):
   return sympy.sin(x)
def cos(x):
   return sympy.cos(x)
def tan(x):
   return sympy.tan(x)
def sqrt(x):
   return sympy.sqrt(x)
def frac(x,y):
   return float(x) / float(y)
#Calculate the base density dynamically based on limits
density = math.sqrt(float(abs(xlim[0] - xlim[1])) * float(abs(ylim[0]-ylim[1]))) / 3.0
x0, x1 = xlim
y0, y1 = ylim

scale = 3.0
colors=['k','r','g','b']

def stream_function(function,U=1, R=1):
   #takes a function string and returns a symbolic function. 
   r = sympy.sqrt(x**2 + y**2)
   theta = sympy.atan2(y, x)
   I = i = sympy.I
   z = sympy.Symbol('z', complex=True)
   z = x + sympy.I*y
   z = sympy.piecewise_fold(mapping(z))
   return eval(function)

def velocity_field(psi):
    if show_streamfunction:
        sympy.preview(psi)
    global w
    if is_complex_potential:
       print "Assuming complex potential given"
       u = sympy.lambdify((x, y), sympy.im(psi.diff(y)), 'numpy')
       v = sympy.lambdify((x, y), -sympy.im(psi.diff(x)), 'numpy')
    else:
       print "Assuming stream function given"
       u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
       v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
   # u = np.vectorize(u)
   # v = np.vectorize(v)
    return u, v

COUNTER=0
def plot_streamlines(ax, u, v, xlim=(-1, 1), ylim=(-1, 1)):
    global COUNTER
    COUNTER+=1
    plt.xlim([x0,x1])
    plt.ylim([y0,y1])
#    plt.xlim([c,c+1])
#    plt.ylim([0.25,0.75])
    Y, X =  np.ogrid[y0-0.25*abs(y0):y1 + 0.25*abs(y1):1000j, x0 - 0.25 * abs(x0):x1 + 0.25 * abs(x1):1000j]
    uu = u(X, Y)
    vv = v(X, Y)
    if not constant_thickness:
       lw = np.sqrt(uu**2 + vv**2)
       lw = lw * thickness_factor
       tooHigh = lw > 5 #If the width is calculated to be higher than this number,
       lw[tooHigh] = 5 #we want to make it equal to this number
       tooLow = lw < 0.05
       lw[tooLow] = 0.05
       lw = 2.0 * thickness_factor
    else:
       lw = 2.0
    print "Plotting..."
    ax_thick = 0.75 * (abs(xlim[0]) + abs(xlim[1]))
    ax.streamplot(X, Y, uu, vv, density=density_factor*density, color=colors[COUNTER-1], linewidth=lw, arrowsize=arrow_size, minlength=0.2)
    ax.axvline(x=0, color='k',  linewidth=ax_thick+1)
    #ax.axvline(x=c, color='red',  linewidth=ax_thick, label="z=c")
    #ax.text(c, -0.10, "$z=c$", size=40, color='red')
    ax.axhline(y=0, color='k',  linewidth=ax_thick+1)
    #circ = plt.Circle((0,0), radius=a, color='b', fill=False, linewidth=8.0)
    #ax.add_artist(circ)
#

def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    for spine in ax.spines.itervalues():
        spine.set_visible(False)


fig, ax = plt.subplots(figsize=(scale*(abs(xlim[0]) + abs(xlim[1])), scale*(abs(ylim[0]) + abs(ylim[1]))))

def addPlot(function):
   print "Setting up stream function"
   psi = stream_function(function)
   print "Calculations..."
   u, v = velocity_field(psi)

   print "Differentiating/Evaluating..."
   plot_streamlines(ax, u, v, xlim, ylim)

   format_axes(ax)

for w in function_list:
   addPlot(w)

plt.savefig("output/" + output_file_name + ".png")
plt.savefig("output/eps/" + output_file_name + ".eps")

#!/usr/bin/python
import sympy, math
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import lic_internal
import sympy.mpmath as mpmath
import pylab as plt
from matplotlib.colors import LinearSegmentedColormap
#======================
#--- Configuration ---#
#======================
show_streamfunction = False # #Display the function that's going to be plotted in a "popup"
output_file_name = "Temp"     #Name the file
xlim=(-2,2.0)                   #Bounds on the display x-axis
ylim=(-2, 2.0)                   #Bounds on the display y-axis
is_complex_potential = True  #True if the functions given are w. False if they're Psi
arrow_size=2
size=1500
density_factor = 1.0             #More or less streamlines
thickness_factor =1.0            #Streamline thickness
constant_thickness = False        #False if thickness based on velocity (sometimes causes error).
kernel_density = 100 #"Smearing Strength"

#List of implicit functions to plot
function_list = [
"i*ln( (z + 1./2 ) / (z-1./2 ) )",
#"z**2 - 2*0.2*z",
]

def mapping(z):
   return z #mapping, `return z' will result in no mapping.

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

#Calculate the base density dynamically based on the field of view
#density=sqrt(width*height)/3 : just a formula that gives decent results, nothing physical
density = math.sqrt(float(abs(xlim[0] - xlim[1])) * float(abs(ylim[0]-ylim[1]))) / 3.0
x0, x1 = xlim
y0, y1 = ylim

scale = 3.0
colors=['k','r','g','b']

def stream_function(function): #takes a string as a function and converts it to symbols.
   #takes a function string and returns a symbolic function. 
   # r is defined symbolically as sqrt(x**2+y**2)
   r = sympy.sqrt(x**2 + y**2)
   # theta is the arctan of y/x
   theta = sympy.atan2(y, x)
   #define both capital and lowercase i as the imaginary unit
   I = i = sympy.I
   #define z as a complex number
   z = sympy.Symbol('z', complex=True)
   #define z as x+iy
   z = x + i*y
   #Run z through the mapping, allow piecewise (beta)
   z = sympy.piecewise_fold(mapping(z))
   return eval(function)

def velocity_field(psi): #takes a symbolic funciton and returns two lambda functions
#to evaluate the derivatives in both the x and y directions.
    if show_streamfunction:
        sympy.preview(psi)
    global w
    if is_complex_potential:
       print "Complex potential, w(z) given"
       #define u, v symbolically as the imaginary part of the derivatives
       u = sympy.lambdify((x, y), sympy.im(psi.diff(y)), 'numpy')
       v = sympy.lambdify((x, y), -sympy.im(psi.diff(x)), 'numpy')
    else:
       #define u,v as the derivatives 
       print "Stream function, psi given"
       u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
       v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    return u, v

COUNTER=0
def plot_streamlines(u, v, xlim=(-1, 1), ylim=(-1, 1)):
    global COUNTER
    COUNTER+=1
    #define a grid on which to calculate
    Y,X = np.ogrid[y0 - 0.25 * abs(y0):y1 + 0.25 * abs(y1):size*1j,
                   x0 - 0.25 * abs(x0):x1 + 0.25 * abs(x1):size*1j]
    uu = u(X, Y) #Evaluate the horizontal derivative at each grid point.
    vv = v(X, Y) #Evaluate the vertical derivative at each grid point.

    print "Plotting..."
    ax_thick = 0.75 * (abs(xlim[0]) + abs(xlim[1]))
    cmap = LinearSegmentedColormap.from_list('name', ['black', 'white', 'black','white'])
    dpi=1200
#    plt.clf()
    plt.axis('off')
    kernel = np.arange(kernel_density).astype(np.float32)

    squ = np.reshape(uu, (size,size)).astype(np.float32) * 100
    sqv = np.reshape(vv, (size,size)).astype(np.float32) * 100

    vectors=np.dstack((squ,sqv)).astype(np.float32)
    texture = np.random.rand(size,size).astype(np.float32)

    image = lic_internal.line_integral_convolution(vectors, texture, kernel)
    #plt.figimage(image,cmap=plt.cm.Greys)

    plt.figimage(image,cmap=cmap)
    velocity = np.linalg.norm(vectors, axis=2)
    np.putmask(velocity, velocity>=20*np.mean(velocity), 20*np.mean(velocity))
#    np.putmask(velocity, velocity<=0.1*np.mean(velocity), 0.1*np.mean(velocity))
    velocity = np.sqrt(velocity)

    plt.figimage(velocity, cmap=plt.cm.YlOrRd, alpha=0.6)
    plt.gcf().set_size_inches((size/float(dpi),size/float(dpi)))
    plt.savefig("flow-image.png",dpi=dpi)


def addPlot(function):
   print "Setting up stream function"
   psi = stream_function(function)
   print "Calculations..."
   u, v = velocity_field(psi)

   print "Differentiating/Evaluating..."
   plot_streamlines(u, v, xlim, ylim)


for w in function_list:
   addPlot(w)


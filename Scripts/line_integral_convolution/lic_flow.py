#!/usr/bin/python
import sympy, math
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import lic_internal
import sympy.mpmath as mpmath
import pylab as plt
import scipy.ndimage
from scipy import stats
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import Normalize
from colormap_adjust import cmap_center_point_adjust

from config import *


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

x0, x1 = xlim
y0, y1 = ylim

def stream_function(function): #takes a string.
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
   z = mapping(z)
   return eval(function)

def velocity_field(psi): #takes a symbolic function and returns two lambda functions
#to evaluate the derivatives in both x and y.
    global w
    if is_complex_potential:
       print "Complex potential, w(z) given"
       #define u, v symbolically as the imaginary part of the derivatives
       u = lambdify((x, y), sympy.im(psi.diff(y)), modules='numpy')
       v = lambdify((x, y), -sympy.im(psi.diff(x)), modules='numpy')
    else:
       #define u,v as the derivatives 
       print "Stream function, psi given"
       u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
       v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    if (branch_cuts): # If it's indicated that there are branch cuts in the mapping,
                      # then we need to return vectorized numpy functions to evaluate
                      # everything numerically, instead of symbolically 
                      # This of course results in a SIGNIFICANT time increase
                      #   (I don't know how to handle more than the primitive root
                      #   (symbolically in Sympy
       return u,v
    else:
       # If there are no branch cuts, then return the symbolic lambda functions (MUCH faster)
       return u,v

def plot_streamlines(u, v, xlim=(-1, 1), ylim=(-1, 1)):
    global COUNTER
    #define a grid on which to calculate everything
    Y,X = np.ogrid[y0 - 0.25 * abs(y0):y1 + 0.25 * abs(y1):size*1j,
                   x0 - 0.25 * abs(x0):x1 + 0.25 * abs(x1):size*1j]
    print "Differentiating"

    u = np.vectorize(u, otypes=[np.float])
    v = np.vectorize(v, otypes=[np.float])
    uu = u(X,Y) #Evaluate the horizontal derivative at each grid point.
    vv = v(X,Y) #Evaluate the vertical derivative at each grid point.

    print "Plotting..."
    #color map for the convolution plot
    cmap = LinearSegmentedColormap.from_list('name', ['black','white','black','white'])
    #define the kernel (just a vector of numbers)
    kernel = np.arange(kernel_density).astype(np.float32)

    #reshape the velocities to fill in grid
    squ = np.reshape(uu, (int(size),int(size))).astype(np.float32)
    sqv = np.reshape(vv, (int(size),int(size))).astype(np.float32)
    #stack the velocities element-wise so we have a 2-tuple at each grid point.
    vectors = np.dstack((squ,sqv)).astype(np.float32)
    #generate the background noise.
    texture = np.random.rand(size/grain_size,size/grain_size).astype(np.float32)
    #resize the background noise to the resolution of the image by nearest neighbor interpolation (in order to provide support for larger grain size)
    texture = scipy.ndimage.zoom(texture, grain_size, order=1)

    #Do the Line Integral Convolution.
    image = lic_internal.line_integral_convolution(vectors, texture, kernel)

    plt.axis('off')
    plt.figimage(image,cmap=cmap)
    #calculate the velocities (ie: norm of velocity vector)
    velocity = np.linalg.norm(vectors, axis=2)
    #Cap the velocities at 10x the mean velocity (to prevent singularities from
    #skewing the color map
#    np.putmask(velocity, velocity>10*np.mean(velocity), 10*np.mean(velocity))

    #sqrt the velocities, to make the differences less drastic.
    velocity = np.sqrt(velocity)

    theCM = plt.cm.get_cmap('bwr')
    theCM._init()

    #oldcm = matplotlib.cm.bwr
    oldcm = matplotlib.cm.Spectral_r

    v_at_infty = math.sqrt(u(1e9,1e9)**2 + v(1e9,1e9)**2)

    scm = cmap_center_point_adjust(oldcm, (np.min(velocity),np.max(velocity)), v_at_infty)


    #plot the heat map
    dpi=300
    imm = plt.figimage(velocity, cmap=scm, alpha=0.5)
    plt.gcf().set_size_inches((size/float(dpi),size/float(dpi)))
    plt.savefig("flow-image.png",dpi=dpi)

def validate():
   global grain_size
   grain_size = int(grain_size)

def addPlot(function):
   validate()
   psi = stream_function(function)
   u, v = velocity_field(psi)
   plot_streamlines(u, v, xlim, ylim)

addPlot(w_psi)


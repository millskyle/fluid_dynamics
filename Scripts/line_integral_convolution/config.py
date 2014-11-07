import math
import sympy
#======================
#--- Configuration ---#
#======================
#Bounds on the display x axis
xlim=(-3,3.0)
#Bounds on the display y-axis
ylim=(-3, 3.0)      #Bounds on the display y-axis
#Size of the grid on which to evaluate (and pixel size of final image)
size=2000
#Pixel size of the random noise ( n x n ). size/grain_size must be integer.
grain_size=8
#Smearing strength (over how many pixels do we smear one pixel?)
kernel_density=400
#if w_psi below is a complex potential, this should be true. If it's a stream function, false
is_complex_potential = True  #True if the functions given are w. False if they're Psi
#Do we need to be careful of branch cuts (nth roots in the function/mapping?)
#   (this slows computation immensely, so only turn on if sure
branch_cuts = True


#Function to plot:
w_psi = " U*((z+ll)*exp(-i*aa) + ((a+ll)**2 / (z+ll))*exp(i*aa)) - (i*gg/(2*pi))*ln(z+ll) "

def mapping(z): #mapping: `return z` results in no mapping
   #Joukowski Transformation (piecewise because of branch cut on negative real axis)
   z = (sympy.Piecewise((1./2.*z+sympy.sqrt(1/4.*z**2-a**2),sympy.re(z)>0),(1./2.*z-sympy.sqrt(1/4.*z**2-a**2),sympy.re(z)<=0),(1./2.*z+sympy.sqrt(1/4.*z**2-a**2),True)) )
   return z


#======================
#---   Constants   ---#
#======================
#Define any constants which are used in the equations above
pi = math.pi
U = 1.0
d = 0.7
aa = -pi/10
a = 1.0
A = 1.0
l = 1.0
ll = 0.15
n = 3
c = 0.25
S=1.0
gg = -4*pi*U*a*math.sin(aa)+1


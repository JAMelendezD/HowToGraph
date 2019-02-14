from sympy import *
import numpy as np
import os
import argparse
from numpy import sin, cos, exp, log, sqrt
import scipy.special as sp
from matplotlib import colors
from sympy.physics.hydrogen import R_nl
   
#cell size
xsize = 80.111
ysize = 80.111
zsize = 80.111

#arguments from terminal
parser = argparse.ArgumentParser()
parser.add_argument("representation", type=str, help="Your desire representation: abs, real, img, field. When using real or img their counterpart will be missing sometimes (l = 3) in this cases you can use abs if m = 0 but for the other cases you need to create the real part rename the output file then create the imaginary part and in the pymol terminal type load outputname.pdb.")
parser.add_argument("l", type=int, help="Angular quantum number between 0 and n-1.")
parser.add_argument("m", type=int, help="Magnetic quantum number between -l and l.")
parser.add_argument("grid", type=int, help="Resolution for new equations maximum is 300")
parser.add_argument("scale", type=int, help="Factor that rescales the coordinates minimum 50")
args = parser.parse_args()

#main variables
factor = args.scale
plot = args.representation
l = args.l 
m = args.m 
grid = args.grid
area = grid*grid   
PHI, THETA = np.mgrid[0:2*np.pi:grid*1j, 0:np.pi:grid*1j]
contador1 = 0

#plot the real part of the spherical harmonics
if plot == 'real':
	R = sp.sph_harm(m, l, PHI, THETA).real
	x = factor*R*sin(THETA)*cos(PHI)
	y = factor*R*sin(THETA)*sin(PHI)
	z = factor*R*cos(THETA)
	color = R/R.max()

	#write information to be read by pymol
	with open('orbital.pdb', 'w') as f:
	    f.write("TITLE     Function\n")
	    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
	    for j in range(len(y)):
	        contador1+=1
	        contador2 = 1
	        for i in range(len(x)):
	            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area-contador1*grid+contador2,x[i][j],y[i][j],z[i][j],color[i][j]))
	            contador2+=1
	    f.write("END")

	os.system('pymol showorbital.pml')

#plot the imaginary part of the spherical harmonics
if plot == 'img':
	R = sp.sph_harm(m, l, PHI, THETA).imag
	x = factor*R*sin(THETA)*cos(PHI)
	y = factor*R*sin(THETA)*sin(PHI)
	z = factor*R*cos(THETA)
	color = R/R.max()

	#write information to be read by pymol
	with open('orbital.pdb', 'w') as f:
	    f.write("TITLE     Function\n")
	    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
	    for j in range(len(y)):
	        contador1+=1
	        contador2 = 1
	        for i in range(len(x)):
	            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area-contador1*grid+contador2,x[i][j],y[i][j],z[i][j],color[i][j]))
	            contador2+=1
	    f.write("END")

	os.system('pymol showorbital.pml')

#plot the absolute value of the spherical harmonics
if plot == 'abs':
	R = np.abs(sp.sph_harm(m, l, PHI, THETA))
	x = factor*R*sin(THETA)*cos(PHI)
	y = factor*R*sin(THETA)*sin(PHI)
	z = factor*R*cos(THETA)
	color = R/R.max()

	#write information to be read by pymol
	with open('orbital.pdb', 'w') as f:
	    f.write("TITLE     Function\n")
	    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
	    for j in range(len(y)):
	        contador1+=1
	        contador2 = 1
	        for i in range(len(x)):
	            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area-contador1*grid+contador2,x[i][j],y[i][j],z[i][j],color[i][j]))
	            contador2+=1
	    f.write("END")

	os.system('pymol showorbital.pml')

#plot the real part of the spherical harmonics like a field
if plot == 'field':
	R = sp.sph_harm(m, l, PHI, THETA).real
	s = 1
	x = factor*(s*R+1)*np.sin(THETA)*np.cos(PHI)
	y = factor*(s*R+1)*np.sin(THETA)*np.sin(PHI)
	z = factor*(s*R+1)*np.cos(THETA)
	color = R/R.max()
	#write information to be read by pymol
	with open('orbital.pdb', 'w') as f:
	    f.write("TITLE     Function\n")
	    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
	    for j in range(len(y)):
	        contador1+=1
	        contador2 = 1
	        for i in range(len(x)):
	            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area-contador1*grid+contador2,x[i][j],y[i][j],z[i][j],color[i][j]))
	            contador2+=1
	    f.write("END")

	os.system('pymol showorbital.pml')


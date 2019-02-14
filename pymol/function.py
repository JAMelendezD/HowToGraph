import numpy as np
import os
import argparse
from numpy import sin, cos, exp, log, sqrt

#arguments from terminal
parser = argparse.ArgumentParser()
parser.add_argument("plot", type=str, help="Your desire plot: saddle, trig, exp, wave, pyramid, paper. If set to new you can type any function you desire in the last argument. If you are using an example type anything you want for the last argument.")
parser.add_argument("lb", type=float, help="Lower limit for x and y")
parser.add_argument("ub", type=float, help="Upper limit for x and y")
parser.add_argument("grid", type=int, help="Resolution for new equations maximum is 300")
parser.add_argument("scale", type=int, help="Factor that rescales the x and y axis maximum 90 minimum 20")
parser.add_argument("equation", type=str, help="Type any function with variables X and Y you can use numpy functions without np. but you need to write parentheses in between ''. ")
args = parser.parse_args()

#cell size
xsize = 80.111
ysize = 80.111
zsize = 80.111

#scale factor and type of plot
plot = args.plot
factor = args.scale/args.ub

#example functions
if plot == 'saddle':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*(X**2-Y**2)

elif plot == 'trig':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*cos(X)*cos(Y)

elif plot == 'exp':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*(1 - X/ 2 + X**7 + Y**3)*exp(-X**2 -Y**2)

elif plot == 'wave':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*10*(sin(sqrt(X**2+Y**2))/sqrt(X**2+Y**2))

elif plot == 'pyramid':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*(1-abs(X+Y)-abs(Y-X))	

elif plot == 'paper':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*sin(X*Y)	

#plot any function
elif plot == 'new':
	grid = args.grid
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*eval('%s' % args.equation)

#change to pdb format
color = np.zeros((len(x),len(y)))
contador1 = 0

#write function information to be read by pymol 
with open('function.pdb', 'w') as f:
    f.write("TITLE     Function\n")
    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
    for j in range(len(y)):
        contador1+=1
        contador2 = 1
        for i in range(len(x)):
            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area - contador1*grid +contador2,x[i],y[grid-j-1],function[i][j],abs(np.min(function)/factor)+(function[i][j]/factor)))
            contador2+=1
    f.write("END")


#write colormap information to be read by pymol
with open('colormap.pdb', 'w') as f:
    f.write("TITLE     Function\n")
    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
    for j in range(len(y)):
        contador1+=1
        contador2 = 1
        for i in range(len(x)):
            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area - contador1*grid +contador2,x[i],y[grid-j-1],color[i][j],abs(np.min(function)/factor)+(function[i][j]/factor)))
            contador2+=1
    f.write("END")

os.system('pymol showfunction.pml')

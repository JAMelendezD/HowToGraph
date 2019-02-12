import numpy as np
import os
import argparse

#arguments from terminal
parser = argparse.ArgumentParser()
parser.add_argument("plot", type=str, help="Your desire plot: saddle, trig, exp, wave, pyramid, paper")
parser.add_argument("lb", type=float, help="Lower limit for x and y")
parser.add_argument("ub", type=float, help="Upper limit for x and y")
parser.add_argument("grid", type=int, help="Resolution for new equations maximum is 300")
parser.add_argument("scale", type=int, help="Factor that rescales the x and y axis maximum 90 minimum 20")
parser.add_argument("equation", type=str, help="Set the plot argument as new then type any function with variables X and Y you can use numpy functions but need to write parentheses in between '' ")
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
	function = factor*np.cos(X)*np.cos(Y)

elif plot == 'exp':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*(1 - X/ 2 + X**7 + Y**3) * np.exp(-X**2 -Y**2)

elif plot == 'wave':
	grid = 50
	area = grid*grid
	x = factor*np.linspace(args.lb,args.ub,grid)
	y = factor*np.linspace(args.lb,args.ub,grid)
	sx = np.linspace(args.lb,args.ub,grid)
	sy = np.linspace(args.lb,args.ub,grid)
	X,Y = np.meshgrid(sx, sy)
	function = factor*10*(np.sin(np.sqrt(X**2+Y**2))/np.sqrt(X**2+Y**2))

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
	function = factor*np.sin(X*Y)	

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

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#function
with open('function.pdb', 'w') as f:
    f.write("TITLE     Function\n")
    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
    for j in range(len(y)):
        contador1+=1
        contador2 = 1
        for i in range(len(x)):
            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area - contador1*grid +contador2,x[i],y[grid-j-1],function[i][j],sigmoid(function[i][j]/factor)))
            contador2+=1
    f.write("END")

#colormap
with open('colormap.pdb', 'w') as f:
    f.write("TITLE     Function\n")
    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
    for j in range(len(y)):
        contador1+=1
        contador2 = 1
        for i in range(len(x)):
            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area - contador1*grid +contador2,x[i],y[grid-j-1],color[i][j],sigmoid(function[i][j]/factor)))
            contador2+=1
    f.write("END")

os.system('pymol show.pml')

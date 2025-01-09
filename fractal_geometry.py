import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize


 # julia is value of the c constant that is added each iteration
def iterator(c,num,brot,julia):
    if brot: #mandelbrot
        z = 0
        for n in range(num):
            z = z**2 + c
            if abs(z) >2:
                return n+1 #returns num of iterations it took to diverge
        return num #didn't diverge so returns max iterations

    else:     #julia set
        z = c
        for n in range(num):
            z = z**2 + julia
            if abs(z) >2:
                return n+1 #returns num of iterations it took to diverge
        return num #didn't diverge so returns max iterations

def brotter(xrange,yrange,brot,julia,max_iterations):

    # creates two lists one with x values and a matching y list for all values between the ranges passed in parameters
    xv, yv = np.meshgrid(xrange,yrange)
    # combines the two lists into one list with the y values being imaginary
    c = xv + 1j*yv
    # passes c values into iterator function to create a list of iterations it took for each x,yj
    iters = [iterator(val,max_iterations,brot,julia) for val in c.flatten()]

    return  xv,yv,np.array(iters) #returns co-ordinates to plot and list of the iterations they took to diverge or not for colouring

def scatterer(xlim1,xlim2,ylim1,ylim2,brot,julia,max_iterations): #brot is a bool and if true then it will just show mandelbrot set
    x_range = np.linspace(xlim1, xlim2, 1000)
    y_range = np.linspace(ylim1, ylim2, 1000)

    xes,yes,iters = brotter(x_range,y_range,brot,julia,max_iterations)

    colors = cm.viridis(iters/max_iterations) #maps number of iterations to colours
    plt.scatter(xes, yes, s=0.1, color=colors) #plots the points

    plt.ylabel("Imaginary")
    plt.xlabel("Real")

    #set axes ticks
    ax = plt.gca()
    ax.set_xlim([xlim1,xlim2]) # range of x values on axes
    ax.set_ylim([ylim1,ylim2]) # range of y values on axes

    norm = Normalize(vmin=0, vmax=max_iterations)  # Normalize the iteration values between 0 and 50 to range of 0 and 1
    cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cm.viridis),ax=ax)
    cbar.set_label("Iterations")

    plt.show()


mandelbrot = True #set to False if you want to plot a julia set ---> then change C value to which set you want to see
c = complex(-0.70176,-0.3842) #program will basically ignore this if mandelbrot is set to true
max_iters = 50   #better pc ---> can increase number of iterations

#play around with the xlims and ylims if the julia set appears to be cut off
scatterer(-2,1,-1.5,1.5,mandelbrot,c,max_iters)




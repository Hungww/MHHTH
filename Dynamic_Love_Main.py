from numpy import *
import pylab as p
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
from random import seed
from random import random
# Definition of parameters
a = 2.
b =4.            
c = -2.
d = -2.
def dX_dt(X, t=0):

    return np.array([ a*X[0] +   b*X[1] ,
                  c*X[0] + d*X[1] ])

X_f0 = np.array([ 0. , 0.])
X_f1 = np.array([ 10. , 10.])
def d2X_dt2(X, t=0):

    return np.array([[a,   b     ],
                  [c ,   d] ])



       

t = np.linspace(0, 10,  1000)              # time
X0 = np.array([5/4, 5/4])                     # initials conditions
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']      

R, J = X.T
f1 = plt.figure("Plot of the Love between Romero and Juliet's Model")
plt.plot(t, R, 'r-', label='Romero`s')
plt.plot(t, J  , 'b-', label='Juliet`s')
plt.grid()
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Love for the other')
plt.title('Love between Romero and Juliet')
f1.savefig('Dynamic_Love_Plot.png')




f2 = plt.figure("Phase Portrait of the Love between Romero and Juliet's Model")


nb_points   = 20

x = linspace(-10, 10, nb_points)
y = linspace(-10, 10, nb_points)

X1 , Y1  = meshgrid(x, y)                       # create a grid
DX1, DY1 = dX_dt([X1, Y1])                      # compute growth rate on the gridt
M = (hypot(DX1, DY1))                           # Norm of the growth rate 
M[ M == 0] = 1.                                 # Avoid zero division errors 
DX1 /= M                                        # Normalize each arrows
DY1 /= M


#1 
values2=([-8,9],[-9,8],       [-2,3],[-3,2],
        [-10,10],[10,-10],[-10,-10],[10,10],
        [-6,-7], [8,1],
        [3,-2],[2,-3],               [9,-8],[8,-9],

        #[-5,-10],[5,10],[2.5,10],[-10,-2.5],[-10,-5],[10,5]
 )
values  = ([10,10])                      # position of X0 between X_f0 and X_f1
 
for v  in (values2 ):
   #(v*X_f1) 
    X0 =  v                              # starting point
    X = integrate.odeint( dX_dt, X0, t)         # we don't need infodict here
    plt.plot( X[:,0], X[:,1],lw=0.6,  color="red")
plt.plot( X[:,0], X[:,1],lw=0.6, label="Trajectory",  color="red",)
plt.plot(0, 0,'o', label="Fixed Point",  color="white", mec='black', ms=7)

   
#-------------------------------------------------------
# Drow direction fields, using matplotlib 's quiver function
# I choose to plot normalized arrows and to use colors to give information on
# the growth speed
plt.title('Love between Romero and Juliet')
Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.jet)
plt.xlabel('Romero`s love for Juliet')
plt.ylabel('Juliet`s love for Romero')
plt.legend(loc='upper right')
plt.grid()


plt.xlim(-10, 10)
plt.ylim(-10, 10)
f2.savefig('Dynamic_Love_PhasePortrait.png')
plt.show()
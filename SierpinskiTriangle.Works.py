#SierpinskiTriangle by Eric Richardson
#9 Feb 2021

import numpy as np
import matplotlib.pyplot as plt
import random

# Try to collect starting point via the Console
# This does not error check for being outside the area bounded by the triangle (however even if you start outside of it you'll end up with just one or two outliers
MyStartX= float(input('random X from 0-10: '))
MyStartY= float(input('random Y from 0-10: '))

# Creating a numpy array last point is the one entered by user at console
X = np.array([0,5,10,MyStartX])
Y = np.array([0,8.66,0,MyStartY])

#confirm to console numbers entered
print ('data entered')
print (MyStartX, MyStartY)

#print iniital plots
plt.scatter(X,Y)

# Plot inital plot which is halfway between a random verticy and entered point
RndList = (random.randint(0,3))
NewMidX=((X[RndList]+MyStartX)/2)
NewMidY=((Y[RndList]+MyStartY)/2)
plt.scatter(NewMidX,NewMidY)

#begin loop to find hte halfway point beween lsat point plotted and a random verticy
#adjust the "while" for how many iterations, here it's set to 100. Be warned it could take qutie a while when you increase it to large numbers
count = 0
while (count < 500):

    #this loop will randomly choose one of the verticies to find the midway point from the last point plotted
    RndList = (random.randint(0,2))
    NewMidX=((X[RndList]+NewMidX)/2)
    NewMidY=((Y[RndList]+NewMidY)/2)
    plt.scatter(NewMidX,NewMidY)
    count = (count + 1)
plt.show()


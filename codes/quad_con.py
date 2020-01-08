#Drawing the Quadrilateral(Kite)
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *

#qadrilateral sides
a = math.sqrt(20)
b = math.sqrt(33)


#quadrilateral coordinates
A = np.array([-a,0]) 
E = np.array([0,a]) 
S = np.array([0,-b]) 
Y = np.array([a,0])
O = np.array([0,0])

#Mid point of AY
O =(A+Y)/2


#Generating all lines
x_AY = line_gen(A,Y)
x_SY = line_gen(S,Y)
x_EY = line_gen(E,Y)
x_AE = line_gen(A,E)
x_AS = line_gen(A,S)
x_ES = line_gen(E,S)

#Plotting all lines
plt.plot(x_SY[0,:],x_SY[1,:],label='$SY$')
plt.plot(x_AY[0,:],x_AY[1,:],label='$AY$')
plt.plot(x_EY[0,:],x_EY[1,:],label='$EY$')
plt.plot(x_AE[0,:],x_AE[1,:],label='$AE$')
plt.plot(x_AS[0,:],x_AS[1,:],label='$AS$')
plt.plot(x_ES[0,:],x_ES[1,:],label='$ES$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(-4,0)')
plt.plot(Y[0], Y[1], 'o')
plt.text(Y[0] * (1 - 0.2), Y[1] * (1) , 'Y(4,0)')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E(0,4.4)')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S(0,5.7)')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O(0,0)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('../figs/quad_con.pdf')
plt.savefig('../figs/quad_con.eps')
plt.show()








import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#Sides
a = 3
b = 5
c = 6
d = 2

#Triangle vertices
A = np.array([a,b]) 
B = np.array([0,0]) 
C = np.array([c,0])

#Mid point of BE and DE
D=(B+C)/3
E=(D+C)/2


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_AE = line_gen(A,E)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_AE[0,:],x_AE[1,:],label='$AE$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(3,5)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(0,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(6,0)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D(2,0)')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E(4,0)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../figs/tri_area.pdf')
plt.savefig('../figs/tri_area.eps')
#subprocess.run(shlex.split("termux-open ./figs/tri_area.pdf"))
#else
plt.show()


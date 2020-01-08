import numpy as np
import matplotlib.pyplot as plt
import math 
from coeffs import *

#Triangle& Rectangle sides
a = 19
c = 7
b = 4
d = 2

#Triangle vertices
A = np.array([d,a]) 
B = np.array([0,c]) 
C = np.array([b,c])
print(A,B,C)

#Rectangle vartices
D = np.array([0,0])
E = np.array([b,0])
print(B,D,C,E)

#Generating all lines
x_AC = line_gen(A,C)
x_BC = line_gen(B,C)
x_AB = line_gen(A,B)
x_BD = line_gen(B,D)
x_CE = line_gen(C,E)
x_DE = line_gen(D,E)


#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_CE[0,:],x_CE[1,:],label='$CE$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(2,19)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(0,7)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(4,7)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D(0,0)')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 - 0.2), E[1] * (1) , 'E(4,0)')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/tri_rect.pdf')
plt.savefig('../figs/tri_rect.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_alt.pdf"))
#else
plt.show()


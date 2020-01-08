#Drawing the isosceles triangle
import numpy as np
import matplotlib.pyplot as plt
import math 
from coeffs import *



#Triangle sides
a = 6
c = 6
b = math.sqrt(a**2 + c**2)

#Triangle vertices
A,B,C = tri_vert(a,b,c)

print(A,B,C)

#Generating all lines
x_AC = line_gen(A,C)
x_BC = line_gen(B,C)
x_AB = line_gen(A,B)


#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(0,6)')
plt.plot(C[0], B[1], 'o')
plt.text(C[0] * (1 - 0.2), C[1] * (1) , 'B(6,0)')
plt.plot(B[0], C[1], 'o')
plt.text(B[0] * (1 + 0.03), B[1] * (1 - 0.1) , 'C(0,0)')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/tri_isosc.pdf')
plt.savefig('../figs/tri_isosc.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_alt.pdf"))
#else
plt.show()


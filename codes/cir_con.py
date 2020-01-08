import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

len = 50
O1=np.array([0,0])
r1=3
O2=np.array([3,0])
r2=3
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O1).T
x_circ2 = np.zeros((2,len))
x_circ2[1,:] = r2*np.cos(theta)
x_circ2[0,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + O2).T

a=3
b=3
c=3
p = (c**2 + b**2-a**2 )/(2*c)
q = np.sqrt(b**2-p**2)
A = np.array([0,0])
B = np.array([3,0])
C = np.array([p,q])
D = np.array([p,-q])

print(B)

#ploting the circles
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle2$')

#Generating all lines
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)
x_AD = line_gen(A,D)
x_BC = line_gen(B,C)
x_BD=line_gen(B,D)
x_CD = line_gen(C,D)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')


#Plotting all points
plt.plot(D[0], D[1], 'D')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D(3/2,-2.59)')
plt.plot(C[0], C[1], 'C')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(3/2,2.59)')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A(0,0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.03), B[1] * (1 - 0.1) , 'B(3,0)')

#Plotting all lines


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/circle_con.pdf')
plt.savefig('../figs/circle_con.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()

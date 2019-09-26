import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from coeffs import * 

k=2
c = 20
x = np.linspace(-1*c,c,1501)


def G(x):
    return eval("lambda x:" + input("Enter f(x):"))
    
f = G(x)
    
plt.plot(x,f(x),color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('f(x)')
       
def F(x):
    return eval("lambda x:" + input("Enter df(x)/dx:"))

df = F(x)

y = eval(input("Take an intial guess:"))


fy = np.array([y,f(y)])
m = np.array([1,df(y)])
ly = line_dir_pt(m,fy,-1*k,k)
plt.plot(fy[0],fy[1],color=(0,1,0),marker='o',label="$f(Intial Guess)$")
plt.plot(ly[0,:],ly[1,:],color=(0,1,0))

z = gda(y,df,"Minimum")

fz = np.array([z,f(z)])
m = np.array([1,df(z)])
lz = line_dir_pt(m,fz,-1*k,k)
plt.plot(fz[0],fz[1],color=(1,0,0),marker='o',label="$f/{min}(x)$")
plt.plot(lz[0,:],lz[1,:],color=(1,0,0))

print("The Minimum of the given function is",f(z),"and occurs at",round(z,3))


plt.axis('equal')
plt.legend(loc='best')
plt.xlim((-20,20))
plt.ylim((-20,20))
plt.show()





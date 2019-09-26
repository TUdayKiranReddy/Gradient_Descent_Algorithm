import numpy as np
import matplotlib.pyplot as plt
from coeffs import * 


c = 10
k = 6
x = np.linspace(-1*c,c,151)
f = x + 2/x
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$ x+ 2/x $')
cur_x = 3 
f_cur_x = cur_x + 2/(cur_x)
mf_cur_x = np.array([cur_x,f_cur_x])
plt.plot(mf_cur_x[0],mf_cur_x[1],color=(0,1,0),marker='.',label="$f(x_0)$")

    
#For finding local minimum
gamma = 0.01 
precision = 0.00000000001
previous_step_size = 1 
max_iters = 10000000 
iters = 0 

df = lambda x: 1 - 2/(x**2)
m = np.array([1,df(cur_x)])
l_cur_x = line_dir_pt(m,mf_cur_x,-0.5*k,0.5*k)
plt.plot(l_cur_x[0,:],l_cur_x[1,:],color=(0,1,0))

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1



f_cur_x = cur_x + 2/(cur_x)
mf_cur_x = np.array([cur_x,f_cur_x])

m = np.array([1,df(cur_x)])
l_cur_x = line_dir_pt(m,mf_cur_x,-1*k,k)
plt.plot(l_cur_x[0,:],l_cur_x[1,:],color=(1,0,0))

#For finding local maximum
cir_x = -3
previous_step_size = 1 
iters = 0
df = lambda x: 1 - 2/(x**2)

f_cir_x = cir_x + 2/cir_x
mf_cir_x = np.array([cir_x,f_cir_x])
m = np.array([1,df(cir_x)])
l_cir_x = line_dir_pt(m,mf_cir_x,-0.5*k,0.5*k)
plt.plot(mf_cir_x[0],mf_cir_x[1],color=(0.5,0.5,0),marker='.',label="$f(y_0)$")
plt.plot(l_cir_x[0,:],l_cir_x[1,:],color=(0.5,0.5,0))

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cir_x
    cir_x += gamma * df(prev_x)
    previous_step_size = abs(cir_x - prev_x)
    iters+=1



f_cir_x = cir_x + 2/cir_x
mf_cir_x = np.array([cir_x,f_cir_x])

m = np.array([1,df(cir_x)])
l_cir_x = line_dir_pt(m,mf_cir_x,-1*k,k)
plt.plot(l_cir_x[0,:],l_cir_x[1,:],color=(0,0,1))

g = lambda x : x + 2/x
if(g(cur_x) > g(cir_x)):
	print("Minimum Value of t\N{SUPERSCRIPT TWO}\N{SUBSCRIPT ONE} is",(g(cir_x))**2)
	plt.plot(mf_cur_x[0],mf_cur_x[1],color=(1,0,0),marker='o',label="$max$$f(x)$")
	plt.plot(mf_cir_x[0],mf_cir_x[1],color=(0,0,1),marker='o',label="$min$$f(x)$")

else:
	print("Minimum Value of {t_1}^2 is",(g(cur_x))**2)
	plt.plot(mf_cur_x[0],mf_cur_x[1],color=(1,0,0),marker='o',label="$min$$f(x)$")
	plt.plot(mf_cir_x[0],mf_cir_x[1],color=(0,0,1),marker='o',label="$max$$f(x)$")


plt.axis('equal')
plt.legend(loc='best')
plt.xlim((-10,10))
plt.ylim((-10,10))
plt.show()


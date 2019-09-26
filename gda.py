import numpy as np
import matplotlib.pyplot as plt
from coeffs import * 


c=10


# ~ f = eval(input("Enter function f(x) :"))
# ~ f = lambda x: f


df =eval(input("Enter function df(x)/dx :"))
df = lambda x: df
#df=lambda x: 1 - 2/x**2

cur_x = eval(input("Take an intial guess:"))

cur_x = gda(cur_x,df,"Minimum")


print(cur_x)

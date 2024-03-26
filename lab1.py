#23
import math
me=math.e
eps=0.01
x=float(input("Input the x:"))
z=1
t=1
v=2
q=0

while abs(v)>eps:
    v=(math.log1p(x**z))/t
    z+=1
    t+=2
    q+=v
print(q)
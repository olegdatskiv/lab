from math import sqrt, exp , log , e
a=17
b=26
hx=0.01
hy=0.2
x=-1
y=-1
while x<=2:
    if x>0 and y>0:
        z=a*pow(x,2)+ log(e,b*x*y)
        print(z)
        x=x+hx
        y=y+hy
    else:
        z=pow(a,x)+pow(b,y)
        print(z)
        x=x+hx
        y=y+hy

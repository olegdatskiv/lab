from math import sqrt, exp , log , e
a=1
b=2
hx=0.1
hy=0.2
x=1
y=1
while x<=2:
    if x+y>1:
        z=a*pow(x,2)+ log(e,b*x*y)
        print(z)
        x=x+hx
        y=y+hy
    else:
        z=pow(a,x)+pow(b,y)
        print(z)
        x=x+hx
        y=y+hy

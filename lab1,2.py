from math import sqrt, exp , atan , e ,cos , sin
x=1.25
y=0.93
a=(1-y)*(((pow((x+y),2)/pow((x+4),3))/(pow(e,-(x-2))+(pow(x,3)+4))))
b=(1+cos(y-2))/(pow(x,2)+pow(sin(y-2),2))
p=a/b
print(p)

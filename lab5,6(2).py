a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    z=a-(b+c)
    print(z)
elif b>a and b>c:
    z=b-(a+c)
    print(z)
elif c>a and c>b:
    z=c-(b+a)
    print(z)
else:
    z=pow(a,2)+pow(b,4)+pow(c,6)
    print(z)

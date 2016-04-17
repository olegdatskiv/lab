F1=1
F2=1
input(1)
input(1)
n=1
while n<20:
    F3=F1+F2
    n=n+1
    F1=F2
    F2=F3
    print(F3)
n=1
F1=1
F2=1
while n<20:
    F3=F1+F2
    n=n+1
    F1=F2
    F2=F3
    if n>=4:
        print(F3)

import math
for i in range(int(input())):
    a=int(input())
    b=a*a
    r=math.sqrt(a)
    if int(r+0.5)**2==a:
        print("True")
    else:
        print("False")
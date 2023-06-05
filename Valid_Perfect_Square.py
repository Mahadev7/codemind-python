import math
for i in range(int(input())):
    x=int(input())
    y=math.sqrt(x)
    if int(y+0.5)**2==x:
        print("True")
    else:
        print("False")
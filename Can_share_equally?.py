a,b=map(int,input().split())
p=(1*a)+(2*b)
if a==0 and b%2==0:
    print("YES")
elif a==0 and b%2!=0:
    print("NO")
elif p%2==0:
    print("YES")
else:
    print("NO")
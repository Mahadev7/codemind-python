a=int(input())
x=list(map(int,input().split()))
if sorted(x)==x[::-1]:
    print("yes")
else:
    print("no")
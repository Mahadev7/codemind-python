a=[]
for i in range(int(input())):
    n=int(input())
    a.append(n)
t=int(input())
c=0
for i in a:
    if i>t:
        c+=2
    else:
        c+=1
print(c)
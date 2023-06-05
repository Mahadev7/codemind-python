b=[]
for i in range(int(input())):
    a=int(input())
    b.append(a)
t=int(input())
c=0
for i in b:
    if i>t:
        c+=2
    else:
        c+=1
print(c)
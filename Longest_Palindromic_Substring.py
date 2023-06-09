a=input()
b=list(a)
c=[]
for i in range(len(b)):
    for j in range(i,len(b)):
        s=b[i:j+1]
        c.append(s)
# print(c)
d=[]
c1=0
for i in c:
    if i==i[::-1]:
        if len(i)>c1: # 
            c1=len(i)
            p=i
print(''.join(p))
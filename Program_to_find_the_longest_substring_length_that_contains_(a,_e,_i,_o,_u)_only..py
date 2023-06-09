s=input()
b=list(s)
c=[]
for i in range(len(b)):
    for  j in range(i,len(b)):
        s=b[i:j+1]
        c.append(s)
v='aeiou'
p=[]
for i in c:
    s=0
    for j in i:
        if j in v:
            s+=1
        else:
            break
    p.append(s)
print(max(p))
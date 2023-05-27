a=input()
x=list(a)
b=[]
for i in range(len(x)):
    if x[i].isalnum():
        b.append(x[i])
        x[i]='*'
b.sort()
for i in range(len(x)):
    if x[i]=='*':
        x[i]=b[0]
        b.pop(0)
print("".join(x))
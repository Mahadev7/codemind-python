n=input()
x=list(n)
a=[]
for i in range(len(x)):
    if x[i].isalnum():
        a.append(x[i])
        x[i]='*'
a.sort()
for i in range(len(x)):
    if x[i]=='*':
        x[i]=a[0]
        a.pop(0)
print("".join(x))
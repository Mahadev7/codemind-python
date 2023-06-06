n=input()
p=list(n)
c=''
l=[]
for i in p:
    i=int(i)
    if i%2!=0:
        c+=str(i**2)
print(c)
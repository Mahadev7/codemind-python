a=input()
b=a.split()
x=[list(i) for i in b]
for i in x:
    print(min(i),max(i),end=' ')
a=input()
a=a.split()
a.sort()
a.sort(key=len)
for i in a:
    print(i,end=' ')
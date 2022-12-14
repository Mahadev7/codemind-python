a=list(map(str,input().split()))
c=''
for i in a:
    if len(i)>len(c):
        c=i
print(len(c))
        
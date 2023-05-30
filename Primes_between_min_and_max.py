def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
a = min(arr)
b = max(arr)
f=0
for i in range(n):
    if arr[i] == a:
        c = i
    if arr[i] == b:
        d = i
l=[]
if c<d:
    # l=[]
    for i in range(c,d+1):
        if fun(arr[i]):
            l.append(arr[i])
    # print(l)
if c>d:
    for i in range(d,c+1):
        if fun(arr[i]):
            l.append(arr[i])
    # print(l)
if c==d:
    if fun(arr[c]):
        l.append(arr[i])
p=set(l)
print(len(p))
        
n=int(input())
x=list(map(int,input().split()))
c=n//2
s1=0
s2=0
for i in range(c):
    s1+=x[i]
for i in range(c,n):
    s2+=x[i]
s=abs(s1-s2)
if s%4==0:
    print('X')
else:
    print("Y")
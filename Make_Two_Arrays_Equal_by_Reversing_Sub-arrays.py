n = int(input())
x = list(map(int,input().split()))
m = int(input())
y = list(map(int,input().split()))
if sorted(x) == sorted(y):
    print("True")
else:
    print("False")
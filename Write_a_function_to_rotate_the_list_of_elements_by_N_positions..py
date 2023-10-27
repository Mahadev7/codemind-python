n = int(input())
x = list(map(int,input().split()))
k = int(input())
c = k%n
a = x[-1*c:]
b = x[:-1*c]
print(*(a+b))
n = int(input())
s = ''
while n>0:
    n-=1
    s+=chr(n%26 + ord('A'))
    n//=26
print(s[::-1])
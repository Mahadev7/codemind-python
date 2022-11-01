n=int(input())
x=list(map(int,input().split()))    # 1 4 2 8 5
max = x[0];    
for i in range(len(x)):    
   if(x[i] > max):    
       max = x[i];    
           
print(str(max))
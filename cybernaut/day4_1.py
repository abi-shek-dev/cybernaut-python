x=list(map(int,input().split()))
y=[]

for i in x:
    if(i%2==0):
       y.append(i)

print(y)
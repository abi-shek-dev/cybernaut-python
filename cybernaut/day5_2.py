x=(5,8,12,3,15)
print("The tuple is: ",x)

z=[]

x=list(x)

y=list(map(int,input("Enter the number to be added in the tuple: ").split(" ")))

for i in y:
    x.append(i)

print("Elements added ...!")

print("The tuple after adding elements is ",tuple(x))

for i in x:
    if i%2 ==0:
        z.append(i**2)
    else:
        z.append(i)

print("The tuple after squaring even numbers is: ",tuple(z))
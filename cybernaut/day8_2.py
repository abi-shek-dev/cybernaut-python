def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
    
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print("The GCD of", x, "and", y, "is:", gcd(x, y))
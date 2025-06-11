x=int(input("Enter a number :"))
y=int(input("Enter another number :"))
z=int(input("Enter a third number :"))
largest = 0

if x > y and x > z:
    largest = x
    print("The largest number is", largest)
elif y > x and y > z:
    largest = y
    print("The largest number is", largest)
else:
    largest = z
    print("The largest number is", largest)

if largest % 2 == 0:
    print( largest," is even")
else:
    print(largest," is odd")
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))

try:
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input, please enter a valid number")
finally:
    print("Execution completed, whether successful or not.")
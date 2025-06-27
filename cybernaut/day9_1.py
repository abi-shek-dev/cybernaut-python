def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

x=int(input("Enter a number to find the sum of digits: "))
print("The sum of digits of", x, "is:", sum_of_digits(x))
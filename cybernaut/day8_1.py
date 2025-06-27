def is_palindrome(x):
    if x == x[::-1]:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

x=input("Enter the String to find whether it is a Palindrome or not: ")
is_palindrome(x)
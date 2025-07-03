numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

positive_odds = filter(lambda x: x > 0 and x % 2 != 0, numbers)

squared_odds = list(map(lambda x: x ** 2, positive_odds))

print(squared_odds)

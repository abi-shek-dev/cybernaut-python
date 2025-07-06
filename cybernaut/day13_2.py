import re

phone_numbers = ['97870 53958', '987-654-321', '98940 67443', 'abc-123-4567']

for number in phone_numbers:
    if re.fullmatch(r'\d{5} \d{5}', number):
        print(f"{number} is valid.")
    else:
        print(f"{number} is invalid.")

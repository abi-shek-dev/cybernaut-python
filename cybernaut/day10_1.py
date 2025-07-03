words = list(map(str,input('Enter the strings separated by space : ').split()))

vowel = filter(lambda word: word[0].lower() in 'aeiou', words)

uppercase = list(map(lambda word: word.upper(), vowel))

print("Words starting with a vowel (in uppercase):")
print(uppercase)
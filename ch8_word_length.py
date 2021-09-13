word = input("Please enter a word: ")

if len(word) > 5:
    print("Your word is greater than 5 characters long.")
elif len(word) < 5:
    print("Your word is less than 5 characters long.")
else:
    print("Your word is 5 characters long.")

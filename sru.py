title = input("Enter the book title: ")

title = title.lower()

vowels = 0
consonants = 0

for letter in title:
    if letter.isalpha():
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

# Question 28
ch = input("Enter a character: ")
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character")
elif ch.lower() in "aeiou":
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")

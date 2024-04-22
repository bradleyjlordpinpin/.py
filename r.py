import re

word = input("Enter a word that starts with 'a' and ends with 'e': ")
pattern = r'"[^"]*"'
match = re.match(pattern, word)

if match:
    print("Valid.")
else:
    print("Invalid")

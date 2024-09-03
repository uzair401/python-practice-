import cs50

x = cs50.get_string("Text: ")

letters = sum(1 for char in x if char.isalpha())
words = sum(1 for word in x.split() if word)
sentences = sum(1 for char in x if char in ['.', '!', '?'])

L = letters / words * 100.0
S = sentences / words * 100.0
# Coleman-Liau formula
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade", grade)

content = ''
with open('text.txt', 'r') as file:
    content = file.read()
reversed = content[::-1]

with open('text.txt', 'a') as file:
    file.writelines( content)

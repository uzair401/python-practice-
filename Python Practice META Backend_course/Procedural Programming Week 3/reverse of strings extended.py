name = 'uzair'

reverse = ""

for i,j in enumerate(name):
    reverse += j[len(name) - i -1]
print(reverse)
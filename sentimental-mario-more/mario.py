import cs50
x = 0
while x < 1 or x > 8:
    x = cs50.get_int("Height: ")
for i in range(x):
    for j in range(x - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for q in range(i + 1):
        print("#", end="")
    print()

from sys import argv
import random
import pyfiglet

figlet = pyfiglet.Figlet()

num_args = len(argv)

if num_args == 1:
    fonts = figlet.getFonts()
    font = random.choice(fonts)
elif num_args == 3:
    arg1 = argv[1]
    arg2 = argv[2]

    if arg1 in ['-f', '--font']:
        font = arg2
    else:
        print("Invalid Usage")
        sys.exit(1)
else:
    print("Invalid Usage")
    sys.exit(1)

figlet.setFont(font=font)

s = input("Input: ")

s = figlet.renderText(s)

print(s)

print("Greetings: ", end="")
s = input()
s = s.lower()
if "hello" in s:
    print("$0")
elif "h" in s[0]:
    print("$20")
else:
    print("$100")

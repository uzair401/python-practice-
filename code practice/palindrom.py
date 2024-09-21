num = 123456789987654321
string = str(num)
print(string)
print(num)
if string == string[::-1]:
    print( f"palindrom")
else:
    print (f"not a palindrom")
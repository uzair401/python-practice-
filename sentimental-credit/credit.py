import cs50
import math

product_1 = 0
product_2 = 0
total = 0

card = cs50.get_int("Number: ")
temp = card

length = 1 if card == 0 else int(math.log10(card)) + 1
templength = 0 if length > 16 else length

if 13 <= length <= 16:
    while templength > 0:
        num = ((card // 10) % 10) * 2
        if num > 9:
            p = (num // 10)
            q = (num % 10)
            num = p + q
        product_1 += num
        product_2 += (card % 10)
        card = card // 100
        templength -= 1

total = product_1 + product_2

n = temp
while n > 100:
    n //= 10

if total % 10 == 0 and 13 <= length <= 16:
    if n // 10 == 3 and (n % 10 == 4 or n % 10 == 7):
        print("AMEX")
    elif n // 10 == 4:
        print("VISA")
    elif n // 10 == 5 and 1 <= n % 10 <= 5:
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")

def add(*args):
    total = 0
    for i in args:
        total += i
    return total

def subtract(*args):
    total = 0
    for i in args:
        total -= i
    return total

def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total
def divide(*args):
    total = 1
    for i in args:
        total /= i
    return total
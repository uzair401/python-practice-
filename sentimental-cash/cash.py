import cs50


def main():
    cents = get_cents()
    cents *= 100

    quarters = calc_quarters(cents)
    cents -= quarters * 25

    dimes = calc_dimes(cents)
    cents -= dimes * 10

    nickels = calc_nickels(cents)
    cents -= nickels * 5

    pennies = calc_pennies(cents)
    cents -= pennies * 1

    coins = quarters + dimes + nickels + pennies

    print(coins)


def get_cents():
    cents = -1
    while cents < 0:
        cents = cs50.get_float("Change Owed: ")
    return cents


def calc_quarters(cents):
    quarters = 0
    while cents >= 25:
        cents -= 25
        quarters += 1
    return quarters


def calc_dimes(cents):
    dimes = 0
    while cents >= 10:
        cents -= 10
        dimes += 1
    return dimes


def calc_nickels(cents):
    nickels = 0
    while cents >= 5:
        cents -= 5
        nickels += 1
    return nickels


def calc_pennies(cents):
    pennies = 0
    while cents >= 1:
        cents -= 1
        pennies += 1
    return pennies


if __name__ == "__main__":
    main()

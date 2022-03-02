from cs50 import get_float
from math import floor


def main():
    while True:
        # Ask user for cents owed
        change = get_float("Change owed: ")
        change_owed = floor(change * 100)

        # If coins are positive int
        if change > 0:
            break

    # Store coins
    coins = 0

    while change_owed > 0:
        if change_owed >= 25:
            change_owed -= 25
            coins += 1
        elif change_owed >= 10:
            change_owed -= 10
            coins += 1
        elif change_owed >= 5:
            change_owed -= 5
            coins += 1
        elif change_owed >= 1:
            change_owed -= 1
            coins += 1

    # Print coins to give
    print(coins)


if __name__ == "__main__":
    main()

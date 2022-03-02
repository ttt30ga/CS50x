from cs50 import get_int


def main():
    while True:
        # Ask user for the height
        height = get_int("Height: ")

        # Move on if height is in between 1 and 8
        if height in range(1, 9):
            break

    # Store variables for spaces and hashes
    spaces = height
    hashes = 0

    # Loop through accepted value printing hashes and spaces
    for i in range(height):
        spaces -= 1
        hashes += 1
        print(" " * spaces, end="")
        print("#" * hashes)


if __name__ == "__main__":
    main()

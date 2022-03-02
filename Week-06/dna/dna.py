import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    strs = []
    with open(sys.argv[1], "r") as file_database:
        reader = csv.DictReader(file_database)
        # Store STRs
        strs = reader.fieldnames[1:]
        # Store database
        for items in reader:
            database.append(items)

    # TODO: Read DNA sequence file into a variable
    dna = {}
    with open(sys.argv[2], "r") as file_dna:
        # Store DNA text
        text = file_dna.read()
        dna = text

    # TODO: Find longest match of each STR in DNA sequence
    match = {}
    for i in strs:
        match[i] = str(longest_match(dna, i))

    # TODO: Check database for matching profiles
    found = False
    for i in database:
        # Make a new list with only values
        li = list(i.values())
        # Remove 'name' from the new list
        li.pop(0)
        # If both lists match print name and switch found to true
        if li == list(match.values()):
            print(i["name"])
            found = True
    if found == False:
        print("No match\n")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

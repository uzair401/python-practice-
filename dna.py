from sys import argv, exit
import csv


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    else:
        file_1 = argv[1]
        file_2 = argv[2]
        if not file_1.lower().endswith('.csv'):
            print("Invalid Input File at Location 1")
            exit(1)
        elif not file_2.lower().endswith('.txt'):
            print("Invalid Input file at location 2")
            exit(1)

    STRs = []
    names = []

    with open(argv[1], mode="r") as database:
        reader = csv.DictReader(database)
        STRs = reader.fieldnames[1:]
        for row in reader:
            names.append(row)

    str_count = dict.fromkeys(STRs, 0)

    with open(argv[2], mode="r") as sequence_file:
        sequence = sequence_file.readline()
        for STR in STRs:
            str_count[STR] = longest_match(sequence, STR)

    for name in names:
        match_count = 0
        for STR in STRs:
            if int(name[STR]) != str_count[STR]:
                continue
            match_count += 1
        if match_count == len(STRs):
            print(name['name'])
            exit(0)

    print("No match")
    exit(1)


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

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()

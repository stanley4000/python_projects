################################
# Completed for CS50 2023, week 6 problem set
# https://cs50.harvard.edu/x/2023/psets/6/dna/
# longest_match() was written by Harvard's CS dept.
##########################################


import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python database.csv FILENAME.txt")
    # Read database file into a variable
    filename = sys.argv[1]
    people = []
    STR = []
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        # note: DictReader uses header info to assign keys by default. Each new line is read as type dict. 
        # databases/large.csv has 8 sequence columns: AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
        # # print for debugging
        # print(csvreader.fieldnames)

        # save fieldnames to STR
        for fieldname in csvreader.fieldnames:
            STR.append(fieldname)
      
        # save data to list people
        for person in csvreader:
            people.append(person)
            
    # # for debugging
    # print(people)
    # #! Note: people is a list of dictionaries. Each dictionary is a person. !!Integer values are stored as "strings"!!
    
    # Read DNA sequence file into a variable
    filename = sys.argv[2]
    sequence = []
    with open(filename, 'r') as file:
        for _ in file:
            sequence.append(_)
    # # for debugging:
    # print(sequence)
    # # Note: sequence is a list containing "DNA sequence as a string".
    
    # convert list element into a single string
    sequence = sequence[0]
    # print(sequence)
    # print(people[0].items)
    # print(STR)

    # Find longest match of each STR in DNA sequence
    profile = {}
    for _ in STR[1:]:
        # Add STR and max number of repetitions to dict profile 
        profile[_] = longest_match(sequence, _)
    # # debug
    # print(profile.keys())
    # for key in profile.keys():
    #     print(key)

    # Check database for matching profiles
    match = []
    for key in profile.keys():
        for person in people:
            profile[key] = int(profile[key])
            person[key] = int(person[key])
            # print(person['name'])
            # print(f"{profile[key]} : {person[key]}")
            if profile[key] == person[key]:
                # print(person['name'])
                match.append(person['name'])
        
    # print(match)
    num_str = len(STR) - 1 #  eliminates name field for STR count
    positive_ID = ""
    # max() function from https://stackoverflow.com/questions/6987285/find-the-item-with-maximum-occurrences-in-a-list
    # max() returns name fo most frequently occuring list member.
    # print(max(match,key=match.count))
    # .count() returns number of occurences:
    # https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item

    if (match.count(max(match,key=match.count))) == num_str:
        positive_ID = max(match,key=match.count)
        print(positive_ID)
    else:
        print("No match")
            
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

import sys

min_voting_age = 18
my_age = int(sys.argv[1])

if my_age >= min_voting_age:
    print("You are eligible to vote in the general elections")
else:
    print("You are not eligible to vote in general elections")

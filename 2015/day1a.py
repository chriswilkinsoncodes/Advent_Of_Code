# https://adventofcode.com/2015/day/1

# - bring in instruction string from external file
# - initialize floor to zero
# - loop through string
# - add to floor for each "("
# - subtract from floor for each ")"
# - print the answer

# add string using import
from file1 import instructions

# set floor
floor = 0

# loop
for char in instructions:
    # add if (
    if char == "(":
        floor += 1
    # subtract if )
    else:
        floor -= 1

# output
print(floor)

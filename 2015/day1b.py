# https://adventofcode.com/2015/day/1

# - bring in instruction string from external file
# - initialize floor, counter to zero
# - loop through string
# - increment counter
# - add to floor for each "("
# - subtract from floor for each ")"
# - check for floor = -1
# - if floor == -1:
# - quit loop
# - print the answer

# - TODO: change output if floor is never -1

# add string using import
from file1 import instructions
# test
# instructions = "()())()())"

# set floor, counter
floor = 0
counter = 0

# loop
for char in instructions:
    # increment counter
    counter += 1
    # add if (
    if char == "(":
        floor += 1
    # subtract if )
    else:
        floor -= 1
    if floor == -1:
        break

# output
print(counter)

# https://adventofcode.com/2015/day/2

# - bring in measurements string from external file
# - split into list of strings based on newline escape characters
# - initialize square_feet to zero
# - loop through list
# - split strings into l, w, h based on 'x' and initialize l, w, h
# - add square feet per gift to square_feet
# - 2*l*w + 2*l*h + 2*w*h + l*w*h/max(l,w,h)
# - print square_feet

# import measurements
from file2 import measurements

# split into list of gift dimensions
gifts = measurements.split("\n")
# test
# gifts = gifts[0:5]

# initialize square_feet
square_feet = 0
feet = 0

# loop through gifts
for gift in gifts:
    # split and initialize dimensions
    l, w, h = map(int, gift.split('x'))

    # increment square_feet by surface area of gift plus extra
    square_feet += 2*l*w + 2*l*h + 2*w*h + l*w*h/max(l,w,h)

    # increment feet by min perimeter of gift plus extra for bow
    feet += 2*l + 2*h + 2*w - 2*max(l,w,h) + l*w*h

# output result
print(square_feet, feet)

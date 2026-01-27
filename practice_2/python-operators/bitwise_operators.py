# & - Sets each bit to 1 if both bits are 1
# | - Sets each bit to 1 if one of two bits is 1
# ^ - Sets each bit to 1 if only one of two bits is 1
# ~ - Inverts all the bits
# << - Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
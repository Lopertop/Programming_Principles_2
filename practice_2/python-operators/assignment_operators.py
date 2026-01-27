# x = 5
# x += 3
# x -= 3
# x *= 3
# x /= 3
# x %= 3
# x //= 3
# x **= 3
# x &= 3
# x |= 3
# x ^= 3
# x >>= 3
# x <<= 3
# print(x := 3)

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
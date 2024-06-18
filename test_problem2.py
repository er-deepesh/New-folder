# Test case 1: a is divisible by b
assert calculate_remainder(10, 5) == 0

# Test case 2: a is not divisible by b
assert calculate_remainder(10, 3) == 1

# Test case 3: a is zero
assert calculate_remainder(0, 5) == 0

# Test case 4: b is zero (should raise ZeroDivisionError)
try:
    calculate_remainder(10, 0)
except ZeroDivisionError:
    pass
else:
    raise AssertionError("ZeroDivisionError not raised")

# Test case 5: negative values of a and b
assert calculate_remainder(-10, -3) == -1
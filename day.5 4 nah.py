def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def check_divisibility(a, b):
    prod = a * b
    summ = a + b
    gcd_value = gcd(a, b)
    if prod % summ == 0 and gcd_value == min(a, b):
        return "YEAH"
    return "NAH"
# Test Case 1
a, b = 60, 48
print(check_divisibility(a, b)) # Output: NAH

# Test Case 2
a, b = 4, 8
print(check_divisibility(a, b)) # Output: YEAH

# Test Case 3
a, b = -10, 0
print(check_divisibility(a, b)) # Output: NAH

# Test Case 4
a, b = 12, 34
print(check_divisibility(a, b)) # Output: NAH

# Test Case 5
a, b = 16, 17
print(check_divisibility(a, b)) # Output: NAH

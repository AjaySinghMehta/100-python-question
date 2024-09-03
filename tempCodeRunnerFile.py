from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_multiple(*args):
    result = args[0]
    for num in args[1:]:
        result = lcm(result, num)
    return result

# Input numbers
li = list(map(int, input('Enter the numbers separated by spaces: ').split()))

# Calculate LCM of the list
lcm_value = lcm_multiple(*li)

print(f"LCM of given numbers {li} is {lcm_value}")
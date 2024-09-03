'''
find lowest commom multiple of given numbers 
'''
from math import sqrt

li = list(map(int, input('enter the numbers : ').split()))
maximum_num = max(li)
lcm = 0


while(lcm==0):
    if(all(maximum_num%i==0 for i in li)):
        lcm = maximum_num
        

    else:
        maximum_num+=1
print(f"lcm of given numbers {li} is {lcm}")
# 2 4 9 12

# from math import gcd

# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)

# def lcm_multiple(*args):
#     result = args[0]
#     for num in args[1:]:
#         result = lcm(result, num)
#     return result

# # Input numbers
# li = list(map(int, input('Enter the numbers separated by spaces: ').split()))

# # Calculate LCM of the list
# lcm_value = lcm_multiple(*li)

# print(f"LCM of given numbers {li} is {lcm_value}")

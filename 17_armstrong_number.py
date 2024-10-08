'''armstrong number is a number whose sum of the power of its digits raised to the number of digits equals the number itself
example : 153 = 1^3 + 5^3 + 3^3 = 1+125+27 = 153
1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1634 itself
import numpy as np'''

# method 1 : 

num = int(input('enter the number : '))

def is_armstrong(num):
    ls = []
    sum = 0
    
    while(num>0):
        ls.append(num%10)
        num = num//10
    for i in ls:
        sum += i**len(ls)
    return sum
        
# print(bool(num == is_armstrong(num)))
        
# method 2 :
def is_armstrong2(num):
    digits = [int(digit) for digit in str(num)]
    return num == sum(digit ** len(digits) for digit in digits)

print(is_armstrong2(num))
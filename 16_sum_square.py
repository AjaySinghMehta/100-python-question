# getting 3 numbers as input and then printing the sum of the squares of each number
# there are two ways to do this 
# method 1 : using pow function
from math import pow
def power(num, p):
    return (pow(num,p))

num1 = int(input('enter the first number : '))
num2 = int(input('enter the second number : '))
num3 = int(input('enter the third number : '))
p = int(input('enter the power you wish to raise the number to : '))

# sum = int(power(num1,p) + power(num2,p) + power(num3,p))

print(f'The sum of digits to the power {p} is : {sum}')

# method 2: using num ** power method
print(num1**p + num2**p + num3**p)

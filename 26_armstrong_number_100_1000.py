'''
printing all the armstrong numbers between 100 and 1000
armstrong number is a number whose sum of the power of its digits raised to the number of digits equals the number itself
example : 153 = 1^3 + 5^3 + 3^3 = 1+125+27 = 153
1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1634 itself
'''
print('the armstrong number between 100 and 1000 are : ')
for i in range(100, 1000):
    digits = [int(digits) for digits in str(i)]
    if(i == sum(digit**len(digits) for digit in digits)):
        print(f'{i}', end=(" "))

        
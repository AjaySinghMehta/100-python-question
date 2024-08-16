# Sum of three digit means the sum of a number which consists of 3 digits and the sum of those digits

def digit_sum(num):
    if num == 0:
        return 0
    sum = 0
    while num > 0:
        sum += num%10
        num = num//10
    return sum
        
    
num = int(input('enter the number: '))

result = digit_sum(num)
print(result)
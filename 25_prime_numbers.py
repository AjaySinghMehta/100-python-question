'''
in this we gotta find whether the given number is prime number or not
prime numbers: the numbers which are divisible by 1 and the number themselves
example : 3, 5, 7, 13, 17, 19, 23, 29, 31, 37....
'''
num = int(input("enter the number : "))
count = 0
for i in range(1, num//2):
    if(num%i==0):
        count += 1
    else:
        continue
if (count<2):
    print(f'the entered number {num} is prime')
else:
    print(f'the entered number {num} is not prime')

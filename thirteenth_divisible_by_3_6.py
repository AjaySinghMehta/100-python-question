# divisible by 3 means num % 3 should be = 0 same for 6

num = int(input('enter the number : '))

if num%6==0 and num%3 == 0:
    print(f'{num} is divisible by both 3 and 6.')
else:
    print(f'{num} is not divisible by both 3 and 6 ')

# whether the entered number is odd or even

def sol(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

num = int(input('enter the number : '))

result = sol(num)

if result:
    print(f'the entered number {num} is even')
else:
    print(f'the entered number {num} is odd')
    

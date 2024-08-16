# reversing a number is writing a number in reverse 423 -> 324

#method 1: using strings

def reverse1(digit):
    digit = str(digit)
    digit = digit[::-1]
    digit = int(digit)
    return digit

# method 2 : 

def reverse2(digit):
    reverse = 0
    while digit != 0:
        reverse = reverse*10 + digit%10
        digit = digit//10
    
    return reverse


digit = int(input('enter the number : '))

result = reverse2(digit)

print(f'the reverse of {digit} is {result}', '\n', bool(result))
        
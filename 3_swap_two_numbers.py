# method 1 : using a third variable
def swap1(a,b):
    print(f'Before swaping the first and second variables are a = {a}, b = {b}')
    temp = a
    a = b
    b = temp
    return a,b

# method 2 : without using third variable
def swap2(a,b):
   print(f'Before swaping the first and second variables are a = {a}, b = {b}')
   a = a+b
   b = a-b
   a = a-b
   return a,b

# method 3 : using XOR operator (^) in python
def swap3(a,b):
   print(f'Before swaping the first and second variables are a = {a}, b = {b}')
   a = a^b
   b = a^b
   a = a^b
   return a,b

a = int(input('enter the first value: '))
b = int(input('enter the second value: '))

a,b = swap3(a,b)
print(f'after swaping the first and second variables are a = {a}, b = {b}')
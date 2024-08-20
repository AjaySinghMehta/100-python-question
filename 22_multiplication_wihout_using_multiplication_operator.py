# mulitplying without using * operator 
# ex = 10, 2 we will add 10 , two times easy right:

a = int(input('enter number 1 : '))
b = int(input('enter number 2 : '))

def multiplication(a,b):
    result = 0
    while (b>0):
       result += a
       b = b - 1
    return result

product = multiplication(a,b)
print(f'the product of two numbers {a} and {b} is {product}')


# factorial of 5 is 5*4*3*2*1 = 120 and  note : factorial of 0 is 1


# mehtod 1 : using for loop 
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
        
# method 2 : using recursion
def factorial2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n*factorial(n-1)



n = int(input('enter the number you wish to find the factorial of : '))
fact = factorial(n)
fact2 = factorial2(n)
print(f'factorial using mehtod 1 of {n} is {fact}, and using method 2 is {fact2}')
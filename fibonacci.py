def fib(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return fib(i-1)+fib(i-2)

limit = int(input('enter the series number : '))
print(fib(limit))
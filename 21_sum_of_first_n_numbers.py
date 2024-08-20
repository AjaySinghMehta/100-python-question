# finding sum of first n numbers : 
n = int(input('enter the limit till which you want the sum of : '))

#mehtod 1 using loops in python
def sum1(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(sum)
    
# method 2 : using mathematical formula i.e. sn = n(n+1)/2
def sum2(n):
    sum = (n*(n+1))/2
    print(int(sum))

print('the sum using method 1 i.e. loop is : ')
sum1(n)
print('the sum using method 2 i.e. formula is : ')
sum2(n)

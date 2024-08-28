'''
getting the limit as an input and printing the odd numbers till that limit 
'''
#method 1 using loop and range

n = int(input('enter the limit till which you wish to print the odd numbers : '))

print("using the first method the output is : ")

if (n%2==0):               # if the limit entered is even then the odd number just before it will be the limit
    for i in range(1,n+1,2):
        print(i,end = ' ')
else:
    for i in range(1,n+2,2): # when the limit is odd printing till the limit
        print(i,end = " ")
print("\n")

#method 2 will be using if under the loop this is more complicated but good for concept building

print("using the second method the output is : ")

if(n%2==0):       # for even limit 
    for i in range(n+1):
        if(i%2!=0):
            print(i, end = " ")
        else:
            continue
else:
    for i in range(n+2):
        if(i%2!=0):
            print(i, end = " ")
        else:
            continue
    
    
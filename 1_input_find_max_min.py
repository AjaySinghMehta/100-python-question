# using 3 different variables:
# a = int(input('enter first value: '))
# b = int(input('enter second value: '))
# c = int(input('enter third value: '))

# def max(a,b,c):
#     if(a==b and b==c):
#         print(f'all the numbers are equal: {a}')
#     elif(a>b and a>c):
#         print(f'the max number is: {a}')
#         if b<c:
#             print(f'the min number is: {b}')
#         else:
#             print(f'the min number is: {c}')
#     elif(b>a and b>c):
#         print(f'the max number is: {b}')
#         if a<c:
#             print(f'the min number is: {a}')
#         else:
#             print(f'the min number is: {c}')
#     else:
#         print(f'the max number is: {c}')
#         if b<a:
#             print(f'the min number is: {b}')
#         else:
#             print(f'the min number is: {a}')
    
    
# max(a,b,c)

#using list
ls = []
size = int(input('enter the number of elements: '))
for i in range(size):
    element = int(input(f'enter the {i+1} number: '))
    ls.append(element)
print('\nthe maximun number is: ', max(ls))
print('the min number is: ', min(ls))


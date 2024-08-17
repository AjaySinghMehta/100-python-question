# # comparing 4 numbers and finding out the maximum and minimum

# # method 1 : using list 

# # ls = []
# # for i in range(4):
# #     element = int(input(f'enter the {i+1} element: '))
# #     ls.append(element)

# # print(f'the maximum number is {max(ls)}, and the minimum number is {min(ls)}')

# # using if else : we arent using elif here finding maximum

num1 = int(input('enter the first number : '))
num2 = int(input('enter the second number : '))
num3 = int(input('enter the third number : '))
num4 = int(input('enter the fourth number : '))


# if(num1 > num2):
#     if(num1>num3):
#         if(num1>num4):
#             print(f'the maximum number is {num1}')
#         else:
#             print(f'the maximum number is {num4}')
#     else:
#         if(num3>num4):
#             print(f'the maximum number is {num3}')
#         else:
#             print(f'the maximum number is {num4}')       
# else:           
#     if(num2>num3):
#         if(num2>num4):
#             print(f'the maximum number is {num2}')
#         else:
#             print(f'the maximum number is {num4}')
#     else:
#         if(num3>num4):
#             print(f'the maximum number is {num3}')
#         else:
#             print(f'the maximum number is {num4}')

# method 3 : using maximum and minimum variable 

maximum = num1
minimum = num1
# if(num2>maximum)
#     maximum = num2
# else:
#     minimum = num2

# if(num3>maximum):
#     maximum = num3
# else:
#     if(num3<minimum):
#         minimum = num3

# if(num4>maximum):
#     maximum = num4
# else:
#     if(num4<minimum):
#         minimum = num4

#using multiple conditions in one for maximum
if(num1>num2 and num1>num3 and num1>num4):
    maximum = num1
if(num2>num1 and num2>num3 and num2>num4):
    maximum = num2
if(num3>num1 and num3>num2 and num3>num4):
    maximum = num3
if(num4>num1 and num4>num2 and num4>num1):
    maximum = num4

print(f'the maximum number is {maximum}')
# print(f'the minimum number is {minimum}')

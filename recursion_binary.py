# def bin(n):
#     if(n==0):
#         return
#     bin(n//2)
#     print(n%2)

# bin(13)
# import math
# def fun(n):
    
#     if (n == 0):
#         return 0
#     else:
#         return 1 + fun(n // 2)
# print(fun(8))
def fun(n):
    if(n==0):
        return 0 
    else:
        return (1 + fun(n//2))
print(fun(8))
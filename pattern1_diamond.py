'''
   0 1 2
0    *   
1  *   *
2    *    
       *    
      * *
     * * *
      * *
       *
 i = 0  j == 3//2 = 1 => Print('*')
 i = 1 j = 0 and 2   => print('*')
 i = 2 j = 3//2 =1 => print('*') 
double loops 
1 row will have 1 star
2nd row will have 2 star                    
3rd row will again have 1 star
'''
n = 5  # This controls the number of rows for the upper half
'''
n = 5
i = 0
n-i-1 = 4
'''
# Top half of the diamond
for i in range(n):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    
    # Print stars
    print('$' * (2 * i + 1))


# Bottom half of the diamond
for i in range(n - 2, -1, -1):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    
    # Print stars
    print('$' * (2 * i + 1))

    
    
# '''
# data types
# 1 - integer 1 2 3 4
# 2 - float  1.0, 2.2, 3.5,
# 3 - string
# 4 - boolean
    
# 4/2 = 2.0 
    
# '''
# print(4%3)

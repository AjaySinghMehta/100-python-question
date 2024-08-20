''' 
in this question we will be given count of heads and number of legs and we need to
find the number of dogs and chicken there could be using that information
suppose : 5 heads are given and number of legs = 20
then there can be only 4 dogs as if any amount of chicken added will abrupt the calculations
(5 heads , 20 lesgs => lets say 1 dog and 4 chicken = 4 * 1 + 2 * 3 = 10 which is less than the given number of legs)
'''
def solution(h,l):
    if(h==0 or l==0):
        return 0,0
    else:
        for i in range(0,h+1):
            dogs, chicken = i , h-i  
            if(dogs*4 + chicken*2 == l):
                return chicken, dogs    
    return -1, -1

headCount = int(input('enter the number of heads : '))
legsCount = int(input('enter the number of legs should be always even : '))
chicken , dog = solution(headCount, legsCount)
print(f'the number of chickens is {chicken} and the number of dogs is {dog}')

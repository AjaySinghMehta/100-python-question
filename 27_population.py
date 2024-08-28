'''
here we are printing the last 10 years population from the given current population of 
town and the percent increment every year
ex:
The current population of a town is 10000. The population of the town is increasing 
at the rate of 10% per year. so we will print 9 - > 9000, 8->8100, 7-> 7290 .... till first year

'''
from math import floor

def population(curr, rate):
    last = curr
    for i in range(1,10):
        last = (last*90)/100
        print(f'The population at the end of year {10-i} is {floor(last)}')
        

li = list(map(int, input('enter the current population and percent increment per year : ').split()))
print(f'the current population is {li[0]}')
population(li[0],li[1])
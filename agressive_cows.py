'''
You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
'''


def fun(mid, stalls, k):
    n = len(stalls)
    count = 1
    target = stalls[0]+mid
    i = 1
    while(i<n):
        if(stalls[i]>=target):
            count+=1
            target = stalls[i]+mid
        i+=1
    return count>=k
        
    
def aggressiveCows(stalls, k):
    stalls.sort()
    l = 0
    r = stalls[-1]-stalls[0]
    n = len(stalls)
    ans = 1
    while(l<=r):
        mid = (l+r)//2
        if(fun(mid, stalls, k)):
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans

stalls = [1,2,4,8,9]
k = 3

print(aggressiveCows(stalls, k))
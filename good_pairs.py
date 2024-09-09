'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
'''
# method 1: using double loops : time complexity (O(n^2))
def goodPair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]==nums[j]):
                count+=1
    return count

nums = list(map(int, input().split()))
print("first method : ",goodPair(nums))
    


# method 2: using maps as in : less time complexity (O(m+n))

def goodPair2(nums):
    m = [0]*101
    count = 0
    for i in nums:
        m[i] += 1
    for i in m:
        if(i>1):
            count+= (i*(i-1))//2
            
    return count




print('second method using map : ',goodPair2(nums))
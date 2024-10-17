'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''
def subarraySum(nums, k):
    res = 0
    prefix = []
    di = {0:1}
    n = len(nums)
    for i in range(n):
        if(i==0):
            prefix.append(nums[i])
        else:
            prefix.append(nums[i]+prefix[i-1])
        if(prefix[i]-k in di):
            res += di[prefix[i]-k]
        if(prefix[i] in di):
            di[prefix[i]] += 1
        else:
            di[prefix[i]] = 1
    return res

k = int(input('enter the sum : '))
array = list(map(int,input('enter array element : ').split()))
print(subarraySum(array,k))
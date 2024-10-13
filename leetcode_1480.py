'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

nums = list(map(int, input('enter element ').split()))
def runningSum(nums: list[int]) -> list[int]:
        sum = 0
        result = []
        for i in range(len(nums)):
            sum = sum+nums[i]
            result.append(sum)
        return result
print(runningSum(nums))
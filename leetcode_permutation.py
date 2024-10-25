'''
given an array of number print all the possible permutations of the numbers

ex 1:
arr = [1,2]
output = [[1,2], [2,1]]
'''
class Solution:
    def permutation(nums):
        n = len(nums)
        ans = []
        def backtrack(index):
            if(index == n):
                ans.append(nums[:])
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        backtrack(0)
        return ans

nums = list(map(int,input('enter array element : ').split()))

res = Solution.permutation(nums)
print(res)
print()
print(len(res))
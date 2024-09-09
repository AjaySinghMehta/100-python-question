# we are given an array i.e. list in python we just need to concatinate it simply return the array two times
#https://leetcode.com/problems/concatenation-of-array/description/

# we can simply concat and return 

def concat(nums):
    ans = nums+nums
    return ans

nums = list(input().split())
print('first method : ',concat(nums))

# but in this method the catch is the list should be string 

#second method is more like we do in c++ defining ans with a fix size and using loops
def concat2(nums):
    n = len(nums)
    ans = [0]*n*2
    for i in range(n):
        ans[i] = nums[i]
        ans[n+i] = nums[i]
            
    return ans

print('second method : ',concat2(nums))

# method 3 : we can do 2 for loops as we need to append it 2 times only
def concat3(nums):
    ans = []
    for i in range(2):
        for ele in nums:
            ans.append(ele)
    return ans

print('third method : ', concat3(nums))
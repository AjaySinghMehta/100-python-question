nums = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,7,7,8,9,10]
n = len(nums)
l = 0
r = n-1
flag = 0
target = 5
while(l<r):
    mid = (l+r)//2
    if(nums[mid]>=target):
        r = mid
    else:
        l = mid+1
    if(l == r and nums[r]< target):
        flag = 1
        print("not present")
if(flag == 0):
    print(l)
        
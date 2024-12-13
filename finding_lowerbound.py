nums = [5,7,7,8,8,10]
n = len(nums)
l = 0
r = n-1
flag = 0
target = 8
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
        

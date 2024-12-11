nums = [1,1,2,2,3,4,5,6,6,6,7,7,8]
target = 6
n = len(nums)
l = 0
r = n-1
flag = 0 
while(l<r):
    mid = (l+r)//2
    if(nums[mid]>target):
        r = mid
    else:
        l = mid+1
    if(l == r and target >= nums[l]):
        flag = 1
        print("not possible")
if(flag == 0):
    print(l)
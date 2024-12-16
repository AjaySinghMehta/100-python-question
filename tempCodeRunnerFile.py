n = 4
m = 7
height = [20, 15, 10, 17]
def maxpossibleheight(n,m,height):
    l = 0
    r = max(height)
    ans = 0
    while(l<=r):
        mid = (l+r)//2
        current_wood = 0
        for i in range(n):
            if(height[i]>mid):
                current_wood += height[i]-mid
        if(current_wood >= m):
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans

print(maxpossibleheight(n,m,height))
'''
print all subarray

1 
1 2
1 2 3
1 2 3 4 5


'''
# arr = list(map(int, input().split()))
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(arr[k],end="")
        print()


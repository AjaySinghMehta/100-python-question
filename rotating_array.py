'''
we have to rotate a list of size n k times from right to left i.e.
1,2,3,4,5 rotating 1 times results in 5,1,2,3,4
1 2 3 4 5 rotated 2 times results in 4 5 1 2 3
'''
li = list(map(int,input('enter the list : ').split()))
print(li)
k = int(input('enter the rotations : '))
while(k>0):
    temp = li[len(li)-1]
    for i in range(len(li)-1,-1,-1):
        li[i]= li[i-1]
    li[0]=temp
    k -= 1   # => k = k-1
print(li)
    


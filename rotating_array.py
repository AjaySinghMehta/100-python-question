'''
we have to rotate a list of size n k times from right to left i.e.
1,2,3,4,5 rotating 1 times results in 5,1,2,3,4
1 2 3 4 5 rotated 2 times results in 4 5 1 2 3
'''
li = list(map(int,input('enter the list : ').split()))
li2 = li
print(li)
k = int(input('enter the rotations : '))
while(k>0):
    temp = li[len(li)-1]
    for i in range(len(li)-1,-1,-1):
        li[i]= li[i-1]
    li[0]=temp
    k -= 1   # => k = k-1
print(li)

# for the above code the time complexity is o(n^2) now we will try to reduce it

n = len(li2)
temp = []
for i in range(n-k,n):
    temp.append(li2[i])
for i in range(n-k):
    temp.append(li2[i])
print(temp)
    
# but in this code we are increasing the space complexity to O(n) now we will try to reduce it

li2.reverse()
for i in range(k//2):
    li2[i], li2[k-i-1] = li2[k-1-i], li2[i]
for j in range(k,(k+n)//2):
    li2[j], li2[n-(abs(j-k))-1] = li2[n-(abs(j-k))-1], li2[j]
    
print(li2)

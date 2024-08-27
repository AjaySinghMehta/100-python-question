# using map function
# li = list(map(int,input('enter the values in list : ').split()))
li = list(input('enter the values in list : ').split())
j = 0
for i in li:
    li[j] = int(i)
    j+=1
print(li,type(li))
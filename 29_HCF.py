# printing the highest comman factor given multiple numbers we need to find their hcf


li = list(map(int, input("enter the numbers : ").split()))
minimum_num = min(li)
hcf = 1

# method 1:
for i in range(1,minimum_num+1):
    if(all(num%i == 0 for num in li)):
        hcf = i
print(f'hcf using method 1 is : {hcf}')   
# method 2 : 
hcf2 = 0
for i in range(1,minimum_num+1):
    count = 0
    for j in li:
        if(j%i==0):
            count += 1
    if(count == len(li)):
        hcf2 = i
print(f'hcf using method 2 is : {hcf2}')

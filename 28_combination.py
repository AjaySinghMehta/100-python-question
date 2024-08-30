'''
program to print all the unique combinations of 1,2,3 and 4
'''
# method 1 : using combinations function from itertools module which creates all the combinations
from itertools import combinations

li1 = list(map(int, input("Enter 4 digits: ").split()))
li2 = []

# for r in range(1, len(li1) + 1):
#     for combo in combinations(li1, r):
#         if combo not in li2:
#             li2.append(combo)

# print(f' using first method combinations are : {li2}')

# method 2 basic and brute force method

# one element combinations
for i in li1:
    if([i] not in li2):
       li2.append([i]) 
       
# two element combinations
for i in li1:
    for j in li1:
        if(i!=j and sorted([i,j]) not in li2):
            li2.append([i,j])
        
# three element combinations
for i in li1:
    for j in li1:
        for k in li1:
            if(i!=j and j!=k and i!=k and sorted([i,j,k]) not in li2):
                li2.append([i,j,k])

# four element combinations
# we can do this in a similar manner but here we know that there are only four elements and there can only be 4
# one combination so we just append it
li2.append(li1)
print(f'using second method combinations are : {li2}')

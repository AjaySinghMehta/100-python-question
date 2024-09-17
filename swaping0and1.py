'''
we have to put all the 1s in the right and all the 0s in left\
ex = given arr = [0,1,0,1,0,1,0] should give result like
result = [0,0,0,0,1,1,1]
'''

# method 1: 

# list = list(map(int,input().split()))
# i = 0 
# n = len(list)


# while(i<n):
#     if(list[i]==0):
#         i+=1
#     elif(list[i]==1):
#         j = i+1
#         while(j<n and list[j]!=0):
#             j+=1
#         if(j<n):
#             list[j], list[i] = list[i], list[j]
#         i = i + 1
# print(list)
        
        
# method 2:
# start = 0
# end = 1
# while(end<n):
#     if(list[start]==0 and list[end]==1):
#         start+=1
#         end+=1
#     elif(list[start]==1 and list[end]==0):
#         list[start], list[end] = list[end], list[start]
#         start += 1
#         end += 1
#     elif(list[start]==0 and list[end]==0):
#         start+=1
#         end+=1
#     else:
#         end+=1

# print(list)


# method 3:

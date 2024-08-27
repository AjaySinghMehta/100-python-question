'''
Given a sorted array 
a
r
r
arr, remove the duplicates from 
a
r
r
arr such that each element appears only once and display the new array.

###Input:

The first line contains 
T
T, the number of test cases. Then the 
T
T test cases follow.
Each test case contains 
2
2 lines of input:
The first line contains 
n
n, the size of array 
a
r
r
arr.
The second line contains 
n
n space separated elements of array 
a
r
r
arr.
###Output: For each test case, output in a single line, the new array. The elements of the array should be separated by space. Your output format should match with that given in the sample output.

###Constraints

1
≤
T
≤
1000
1≤T≤1000
1
≤
n
≤
1
0
4
1≤n≤10 
4
 
−
1
0
5
≤
a
r
r
[
i
]
≤
1
0
5
−10 
5
 ≤arr[i]≤10 
5
'''

t = int(input())
for i in range(t):
    #method 1 using set
    n = int(input())
    li = list(map(int,input().split()))
    # new_li = list(set(li))
    # new_li = sorted(new_li)
    # print(new_li)
    
    #method 2 : normal method using for loop: using not in
    
    new_li = []
    # for i in li:
    #     if(i not in new_li):
    #         new_li.append(i)
    #     else:
    #         continue
    # for i in new_li:
    #     print(i,end=" ")
    
    # method 3: without using not in
    
    for i in li:
        if i in new_li:
            continue
        else:
            new_li.append(i)
    for i in new_li:
        print(i,end=' ')
    print()
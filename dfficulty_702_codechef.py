'''
Chef and his Apps
Chef's phone has a total storage of 
S
S MB. Also, Chef has 
2
2 apps already installed on his phone which occupy 
X
X MB and 
Y
Y MB respectively.

He wants to install another app on his phone whose memory requirement is 
Z
Z MB. For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

Input Format
The first line contains a single integer 
T
T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains four integers 
S
,
X
,
Y
S,X,Y and 
Z
Z — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.
Output Format
For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
S
≤
500
1≤S≤500
1
≤
X
≤
Y
≤
S
1≤X≤Y≤S
X
+
Y
≤
S
X+Y≤S
Z
≤
S
Z≤S
'''

n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    total_space = li[0]
    occupied_space = li[1] + li[2]
    free_space = total_space - occupied_space

    if(li[3]<=free_space):
        print(0)
    elif((li[3]>=free_space) and (li[3]<=free_space+li[1] or li[3]<=free_space+li[2])):
        print(1)
    elif(li[3]<=free_space+li[1]+li[2]):
        print(2)
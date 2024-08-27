'''
B - One Clue  / 
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 
200 points

Problem Statement
There are 
2000001 stones placed on a number line. The coordinates of these stones are 
−1000000,−999999,−999998,…,999999,1000000.

Among them, some 
K consecutive stones are painted black, and the others are painted white.

Additionally, we know that the stone at coordinate 
X is painted black.

Print all coordinates that potentially contain a stone painted black, in ascending order.

Constraints
1≤K≤100
0≤X≤100
All values in input are integers.
'''

t = int(input())
for i in range(t):
    # l = int(input("enter the length of black : "))
    # c = int(input('enter the given coordinate'))
    li = list(map(int, input('enter the length and co-ordinate : ').split()))
    # for i in range(c-l+1,c+l):
    #     print(i, end=" ")
    i = li[1]-li[0]+1
    while(i!=li[1]):
        print(i,end=" ")
        i+=1
    print(li[1],end=" ")
    i = li[1]+1
    while(i<li[1]+li[0]):
        print(i,end = " ")
        
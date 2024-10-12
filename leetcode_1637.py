'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
'''

length = int(input('enter length '))
points = []
for i in range(length):
    temp = list(map(int, input('enter co-ordinates').split()))
    points.append(temp)

# Method 1 :

def maxWidthOfVerticalArea(points):
        horizontal = []
        for i in range(len(points)):
            horizontal.append(points[i][0])
        horizontal = sorted(horizontal)
        print(horizontal)
        maximum = float("-inf")
        i = 0 
        while(i<len(horizontal)-1):
            maximum = max(maximum, abs(horizontal[i]-horizontal[i+1]))
            i += 1
        return maximum

print(maxWidthOfVerticalArea(points))

'''
n a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
'''

# Method 1 : using backtracking


class Solution:
    ans = 0
    def getMaximumGold(self, grid):
        def maxGold(row,col,n,m,gold,grid):
            if(row<0 or col<0 or row>=n or col>=m):
                return False
            if(grid[row][col]==0):
                return False
            gold += grid[row][col]
            Solution.ans = max(Solution.ans,gold)
            temp = grid[row][col]
            grid[row][col]=0
            maxGold(row+1,col,n,m,gold,grid)
            maxGold(row-1,col,n,m,gold,grid)
            maxGold(row,col-1,n,m,gold,grid)
            maxGold(row,col+1,n,m,gold,grid)
            grid[row][col] = temp
            gold -= temp
            return gold
        n = len(grid)
        m = len(grid[0])
        Solution.ans = 0
        for i in range(n):
            for j in range(m):
                gold = maxGold(i,j,n,m,0,grid)
        res = Solution.ans
        return res
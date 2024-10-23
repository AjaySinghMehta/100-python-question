'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''
class Solution:
    def solveNQueens(self, n: int):
        board = [['.']*n for i in range(n)]
        res = []
        v_row = set()
        v_col = set()
        v_primary_diagonal = set()
        v_secondary_diagonal = set()
        def backtrack(row):
            if(row == n):
                res.append(["".join(row) for row in board])
            for col in range(n):
                if(col not in v_col and row not in v_row and (row-col) not in v_primary_diagonal and (row+col) not in v_secondary_diagonal):
                    board[row][col] = 'Q'
                    v_row.add(row)
                    v_col.add(col)
                    v_primary_diagonal.add((row-col))
                    v_secondary_diagonal.add((row+col))
                    backtrack(row+1)
                    v_secondary_diagonal.remove((row+col))
                    v_primary_diagonal.remove((row-col))
                    v_col.remove(col)
                    v_row.remove(row)           
                    board[row][col] = '.'
        backtrack(0)
        return res
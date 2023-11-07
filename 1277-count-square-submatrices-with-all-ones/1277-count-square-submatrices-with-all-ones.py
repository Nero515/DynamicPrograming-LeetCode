class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        mem = matrix
        
        for i in range(1, rowLen):
            for j in range(1, colLen):
                if matrix[i][j] == 1:
                    mem[i][j] += min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
        count = sum([sum(mem_col) for mem_col in mem])
        return count
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for curr in rows:
            matrix[curr] = [0 for i in range(len(matrix[curr]))]
        
        for curc in cols:
            for i in range(len(matrix)):
                matrix[i][curc] = 0
                
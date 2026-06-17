class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0,1), (1, 0), (0,-1), (-1, 0)]
        maxval = n*n 
        c = 1
        row = 0
        col=0
        d = 0
        while c<=maxval:
            res[row][col] = c
            dr, dc = directions[d]
            nr, nc = row+dr,col+dc 
            if nr<0 or nr>=n or nc<0 or nc>=n or res[nr][nc] !=0:
                d+=1
                if d>=4:
                    d=0
            dr, dc = directions[d]
            row, col = row+dr,col+dc  
            c+=1
        return res
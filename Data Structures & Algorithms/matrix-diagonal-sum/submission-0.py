class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x=0
        y = 0
        res = 0
        while y<len(mat) and x<len(mat[y]):
            res+=mat[x][y]
            x+=1
            y+=1
        
        y=len(mat)-1
        x=0
        while y>=0 and x<len(mat[y]):
            if x!=y:
                res+=mat[x][y]
            y-=1
            x+=1
        return res
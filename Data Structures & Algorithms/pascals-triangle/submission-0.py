class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1], [1, 1]]
        
        dp = [[1], [1, 1]]
        def get_further():
            
            if len(dp)==numRows:
                return
            
            currow = [1 for _ in range(len(dp[-1])+1) ]

            for i in range(1, len(currow)-1):
                currow[i] = dp[-1][i-1] + dp[-1][i]
            
            dp.append(currow)
            get_further()
        
        get_further()
        return dp


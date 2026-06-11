class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0]]
        
        for i in range(1, len(triangle)):
            temp = [triangle[i][0]+dp[-1][0]]
            for j in range(1, len(triangle[i])-1): 
                cur = min(dp[-1][j-1], dp[-1][j])
                temp.append(cur+triangle[i][j])
            temp.append(triangle[i][len(triangle[i])-1]+dp[i-1][-1])
            
            dp.append(temp)
        
        return min(dp[-1])

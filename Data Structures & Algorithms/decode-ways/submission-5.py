class Solution:
    def numDecodings(self, s: str) -> int:
       
        dp = {len(s):1}
        total = len(s)-1
       
        for i in range(total, -1, -1):
            if s[i]=='0':
                dp[i]=0
            else:
                dp[i] = dp[i+1]
            
            if i+1<len(s) and s[i]!="0" and int(s[i]+s[i+1])<=26:
                #print(int(s[i]+s[i+1]), dp)
                dp[i]+=dp[i+2]

        return dp[0]

        
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)
            if i<len(s)-1:
                if int(s[i]+s[i+1])<=26:
                    res+=dfs(i+2)
            return res
        return dfs(0)
            

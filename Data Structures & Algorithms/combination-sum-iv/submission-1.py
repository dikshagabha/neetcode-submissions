class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        dp = {}
        def dfs(t):
            if t>target:
                return 0
            if t==target:
                return 1
            res = 0
            for i in nums:
                if i+t in dp:
                    res+=dp[i+t]
                else:
                    v = dfs(i+t)
                    res += v
                    dp[i+t] = v
            return res
        return dfs(0)
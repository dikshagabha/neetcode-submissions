class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        def getdp(nums1):
            n = len(nums1)
            dp=[0]*n
            dp[0] = nums1[0]
            dp[1] = max(nums1[1], nums1[0])
            for i in range(2, n):            
                dp[i] = max(dp[i-1], nums1[i]+dp[i-2])
            return dp[-1]
        
        return max(getdp(nums[1:]), getdp(nums[:-1]))



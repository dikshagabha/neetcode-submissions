class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return max(nums)

        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1]=nums[1]
        for i in range(2, len(nums)):

            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        print(dp)
        # prev= 0
        # res = 0
        # i=1
        # while i<len(nums):
        #     if nums[i] > nums[i-1]:
        #         prev = i
        #         res+=nums[i]
        #     else:
        #         prev = i-1
        #         res+=nums[i]
        #     i=pev+2

        # return max(dp[-1], dp[-2])

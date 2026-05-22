class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l=0
        res = 0
        while l<len(nums):
            r=l+1
            cursum = nums[l]
            while r<len(nums) and nums[r]>nums[r-1]:
                cursum+=nums[r]
                r+=1
            res = max(res, cursum)
            l=r
        return res
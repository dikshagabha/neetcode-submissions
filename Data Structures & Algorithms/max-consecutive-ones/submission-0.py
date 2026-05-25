class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,res=0, 0
        while l<len(nums):
            if nums[l]!=1:
                l+=1
                continue
            r = l
            while r<len(nums) and nums[r]==1:
                r+=1
            res = max(res, r-l)
            l=r
        return res
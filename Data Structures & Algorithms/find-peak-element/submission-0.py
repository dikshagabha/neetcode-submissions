class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        f =  max(nums)
        for key, i in enumerate(nums):
            if i==f:
                return key
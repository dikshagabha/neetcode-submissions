class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            if i-1 not in nums:
                l=1
                while i+l in nums:
                    l+=1
                res=max(res, l)
        return res
                
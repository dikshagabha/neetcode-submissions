class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        i=0
        for start in nums:
            l = 0
            while start+l in nums:
                l+=1
            
            res=max(res, l)
            i+=1
        
        
            
        return res
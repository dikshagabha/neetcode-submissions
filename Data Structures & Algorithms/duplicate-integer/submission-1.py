class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i in nums:
            s[i] = s.get(i, 0)+1
            if s[i]>1:
                return True
        
        return False
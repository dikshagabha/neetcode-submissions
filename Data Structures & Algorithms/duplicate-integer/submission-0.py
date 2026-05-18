class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in nums:
            hmap[i] = hmap.get(i, 0)+1
            if hmap[i]>1:
                return True
        
        return False
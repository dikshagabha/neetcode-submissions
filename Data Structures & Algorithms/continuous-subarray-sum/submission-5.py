class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        l = 0
        cursum = 0
        cs = {0:-1}
        
        for i, n in enumerate(nums):
            cursum+=n
            r = cursum % k 
            if r not in cs:
                cs[r] = i
            elif i-cs[r]>1:
                return True
        
        return False
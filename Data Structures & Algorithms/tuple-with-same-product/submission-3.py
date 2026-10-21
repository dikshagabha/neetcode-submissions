class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        v = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                v[nums[i]*nums[j]] = v.get(nums[i]*nums[j], 0)+1
        res = 0
        for i in v.values():
            res+=(4)*(i)*(i-1)
            
            
        return res
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cs = {}
        for i in nums:
            cs[i]=cs.get(i,0)+1
        res = 0
        for j in cs.values():
            if j==1:
                continue
            
            res += (j*(j-1))//2
        return res

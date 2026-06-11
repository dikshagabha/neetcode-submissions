class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l = {}
        for i in nums:
            l[i] = l.get(i, 0)+1
        res = []
        for i, j in l.items():
            if j==1:
                res.append(i)
        return res
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        print(0^3)
        for i in nums:
            res = res ^ i
        return res
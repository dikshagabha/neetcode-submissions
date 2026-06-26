class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 + 7
        r=len(nums)-1
        for l in range(0, len(nums)):
            while l<=r and nums[l]+nums[r]>target:
                r-=1
            if l<=r:
                res += pow(2, r-l, mod)
                res %= mod
        return res
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        i=len(nums)-1
        while i>=0:
            cur_val = nums[i]
            j = i-1
            ops = k
            while abs(cur_val-nums[j])<=ops and j>=0:
                ops-=abs(cur_val-nums[j])
                res = max(res, i-j+1)
                j-=1
            if j<=0:
                return res
           
            i-=1
        return res

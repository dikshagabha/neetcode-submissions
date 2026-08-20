class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target>sum(nums): return 0
        l=0
        cursum = 0
        res = len(nums)
        for r in range(len(nums)):
            cursum += nums[r]
            #print(cursum, r, l)
            #if cursum>=target:
                #res = min(res, r-l+1)
            while cursum>=target:
                cursum-=nums[l]
                res = min(res, r-l+1)
                l+=1
        
        return res
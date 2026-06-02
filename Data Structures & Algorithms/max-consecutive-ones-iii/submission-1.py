class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        count0=0
        res = 0
        for r in range(len(nums)):
            
            if nums[r] == 0:
                count0 +=1
            
            if count0>k:
                res = max(r-l, res)
                while nums[l]==1:
                    l+=1
                l+=1
                count0-=1
                
        print(r, l)
        res = max(r-l+1, res)
        return res
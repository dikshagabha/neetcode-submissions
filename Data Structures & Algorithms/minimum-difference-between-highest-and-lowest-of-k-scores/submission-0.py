class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        nums.sort()
        #print(nums)
        for i in range(len(nums)-k+1):
            print(nums[i:i+k], i)
            res = min(res, (max(nums[i:i+k])-min(nums[i:i+k])))
        
        return res
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 1
        n=1
        while n<len(nums):
            if nums[n]==nums[n-1]:
                nums.pop(n)
                continue
            n+=1
        return len(nums) 
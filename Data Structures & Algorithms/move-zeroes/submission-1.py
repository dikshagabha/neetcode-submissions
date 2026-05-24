class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curi = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[curi] = nums[curi], nums[i]
                curi+=1
        # i=0
        # n = len(nums)
        # while i<len(nums):
        #     if nums[i]==0:
        #         nums.pop(i)
        #         continue
        #     i+=1
        # nums.extend([0]*(n-len(nums)))
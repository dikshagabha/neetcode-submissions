class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        first0 = 0
        while first0<len(nums) and nums[first0]!=0:
                    first0+=1
        while i<len(nums):
            print(i, first0)
            if nums[i] !=0 and i> first0:
                nums[i], nums[first0] = nums[first0], nums[i]
                while first0<len(nums) and nums[first0]!=0:
                    first0+=1
            #print(first0, i)
            i+=1

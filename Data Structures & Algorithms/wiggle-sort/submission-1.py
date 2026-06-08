class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        i=1
        op = 0
        while i<len(nums):
            if op==0: 
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                op=1
            else:
                if nums[i-1] < nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                op=0
            i+=1


                
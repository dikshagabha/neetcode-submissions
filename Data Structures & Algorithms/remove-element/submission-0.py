class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        while j<len(nums):
            if nums[j] == val:
                del nums[j]
                continue
            j+=1
        return len(nums)
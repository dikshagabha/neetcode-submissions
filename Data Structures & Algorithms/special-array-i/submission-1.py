class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        l=0
        while l<len(nums)-1:
            if (nums[l] %2 == nums[l+1] %2):
                return False
            l+=1
        return True
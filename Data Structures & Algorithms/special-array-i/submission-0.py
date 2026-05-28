class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        l=0
        while l<len(nums)-1:
            if (nums[l] %2==0 and nums[l+1] %2 ==0) or(nums[l] %2!=0 and nums[l+1] %2 !=0):
                return False
            l+=1
        return True
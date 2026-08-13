class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        preveven = (nums[0] %2 ==0)
        for i in range(1, len(nums)):
            cureven = (nums[i] %2 ==0)
            if cureven == preveven:
                return False
            preveven = cureven
        
        return True

        
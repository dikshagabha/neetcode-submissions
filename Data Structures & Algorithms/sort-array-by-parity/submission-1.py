class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)<1:
            return nums

        l, r = 0, len(nums)-1
        while l<r:
            while l<r and nums[l] %2 ==0:
                l+=1
            while l<r and nums[r]%2 != 0:
                r-=1
            
            nums[l], nums[r] = nums[r], nums[l]
            r-=1
            l+=1
        return nums


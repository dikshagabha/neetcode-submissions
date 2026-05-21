class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        cur = set(nums)
        res = [i for i in range(1, n+1) if i not in cur]
        return res
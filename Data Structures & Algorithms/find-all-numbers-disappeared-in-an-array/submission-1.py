class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(1, len(nums)+1):
        #     if i not in nums:
        #         res.append(i)
        n = len(nums)
        cur = set(nums)
        res = [i for i in range(1, n+1) if i not in cur]
        return res
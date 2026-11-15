class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, curtotal):
            if i==len(nums):
                return curtotal
            return dfs(i+1, curtotal) + dfs(i+1, curtotal^nums[i])
        
        return dfs(0, 0)
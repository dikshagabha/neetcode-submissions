class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = [1]*len(nums)
        c = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    if l[j]+1>l[i]:
                        l[i] = l[j]+1
                        c[i] = c[j]
                    elif l[j]+1==l[i]:
                        c[i]+=c[j]
                
                
            
        b = max(l)
        return sum([j for i, j in zip(l, c) if i==b])
        print(l, c)
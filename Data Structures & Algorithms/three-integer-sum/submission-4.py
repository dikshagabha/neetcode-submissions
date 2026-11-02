class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0

        nums.sort()
        def two_sum(start,t):
            l = start+1
            r = len(nums)-1
            res = []
            while r>l:
                if nums[l]+nums[r]>t:
                    r-=1
                elif nums[l]+nums[r]==t:
                   
                    res.append([nums[l], nums[r], nums[start]])
                    r-=1
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                else:
                    l+=1
            return res

        l = 0
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            cur = two_sum(i, target-nums[i])
            
            if len(cur):
                if cur not in res:
                    res.extend(cur)
        return res
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #nums = list(set(nums))
        nums.sort()
        def two_sum(l, targetval):
            if len(l)<2:
                return []
            i=0
            j = len(l)-1
            res = []
            while i<j:
                if l[i]+l[j]>targetval:
                    j-=1
                elif l[i]+l[j]<targetval:
                    i+=1
                else:
                    if [l[i], l[j]] not in res:
                        res.append([l[i], l[j]])
                    i+=1
                    j-=1
            return res
        res= []
        visited = set()
        for i in range(len(nums)):
            j = len(nums)-1
            while j>i :
               # print(visited, nums[i], nums[j])
                if (nums[i], nums[j]) not in visited:
                    visited.add((nums[i], nums[j]))
                    find_next = two_sum(nums[i+1:j], target-(nums[i]+nums[j]))
                    #print(find_next)
                    if len(find_next):
                       # print([[nums[i], l, r, nums[j]] for l,r in find_next])
                        res.extend([[nums[i], l, r, nums[j]] for l,r in find_next])
                j-=1
        return res







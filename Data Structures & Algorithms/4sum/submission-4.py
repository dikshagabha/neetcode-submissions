class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        def two_sum(t,p1, p2):
            print(t)
            l,r = p2+1, len(nums)-1
            res = []
            while r>l:
                # if used[r]==True:
                #     r-=1
                #     continue
                # if used[l]==True:
                #     l+=1
                #     continue
                if nums[l]+nums[r]==t:
                    #used[l], used[r] = True, True
                    res.append([nums[l], nums[r], nums[p1], nums[p2]])
                    #used[l], used[r] = False, False
                    l+=1;r-=1
                    while l<r and nums[l-1]==nums[l]: l+=1;
                    while l<r and nums[r+1]==nums[r]: r-=1;
                elif nums[l]+nums[r]>t:
                    r-=1
                else:
                    l+=1
            return res
        
        p1 = 0
        res = []
        #used = [False]*len(nums)
        while p1<len(nums):
            if p1>0 and nums[p1]==nums[p1-1]:
                p1+=1
                continue
            #used[p1] = True
            p2=p1+1
            while p2<len(nums):
                if p2>p1+1 and p2<len(nums) and nums[p2]==nums[p2-1]:
                    p2+=1
                    continue
                print(nums[p2], p2)
                # if nums[p1]+nums[p2]>target:
                #     break
                #used[p2] = True

                res.extend(two_sum(target-nums[p1]-nums[p2], p1, p2))
                #used[p2]= False
                p2+=1
            #used[p1] = False
            p1+=1
        return res
        
        
        
        # nums.sort()
        # def two_sum(l, targetval):
        #     if len(l)<2:
        #         return []
        #     i=0
        #     j = len(l)-1
        #     res = []
        #     while i<j:
        #         if l[i]+l[j]>targetval:
        #             j-=1
        #         elif l[i]+l[j]<targetval:
        #             i+=1
        #         else:
        #             if [l[i], l[j]] not in res:
        #                 res.append([l[i], l[j]])
        #             i+=1
        #             j-=1
        #     return res
        # res= []
        # visited = set()
        # for i in range(len(nums)):
        #     j = len(nums)-1
        #     while j>i :
        #        # print(visited, nums[i], nums[j])
        #         if (nums[i], nums[j]) not in visited:
        #             visited.add((nums[i], nums[j]))
        #             find_next = two_sum(nums[i+1:j], target-(nums[i]+nums[j]))
        #             #print(find_next)
        #             if len(find_next):
        #                # print([[nums[i], l, r, nums[j]] for l,r in find_next])
        #                 res.extend([[nums[i], l, r, nums[j]] for l,r in find_next])
        #         j-=1
        # return res







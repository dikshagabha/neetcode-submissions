class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[0]*(len(nums))
        for i in nums:
            l[i-1]+=1
        print(l)

        for key, j in enumerate(l):
            if j==0:
                missing = key+1
            if j==2:
                repeat = key+1
        return [repeat, missing]
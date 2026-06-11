class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]

        return sorted(nums)

        # if len(nums)==0:
        #     return []
        # if len(nums)==1:
        #     return [nums[0]*nums[0]]
        # cur=0
        # #print(abs(nums[0]) > nums[1])
        # while nums[0]<0 and abs(nums[0]) >= abs(nums[1]):
        #     cur=0
        #     while cur< len(nums) and abs(nums[cur]) == abs(nums[cur+1]):
        #         cur+=1
        #     print(cur)
        #     i=cur
        #     while i<len(nums)-1 and abs(nums[i]) >= abs(nums[i+1]):
        #         nums[i], nums[i+1] = nums[i+1], nums[i]
        #         i+=1
        #     print(nums)
        #     return

        # res = []
        # for j in nums:
        #     res.append(j**2)

        # return res
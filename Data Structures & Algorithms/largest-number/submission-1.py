class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [i for i in nums]
        for i in range(len(nums)):
            arr[i] = str(nums[i])
        res = ''
        while arr:
            maxi = 0
            for i in range(1, len(arr)):
                if arr[i]+arr[maxi] > arr[maxi]+arr[i]:
                    maxi = i
            res+=arr[maxi]
            arr.pop(maxi)
        return res if res[0] != '0' else '0'
        
        # print(nums, res)
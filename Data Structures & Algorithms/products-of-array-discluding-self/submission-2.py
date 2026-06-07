class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]

        for i in nums:
            pre.append(pre[-1]*i)
        for i in range(len(nums)-1,-1,-1):
            suf.append(suf[-1]*nums[i])
       # print(pre, suf)
        res = []
        for i in range(1, len(pre)):
           # print(i, len(suf)-i-1)
            res.append(pre[i-1]*suf[len(suf)-i-1])
        return res

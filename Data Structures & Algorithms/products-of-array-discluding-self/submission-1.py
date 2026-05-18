class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        post = [1]
        n = len(nums)
        for i in range(n-1):
            pre.append(pre[-1]*nums[i])
            post.append(post[-1]*nums[n-1-i])

        for i in range(n-1,-1,-1):
            pre[n-1-i] = pre[n-1-i]*post[i]
        
        return pre

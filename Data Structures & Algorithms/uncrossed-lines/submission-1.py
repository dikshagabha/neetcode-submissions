class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1),len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
       
        for i in range(n):
            for j in range(m):
                if nums2[j]==nums1[i]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                   dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[n][m]
        def helper(nums1, nums2):
            l1, l2 = 0, 0
            res = 0
            
            while l1<n and l2<m:
                temp = l2
            
                while temp<m and nums1[l1]!=nums2[temp]:
                    temp+=1
                if temp<=m-1:
                    res+=1
                    l2=temp
                    print(temp, l1, res)
                #l2+=1
                l1+=1
            return res

        return max(helper(nums1, nums2), helper(nums2, nums1))

class Solution:
    def longestPalindrome(self, s: str) -> int:

        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0)+1
        res, mid = 0,0
        for i in counts.values():
                res+=i//2
                if i%2==1:
                    mid=1
        res = res*2
        if mid:
            res+=1
        return res
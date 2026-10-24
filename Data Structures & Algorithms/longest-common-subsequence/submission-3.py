class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        
        def find(a, b):
            if a>=len(text1) or b>=len(text2):
                return 0
            if (a, b) in memo:
                return memo[(a, b)]
            
            if text1[a]==text2[b]:
                memo[(a, b)] = 1+ find(a+1, b+1)
            else:
                memo[(a, b)] =  max(find(a+1, b), find(a, b+1))
            
            return memo[(a, b)]
        
        return find(0, 0)

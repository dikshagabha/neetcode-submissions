class Solution:
    def hammingWeight(self, n: int) -> int:
        l=0
        
        while n:
            rem=n%2
           
            l+=rem
            n=n//2
        return l
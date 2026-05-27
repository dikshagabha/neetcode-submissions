class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        res = []
       
        while x:
            r=x%10
            x=x//10
            res.append(r)
        return res==res[::-1]
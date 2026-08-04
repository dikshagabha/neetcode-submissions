class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        for i in range(n):
            res = res*x
        
        return x**n
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n
        temp = [0]*(n+1)
        temp[1], temp[2] = 1, 2
        for i in range(3, n+1):
            temp[i] = temp[i-1]+temp[i-2]
        return temp[n]

        # if n==1 or n==0:
        #     return 1
        # if n<0:
        #     return 0
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
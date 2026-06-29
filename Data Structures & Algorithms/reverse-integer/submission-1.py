class Solution:
    def reverse(self, x: int) -> int:
        if x<10 and x>-10:
            return x
        
        temp = abs(x)
        c = ""
        while temp>0:
            c = c+str(temp%10)
            
            temp=temp//10
        res = 0
        if x>0:
            res= int(c)
        else:
            res= - int(c)
            

        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res

        
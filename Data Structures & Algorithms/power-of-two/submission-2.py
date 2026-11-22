class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        
        l = bin(n)
        #print(l)
        c = 0
        for i in l:
            if i=='1':
                c+=1
            if c==2:
                return False
        return True
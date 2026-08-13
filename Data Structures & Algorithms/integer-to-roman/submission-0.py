class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1,5,10,50,100,500,1000]
        romans= ['I','V','X', 'L', 'C', 'D', 'M']
        def get_smaller(n):
            for i in range(7):
                if nums[i]==n:
                    return romans[i], nums[i]
                if nums[i]>n:
                    return romans[i-1], nums[i-1]
            
            return romans[i], nums[i]
        
        def get_greater(n):
           for i in range(6, -1, -1):
                if nums[i]==n:
                    return romans[i], nums[i]
                if nums[i]<n:
                    return romans[i+1], nums[i+1]
        
        res = ''
        multiplier = 1
        while num:
            l = num%10
            cur = l * multiplier
            #print(cur)
            cs = ''
            addbefore = False
            while cur>0:

                if str(cur).startswith('4') or str(cur).startswith('9'):
                    n, r =  get_greater(cur)
                    addbefore = True
                    
                else:
                    n, r =  get_smaller(cur)
                
                if addbefore:
                    cs = n + cs
                else:
                    cs = cs + n
                cur = abs(cur-r)
            
            res = cs + res
                

            num = num//10
            multiplier*=10
            #print(cur, num)
        return res

        

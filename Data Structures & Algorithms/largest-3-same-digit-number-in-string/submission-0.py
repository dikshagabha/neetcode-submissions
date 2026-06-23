class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=0
        cur= -1
        while l<len(num):
            r = 0
            while r<3 and l+r<len(num) and num[l+r] == num[l]:
                r+=1
            print(l, r, num[l:l+r])
            if len(num[l:l+r])==3:
                print(int(num[l:l+r]))
                cur=max(cur, int(num[l:l+r]))
            l+=1
        if cur==-1:
            return ''
        if cur==0:
            return '0'*3
        return str(cur)
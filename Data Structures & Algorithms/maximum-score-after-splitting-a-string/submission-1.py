class Solution:
    def maxScore(self, s: str) -> int:
        countone, countzero=0, 0
        for i in range(len(s)):
            if s[i]=='1':
                countone+=1
           

        res = 0
        for r in range(len(s)-1):
            if s[r]=='0':
                countzero+=1
            else:
                countone-=1
            res = max(res, countzero+countone)
        return res


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        si, ei = [], []
        for s, e in intervals:
            si.append(s)
            ei.append(e)
        si.sort()
        ei.sort()

        j, res = 0, 0
        for i, s in enumerate(si):
            while ei[j]<s:
                j+=1
            res = max(res, i-j+1) 
        return res
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = sorted(intervals)
        res = 0
        
        for i in range(1, len(l)):
            curS, curE = l[i][0] , l[i][1]
            prevS, prevE = l[i-1][0] , l[i-1][1]
            if curS>=prevS and curS<prevE:
                #l[i] = [min(curS, prevS), min(curE, prevE)]
                l[i] = [min(curS, prevS), min(curE, prevE)]
                res+=1
            print(l)
        return res
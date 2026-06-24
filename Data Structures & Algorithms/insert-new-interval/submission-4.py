class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals
        apply=0
        while apply<len(intervals):
            if intervals[apply][0]>newInterval[0]:
                break
            apply+=1
        intervals = intervals[:apply]+[newInterval]+intervals[apply:]
        res = [intervals[0]]
        for start, end in intervals:
            if start <= res[-1][1] and start>=res[-1][0]:
                res[-1] = [min(start, res[-1][0]), max(res[-1][1], end)]
            else:
                res.append([start, end])
        
       
        return res
       
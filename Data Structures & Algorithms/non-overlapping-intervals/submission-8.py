class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        c=0
        prev_start, prev_end =intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if (start>prev_start and start<prev_end) or (prev_end>start and prev_end<end):
                res.append([min(prev_start, start), min(prev_end, end)])
                c+=1
            elif (start==prev_start) and (prev_end==end):
                c+=1
                res.append([start, end])
            else:
                res.append([start, end])
            prev_start, prev_end =res[-1][0], res[-1][1]
            #print(res)
        return  c

            
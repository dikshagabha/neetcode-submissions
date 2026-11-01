class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curbestleft = values[0]
        res = 0
        for i in range(1, len(values)):
            res = max(res, curbestleft+values[i]-i)
            curbestleft = max(curbestleft, values[i]+i)
        return res
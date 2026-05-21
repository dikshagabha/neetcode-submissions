class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        temp = {}
        for key, i in enumerate(x):
            temp[i] = temp.get(i, 0)
            temp[i] = max(temp[i], y[key])

        s = sorted(temp.values())
        if len(s)<3:
            return -1
        return sum(s[-3:])
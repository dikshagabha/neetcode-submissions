class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # l = []
        # heapq.heapify(l)
        
        temp = {}
        l = []
        heapq.heapify_max(l)
        for key, i in enumerate(x):
            temp[i] = temp.get(i, 0)
            temp[i] = max(temp[i], y[key])

        l=list(temp.values())
        heapq.heapify_max(l)
        if len(l)<3:
            return -1
        return heapq.heappop_max(l)+heapq.heappop_max(l)+heapq.heappop_max(l)
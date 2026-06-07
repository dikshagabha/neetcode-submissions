class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curmax = -1
        for i in range(len(arr)-1, -1, -1):
            t = arr[i]
            arr[i] = curmax
            curmax = max(curmax, t)
        return arr
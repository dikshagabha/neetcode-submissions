class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        #a=arr
        res = -1
        l=0
        while l<=len(arr)-1:
            r = l+1
            while r<len(arr) and arr[r] == arr[r-1]:
                r+=1
            if arr[r-1]==r-l:
                res=r-l
            l=r
        return res
            
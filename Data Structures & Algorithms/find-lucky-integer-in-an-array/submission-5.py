class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp = {}
        res = -1
        for i in arr:
            temp[i] = temp.get(i, 0)+1

        for key, j in temp.items():
            if key==j:
                res=max(res, key)
        # arr.sort()
        # #a=arr
        # res = -1
        # l=0
        # while l<=len(arr)-1:
        #     r = l+1
        #     while r<len(arr) and arr[r] == arr[r-1]:
        #         r+=1
        #     if arr[r-1]==r-l:
        #         res=r-l
        #     l=r
        return res
            
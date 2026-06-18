class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, total = 0, 0
        res=0
        for r in range(len(arr)):
            total += arr[r]
            if r-l+1==k:
                avg = total/k
                if avg>=threshold:
                    res+=1
                total-=arr[l]
                l+=1
        return res
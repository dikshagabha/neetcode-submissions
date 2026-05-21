class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l, a=0, 0
        r, b= len(piles)-1, 0

        while l<r:
            a+=max(piles[l], piles[r])
            b+=min(piles[l], piles[r])

            l+=1
            r-=1
        return a>b


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high==low:
            return 0 if high%2==0 else 1
        return (high-low)//2 +1
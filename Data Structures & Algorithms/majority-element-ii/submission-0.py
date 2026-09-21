class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0)+1

        size = len(nums)//3
        res = []
        for num, count in counts.items():
            if count>size:
                res.append(num)
        return res
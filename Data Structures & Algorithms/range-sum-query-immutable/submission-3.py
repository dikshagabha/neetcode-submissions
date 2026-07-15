class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers = nums
        self.sum_until = [0] 
        for i in range(len(self.numbers)):
            self.sum_until.append(self.sum_until[i]+self.numbers[i])

    def sumRange(self, left: int, right: int) -> int:
        return(self.sum_until[right+1]-self.sum_until[left])
       
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
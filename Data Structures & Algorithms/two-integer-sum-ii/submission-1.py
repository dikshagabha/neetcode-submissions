class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers)-1

        while l<r:
            c = numbers[l]+numbers[r]
            if c>target:
                r-=1
            elif c<target:
                l+=1
            else:
                return [l+1, r+1]



        if len(numbers)==0:
            return 0

        current = numbers[0]+numbers[-1]

        if current>target:
            return self.twoSum(numbers[:-1], target)
        elif current<target:
            return self.twoSum(numbers[1:], target)
        else:
            return [numbers[0], numbers[-1]]

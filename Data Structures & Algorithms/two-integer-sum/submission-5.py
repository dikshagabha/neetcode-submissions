class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

        
#         l = []
#         heapq.heapify(l)
#         for i in range(len(nums)):
#             heapq.heappush(l, (nums[i], i))
#         i= 0
#         j = len(l)-1
#         print(l)
#         while i<j:
#             cursum = l[i][0] + l[j][0]
#             print(cursum)
#             if cursum==target:
#                 if l[i][1]<l[j][1]:
#                     return([l[i][1] , l[j][1]])
#                 else:
#                     return([l[j][1] , l[i][1]])
#             elif cursum>target:
#                 j-=1
#             else:
#                 i+=1
#         return[]
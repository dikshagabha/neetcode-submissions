class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start, end = [0, 0], [len(matrix)-1, len(matrix[0])-1]
        # while (start[0]<end[0]) or (start[0]==end[0] and start[1]<end[1]):
        #     mid = 

        def binary_search(arr):
            if len(arr) == 0:
                return False
            l = 0 
            r=len(arr)-1
            mid = (r-l)//2
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                return binary_search(arr[mid+1:])
            else:
                return binary_search(arr[:mid])
            return False

        for i in range(len(matrix)):
            if matrix[i][-1]>=target and matrix[i][0]<=target:
                return binary_search(matrix[i])
            
        return False
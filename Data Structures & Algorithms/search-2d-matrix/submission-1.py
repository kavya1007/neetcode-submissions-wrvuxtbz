class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        s, e = 0, rows*cols -1
        while (s<=e):
            mid = (s+e)//2
            mid_value = matrix[mid//cols][mid%cols]
            if mid_value == target:
                return True

            elif mid_value < target:
                s = mid+1
            else:
                e =mid -1

        return False
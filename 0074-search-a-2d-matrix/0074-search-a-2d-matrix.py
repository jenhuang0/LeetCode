class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we can first find which row we should be searching 
        rows, cols = len(matrix), len(matrix[0])
        top, bom = 0, rows-1
        while top<=bom:
            mid= (top+bom)//2
            if target > matrix[mid][-1]:
                top =mid+1
            elif target < matrix[mid][0]:
                bom = mid -1
            else: 
                break
        if not(top<=bom):
            return False
        
        row = (top+bom)//2
        l, r = 0, cols-1

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] > target:
                r = mid-1
            elif matrix[row][mid] <target:
                l = mid+1
            else:
                return True
        return False
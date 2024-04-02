class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first we can choose which row has the target num
        #after find the target row we can using bs to find the target in that row
        # in first step we might also not about the find the target row (keep that in mind: return false)

        row = len(matrix)
        col = len(matrix[0])
        top = 0
        btm = row-1

        while top<=btm:
            mid = (top+btm)//2
            if matrix[mid][0] > target:
                btm = mid-1
            elif matrix[mid][-1] < target:
                top = mid+1
            else:
                break
        if not top<=btm:
            return False #mean the target is not in any row
        
        row = (top+btm)//2
        l = 0 
        r = col -1

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]> target:
                l = mid+1
            elif matrix[row][mid] < target:
                r = mid-1
            else:
                return True
        return False
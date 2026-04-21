class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target: 
                l = mid + 1   
                ans = mid
            else:
                r = mid - 1
        
        if ans == -1:
            return False
        if target > matrix[ans][-1]:
            return False
        l, r = 0, len(matrix[0])-1
        
        while l<=r:
            mid = (l+r)//2
            if matrix[ans][mid]==target:
                return True
            elif matrix[ans][mid]>target:
                r = mid - 1
            else: 
                l = mid + 1

        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = 0
        for row in matrix:
            i=0
            j=len(row)-1
            while i<=j:
                    mid = (i+j)//2
                    if row[mid]==target:
                       print(matrix[row_count][mid],row_count,mid) 
                       return True
                    if row[i]<target:
                       i=mid+1
                    else:
                       j=mid-1
            row_count+=1           

        return False                       

                   
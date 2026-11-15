class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows,cols = len(matrix),len(matrix[0])
        zero_lookup = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                   zero_lookup.append((r,c))


        for r,c in zero_lookup:
            for r1 in range(rows):
                matrix[r1][c]=0
            for c1 in range(cols):
                matrix[r][c1]=0

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_inverse = [list(row)[::-1] for row in zip(*matrix)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c]=matrix_inverse[r][c]
                
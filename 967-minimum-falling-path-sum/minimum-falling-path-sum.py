from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Initialize a copy of the matrix to store the minimum falling path sum
        dp = [[0] * cols for _ in range(rows)]
        for i in range(cols):
            dp[0][i] = matrix[0][i]

        # Iterate through the matrix to compute the minimum falling path sum
        for i in range(1, rows):
            for j in range(cols):
                # Compute the minimum falling path sum for the current element
                dp[i][j] = matrix[i][j] + min(
                    dp[i-1][j-1] if j-1 >= 0 else float('inf'),
                    dp[i-1][j],
                    dp[i-1][j+1] if j+1 < cols else float('inf')
                )

        # Return the minimum falling path sum for the last row
        return min(dp[rows-1])

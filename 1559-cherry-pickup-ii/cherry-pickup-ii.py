class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(m)]

        # Initialize bottom row (Base Case)
        for col1 in range(n):
            for col2 in range(n):
                if col1 == col2:
                    dp[m - 1][col1][col2] = grid[m - 1][col1]
                else:
                    dp[m - 1][col1][col2] = grid[m - 1][col1] + grid[m - 1][col2]

        # Bottom-up iteration 
        for row in range(m - 2, -1, -1):
            for col1 in range(n):
                for col2 in range(n):
                    best = float('-inf') 
                    for dx1 in [-1, 0, 1]:
                        for dx2 in [-1, 0, 1]:
                            prev_col1 = col1 + dx1
                            prev_col2 = col2 + dx2
                            if 0 <= prev_col1 < n and 0 <= prev_col2 < n:
                                best = max(best, dp[row + 1][prev_col1][prev_col2])

                    cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
                    dp[row][col1][col2] = cherries + best  

        return dp[0][0][n - 1]

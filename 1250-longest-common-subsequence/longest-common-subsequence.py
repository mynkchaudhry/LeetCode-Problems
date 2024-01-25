class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Initialize a 2D array to store the length of the common subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The bottom-right cell contains the length of the longest common subsequence
        return dp[m][n]

# Example usage:
solution = Solution()
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(result)

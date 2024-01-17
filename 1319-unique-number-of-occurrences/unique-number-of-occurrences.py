from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Dictionary to store the count of occurrences for each unique value
        count_dict = {}

        # Count occurrences of each value in arr
        for num in arr:
            count_dict[num] = count_dict.get(num, 0) + 1

        # Check if the count of occurrences is unique
        return len(count_dict.values()) == len(set(count_dict.values()))

# Example usage:
sol = Solution()
arr = [1, 2, 2, 1, 1, 3]
result = sol.uniqueOccurrences(arr)
print(result)

from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            current_profit = jobs[i - 1][2]
            start_time = jobs[i - 1][0]
            prev_non_conflicting = self.find_prev_non_conflicting(jobs, i)

            dp[i] = max(current_profit + dp[prev_non_conflicting], dp[i - 1])

        return dp[-1]

    def find_prev_non_conflicting(self, jobs, current):
        low, high = 0, current - 1

        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[current - 1][0]:
                if jobs[mid + 1][1] <= jobs[current - 1][0]:
                    low = mid + 1
                else:
                    return mid + 1
            else:
                high = mid - 1

        return 0

# Example usage:
sol = Solution()
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
max_profit = sol.jobScheduling(startTime, endTime, profit)
print(max_profit)  # Output will be the maximum profit achievable

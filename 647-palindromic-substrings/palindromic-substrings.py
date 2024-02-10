class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # Check for every possible center of a palindrome
        for i in range(len(s)):            
            # Odd-length palindromes
            count += self.count_palindromes(s, i, i) 
            
            # Even-length palindromes
            count += self.count_palindromes(s, i, i + 1)  

        return count

    def count_palindromes(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

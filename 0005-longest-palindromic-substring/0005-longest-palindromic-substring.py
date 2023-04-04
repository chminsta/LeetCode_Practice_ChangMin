class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # Initialize dp table
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome = s[0]
        
        # Check for palindromes
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > len(longest_palindrome):
                        longest_palindrome = s[i:j+1]
        
        return longest_palindrome
